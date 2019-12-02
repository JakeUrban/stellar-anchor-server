from django.apps import AppConfig


class AnchorConfig(AppConfig):
    name = "app"

    def ready(self):
        from polaris.integrations import register_integrations
        from .integrations import MyDepositIntegration, MyWithdrawalIntegration

        register_integrations(
            deposit=MyDepositIntegration(), withdrawal=MyWithdrawalIntegration()
        )
