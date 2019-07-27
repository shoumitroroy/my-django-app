import os, sys
sys.path.append('/home/shoumitro/myproject/myproject')
sys.path.append('/home/shoumitro/myproject/myproject/cms')
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings.py'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()
