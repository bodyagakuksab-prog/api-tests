from sqlalchemy import Column, Integer, String, DateTime
from SRC.main.api.db.base import Base

class Transaction(Base):
    __tablename__ = "transaction"

    id = Column(Integer, primary_key=True, autoincrement=True )
    to_account_id = Column(Integer)
    from_account_id = Column(Integer)
    credit_id = Column(Integer)
    amount = Column(Integer, nullable=False)
    transaction_type = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False)