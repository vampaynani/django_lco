# Django Online Courses

Django little implementation for an online video course platform.

## Libraries
- virtualenv (`apt-get install python3-venv`) 
- [Django](https://github.com/django/django) 

## Before start
Set up Virtual Environment
```
python3 -m venv venv
```
Initialize project
```
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py loaddata viewer/fixtures/courses.json
python manage.py loaddata viewer/fixtures/videos.json
```
## Get started
```
python manage.py runserver
```