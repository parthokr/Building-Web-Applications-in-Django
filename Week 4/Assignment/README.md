Edit your settings.py as following

Add os.path.join(BASE_DIR, 'polls/templates') to your TEMPLATES
Add 'polls' app to INSTALLED_APPS
Set allowed hosts to all ALLOWED_HOSTS = ['*']
