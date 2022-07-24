## Mój pierwszy projekt w Django (MVT)

Miała być to strona Muzeum Telefonii Komórkowej w Sosnowcu

## Technologie
Projekt jest stworzony w oparciu o:
* Python 3.10
* Django 3.2.3
* Bootstrap 5
* TinyMCE
* Docker
* Docker-compose

## Baza danych
* PostgreSQL 14.2

## Sposób działania
Dostępne po zalogowaniu jako administrator
### Aby utworzyć konto administratora 
```
$ make admin
```
lub
```
$ docker-compose run muztelkom python manage.py createsuperuser
```
* Dodawanie telefonów:
   * http://127.0.0.1:8000/gallery/create
   * markę telefonu należy dodać w panelu administratora
        * http://127.0.0.1:8000/admin
* Dodawanie artykułów
  * http://127.0.0.1:8000/articles/create

## Instalacja

Aby pobrać projekt:
```
$ git clone https://github.com/Fejren/muzeum.git
```
Aby uruchomić projekt:
```
$ docker-compose up
```
lub
```
$ make up
```
