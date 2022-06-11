# Canida
<p>Course Management API</p>

## About

You will build the backend for a university course management software. <br/>
The application consists of 3 different entities:

A **professor** has a unique name and leads an arbitrary amount of courses. <br/>
Courses are always led by a single professor. Each **course** has a unique name and multiple **students** are enrolled in the course. <br/>
A student has a name and may enroll in an arbitrary amount of courses.

For the sake of this task you can assume that each entity has a name and we don’t care about other attributes. <br/>
The final application is simple: It will show a list of courses. When an individual course is selected it will display the professor and a list of the enrolled students. <br/>
Please note that this assignment is only about the backend implementation. You are not asked to build a frontend to visualize anything.

## Getting Started
1. Change the current path of your shell to the location where you want to clone the repo.
2. Create a virtual environment for installing dependencies: 
<br/><nbsp/>`python -m venv canida-env`
3. Source the virtual environment:
<br/><nbsp/>`source canida-env/bin/activate`

## installation
- clone the repo
- install dependencies
```bash
$ pip install -r requirements.txt
```
- Copy & rename .env.example file to .env
- Set the env vars appropriately inside .env
- Make DB Migrations - 
```bash
$ flask db upgrade
```
- Seed the DB - 
```bash
$ python seeder.py
```
- run the app
```bash
$ python app.py
```
- or
```bash
$ pipenv run gunicorn -b 0.0.0.0:5000 --access-logfile - --reload "app:create_app()"
```
- Head to
```bash
http://localhost:5000/apidocs
```


## Run with Docker
- Make sure [Docker](https://docs.docker.com/install/ "Docker") & [Docker-Compose](https://docs.docker.com/compose/install/ "Docker-Compose") are installed
- run
```bash
$ docker-compose up -d
```
- Head to
```bash
http://localhost:5000/apidocs
```
- clean up
```bash
$ docker-compose down -v
```


## API documentation
- http://localhost:5000/apidocs