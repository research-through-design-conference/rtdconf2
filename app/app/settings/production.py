from base import *

AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']

AWS_STORAGE_BUCKET_NAME = 'rtd-production'

STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, '../../srv/assets'),
)

STATIC_ROOT = 'http://rtd-production.s3.amazonaws.com/static/'
STATIC_URL = 'http://rtd-production.s3.amazonaws.com/static/'

MEDIA_ROOT = 'http://rtd-production.s3.amazonaws.com/media/'
MEDIA_URL = 'http://rtd-production.s3.amazonaws.com/media/'
