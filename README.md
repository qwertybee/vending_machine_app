[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=qwertybee_vending_machine_app&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=qwertybee_vending_machine_app)    [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=qwertybee_vending_machine_app&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=qwertybee_vending_machine_app)

Directory Structure
```
.
├── README.md
├── __pycache__
├── poetry.lock 
├── pyproject.toml 
├── sonar-project.properties 
├── tox.ini 
└── vending_machine_django 
    ├── accounts
    │   ├── admin.py
    │   ├── apps.py
    │   ├── conftest.py
    │   ├── forms.py
    │   ├── migrations
    │   ├── models.py
    │   ├── tests
    │   ├── urls.py
    │   └── views.py
    ├── db.sqlite3
    ├── manage.py
    └── vending_machine_django
        ├── asgi.py
        ├── settings.py
        ├── urls.py
        └── wsgi.py
```

# Vending Machine Application
A vending machine tracker application

## Features
- Basic APIs pertinent to a vending machine tracking application
  - To perform CRUD operations on vending machines, products, stocks

- API UI
  - Utilizing Django's built-in setup of SQLite and its connection to a given native UI
    - Disregard need of external API testers (i.e. Postman, etc.) to manipulate database
  - Personal touch to frontend to display, manipulate, test data

