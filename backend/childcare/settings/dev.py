from .base import *

from reservations.mongo_config import *

# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# DEFAULT_FROM_EMAIL = 'Childcare Reservations <noreply@childcare-reservations.com>'

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",  # Vite frontend
]

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'email-smtp.us-east-1.amazonaws.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.getenv('SES_SMTP_USERNAME')
EMAIL_HOST_PASSWORD = os.getenv('SES_SMTP_PASSWORD')
DEFAULT_FROM_EMAIL = 'Childcare Reservations <noreply@mail.big-heart-ventures.com>'