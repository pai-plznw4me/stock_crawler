from django.apps import AppConfig
from django.conf import settings


class StockCrawlingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'stock_crawling'

    def ready(self):
        if settings.SCHEDULER_DEFAULT:
            from crawling_server import operator
            operator.start()
