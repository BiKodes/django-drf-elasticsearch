#### NOTE: This project implements Django Haystack and Elastic Search DSL for enrichment of search via Search Indexing.
####       The commented code is a representation of Django Haystack implementation well articulated.

# Software Archtecture & Principles

   - 12 Factor App
   - SOLID Principles
   - Principles of Clean Code .(NOTE: Apart from keeping the commented code.)

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

from blog.models import Categ

Run the following command to populate the DB:

Management commands for creating, deleting, rebuilding and populating indices.

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