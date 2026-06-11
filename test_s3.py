import os
import django
import logging
import sys
from dotenv import load_dotenv

load_dotenv()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logging.getLogger('boto3').setLevel(logging.DEBUG)
logging.getLogger('botocore').setLevel(logging.DEBUG)
logging.getLogger('botocore.endpoint').setLevel(logging.DEBUG)

from django.core.files.storage import default_storage

try:
    print("Testing head_object via django-storages default_storage...")
    # This will trigger head_object
    exists = default_storage.exists('test.jpg')
    print(f"SUCCESS: exists() returned {exists} (gracefully handled)")
except Exception as e:
    print(f"FAILED: {e}")

