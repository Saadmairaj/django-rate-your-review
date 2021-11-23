# django-rate-your-review

[![CodeFactor](https://www.codefactor.io/repository/github/saadmairaj/django-rate-your-review/badge/master)](https://www.codefactor.io/repository/github/saadmairaj/django-rate-your-review/overview/master)

An online application that will give a rating to your reviews.

<p align="center">
  <img width="700" alt="Screenshot 2021-04-09 at 13 31 57" src="https://user-images.githubusercontent.com/46227224/114148942-f6ee5e80-9937-11eb-8fa3-4d5ccda6e393.png">
  <img width="700" alt="Screenshot 2021-04-09 at 13 30 36" src="https://user-images.githubusercontent.com/46227224/114148894-ea6a0600-9937-11eb-91c3-c4769bf8d4c4.png"> 
<p>

## Requirement

Install all the requirements with [requirements.txt](https://github.com/Saadmairaj/django-rate-your-review/blob/master/requirements.txt) with the command

```bash
pip install -r requirements.txt
```

Main packages used in the application are:

- Django
- django-crispy-forms
- tensorflow

## Installation

Install and run the server

1. Clone the repository.

2. Create a virtual environment in the cloned directory with the following command:

```bash
$ python3 -m venv env
```

Note: If you get an error saying venv doesn't exist then install venv first with command [`pip install virtualenv`](https://pypi.org/project/virtualenv/).

3. After creating the virtual environment, activate it with command:

```bash
$ source ./env/bin/activate
```

4. Now install the requirements into the virtual environment `evn` with command:

```bash
$ pip install -r requirements.txt
```

5. Create migrations and migrate with

```bash
$ python manage.py makemigrations
$ python manage.py migrate

Operations to perform:
  Apply all migrations: admin, auth, contenttypes, review, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying review.0001_initial... OK
  Applying review.0002_auto_20210329_0722... OK
  Applying review.0003_auto_20210329_0726... OK
  Applying review.0004_review_last_update... OK
  Applying review.0005_auto_20210329_1901... OK
  Applying review.0006_consent... OK
  Applying review.0007_auto_20211123_0940... OK
  Applying sessions.0001_initial... OK
```

6. Create superuser with

```bash
$ python manage.py createsuperuser

Username (leave blank to use 'saad'): admin
Email address: admin@gmail.com
Password:
Password (again):
Superuser created successfully.
```

6. After installing all the requirements we are set to go! Just go run the server with the following command

```bash
$ python manage.py runserver
```
