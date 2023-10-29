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
fourth_project = Project(
    title="Best shows",
    description="demonstrating API consumption",
    technology="", 
    )
```

```bash
fourth_project.save()
```

```bash
exit()
```

### Now we create Views

- creating view functions to send data from database to the templates to display in the portfolio site.

- create two different views in the projects app
  - index view
  - Detail view
- add both views to views.py file already created by Django!
  - we will import project class from models.py, create a function project_index() that has ORM query for selecting all objects in the projects table, to render the template project_index.html.  

```python
# projects/views.py


from django.shortcuts import render

from projects.models import Project


def project_index(request):

    projects = Project.objects.all()

    context = {

        "projects": projects

    }

    return render(request, "projects/project_index.html", context)
```

- then get the project view 

```python
# project_detail()
# this function has the primary key of the project that is being viewed
# .

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        "project": project
    }
    return render(request, "projects/project_detail.html", context)
```
- Now we get to craft the templates:
  - we can use prestyled components from bootstrap to make the project_index and the project_detail html files
  - in the projects/templates/projects
  ```Bash
  mkdir -p projects/templates/projects
  touch projects/templates/projects/project_index.html
  touch projects/templates/projects/project_detail.html
  - ```
- we will create a grid of bootstrap cards with each card displaying details about the projects.
- to avoid hand coding all the cards, we will use a feature of Django template engine that uses [for loops](https://realpython.com/python-for-loop/)

```html
<!-- projects/templates/projects/project_index.html -->


{% extends "base.html" %}


{% block page_content %}

<h1>Projects</h1>

<div class="row">

{% for project in projects %}

    <div class="col-md-4">

        <div class="card mb-2">

            <div class="card-body">

                <h5 class="card-title">{{ project.title }}</h5>

                <p class="card-text">{{ project.description }}</p>

                <a href="{% url 'project_detail' project.pk %}"

                   class="btn btn-primary">

                    Read More

                </a>

            </div>

        </div>

    </div>

    {% endfor %}

</div>

{% endblock %}
```
- we have extended the base.html
- begun a for loop and looping over all the projects that the context dictionary passes in 
- inside the for loop you can access each individual project.
- to access the projects attributes you use the dot notation inside the double curly brackets 
- {{project.title}} for example.


- create the details page
```html
<!-- projects/templates/projects/project_detail.html -->

{% extends "base.html" %}

{% block page_content %}
<h1>{{ project.title }}</h1>
<div class="row">
    <div class="col-md-4">
        <h5>About the project:</h5>
        <p>{{ project.description }}</p>
        <br>
        <h5>Technology used:</h5>
        <p>{{ project.technology }}</p>
    </div>
</div>
{% endblock page_content %}

```

### Add the routes 

- routes hook up the functions we created to the urls
  - create [projects/urls.py](https://gist.github.com/odhiambo123/4819d6bf9131609f8cf1c96aecf5deb7)
  - hook up the routes to the main project in [personal_portfolio/urls.py](https://gist.github.com/odhiambo123/9b5213d360641f775cbb1b05a79df3a4)
- 
- Apply the existing migrations.
```Bash
  python manage.py migrate
```
- set up your Django Admin site
```Bash
python manage.py createsuperuser
```
open and log in to your admin server
```bash
open http://localhost:8000/admin
```
- The Django admin are lets you manage your projects in the browser instead of in the shell
- [register the models,](https://gist.github.com/odhiambo123/10a21c07684bb7ae26a42d9f097dd862) so you can access them in the Django Admin
  - use the admin.py  file in the projects' app:
  
- 
```python
  # projects/admin.py

from django.contrib import admin
from projects.models import Project

class ProjectAdmin(admin.ModelAdmin):
    pass

admin.site.register(Project, ProjectAdmin)


```
you can add more projects as you please.

<https://realpython.com/get-started-with-django-1/>

## Upload images

- Open models.py and add images to it.
```python
# projects/models.py

from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.FileField(upload_to="project_images/", blank=True)

```
- In the Project model, we define a FileField with a subfolder named project_images/. This is where
- Django stores images when we upload them, we also set blank to true so that it's ok for a project not to have one.
```text
Note: You could be even more explicit and use an ImageField for your images. If you do so, 
then you need to install pillow into your development environment first.
```

- In the sittings.py add the [MEDIA_ROOT](https://docs.djangoproject.com/en/4.2/ref/settings/#media-root) and MEDIA_URL to
- define folder that store image files and present images to users respectively.
- We also need to register the static routes to these files in urls.py in the personal_portfolio/:
```python
# personal_portfolio/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("pages.urls")),
    path("projects/", include("projects.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

```
- add images through Django admin then connect the images in the templates html files

```html
<!-- projects/templates/projects/project_index.html -->


{% extends "base.html" %}


{% block page_content %}

<h1>Projects</h1>

<div class="row">

{% for project in projects %}

    <div class="col-md-4">

        <div class="card mb-2">

            {% if project.image %}

                <img class="card-img-top" src="{{ project.image.url }}">

            {% endif %}

            <div class="card-body">

                <h5 class="card-title">{{ project.title }}</h5>

                <p class="card-text">{{ project.description }}</p>

                <a href="{% url 'project_detail' project.pk %}"

                   class="btn btn-primary">

                    Read More

                </a>

            </div>

        </div>

    </div>

    {% endfor %}

</div>

{% endblock %}

```
- it checks if the project has an image then loads it to the visitor.
- Add images to the details page as well
```html
<!-- projects/templates/projects/project_detail.html -->

{% extends "base.html" %}

{% block page_content %}
<h1>{{ project.title }}</h1>
<div class="row">
    <div class="col-md-8">
        {% if project.image %}
            <img src="{{ project.image.url }}" width="100%">
        {% endif %}
    </div>
    <div class="col-md-4">
        <h5>About the project:</h5>
        <p>{{ project.description }}</p>
        <br>
        <h5>Technology used:</h5>
        <p>{{ project.technology }}</p>
    </div>
</div>
{% endblock page_content %}

```