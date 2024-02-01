# ZOGO

Zogo is a small program that supports static grapevine for whistleblowing in both
public and private sectors. 

It puts modular archtecture in practice as it consist of multiple models, which are 
serialized and served via Django REST Framework. 

This program is integrated with Elasticsearch, and respective endpoints are wired up 
to blooster looking up different authors, categories, and articles.

To keep the  code clean and modular, the project is split into the following apps:

    blog - for our Django models, serializers, and ViewSets
    search - for Elasticsearch documents, indexes, and queries

### How setup the project locally:

$ mkdir django-drf-elasticsearch 
$ cd django-drf-elasticsearch
$ python3.12 -m venv env
$ source env/bin/activate

(env)$ pip install django==4.2.7
(env)$ django-admin startproject core .

### Populate the Database

You need some initial data to work with the program. I've created a simple command you can use to populate the database.

Create a new folder in "data" on the root directory of the project and then inside 
of the folder, create a new file called populate_db.py.

               management
               └── commands
                     └── populate_db.py

Copy the file contents the following contents and paste it inside your populate_db.py:

```
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from blog.models import Category, Article


class Command(BaseCommand):
    help = "Populates the database with some testing data."

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Started database population process..."))

        if User.objects.filter(username="BiKodes").exists():
            self.stdout.write(self.style.SUCCESS("Database has already been populated. Cancelling the operation."))
            return

        # Create users
        bikodes = User.objects.create_user(username="bikodes", password="really_strong_password123")
        bikodes.first_name = "BiKodes"
        bikodes.last_name = "Olianga"
        bikodes.save()

        jasiri = User.objects.create_user(username="jasiri_", password="really_strong_password123")
        jasiri.first_name = "jasiri"
        jasiri.last_name = "Biko"
        jasiri.save()

        almasi = User.objects.create_user(username="almasi", password="really_strong_password123")
        almasi.first_name = "almasi"
        almasi.last_name = "Davis"
        almasi.save()

        # Create categories
        system_administration = Category.objects.create(name="System administration")
        seo_optimization = Category.objects.create(name="SEO optimization")
        programming = Category.objects.create(name="Programming")

        # Create articles
        website_article = Article.objects.create(
           title="How to code and deploy a website?",
           author=bikodes,        
           type="TU",
           content="There are numerous ways of how you can deploy a website...",
        )
        website_article.save()
        website_article.categories.add(programming, system_administration, seo_optimization)

        google_article = Article.objects.create(
           title="How to improve your Google rating?",
           author=jasiri,
           type="TU",
           content="Firstly, add the correct SEO tags...",
        )
        google_article.save()
        google_article.categories.add(seo_optimization)

        programming_article = Article.objects.create(
           title="Which programming language is the best?",
           author=jasiri,
           type="RS",
           content="The best programming languages are:\n1) Python\n2) Golang\n3) Golang...",
        )
        programming_article.save()
        programming_article.categories.add(programming)

        ubuntu_article = Article.objects.create(
           title="Installing the latest version of Ubuntu",
           author=almasi,
           type="TU",
           content="In this tutorial, we'll take a look at how to setup the latest version of Ubuntu. Ubuntu "
                   "(/ʊˈbʊntuː/ is a Linux distribution based on Debian and composed mostly of free and open-source"
                   " software. Ubuntu is officially released in three editions: Desktop, Server, and Core for "
                   "Internet of things devices and robots.",
        )
        ubuntu_article.save()
        ubuntu_article.categories.add(system_administration)

        django_article = Article.objects.create(
           title="Django REST Framework and Elasticsearch",
           author=almasi,
           type="TU",
           content="In this tutorial, we'll look at how to integrate Django REST Framework with Elasticsearch. "
           "We'll use Django to model our data and DRF to serialize and serve it. Finally, we'll index the data "
           "with Elasticsearch and make it searchable.",
        )
        django_article.save()
        django_article.categories.add(system_administration)

        self.stdout.write(self.style.SUCCESS("Successfully populated the database."))

```

Run the following command to populate the DB:

```(env)$ python manage.py populate_db```

If everything went well you should see a Successfully populated the database. message in the console and there should be a few articles in your database.

### Elasticsearch Setup

Follow the following steps to install and run Elasticsearch in the background.

#### Run Elasticsearch locally

1. Ensure you have docker setup and running locally. The run the following commands:

```docker network create elastic```
```docker pull docker.elastic.co/elasticsearch/elasticsearch:8.11.4```
```docker run --name elasticsearch --net elastic -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" -t docker.elastic.co/elasticsearch/elasticsearch:8.11.4```

2. When you start Elasticsearch for the first time, the generated elastic user password and Kibana enrollment token are output to the terminal.

3. Copy the generated password and enrollment token and save them in a secure location. These values are shown only when you start Elasticsearch for the first time. You’ll use these to enroll Kibana with your Elasticsearch cluster and log in.

3. Start Kibana

Kibana enables you to easily send requests to Elasticsearch and analyze, visualize, and manage data interactively.

4. In a new terminal session, start Kibana and connect it to your Elasticsearch container using the following commands:

```docker pull docker.elastic.co/kibana/kibana:8.11.4```
```docker run --name kibana --net elastic -p 5601:5601 docker.elastic.co/kibana/kibana:8.11.4```

When you start Kibana, a unique URL is output to your terminal.

5. To access Kibana, open the generated URL in your browser.

Paste the enrollment token that you copied when starting Elasticsearch and click the button to connect your Kibana instance with Elasticsearch.
Log in to Kibana as the elastic user with the password that was generated when you started Elasticsearch.

6. Send requests to Elasticsearch

You send data and other requests to Elasticsearch through REST APIs. 

You can interact with Elasticsearch using any client that sends HTTP requests, such as the Elasticsearch language clients and curl.

However, in this project we are using Kibana. Kibana’s developer console provides an easy way to experiment and test requests. 

To access the console, go to Management > Dev Tools.

#### To create and populate the Elasticsearch index and mapping, use the search_index command:

```python manage.py search_index --rebuild```

### [Install Elasticsearch With Docker](https://www.elastic.co/guide/en/elasticsearch/reference/8.11/docker.html)


### To create and populate the Elasticsearch index and mapping, use the search_index command:

```python manage.py search_index --rebuild```