from django.core.exceptions import SuspiciousOperation
import time


class TooManyRequestsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.timer = time.time()
        self.ips = {'127.0.0.1': 0}

    def __call__(self, request):

        ip = request.META.get('REMOTE_ADDR')

        if ip in self.ips:
            self.ips[ip] += 1
            print(self.ips[ip])
            if self.ips[ip] > 10 and time.time() - self.timer < 60.0:
                raise SuspiciousOperation
            elif time.time() - self.timer >= 60.0:
                self.timer = time.time()
                self.ips[ip] = 0

        response = self.get_response(request)

        return response
