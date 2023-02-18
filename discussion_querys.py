from db import db
from sqlalchemy.sql import text


def get_discussion_zones():

    # Returns list of (id, name) of discussion zones

    sql = text("SELECT id, name FROM discussion_zones ORDER BY id")
    result = db.session.execute(sql)
    zones =  result.fetchall()
    return zones

def get_zone_name(name):

    # As a parameter gets discussion zone name
    # Returns zone name with id

    sql = text("SELECT name, id FROM discussion_zones WHERE name=:name")
    result = db.session.execute(sql,  {"name":name})
    zone =  result.fetchone()
    return zone

def get_topics(zone_id):

    # Receives zone id as a parameter
    # Returns list of topics with: title, user_id, username, content, created_at

    sql2 = text("""SELECT topics.id, topics.user_id, topics.title, topics.content,
                users.username, topics.created_at FROM topics LEFT JOIN users ON users.id=topics.user_id
                WHERE topics.discussion_zone_id=:zoneid ORDER BY topics.created_at DESC""")

    result2 = db.session.execute(sql2, {"zoneid":zone_id})
    topics = result2.fetchall()

    return topics

def get_first_message(topic_id):

    # Gets topic_id, returns first message information
    
    sql = text("""SELECT topics.id, topics.title, topics.content, topics.created_at, users.username
                FROM topics LEFT JOIN users ON users.id=topics.user_id WHERE topics.id=:topic_id""")

    result = db.session.execute(sql, {"topic_id":topic_id})
    topic = result.fetchone()
    return topic

def get_replies(topic_id):

    # With parameter topic_id, returns all replies.

    sql2 = text("""SELECT replies.id, users.username, replies.content, replies.created_at FROM replies 
                LEFT JOIN users ON  users.id=replies.user_id WHERE topic_id=:topic_id 
                ORDER BY replies.created_at""")
                
    result2 = db.session.execute(sql2, {"topic_id":topic_id})
    replies = result2.fetchall()
    return replies
