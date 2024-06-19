# settings.py

import os

# BASE_DIR is usually defined at the top of the settings.py file
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Media files (uploads)
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
