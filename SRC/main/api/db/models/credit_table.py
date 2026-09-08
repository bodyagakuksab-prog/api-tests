from sqlalchemy import Column, DateTime, Integer
from SRC.main.api.db.base import Base

class Credit(Base):
    __tablename__ = "credit"

    id = Column(Integer, primary_key=True, autoincrement=True)
    account_id = Column(Integer, nullable=False)
    amount = Column(Integer, nullable=False)
    term_months = Column(Integer, nullable=False)
    balance = Column(Integer, nullable=False)
    created_at = Column(DateTime, nullable=False)