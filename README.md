# Exactuals

Environment setup (only run it once)

```
run setup.sh
./setup.sh
```

Run `pipenv install django djangorestframework` to install django <br>
Use `exit` to exit out of pipenv

---

```sh
pipenv shell
python manage.py runserver
```

## API Guide

ModelViewSet takes care of basic CRUD operation. <br><br>

#### Specific API Endpoints

<strong>User</strong>

- getting User by name (first or last): `<url>/users/<string:pk>/get_by_name/`

<strong>Transaction</strong>

- getting Transaction by Payor_Payee_Id: `<url>/transaction/<string:ppid>/get_by_ppid/`
