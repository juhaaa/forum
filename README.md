# Forum app using python/flask

- This project is for University of Helsinki TSOHA course.
- The goal of this project is to develop a traditional discussion forum using python/flask and PostgreSQL while trying these techniques for the first time.
- Documentation and code will be written in english.

## Features

### Users

The app has two user roles

|                 	| **Admin** 	| **Basic** 	|
|:---------------:	|:---------:	|:---------:	|
|   Create topic  	|     x     	|     x     	|
|  Reply to topic 	|     x     	|     x     	|
|    Like reply   	|     x     	|     x     	|
|   Modify topic  	|     x     	|     x     	|
|   Modify reply  	|     x     	|     x     	|
|   Create zone   	|     x     	|           	|
|   Delete zone   	|     x     	|           	|
|   Delete topic  	|     x     	|           	|
|   Delete reply  	|     x     	|           	|
|  Search topics  	|     x     	|     x     	|
|   Search users  	|     x     	|           	|
| Ban/unban users 	|     x     	|           	|

### Security

- Only visible for registered users. When users logs in, credentials are checked and session tokens are set.
- In log in user is assigned flask session username and csrf- token and if user is admin, an separate admin session cookie.
- Pages are only visible on need to see bases.
- In logout session info is set back to none.
- Session is not permanent.



## Interface

- The app launches in login screen, where you can login or create new user.
![Home](/screenshots/home.png)
- The forum is only visible when logged in.
- After log in the user is directed to the forum.
- Nac bar contents change based on user roles.
![Home](/screenshots/forumfront.png)
- Topic replies layout
![Reply](/screenshots/message.png)
- Page gives user feedback via flash messages
![Flash](/screenshots/flashresponse.png)
- Errors 404, 403 ad 500 are being handled by the app.
![BAnned](/screenshots/banned.png)

## Changelog


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

### Week 7

- Admins can now ban/unban users.
- Ban affect users capability to post and modify messages
- errors.py handles 403, 404, 500

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
