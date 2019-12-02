import logging
from typing import List, Dict

from django.db.models import QuerySet
from polaris.models import Transaction
from polaris.integrations import DepositIntegration, WithdrawalIntegration


logger = logging.getLogger(__name__)


class MyDepositIntegration(DepositIntegration):
    @classmethod
    def poll_pending_deposits(cls, pending_deposits: QuerySet) -> List[Transaction]:
        """
        Anchors should implement their banking rails here, as described
        in the :class:`.DepositIntegration` docstrings.

        For the purposes of this reference implementation, we simply return
        all pending deposits.
        """
        return list(pending_deposits)

    @classmethod
    def after_deposit(cls, transaction: Transaction):
        logger.info(f"Successfully processed transaction {transaction.id}")


class MyWithdrawalIntegration(WithdrawalIntegration):
    @classmethod
    def process_withdrawal(cls, response: Dict, transaction: Transaction):
        logger.info(f"Processing transaction {transaction.id}")
