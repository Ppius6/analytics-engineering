# Getting Started with Django

As the internet has evolved and continues to evolve, the line between websites and mobile apps has blurred. Both help users interact with data in a variety of ways. 

Fortunately, we can use Django to build a single project that serves a dynamic website as well as a set of mobile apps. 

`Django` is Python's most popular _web framework_, a set of tools designed for building interactive web applications.

`Django` can respond to page requests and make it easier to read and write to a database, manage users, and much more.

## Setting up a Project

When starting work on something as significant as a mobile application, we first need to describe the project's goals in a specification. Then we can identify manageable tasks to achieve those goals.

### Writing a Spec

A full spec details the project goals, describe the project's functionality, and discusses its appearance and user interface. 

Our spec is as follows:

    We will write a web app called Learning Log that allows users to log the topics they are interested in and make journal entries as they learn about each topic. The Learning Log home page will describe the site and invite users to either register or log in. Once logged in, a user can create new topics, add new entries, and read and edit existing entries.

## Project setup

First, we will set up a __virtual environment__. It is a place on our system where we can install packages and isolate them from all other Python packages. 

Can be done using the command:

```python

python -m venv env

```

or if using uv

```python

uv venv env

```

`uv` is a fast Python package installer and resolver written in Rust. It is a modern replacement for `pip` and `venv` that is significantly faster and more reliable.

To activate the environment, we run

```python

source env/bin/activate

```

and to stop using it, we run

```python

deactivate

```

So, to install `django`, we use:

```python

pip install --upgrade pip
pip install django

```

or for `uv`:

```python

uv pip install django

```

or 

```

uv add django

```

if we are in a project with a `pyproject.toml` file. It adds dependencies to our project file and manages them.

### Creating a Project in Django

To create a project, we enter the following commands:

```python

django-admin startproject learning_log_project .

ls 

ls learning_log_project

```

`ls` is short for `list directory` which helps us confirm if `Django` has created a new directory for our project `11_project`. Once confirmed, we can also list what is inside the directory of our project.

```
__init__.py     asgi.py         settings.py     urls.py         wsgi.py
```

The `dot(.)` command at the end of the command creates the new project with a directory structure that will make it easy to deploy the app to a server when we are done developing it.

First, the `manage.py` created outside the project is a short program that takes in commands and feeds them to the relevant part of Django. They will be useful in managing tasks, such as working with databases and running servers.

The project directory contains four files with the most important ones are `settings.py`, `urls.py`, and `wsgi.py`. 

- The `settings.py` controls how Django interacts with our system and manages our project. 
- The `urls.py` file tells Django which pages to build in response to browser requests. 
- The `wsgi.py` file helps Django serve the files it creates. The filename is an acronym for `web server gateway interface`

### Creating the Database

Django stores most of the information for a project in a database, so next we need to create a database that Django can work with. 

We enter the following command:

```python

python manage.py migrate

```

The output is:

```python
(python) pius@Piuss-MBP learning_log % python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
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
  Applying sessions.0001_initial... OK
```

Anytime we modify a database, we say we are _migrating_ the database. 

Issuing the `migrate` command for the first time tells Django to make sure the database matches the current state of the project. The first time we run this command in a new project using `SQLite`, Django will create a new database for us. Here, Django reports that it will prepare the database to store information it needs to handle administrative and authentication tasks.

Running the `ls` command shows that Django created another file called `db.sqlite3`

```python

(python) pius@Piuss-MBP learning_log % ls
db.sqlite3              learning_log_project    manage.py

```

_SQLite_ is a database that runs off a single file; it is ideal for writing simple apps because we will not have to pay much attention to managing the database.

### Viewing the Project

To make sure that Django has set up the project properly, we enter the `runserver` command to view the project in its current state:

```python

python manage.py runserver

```

```python
(python) pius@Piuss-MBP learning_log % python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
January 28, 2026 - 07:51:01
Django version 6.0.1, using settings 'learning_log_project.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

WARNING: This is a development server. Do not use it in a production setting. Use a production WSGI or ASGI server instead.
For more information on production servers see: https://docs.djangoproject.com/en/6.0/howto/deployment/
```

Django should start a server called the `development server` which should help us view the project, how it works as we build it. It can be viewed by following the url specified (`http://127.0.0.1:8000/`) after checking there are no issues, and then reporting the version of Django in use and the name of the settings file in use. 

![Output](scripts/files/django-first.png)

From the url, we see that the project is listening for requests on port `8000` on out computer, also called a `localhost`. The term `localhost` refers to a server that only processes requests on our system; it does not allow anyone else to see the pages we are building.

`NOTE`: _If we receive the error message "That port is already in use," tell Django to use a different port by entering `python manage.py runserver 8001` and then cycling through higher numbers until you find an open port_.