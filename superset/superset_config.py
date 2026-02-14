import os
import logging
from flask_caching.backends.filesystemcache import FileSystemCache
from celery.schedules import crontab

# Add a visible marker for terminal logs
print("\n" + "="*80)
print("🔴 LOADING CUSTOM CONFIG FROM ROOT - IFRAME FIX APPLIED")
print("="*80 + "\n")

logger = logging.getLogger()

# ========================
# Secret Key
# ========================
SECRET_KEY = os.getenv(
    "SUPERSET_SECRET_KEY",
    "1NRafdQKXuPl/s2yFDy9XZWbUXrdoID1xwjL4SyDenocaQTWKMcbXo05"
)

# ========================
# Database Configuration
# ========================
# We use the default database at ~/.superset/superset.db
# Unless explicitly overridden via environment variables
# SQLALCHEMY_DATABASE_URI = 'sqlite:////home/sabya/.superset/superset.db'

# Global Postgres connection for metadata
SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://superset_user:StrongPassword123@52.202.251.212:5432/superset_metadata"
# SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://superset_user:XXXXXXXXXX@127.0.0.1:5432/superset_demo"
# ========================
# Caching / Redis (optional for dev)
# ========================
REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = os.getenv("REDIS_PORT", "6379")
REDIS_CELERY_DB = os.getenv("REDIS_CELERY_DB", "0")
REDIS_RESULTS_DB = os.getenv("REDIS_RESULTS_DB", "1")

# RESULTS_BACKEND = FileSystemCache("/tmp/superset_sqllab_cache") # Already default

CACHE_CONFIG = {
    "CACHE_TYPE": "FileSystemCache",
    "CACHE_DIR": "/tmp/superset_cache",
    "CACHE_DEFAULT_TIMEOUT": 300,
}

DATA_CACHE_CONFIG = CACHE_CONFIG
THUMBNAIL_CACHE_CONFIG = CACHE_CONFIG

# ========================
# Celery Config (Disabled Redis dependency for local dev)
# ========================
class CeleryConfig:
    # broker_url = f"redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_CELERY_DB}"
    # result_backend = f"redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_RESULTS_DB}"
    worker_prefetch_multiplier = 1
    task_acks_late = False
    beat_schedule = {
        "reports.scheduler": {
            "task": "reports.scheduler",
            "schedule": crontab(minute="*", hour="*"),
        },
        "reports.prune_log": {
            "task": "reports.prune_log",
            "schedule": crontab(minute=10, hour=0),
        },
    }

CELERY_CONFIG = CeleryConfig

# ========================
# Feature Flags
# ========================
FEATURE_FLAGS = {
    "EMBEDDED_SUPERSET": True,
    "GUEST_TOKEN": True,
    "DASHBOARD_NATIVE_FILTERS": True,
    "ALERT_REPORTS": True,
    "DATASET_FOLDERS": True,
    "DASHBOARD_RBAC": True,
}

# ========================
# Guest / Public role
# ========================
GUEST_ROLE_NAME = "Public"
PUBLIC_ROLE_LIKE = "Public"

# ========================
# Guest Token JWT Settings
# ========================
GUEST_TOKEN_JWT_SECRET = "a4ebcdcff80762d26910655acef70db602801785f38dc337db6742354e71fd93"
GUEST_TOKEN_JWT_ALGO = "HS256"
GUEST_TOKEN_HEADER_NAME = "X-GuestToken"
GUEST_TOKEN_JWT_EXP_SECONDS = 7 * 24 * 60 * 60  # 7 days

# ========================
# CORS Configuration
# ========================
ENABLE_CORS = True
CORS_OPTIONS = {
    "supports_credentials": True,
    "origins": [
        "http://localhost:3000",
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    "allow_headers": ["*"],
    "expose_headers": ["*"],
    "methods": ["GET", "POST", "OPTIONS"],
    "resources": {"*": {"origins": "*"}},
}

# ========================
# Cookie and session settings for dev (Modified for Chrome iframe)
# ========================
SESSION_COOKIE_SAMESITE = 'None'
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True

# ========================
# Talisman / CSP configuration for iframe embedding
# ========================
TALISMAN_ENABLED = True
TALISMAN_CONFIG = {
    "content_security_policy": {
        "base-uri": ["'self'"],
        "default-src": ["'self'"],
        "img-src": ["'self'", "blob:", "data:"],
        "worker-src": ["'self'", "blob:"],
        "connect-src": ["'self'"],
        "object-src": ["'none'"],
        "style-src": ["'self'", "'unsafe-inline'"],
        "font-src": ["'self'"],
        "script-src": ["'self'", "'unsafe-inline'", "'unsafe-eval'"],
        "frame-ancestors": [
            "'self'",
            "http://localhost:3000",
            "http://localhost:5173",
            "http://127.0.0.1:5173",
            "https://localhost:8088",
        ],
        "frame-src": ["'self'"],
    },
    "content_security_policy_nonce_in": ["script-src"],
    "force_https": False,
    "session_cookie_secure": False,
    "frame_options": None,
}

# IMPORTANT: Dev mode uses TALISMAN_DEV_CONFIG
TALISMAN_DEV_CONFIG = TALISMAN_CONFIG

# IMPORTANT: Chrome often rejects X-Frame-Options: ALLOWALL
# We rely on TALISMAN frame-ancestors instead
OVERRIDE_HTTP_HEADERS = {}
HTTP_HEADERS = {}

# ========================
# Logging
# ========================
ALERT_REPORTS_NOTIFICATION_DRY_RUN = True
SQLLAB_CTAS_NO_LIMIT = True

log_level_text = os.getenv("SUPERSET_LOG_LEVEL", "INFO")
LOG_LEVEL = getattr(logging, log_level_text.upper(), logging.INFO)
