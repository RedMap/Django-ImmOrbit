# Django-ImmOrbit

# Installation

Install using pip, including any optional packages you want...

````
pip install djangorestframework
git clone git@github.com:RedMap/Django-ImmOrbit.git
pip install markdown       # Markdown support for the browsable API.
pip install django-filter  # Filtering support
````

Add 'rest_framework' to your <INSTALLED_APPS> setting.

````
INSTALLED_APPS = (
    ...
    'ImmOrbit',
    'rest_framework',
)
````
