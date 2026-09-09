from datetime import datetime
from typing import List, Optional
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.database import Base

class Product(Base):
    __tablename__ = "products"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    price: Mapped[float] = mapped_column(nullable=False)
    vendor_id: Mapped[int] = mapped_column(ForeignKey("vendors.id"))
    weight: Mapped[float] = mapped_column(nullable=False)
    added_at: Mapped[datetime] = mapped_column(default=datetime.utcnow())

class Vendor(Base):
    __tablename__ = "vendors"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    products: Mapped[List["Product"]] = relationship(backref="vendor", cascade="all, delete-orphan")
