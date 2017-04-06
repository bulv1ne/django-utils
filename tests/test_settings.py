import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SECRET_KEY = 'secret_key'

DEBUG = False

ALLOWED_HOSTS = []

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'django.contrib.humanize',
    'django.contrib.sites',
    'django.contrib.redirects',
    'pipeline',
    'utils',
)

MIDDLEWARE = (
    'utils.middlewares.latency.LatencyMiddleware',
    'django.contrib.redirects.middleware.RedirectFallbackMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'tests.urls'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',
    },
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Stockholm'

USE_I18N = True

USE_L10N = True

USE_TZ = True

UNICODE_JSON = True

SITE_URL = 'http://www.example.com'

STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')

STATIC_URL = '/static/'

STATICFILES_STORAGE = 'utils.storage.PipelineManifestStorage'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'pipeline.finders.PipelineFinder',
)

DEFAULT_FILE_STORAGE = 'utils.storage.S3MediaStorage'
MEDIA_BUCKET = 'sprancher-media'

PIPELINE = {
    'STYLESHEETS': {
        'main': {
            'source_filenames': (
                'example/sass/main.scss',
            ),
            'output_filename': 'example/css/main.css',
        },
    },
    'COMPILERS': [
        'utils.pipeline_compilers.SassCompiler',
    ],
    'CSS_COMPRESSOR': 'utils.pipeline_compressors.CssCompressor',
}

RAVEN_CONFIG = None
