# VishChat_App

This is a simple real time chat application built in django which uses websocket protocol...
<p>

![Alt text](https://github.com/visha1codehub/VishChat_App/blob/master/screenshots/vishchat_screenshot.png?raw=true "Screeshot")

</p>


<p align="center">
  View <a href="http://www.vishchat.in/">Live demo</a>.
</p>

## Installation

<!-- ### Method-1: Using docker (make sure you have [docker](https://docs.docker.com/get-docker/) installed on your system..)
```bash
$ docker pull vishalhub/django-chatapp:latest
$ docker run --name yourchoice -itd -p 8080:8000 vishalhub/django-chatapp:latest
``` -->
### Method-1: Using general approach

```bash
$ git clone https://github.com/visha1codehub/VishChat_App.git
$ cd VishChat_App
$ pip install requirements.txt
$ python manage.py runserver
```
### Method-2: using pipenv(make sure you have installed [pipenv](https://pypi.org/project/pipenv/) on your system)
```bash
$ git clone https://github.com/visha1codehub/VishChat_App.git
$ cd VishChat_App
$ pipenv install
$ pipenv shell
$ python manage.py runserver
```
