from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Category(Base):
    __tablename__ = "categories"

    cat_id = Column(Integer, primary_key=True, index=True, autoincrement=True)

    cat_title = Column(String, nullable=False)
    cat_href = Column(String, nullable=False)
    cat_photo = Column(String, nullable=False)
    id_added = Column(Integer, default=0)
    id_modify = Column(Integer, default=0)
    id_deleted = Column(Integer, default=0)
    date_added = Column(Integer, default=0)
    date_modify = Column(Integer, default=0)
    date_deleted = Column(Integer, default=0)
    ip_address = Column(String, nullable=False) 



