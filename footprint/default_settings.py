# UrbanFootprint v1.5
# Copyright (C) 2017 Calthorpe Analytics
#
# This file is part of UrbanFootprint version 1.5
#
# UrbanFootprint is distributed under the terms of the GNU General
# Public License version 3, as published by the Free Software Foundation. This
# code is distributed WITHOUT ANY WARRANTY, without implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General
# Public License v3 for more details; see <http://www.gnu.org/licenses/>.

#
from __future__ import absolute_import
from platform import system

import os
import sys
import datetime

import environ

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

CLIENT = None

set_var_from_env = env

# UrbanFootprint's custom User class
AUTH_USER_MODEL = "auth.User"

# Tastypie. Remove the limit of results per page
# This is essential. The app won't funcion with limited results
API_LIMIT_PER_PAGE = 0

# celery generic
CELERY_TASK_RESULT_EXPIRES = 18000  # 5 hours.
CELERY_RESULT_PERSISTENT = True
CELERYD_MAX_TASKS_PER_CHILD = 5

INSTALL_LOCATION = "/srv/"

SOCKETIO_HOST = "0.0.0.0"
SOCKETIO_PORT = "8000"

TILE_CACHE = "Disk"


# This is used so that public tables specific to all clients are created by South
# This allows us to have a single migration path across deployments (see models/__init__.py)
ALL_CLIENTS = ["sacog", "scag_dm"]

DEBUG = False
TEMPLATE_DEBUG = DEBUG

# Use tables with _sample suffixes from the source database when importing feature data
USE_SAMPLE_DATA_SETS = False
# This is true for dev sites
DEV = False

# Set the source for built form imports, or don't import them at all
IMPORT_BUILT_FORMS = "JSON"  # set to 'CSV' to run full import, 'JSON' to use fixtures, or 'FALSE' to skip import
# Skip slow calculations for testing
SKIP_ALL_BUILT_FORMS = False
TEST_SKIP_BUILT_FORM_COMPUTATIONS = False
# Attempts to import features from the 'import' database
EXTERNALLY_IMPORT_FEATURES = True

# Enables or disables geoserver. Disabling it speeds up tests
# The current tastypie API version
API_VERSION = 1
API_PATH = "/footprint/api/v{0}".format(API_VERSION)

PYTHON_INTERPRETER = os.path.join(INSTALL_LOCATION, "calthorpe_env/bin/python")
GIT_ROOT = os.path.join(INSTALL_LOCATION, "calthorpe")
ROOT_PATH = os.path.join(GIT_ROOT, "urbanfootprint")
WEBSOCKETS_ROOT = os.path.join(ROOT_PATH, "websockets")

IMPORT_BASE_FEATURE = False

LOG_FILE = os.path.join(ROOT_PATH, "debug.log")

# This is used by django-guardian
ANONYMOUS_USER_ID = None
GUARDIAN_RAISE_403 = True

ADMINS = (("Admin User", "admin@urbanfootprint.net"),)

LOGIN_REDIRECT_URL = "/footprint"

MANAGERS = ADMINS


DATABASES = {
    "default": env.db_url(),
}
if "SOURCE_DATABASE_URL" in env:
    DATABASES["source"] = env.db_url("SOURCE_DATABASE_URL")
else:
    DATABASES["source"] = DATABASES["default"]

CALTHORPE_ENGINE_PATH = os.path.join(ROOT_PATH, "engines")

TIME_ZONE = "America/Los_Angeles"
USE_TZ = True
# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = "en-us"
DEFAULT_CHARSET = "utf-8"

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True
# If you set this to False, Django will not format dates, numbers and # calendars according to the current locale
USE_L10N = True

ALLOWED_HOSTS = ["*.urbanfootprint.net", "0.0.0.0", "localhost"]

STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.DefaultStorageFinder",
)

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join("/srv/", "calthorpe_media")

# This is used for the development server, only when DEBUG = True
STATIC_DOC_ROOT = MEDIA_ROOT

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = "/media/"
STATIC_URL = "/static/"

TEMP_DIR = "/tmp/"

STATIC_ROOT = os.path.join("/srv", "calthorpe_static")

ADMIN_MEDIA_PREFIX = STATIC_URL + "grappelli/"

# Make this unique, and don't share it with anybody.
SECRET_KEY = "$z7yrc#(il44#+y8y2gwfv8g8u%b+gx!pv16q9%@5l=jl9zx6p"

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    "django.template.loaders.filesystem.Loader",
    "django.template.loaders.app_directories.Loader",
    "django.template.loaders.eggs.Loader",
)

MIDDLEWARE_CLASSES = (
    "django.middleware.common.CommonMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.transaction.TransactionMiddleware",
    "oauth2_provider.middleware.OAuth2TokenMiddleware",
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.static",
)

AUTHENTICATION_BACKENDS = (
    # "oauth2_provider.backends.OAuth2Backend",
    "django.contrib.auth.backends.ModelBackend",
    # "guardian.backends.ObjectPermissionBackend",
)

ROOT_URLCONF = "footprint.urls"

TEMPLATE_DIRS = (
    os.path.join(ROOT_PATH, "footprint/templates"),
    os.path.join(ROOT_PATH, "footprint/main/templates"),
)

