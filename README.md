# Exactuals

Run `pipenv install django djangorestframework` to install django and django rest framework <br>
Use `exit` to exit out of pipenv

To start local server, run:

```sh
pipenv shell
python manage.py runserver
```

## API Guide

ModelViewSet takes care of basic CRUD operation. <br><br>

#### API Endpoints

<strong>User</strong>

- getting User by name (first or last): `<url>/user/<string:pk>/get_by_name/`

<strong>Transaction</strong>

- getting Transaction by Payor_Payee_Id: `<url>/transaction/<string:ppid>/get_by_ppid/`
