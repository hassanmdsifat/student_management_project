# Introduction:

This is a challenge project from Manatal back end team to evaluate how good you are with building APIs with Django.

## Step 1

The first step focuses on Django setup and models.

1. Create a Django app, with:
     - Postgres as a database
     - Pipenv as a Python dependency manager.
     - Environment file (for sensitive information, etc.)

2. Add models to create the following structure:
     - Students have a first name, a last name, and a student identification string (20 characters max for each)
     - Schools have a name (20 char max) and a maximum number of student (any positive integer)
     - Each student object must belong to a school object

Total Time Taken: 50 minutes

####N.B:  Added the .env file in git-repository as it is an interview project. Never include .env file in repository as it includes sensitive information

## Step 2

This second step focuses on Django Rest Framework (DRF).

Feel free to cover edge cases. (Add a reference to it in your README.md)
We encourage you to use `ModelViewSet` and `ModelSerializer` classes to automatically handle the different API HTTP methods.

1. Add __Django REST framework__ library to your project by using Pipenv

2. Enable and use the DRF browsable API for testing things manually.

3. Design your API according to specifications below (make sure to test and customize your solution) by creating urls, views, serializers, tests for all your models so that:
     - Endpoint `students/` will return all students (GET) and allow student creation (POST)
     - Endpoint `/schools/` will return all schools (GET) and allow school creation (POST)
     - Endpoint `/schools/:id` and `/students/:id` will return the object by :id (GET) and allow editing (PUT/PATCH) or deleting (DELETE)
     - Student creation will generate a unique identification string (like random hexadecimal or uuid4 or anything of your choice)
     - Trying to add a student in a full school (maximum number of student reached) will return a DRF error message

Total Time Taken: 1 hour 10 minutes

## Step 3

This third step focuses on __Django Nested Routers__.

1. Add Django Nested Routers library to your project by using Pipenv

2. Design your API according to specifications below:
     - Endpoint /schools/:id/students will return students who belong to school :id (GET)
     - Endpoint /schools/:id/students will allow student creation in the school :id (POST)
     - Your nested endpoint will allow GET/PUT/PATCH/DELETE methods on /schools/:id/students/:id
     - Your nested endpoint will respect the same two last rules of Step 2 too
     
Total Time Taken: 30 minutes

## Additional Steps:
1. Added unit test for the api end points
2. Added search, filter, pagination, ordering for list views
3. Added search, filter, pagination, ordering for list views on Django Nested Routers

