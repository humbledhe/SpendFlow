from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from uuid import UUID

from app.models.category import Category
from app.schemas.category import CategoryCreateModel, CategoryUpdateModel


class CategoryServices:
    async def get_categories(self, session: AsyncSession):
        stmt = select(Category)
        result = await session.execute(stmt)
        categories = result.scalars().all()

        return categories

    async def get_category(self, category_uid: UUID, session: AsyncSession):
        stmt = select(Category).where(Category.id == category_uid)
        result = await session.execute(stmt)
        category = result.scalar()

        return category

    async def create_category(
        self, category: CategoryCreateModel, session: AsyncSession
    ):
        new_category = Category(**category.model_dump())

        session.add(new_category)
        await session.commit()
        await session.refresh(new_category)

        return new_category

    async def update_category(
        self,
        category_uid: UUID,
        new_category: CategoryUpdateModel,
        session: AsyncSession,
    ):
        stmt = (
            update(Category)
            .where(Category.id == category_uid)
            .values(**new_category.model_dump())
            .returning(Category)
        )
        result = await session.execute(stmt)
        updated_category = result.scalars().first()

        await session.commit()

        return updated_category

    async def delete_category(self, category_uid: UUID, session: AsyncSession):
        stmt = delete(Category).where(Category.id == category_uid)
        result = await session.execute(stmt)

        await session.commit()
