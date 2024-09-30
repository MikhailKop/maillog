DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("POSTGRES_NAME", default="maillog_database"),
        "USER": os.getenv("POSTGRES_USER", default="app"),
        "PASSWORD": os.getenv("POSTGRES_PASSWORD"),
        "HOST": os.getenv("POSTGRES_HOST", default="127.0.0.1"),
        "PORT": os.getenv("POSTGRES_PORT", default="5432"),
        "OPTIONS": {"options": "-c search_path=public,maillog"},
    }
}
