# Forum app using python/flask

- This project is for University of Helsinki TSOHA course.
- The goal of this project is to develop a traditional discussion forum using
python/flask and PostgreSQL while trying these techniques for the first time.
- Documentation and code will be written in english.
## Intended features

- Two types of users, ADMIN/basic
- Basic users can create account,  log in, create topics and write messages
 under topics.
- Messages can also be modified.
- In addition to basic user capabilities, admin is able to delete messages,
users and topics. 
- Admins are also able to add/delete discussion zone for different topics.
- Search- function.
- only visible for registered users.
- user message count?
- Message timestamping. 

## Interface

- The app launches in login screen, where you can login or create new user.
- The forum is only visible when logged in.
- After log in the user is directed to the forum. 

## Changelog

>- Where are we now?

>### Week 1 and 2

>- Pretty much just trying to test and understand flask

>### Week 3

>- Project somewhat on its way. Basic html design is pretty much done and I'm pretty sure my schema if fine. Now there remains implementing almost all database functionality.

## How to open?

- 1st you need to setup virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r ./requirements.txt
```
- Then you can apply the database schema:

```bash
psql < schema.sql
```

- Optionally you can also add something in the empty database:

```bash
psql < schema_test_add.sql
```

- After these theps you will be able to run the app:

```bash
flask run
```
