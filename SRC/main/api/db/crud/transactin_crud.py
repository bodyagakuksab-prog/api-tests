from sqlalchemy.orm import Session
from SRC.main.api.db.models.transaction_table import Transaction

class TransactionCrudDb:
    @staticmethod
    def get_last_transaction_by_account_id(
            db_session: Session,
            account_id: int
    ):
        return (
            db_session.query(Transaction)
            .filter(
                (Transaction.to_id == account_id) |
                (Transaction.from_account_id == account_id)
            )
            .order_by(Transaction.id.desc())
            .first()
        )