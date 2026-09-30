from pydantic import BaseModel, Field, ConfigDict, AwareDatetime


class CategoryBaseModel(BaseModel):
    model_config = ConfigDict(from_attributes=True, populate_by_name=True)

    name: str
    description: str


class CategoryCreateModel(CategoryBaseModel):
    pass


class CategoryUpdateModel(CategoryBaseModel):
    pass


class CategoryResponseModel(CategoryBaseModel):
    created_at: AwareDatetime = Field(alias="createdAt")
    updated_at: AwareDatetime = Field(alias="updatedAt")
