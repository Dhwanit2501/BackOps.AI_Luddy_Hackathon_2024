from sqlmodel import Field, SQLModel

class KeyValueBase(SQLModel):
    key: str = Field(primary_key=True)
    value: str = Field(index=True)

class KeyValue(KeyValueBase, table=True):
    created_time: str
    updated_time: str

class KeyValueUpdate(KeyValueBase):
    updated_time: str