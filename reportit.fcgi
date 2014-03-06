#!/home5/dbriones/python/bin/python
import sys, os

sys.path.insert(0, "/home5/dbriones/python")
sys.path.insert(13, "/home5/dbriones/public_html/sitios/reportit")

os.environ['DJANGO_SETTINGS_MODULE'] = 'reportit.settings'
os.environ['PYTHON_EGG_CACHE'] = 'tmp/trac-eggs'
from django.core.servers.fastcgi import runfastcgi
runfastcgi(method="threaded", daemonize="false")
