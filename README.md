# VishChat_App

This is a simple real time chat application built in django which uses websocket protocol...
<p>

![Alt text](https://github.com/visha1codehub/VishChat_App/blob/master/screenshots/vishchat_screenshot.png?raw=true "Screeshot")

</p>


<h1 align="center">
  View <a href="http://www.vishchat.in/">Live demo</a>.
</h1>

## Installation

### Method-1: Using docker (make sure you have [docker](https://docs.docker.com/get-docker/) installed on your system..)
```bash
$ git clone https://github.com/visha1codehub/VishChat_App.git
$ cd VishChat_App
$ docker build -t imagename:tag .
$ docker run -it -p 8000:8000 imagename:tag
```
Then go to http://localhost:8000/ 
### Method-2: Using general approach

```bash
$ git clone https://github.com/visha1codehub/VishChat_App.git
$ cd VishChat_App
$ pip install requirements.txt
$ python manage.py runserver
```
Then go to http://localhost:8000/

### Method-3: using pipenv(make sure you have installed [pipenv](https://pypi.org/project/pipenv/) on your system)
```bash
$ git clone https://github.com/visha1codehub/VishChat_App.git
$ cd VishChat_App
$ pipenv install
$ pipenv shell
$ python manage.py runserver
```
Then go to http://localhost:8000/
