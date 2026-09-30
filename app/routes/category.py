from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from typing import Annotated
from uuid import UUID

from app.core.dependencies import get_async_db
from app.core.exceptions import CategoryNotFoundError
from app.services.category import CategoryServices
from app.schemas.category import (
    CategoryCreateModel,
    CategoryUpdateModel,
    CategoryResponseModel,
)

router = APIRouter()
category_services = CategoryServices()

DbDependency = Annotated[AsyncSession, Depends(get_async_db)]


@router.get("/")
async def get_categories(session: DbDependency):
    categories = await category_services.get_categories(session)

    return categories


@router.get("/{category_uid}", response_model=CategoryResponseModel)
async def get_category(category_uid: UUID, session: DbDependency):
    category = await category_services.get_category(category_uid, session)

    return category


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_category(category: CategoryCreateModel, session: DbDependency):
    new_category = await category_services.create_category(category, session)

    return new_category


@router.put("/{category_uid}")
async def update_category(
    category_uid: UUID, new_category: CategoryUpdateModel, session: DbDependency
):
    category = await category_services.get_category(category_uid, session)

    if not category:
        raise CategoryNotFoundError("The requested category cannot be found")

    updated_category = await category_services.update_category(
        category_uid, new_category, session
    )

    return updated_category


@router.delete("/{category_uid}", status_code=status.HTTP_204_NO_CONTENT)
async def update_category(category_uid: UUID, session: DbDependency):
    category = await category_services.get_category(category_uid, session)

    if not category:
        raise CategoryNotFoundError("The requested category cannot be found")

    await category_services.delete_category(category_uid, session)

    return {"message": "Category has been deleted successfully"}
