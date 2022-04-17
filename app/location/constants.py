from django.conf import settings

HTTP_URL = f"http://{settings.IPSTACK_HOST}"
HTTPS_URL = f"https://{settings.IPSTACK_HOST}"
ACCESS_KEY = settings.IPSTACK_API_KEY
