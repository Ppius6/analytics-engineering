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

### uv

It is a:

- Fast Python package installer and resolver written in Rust
- Modern replacement for `pip`, `venv`, and `virtualenv`
- Significantly faster and more reliable dependency resolution
- Backward compatible with `pip`

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

## Starting an App

A Django _project_ is organized as a group of individual __apps__ that work together to make the project work as a whole. 

While keeping the development server, we will proceed to start an app:

```python

python manage.py startapp learning_logs

```

This command `startapp _appname_` tells Django to create the infrastructure needed to build an application. When we look in the project directory, there is a new folder called `learning_logs`. 

If we run `ls`, we see the following files:

```python
(python) pius@macbookpro learning_logs % ls
__init__.py     admin.py        apps.py         migrations      models.py       tests.py        views.py
```

The most important files are `models.py`, `admin.py`, and `views.py`. We will use `models.py` to define the data we want to manage in our application.

### Defining Models

While thinking about our data, each user will need to create a number of topics in their learning log. Each entry they make will be tied to a topic, and these entries will be displayed as text. We will also need to store the timestamp of each entry so we can show users when they made each one.

If we open the file `models.py` and look at its existing content:

```python

from django.db import models

# Create your models here.

```

A module called `models` is being imported, and we are being invited to create models of our own. A `model` tells Django how to work with the data that will be stored in the app. A model is a class; it has attributes and methods, just like every class we have discussed.

For the model for the topics users will store:

```python

from django.db import models


class Topic(models.Model):
    """A topic the user is learning about."""

    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        """Return a string representation of the model."""
        return self.text
```

We have created a class called `Topic` which inherits from `Model`, a parent class included in Django that defines a model's basic functionality. We add two attributes to the Topic class: `text` and `date_added`.

The `text` attribute is a `CharField`, a piece of data that is made up or characters or text. We can use `CharField` when we want to store a small amount of text, such as a name, a title, or a city. When we define a `CharField` attribute, we have to tell Django how much space it should reserve in the database. Here, we give it a `max_length` of 200 characters, which should be enough to hold most topic names.

The `date_added` attribute is a `DateTimeField`, a piece of data that will record a date and time. We pass the argument `auto_now_add=True`, which tells Django to automatically set this attribute to the current date and time whenever the user creates a new topic.

It is a good idea to tell Django how we want it to represent an instance of a model. If a model has a `__str__()` method, Django calls that method whenever it needs to generate output referring to an instance of that model. Here, we have written a `__str__()` method that returns the value assigned to the text attribute.

