import os

BASE_URL = os.environ.get(
    "MEMES_API_BASE_URL", "http://memesapi.course.qa-practice.com"
).rstrip("/")
REQUEST_TIMEOUT = (5, 15)  # Connection and read timeouts, in seconds.
