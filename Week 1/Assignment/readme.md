# Creating app config file
## **apps.py** should look like
> Assume your app name is **sample**
```
from django.apps import AppConfig

class sample_app_config(AppConfig):
    name = 'sample'
    verbose_name = 'sample_app'
```

# Add app into **settings.py**

```
...
INSTALLED_APPS = [
    ...,
    sample.apps.sample_app_config
]
...
```
