# portfolio_app

# portfolio_Apps

```bash
mkdir rp-portfolio
```

```bash

cd rp-portfolio

```

```bash
python -m venv venv

```

 ```bash
 source venv/bin/activate

 ```

```bash
python -m pip install Django

```

- Make sure you’re in the rp_portfolio/ directory, and the virtual environment is activated.
- create the project

```bash

django-admin startproject personal_portfolio .

```

- don't forget the dot (.)

-

```md
rp-portfolio/
│
├── personal_portfolio/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── venv/
│
└── manage.py
```

start the developnebt server

```bash
python3 manage.py runserver

```

### create a second app for pages

```bash
python manage.py startapp pages

```

- After creating the second app, install it to the project by adding it to the main app's settings.py installed apps list

-

```python
INSTALLED_APPS = [
    "pages.apps.PagesConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]
```

### create a view in the apps view.py  file

```python
# pages/views.py

from django.shortcuts import render

def home(request):
    return render(request, "pages/home.html", {})

```

- create the HTML templates  directory with subdirectories for each app you create to host the app's templates. example:

```bash
mkdir -p pages/templates/pages
touch pages/templates/pages/home.html

```

### Add a route

- create a new route that will tell django when to serve the view by creating a new route to the project.
- in the main app's folder (personal_portfolio) open the urls.py and add the configuration.

```python
# personal_portfolio/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("pages.urls")),
]

```

- This path url pattern creates a new route for the project
- Create the pages.urls module in the pages directory

```bash

touch pages/urls.py

```

# pages/urls.py

```python


from django.urls import path
from pages import views

urlpatterns = [
    path("", views.home, name='home'),
]

```

### Add bootstrap to the project

- create 'templates' directory in the root folder.

```bash
cd rp_portfolio
mkdir templates/
touch templates/base.html
```

- All future templates that you create will extend base.html and inherit the Bootstrap styling on every page without having to import the styles again.

### use of {% block %}

- can be used to define content blocks that you can use to override child templates that extend the parent template.
- example
  - adjust the home.html

```html
{% extends "base.html" %}

{% block page_content %}
    <h1>Hello, World!</h1>
{% endblock page_content %}

```

- now tell the project that base.html exists.

 ```bash
 # personal_portfolio/settings.py

# ...

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            BASE_DIR / "templates/",
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

# ...

 ```

- we defined the constant BASE_DIR in the settings.py and it point to the root directory.
- now we join the path with the forward slash operator (/) from pathlib to point to the templates/ directory and add it to the DIRS list

```bash
python3 manage.py runserver

```

- adding the projects app
 use the command to start a new app called projects.

 ```bash
 python manage.py startapp projects

 ```

 then add     "projects.apps.ProjectsConfig",  to the installed projects at # personal_portfolio/settings.py

```python
# personal_portfolio/settings.py

# ...

INSTALLED_APPS = [
    "pages.apps.PagesConfig",
    "projects.apps.ProjectsConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

# ...

```

### DEFINE A MODEL

Django has a built in ```object relational mapping (ORM)```
Using ORM helps avoid having to learn a whole new language for the database

in ORM the classes that represent tables are called models and they live in models.py module of each app

For this app we only need one table to show our projects which means we only make one model in the models.py

there are many django built in [model types](https://docs.djangoproject.com/en/4.2/ref/models/fields/)

after creating the class now we need to create the database by creating a migration, a migrations is a file containing Migration class with rules that tell Django what changes you are making to the database.

run:

```bash

python3 manage.py makemigrations projects


```

 this creates the folder migrations inside projects/ and a file named 0001_initial.py is also created. this is the files that contains the instructions for Django on what to perform on the Database..
 migrate the project

 ```bash
 python3 manage.py migrate projects

 ```

- In the comands above we added projects to let Django know that we are adding migrations to the projects project only. if this is not done then all the migrations will be done to all default Django projects

 now you should see the file db.sqlite3 which is our database, now we create rows in our table to list previous projects we want to show on the site.

### Diving into Django shell

- It is similar to python shell but allows you to access the database and create entries.
- To enter Django shell use:

```bash
python3 manage.py shell
```

notice now we see the carets (>>>)

import your project here

```powershell
from projects.models import Project
```

create an instance of the projects class in the Django shell

```bash
first_project = Project(
    title="Intro to HTML, CSS, JavaScript",
    description="A web development project.",
    technology="GitHub, Ruby, Markdown, Html, CSS, JS", 
    )
```

- save the project

```bash
first_project.save()
```

- Repeat for second, third and all other projects.

```bash
second_project = Project(
    title="Intro to HTML, CSS, JavaScript",
    description="A web development project.",
    technology="GitHub, Ruby, Markdown, Html, CSS, JS", 
    )
```

<https://realpython.com/get-started-with-django-1/>
