# Forum app using python/flask

- This project is for University of Helsinki TSOHA course.
- The goal of this project is to develop a traditional discussion forum using python/flask and PostgreSQL while trying these techniques for the first time.
- Documentation and code will be written in english.
## Intended features

### Done:
- Two types of users, ADMIN/basic
- Basic users can create account,  log in, create topics and write messages under topics.
- Messages can also be modified.
- In addition to basic user capabilities, admin is able to delete messages users and topics.
- Admins are also able to add discussion zone for different topics.
- Only visible for registered users.
- Message timestamping.
- Liking other users replies, not you own.
- Deleting discussion zones
- Search for topics and first messages
- Csrf- tokens

### TODO:
- error handling
- Deleting users, or ability to post?


## Interface

- The app launches in login screen, where you can login or create new user.
- The forum is only visible when logged in.
- After log in the user is directed to the forum. 

## Changelog

- Where are we now?

### Week 1 and 2

- Pretty much just trying to test and understand flask

### Week 3

- Project somewhat on its way. Basic html design is pretty much done and I'm pretty sure my schema is fine. Now there remains implementing almost all database functionality.
- Still trying to figure out the proper structure.

### Week 4

- Implementing basic queries to serve forum structure

### Week 5

- Ability to post topics and messages. Admin can create new zones.
- Users can modify their own messages and topics. Admins are able to do that and also delete every message and topic.
- Looks like a forum.

### Week 6

- Users can now like other users posts. Added database table votes to help with this.
- Implementation of search.
- Added csrf tokens and backend user checks to routes.

## How to open?

- 1st you need download the project and setup virtual environment:

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

- You have to create .env file and define database url, whatever works for you, and a own secret key e.g.:

```bash
DATABASE_URL=postgresql+psycopg2://
SECRET_KEY=<secret-key>
```

- After these theps you will be able to run the app:

```bash
flask run
```
- For you to be able to try the admin capabilities, you need to set users is_admin to True.
- First of course, you need to register user.

```bash
UPDATE users SET is_admin=True WHERE username='YOUR_USERNAME';
```
