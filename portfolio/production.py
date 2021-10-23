from .settings import *
from decouple import config
import dj_database_url

ALLOWED_HOSTS = ['.herokuapp.com', ".com"]


DEBUG = True # CHANGE TO FALSE
CORS_REPLACE_HTTPS_REFERER = True
HOST_SCHEME = "https://"
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_SECONDS = 1000000
SECURE_FRAME_DENY = True


SECURE_HSTS_PRELOAD = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True

# Content Security Policy
CSP_DEFAULT_SRC = ("'none'", )
CSP_STYLE_SRC = ("'self'", )
CSP_SCRIPT_SRC = ("'self'", )
CSP_IMG_SRC = ("'self'", )
CSP_FONT_SRC = ("'self'", )
# Google Tag Manager or Google Analytics should be allowed in your CSP policy.
CSP_DEFAULT_SRC = ("'none'", )
CSP_STYLE_SRC = ("'self'", "fonts.googleapis.com", "'sha256-/3kWSXHts8LrwfemLzY9W0tOv5I4eLIhrf0pT8cU0WI='")
CSP_SCRIPT_SRC = ("'self'", "ajax.googleapis.com", "www.googletagmanager.com", "www.google-analytics.com")
CSP_IMG_SRC = ("'self'", "data:", "www.googletagmanager.com", "www.google-analytics.com")
CSP_FONT_SRC = ("'self'", "fonts.gstatic.com")
CSP_CONNECT_SRC = ("'self'", )
CSP_OBJECT_SRC = ("'none'", )
CSP_BASE_URI = ("'none'", )
CSP_FRAME_ANCESTORS = ("'none'", )
CSP_FORM_ACTION = ("'self'", )
CSP_INCLUDE_NONCE_IN = ('script-src',)

X_FRAME_OPTIONS = 'ALLOWALL'
XS_SHARING_ALLOWED_METHODS = ['POST','GET','OPTIONS', 'PUT', 'DELETE']

# Database
DATABASES = {
    'default': {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
    }
}
prod_db = dj_database_url.config()
DATABASES['default'].update(prod_db)

MIDDLEWARE += [
    'whitenoise.middleware.WhiteNoiseMiddleware',
]