# Forum app using python/flask

- This project is for University of Helsinki TSOHA course.
- The goal of this project is to develop a traditional discussion forum using python/flask and PostgreSQL while trying these techniques for the first time.

## Features

This is a classic forum style flask app. The basic structure consists of discussion zones, which define the broad subject. Under the zones there are topics, which are more specific subjects and users are able to post replies under the topics.

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
- Nav bar contents change based on user roles.
![Home](/screenshots/forumfront.png)
- Topic replies layout
![Reply](/screenshots/message.png)
- Page gives user feedback via flash messages
![Flash](/screenshots/flashresponse.png)
- Errors 404, 403 ad 500 are being handled by the app.
![BAnned](/screenshots/banned.png)


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
