from sqlalchemy import MetaData
from sqlalchemy.orm import DeclarativeBase

from app.core.config import get_settings


class Base(DeclarativeBase):
    
    __abstract__ = True

    metadata = MetaData(
        naming_convention=get_settings().naming_convention
    )
