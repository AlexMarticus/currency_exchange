from sqlalchemy import BigInteger
from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base


class Users(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, index=True)
    email: Mapped[str] = mapped_column(unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    password_salt: Mapped[str] = mapped_column(nullable=False)