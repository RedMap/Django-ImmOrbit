# Django-ImmOrbit

# Installation

Install using pip, including any optional packages you want...

````
pip install --upgrade git+git://github.com/RedMap/Django-ImmOrbit.git@master
````

Add 'rest_framework' to your <INSTALLED_APPS> setting.

````
INSTALLED_APPS = (
    ...
    'ImmOrbit',
    'rest_framework',
    'markdown',
    'django_filters',
)
````

# settings.py

````
from ImmOrbit.settings import *
````

# urls.py

````
...
from ImmOrbit.api import router
...
  url(r'^api/', include(router.urls)),
  url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
...


````
