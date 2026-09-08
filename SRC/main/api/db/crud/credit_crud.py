from sqlalchemy.orm import Session
from SRC.main.api.db.models.credit_table import Credit

class CreditCrudDb:
    @staticmethod
    def get_credit_by_account_id(
        db_session: Session,
        account_id: int
    ):
        return(
            db_session.query(Credit)
            .filter(Credit.account_id == account_id)
            .order_by(Credit.created_at.desc())
            .first()
        )