FOOTPRINT_TEMPLATE_DIR = os.path.join(ROOT_PATH, "footprint/main/templates/footprint")

FIXTURE_DIRS = (os.path.join(ROOT_PATH, "footprint/fixtures"),)

# Disabling this to allow the stdlib UnitTest
TEST_RUNNER = "django_nose.NoseTestSuiteRunner"

DJANGO_APPS = (
    # "django.contrib.webdesign",
    "django.contrib.staticfiles",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.gis",
)

THIRD_PARTY_APPS = (
    # "django_extensions",
    "django.contrib.admin",
    "django.contrib.admindocs",
    "django",
    "django_tasks",
    "django_tasks.backends.database",
)

PROJECT_APPS = (
    "footprint.main",
    "footprint.upload_manager",
    "footprint.client",
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + PROJECT_APPS

INTERNAL_IPS = ("127.0.0.1",)

# This is the official geojson way of specifying srids. Just insert the SRID in the {0}
SRID_PREFIX = "urn:ogc:def:crs:EPSG::{0}"
DEFAULT_SRID = 4326  # X/Y values, as opposed to Spherical Mercator (EPSG:900913 or 3857) which is meters
# These are the bounds used for 4326, since the project extends infinitely toward the poles
DEFAULT_SRID_BOUNDS = [-20037508.34, -20037508.34, 20037508.34, 20037508.34]

SERIALIZATION_MODULES = {}

# Here we define the default paths that UrbanFootprint will use during installation and stuff

CALTHORPE_DATA_DUMP_LOCATION = os.path.join("/srv/", "datadump")

SENDFILE_ROOT = os.path.join(MEDIA_ROOT, "downloadable")

SENDFILE_URL = "/downloads"
# if you wanted to exclude a folder, add "--exclude 'public/cache/*'"
CALTHORPE_DAILY_DUMP_RSYNC_EXTRA_PARAMS = ""

LOGGING = {
    "version": 1,
    "disable_existing_loggers": True,
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s"
        },
        "simple": {"format": "%(levelname)s %(message)s"},
    },
    "filters": {},
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "stream": sys.stdout,
            #'formatter': 'simple'
        },
    },
    "loggers": {
        "django": {
            "propagate": False,
            "level": "INFO",
        },
        "django.db.backends": {
            "propagate": False,
            "level": "DEBUG",
        },
    },
}

if DEBUG:
    SENDFILE_BACKEND = "sendfile.backends.development"
else:
    SENDFILE_BACKEND = "sendfile.backends.nginx"

DOWNLOAD_FILE_EXPIRY = datetime.timedelta(days=1)

# celery settings
# CELERYBEAT_SCHEDULER = "djcelery.schedulers.DatabaseScheduler"
if system() == "Linux":
    BIN_DIR = "/usr/bin"
elif system() == "Darwin":
    BIN_DIR = "/usr/local/bin"
else:
    import platform

    raise Exception(platform.platform() + "is not supported by UrbanFootprint")

TASKS = {"default": {"BACKEND": "django_tasks.backends.database.DatabaseBackend"}}

SQL_PATH = os.path.join(STATIC_ROOT, "sql")

PATH_CONFIGURATIONS = {
    "default": dict(
        ROOT="/srv/",
        GIT_ROOT="/srv/calthorpe",
        BASE_PATH="/srv/calthorpe/urbanfootprint/",
        PYTHON_INTERPRETER="/srv/calthorpe_env/bin/python",
        ROOT_PATH="/srv/calthorpe/urbanfootprint/",
        PROJ_ROOT="/srv/calthorpe/urbanfootprint/footprint/",
        WEBSOCKETS_ROOT="/srv/calthorpe/urbanfootprint/websockets",
    ),
}


REQUIRED_SHAPEFILE_TYPES = [".shp", ".shx", ".dbf"]
OPTIONAL_SHAPEFILE_TYPES = [".prj"]
EXTRA_SHAPEFILE_TYPES = [
    ".sbn",
    ".sbx",
    ".fbn",
    ".fbx",
    ".ain",
    ".aih",
    ".ixs",
    ".mxs",
    ".atx",
    ".shp.xml",
    ".cpg",
]
OTHER_ALLOWED_TYPES = [".pdf", ".txt"]
SHAPEFILE_TYPES = (
    REQUIRED_SHAPEFILE_TYPES
    + OPTIONAL_SHAPEFILE_TYPES
    + EXTRA_SHAPEFILE_TYPES
    + OTHER_ALLOWED_TYPES
)

STATICFILES_DIRS = (os.path.join(ROOT_PATH, "footprint", "main"),)
# Override this in settings_*.py in order to limit to the host's name
ALLOWED_HOSTS = ["*"]

# The schema to use for importing upload-generated table definitions
IMPORT_SCHEMA = "import"

MAX_UPLOAD_SIZE = 104857600  # 100 Mb

SESSION_COOKIE_AGE = (
    24 * 60 * 60
)  # 1 day, matches the expiry period used in the sproutcore framework
SPROUTCORE_COOKIE_KEY = "user.api_key"

FOOTPRINT_INIT = False
