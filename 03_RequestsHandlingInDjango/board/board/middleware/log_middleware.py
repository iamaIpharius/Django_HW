import time
import datetime
from loguru import logger
from pathlib import Path

log_path = Path('03_RequestsHandlingInDjango','board', 'logs', 'log.log')
logger.add(log_path, format="{time} {level} {message}", level="INFO")



class LogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.count = 0

    def __call__(self, request):

        logger.info(f"URL {request.build_absolute_uri()} HTTP method {request.method}")

        response = self.get_response(request)

        return response
