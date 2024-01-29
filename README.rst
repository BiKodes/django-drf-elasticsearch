ZOGO

Zogo is a small program that supports static grapevine for whistleblowing in both
public and private sectors. 

It puts modular archtecture in practice as it consist of multiple models, which are 
serialized and served via Django REST Framework. 

This program is integrated with Elasticsearch, and respective endpoints are wired up 
to blooster looking up different authors, categories, and articles.

To keep the  code clean and modular, the project is split into the following apps:

    blog - for our Django models, serializers, and ViewSets
    search - for Elasticsearch documents, indexes, and queries

How setup the project locally:

$ mkdir django-drf-elasticsearch 
$ cd django-drf-elasticsearch
$ python3.12 -m venv env
$ source env/bin/activate

(env)$ pip install django==4.2.7
(env)$ django-admin startproject core .
