from .base import *

from reservations.mongo_config import *

DEBUG = True
# DATABASES = {


#     "default": {
#         "ENGINE": "django.db.backends.postgresql",
#         "NAME": "mydatabase",
#         "USER": "myuser",
#         "PASSWORD": "mypassword",
#         "HOST": "localhost",
#         "PORT": "5432",
#     }
# }

ALLOWED_HOSTS = ["jv.tools.childcare-reservations.big-heart-ventures.com",
                 "localhost"]

CORS_ALLOWED_ORIGINS = [
    "https://jv.tools.childcare-reservations.big-heart-ventures.com",  # Vite frontend
]

# Email settings for AWS SES
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'email-smtp.us-east-1.amazonaws.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.getenv('SES_SMTP_USERNAME')
EMAIL_HOST_PASSWORD = os.getenv('SES_SMTP_PASSWORD')
DEFAULT_FROM_EMAIL = 'Childcare Reservations <noreply@mail.big-heart-ventures.com>'

LOGGING = {
    "version": 1,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        }
    },
    "root": {
        "handlers": ["console"],
        "level": "DEBUG",
    },
}