NOTE: To see the different kinds of fields we can use in Django models, refer to the [Django Model Field Reference](https://docs.djangoproject.com/en/6.0/ref/models/fields/).

### Activating Models

To use our models, we have to tell Django to include our app in the overall project. We do this by modifying the `settings.py` file in the project directory, and adding our app to the `INSTALLED_APPS` list.

```python

# Application definition

INSTALLED_APPS = [
    # My apps
    'learning_logs',
    # Default Django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

```

We add the name of our app, `learning_logs`, to the list of installed apps.

Grouping apps together in a project helps keep track of them as the project grows to include more apps. We place our own apps before the default Django apps to make it easier to find them later.

Now, we need to tell Django to modify the database so it can store information related to the model `Topic` we just created. We do this in two steps:

```python

python manage.py makemigrations learning_logs
python manage.py migrate

```

The first command, `makemigrations`, tells Django to figure out how to modify the database so it can store information for the models we have created. The second command, `migrate`, applies those changes to the database.

The output of the first command is:

```python

(python) pius@macbookpro learning_log % python manage.py makemigrations learning_logs
Migrations for 'learning_logs':
  learning_logs/migrations/0001_initial.py
    + Create model Topic
(python) pius@macbookpro learning_log %

```

Django reports that it has created a migration file called `0001_initial.py` in the `migrations` directory of our app. This file contains the instructions Django will use to modify the database.

When we run the `migrate` command, Django applies the migration and modifies the database accordingly. The output is:

```python

Operations to perform:
  Apply all migrations: admin, auth, contenttypes, learning_logs, sessions
Running migrations:
  Applying learning_logs.0001_initial... OK
(python) pius@macbookpro learning_log %
```

Django reports that it has applied the migration we just created. Now the database is ready to store information related to the `Topic` model.

Whenever we want to modify the data that Learning Log manages, we will follow these three steps: 

- Modify the models in `models.py`

- Call `makemigrations` to tell Django to prepare a migration

- Tell Django to apply the migration to the database by calling `migrate`

### The Django Admin Site

Django makes it easy to work with our models through its admin site. It is only meant to be used by the site administrators, not by regular users of the site.

#### Setting up a Superuser

Django allows us to create a `superuser`, a user who has all privileges available on a site. A user's `privileges` control the actions they can take. The more restrictive privilege settings allow a user to only read public information on the site. Registered users typically have the privilege of reading their own private data and some selected information available only to members.

To create a superuser in Django, we enter the following command:

```python

python manage.py createsuperuser

```

The command above gives us prompts to enter a username, email address, and password for the superuser. After entering the required information, the superuser is created.

#### Registering Models with the Admin Site

Django includes some models in the admin site automatically, such as `User` and `Group`, but the models we create need to be added manually. 

When we started the `learning_logs` app, Django created an `admin.py` file in the same directory as `models.py`. 

```python

from django.contrib import admin

# Register your models here.
```

To register `Topic` with the admin site, we enter the following:

```python

from django.contrib import admin

from .models import Topic

admin.site.register(Topic)
```

The code above first imports the model we want to register, `Topic`. The dot in front of `models` tells Django to look for `models.py` in the same directory as `admin.py`. The code `admin.site.register()` tells Django to manage our model through the admin site.

To access the admin site, we use our superuser credentials. We navigate to `http://localhost:8000/admin/

This page allows us to add new users and groups, and change existing ones. We can also work with data related to the `Topic` model that we just defined.

![Admin](scripts/files/django-admin.png)

#### Adding Topics

Now that `Topic` has been registered with the admin site, we can add our first topic. The steps are as follows:

- Click `Topics` to go to the topics page, which is mostly empty since we have not added any topics yet.

- Click `Add Topic` in the upper right corner to go to the page for adding a new topic.

- Enter a name for the topic in the `Text` field. The `Date added` field is filled in automatically. You will be sent back to the `Topics` page, which now shows the topic you just added.

After adding some topics, the examples page looks like this:

![Topics](scripts/files/topics.png)

### Defining the Entry Model

For a user to record what they have been learning about chess and rock climbing, we need to define a model for the kinds of entries users can make in their learning logs. Each entry needs to be associated with a particular topic. This relationship is called a `one-to-many` relationship because each topic can have many entries, but each entry is associated with only one topic.

To define the `Entry` model, we open `models.py` in the `learning_logs` app and add the following code:

```python

from django.db import models


class Topic(models.Model):
    """A topic the user is learning about."""

    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.text


class Entry(models.Model):
    """Something specific learned about a topic"""

    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'entries'
        
    def __str__(self):
        """Return a simple string representing the entry."""
        return f"{self.text[:50]}..."

```

In the code above, the `Entry` class inherits from Django's base `Model` class, just as `Topic` did. The first attribute, `topic` is a `ForeignKey` instance, meaning a reference to another record in the database. 

This is the code that connects each entry to a specific topic. Each topic is assigned a `key`, or ID, when it's created. When Django needs to establish a connection between two pieces of data, it uses the keys associated with each piece of information. 

We will use these connections shortly to retrieve all the entries associated with a certain topic. The `on_delete=models.CASCADE` argument tells Django that when a topic is deleted, all the entries associated with that topics should be deleted as well. This is known as a `cascading delete`.

Next, the attribute `text` is an instance of `TextField`. It does not need a size limit, because we do not want to limit the size of individual entries. The `date_added` attribute allows us to present entries in the order they were created, and to place a timestamp next to each entry.

The `Meta` class is nested inside the `Entry` class. The `Meta` class holds extra information for managing a model; here, it lets us set a special attribute telling Django to use `Entries` when it needs to refer to more than one entry. Without this, Django would refer to multiple entries as `Entrys`.

The `__str__()` method tells Django which information to show when it refers to individual entries. Because an entry can be a long body of text,`__str__()` returns just the first 50 characters of text. We also add an ellipsis to clarify that we are not always displaying the entire entry. 

### Migrating the Entry Model

Since we have added a new model, we need to migrate the database again. This process will become quite familiar: 

- You modify `models.py`,
- Run the command `python manage.py makemigrations app_name`
- Then run the command `python manage.py migrate`

The output:

```python

Migrations for 'learning_logs':
  learning_logs/migrations/0002_entry.py
    + Create model Entry
(python) pius@macbookpro learning_log % python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, learning_logs, sessions
Running migrations:
  Applying learning_logs.0002_entry... OK
(python) pius@macbookpro learning_log %

```

A new migration called _0002_entry.py_ is generated, which tells Django how to modify the database to store information related to the model `Entry`. When we issue the `migrate` command, we see that Django applies this migration and everything worked properly.

### Registering Entry with the Admin Site.

We also need to register the `Entry` model. The `admin.py` should look like this:

```python

from django.contrib import admin

from .models import Topic, Entry

admin.site.register(Topic)
admin.site.register(Entry)

```

`Entries` is now listed:

![Entries](scripts/files/entries.png)

We will then add an entry for one of our topic created earlier.


  The opening is the first part of the game, roughly the first ten moves or so. In the opening, it is a good idea to do three things - bring out your bishops and knights, try to control the center of the board, and castle your king.

  Of course, these are just guidelines. It will be important to learn when to follow these guidelines and when to disregard these suggestions.

When we click `Save`, we are brought back to the main admin page for entries. Here, we will see the benefit of using `text[:50]` as the string representation for each entry; it is much easier to work with multiple entries in the admin interface if you see only the first part of an entry, rather than the entire text of each entry. 

We can add more entries:

For `Chess`

  In the opening phase of the game, it is important to bring out your bishops and knights. These pieces are powerful and maneuverable enough to play a significant role in the beginning moves of a game.

For `Rock Climbing`

  One of the most important concepts in climbing is to keep your weight on your feet as much as possible. There's a myth that climbers can hang all day on their arms. In reality, good climbers have practiced specific ways of keeping their weight over their feet whenever possible.

These three entries will give us something to work with as we continue to develop `Learning Log`.

### The Django Shell

Now that we have entered some data, we can examine it programmatically through an interactive terminal session. This interactive environment is called the Django _shell_ and is a great place to test and troubleshoot our projects.

An example of an interactive shell session is as shown;

```python

(python) pius@macbookpro learning_log % python manage.py shell                                                     
14 objects imported automatically (use -v 2 for details).

Cmd click to launch VS Code Native REPL
Python 3.14.2 (main, Jan 14 2026, 23:37:46) [Clang 21.1.4 ] on darwin
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from learning_logs.models import Topic
>>> Topic.objects.all()
<QuerySet [<Topic: Chess>, <Topic: Rock Climbing>]>
>>>

```

After using the method `Topic.objects.all()` to get all instances of the model `Topic`, we get a `queryset`

We can further loop over the queryset just as we would loop over a list. Here is how we can see the ID that has been assigned to each topic object:

```python

>>> topics = Topic.objects.all()
>>> for topic in topics:
...     print(topic.id, topic)
... 
1 Chess
2 Rock Climbing
>>>

```

We assign the queryset to `topics` and then print each topic's `id` attribute and the string representation of each topic. We can see that `Chess` has an ID of `1` and `Rock Climbing` has an ID of `2`

If we know the ID of a particular object, we can use the method `Topic.objects.get()` to retrieve that object and examine any attribute the object has. We can look at the `text` and `date_added` values for `Chess`:

```python

>>> t = Topic.objects.get(id=1)
>>> t.text
'Chess'
>>> t.date_added
datetime.datetime(2026, 1, 30, 6, 26, 14, 3773, tzinfo=datetime.timezone.utc)
>>> 

```

We can also look at the entries related to a certain topic. Earlier we defined the `topic` attribute for the `Entry` model. This was a `Foreignkey`, a connection between each entry and a topic. Django can use this connection to get every entry related to a certain topic, like this:

```python

>>> t.entry_set.all()
<QuerySet [<Entry: The opening is the first part of the game, roughly...>, <Entry: In the opening phase of the game, it is important ...>]>
>>>

```

To get data through a foreign key relationship, we can use the lowercase name of the related model followed by an underscore and the word `set`. For example, say we have the models `Pizza` and `Topping`, and `Topping` is related to `Pizza` through a foreign key. If our object is called `my_pizza`, representing a single pizza, we can get all of the pizza's toppings using the code `my_pizza.topping_set.all()`

We will use this syntax when we begin to code the pages users can request. 

## Making Pages: The Learning Log Home Page