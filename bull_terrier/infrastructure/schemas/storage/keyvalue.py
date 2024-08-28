from pydantic import AwareDatetime, BaseModel


class CellSchema(BaseModel):
    """The cell schema."""

    key: str
    value: str
    expire_dttm: AwareDatetime
