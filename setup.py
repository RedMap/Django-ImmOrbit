from distutils.core import setup

setup(
    # Application name:
    name="Django-ImmOrbit",

    # Version number (initial):
    version="0.1.0",

    # Application author details:
    author="Steffen Exler",
    author_email="exelstore@gmail.com",

    # Packages
    packages=["ImmOrbit"],

    # Include additional files into the package
    include_package_data=True,

    # Details
    url="https://github.com/RedMap/Django-ImmOrbit",

    #
    # license="LICENSE.txt",
    description="Apache 2.0",

    # long_description=open("README.txt").read(),

    # Dependent packages (distributions)
    install_requires=[
        "djangorestframework",
        "markdown",
        "django-filter",
        "django-twilio",
    ],
)
