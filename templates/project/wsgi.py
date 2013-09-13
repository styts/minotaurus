import os
import sys
import glob

### Put required packages on sys path ###

# site-packages
path = os.path.abspath(os.path.join(os.path.dirname(__file__),
    "../env/lib/python2.%s/site-packages" % sys.version_info[1]))
if path not in sys.path:
    sys.path.append(path)

# packages in env/src
path = os.path.abspath(os.path.join(os.path.dirname(__file__),
    "../env/src"))
for f in glob.glob(path + "/*"):
    if os.path.isdir(f) and f not in sys.path:
        sys.path.append(f)

# project dir
path = os.path.abspath(os.path.join(os.path.dirname(__file__), "."))
if path not in sys.path:
    sys.path.append(path)

# one above project dir
path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if path not in sys.path:
    sys.path.append(path)

# lib above project dir
path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../lib"))
if path not in sys.path:
    sys.path.append(path)

print sys.path

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
