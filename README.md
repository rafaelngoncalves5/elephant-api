# Elephant API 🐘 🐘 🐘

![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Insomnia](https://img.shields.io/badge/Insomnia-black?style=for-the-badge&logo=insomnia&logoColor=5849BE)

## Endpoints

- **sanctuary/create**: - Creates a new sanctuary, receives: name, country and elephants_living. Visit it with a GET HTTP method to get more information about how it works

- **sanctuary/read**: - Displays all available sanctuaries in the Database. Visit it with a GET HTTP method to get more information about how it works

- **sanctuary/update**: - Updates a created sanctuary, receives: id, name, country and elephants_living. Visit it with a GET HTTP method to get more information about how it works

- **sanctuary/delete**: - Deletes a sanctuary with id equals the received query name id. Visit it with a GET HTTP method to get more information about how it works

- **sanctuary/country/read**: - Displays all available countries in the Database. Visit it with a GET HTTP method to get more information about how it works

## Documentation

See [docs](https://github.com/rafaelngoncalves5/elephant-api/tree/master/docs) for a deeper grasp

### The API is represented by the following document:

<br />

![arch](https://github.com/rafaelngoncalves5/elephant-api/blob/master/docs/arch.jpg)

<hr />

### The model is represented solely by the following Entity (Chen Notation)

<br/>

![entity](https://github.com/rafaelngoncalves5/elephant-api/blob/master/docs/entity.jpg)

Most of the reaserch followed the article from [yogawinetravel](https://www.yogawinetravel.com/wanderlust-wednesday-elephant-sanctuaries-orphanages-and-parks-around-the-world/)
