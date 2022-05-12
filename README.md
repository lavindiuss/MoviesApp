# Movies APP V0.0.1

**Programming Language**

- Python :: 3.8.2

**Framework**

- Django :: 2.2

**Installation Steps**

- pip install virtualenv
- virtualenv env
- source ./env/bin/activate
- pip install -r requirements.txt
- python manage.py migrate
- python manage.py runserver
- Note: you should have mysql server running on your machine.
- Now feel free to fetch your movies data :D
- All configuration variables included in .env file.
- Depending on your device configurations you may face this error --> AttributeError: 'str' object has no attribute 'decode' on migration, don't worry.. kindly follow this small solution https://stackoverflow.com/questions/56820895/migrations-error-in-django-2-attributeerror-str-object-has-no-attribute-dec

**Postman Collection**

- https://www.getpostman.com/collections/7fa1d94e4db297204daa
