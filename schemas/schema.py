from pydantic import BaseModel

class CategoryCreate(BaseModel):
    cat_title: str
    cat_href: str
    cat_photo: str
    id_added: int = 0
    id_modify: int = 0
    id_deleted: int = 0
    date_added: int = 0
    date_modify: int = 0
    date_deleted: int = 0
    ip_address: str

class CategoryResponse(BaseModel):
    cat_id: int
    cat_title: str
    cat_href: str
    cat_photo: str
    id_added: int
    id_modify: int
    id_deleted: int
    date_added: int
    date_modify: int
    date_deleted: int
    ip_address: str

    class Config:
        from_attributes = True