## Project Title
AWWWARDS APP

## About
This application will allow a user to post a project he/she has created,see projects created by others,and vote for them depending on criterias like Design,Usability and Content.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites
The awwards project requires a prerequisite understanding of the following:

Django Framework Python3.10 Postgres Python virtualenv

### Set up & Installation
Activate virtual environment Activate virtual environment using python3.10 as default handler :'source env/bin/activate'

### Install dependancies
Install dependancies that will create an environment for the app to run pip3 install -r requirements.txt

## Create the Database
psql CREATE DATABASE 'awwards' SECRET_KEY = '<Secret_key>' DB_NAME = 'awwards' USER = '' PASSWORD = '' DEBUG = True

## Run initial Migration
python3.10 manage.py makemigrations awwards python3.10 manage.py migrate Run the app python manage.py runserver

## Deployment
The application is deployed on Heroku and is live on this link:

## Built With
Django 4.0.4 - Back end logic of the application. Bootstrap4 - Used for overall design and responsive site Pillow 9.1.1 - Used for image uploads.

## Authors
Wanjiru Charity

## License
MIT License

Copyright (c) 2022 Wanjiru Charity

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
