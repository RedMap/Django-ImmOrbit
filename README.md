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
    'rest_framework.authtoken',
    'markdown',
    'django_filters',
    'django_twilio',
)
````

# settings.py

````
from ImmOrbit.settings import *
....
# Your Twillo Account
TWILIO_ACCOUNT_SID = 'ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
TWILIO_AUTH_TOKEN = 'YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY'
TWILIO_PHONE_NUMBER = '+15005550006' # +15005550006 is Twillos Test Number for DEV
````


# urls.py

````
...
# add for ImmOrbit
from rest_framework.authtoken import views
from ImmOrbit.api import router
# ImmOrbit end
...
  url(r'^api/', include(router.urls)),
  url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
  url(r'^api-token-auth/', views.obtain_auth_token),
...


````

# ToDO
* User Registration via SMS
* Send User Token via SMS or JSON session
