# Vending Machine Application
A vending machine tracker application

## Features
- Basic APIs pertinent to a vending machine tracking application
  - To perform CRUD operations on vending machines, products, stocks
  
- API UI
  - Utilizing Django's built-in setup of SQLite and its connection to a given native UI
    - Disregard need of external API testers (i.e. Postman, etc.) to manipulate database
  - Personal touch to frontend to display, manipulate, test data
  
## Installation
Create then run virtual environment and perform the following in directory
```
pip install django
pip install djangorestframework
python manage.py migrate
python manage.py runserver
```
