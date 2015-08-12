# Django-ImmOrbit

# Installation

Install using pip, including any optional packages you want...

````
pip install --upgrade git+git://github.com/RedMap/Django-ImmOrbit.git@master
pip install djangorestframework
pip install markdown       # Markdown support for the browsable API.
pip install django-filter  # Filtering support
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
REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}
````
