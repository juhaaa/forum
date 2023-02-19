from db import db
from sqlalchemy.sql import text


def get_discussion_zones():
    """ Gets discussion zone names and id's

    Returns:
        List: List containing tuples (id, name)
    """

    sql = text("SELECT id, name FROM discussion_zones ORDER BY id")
    result = db.session.execute(sql)
    zones =  result.fetchall()
    return zones

def get_zone_name(name):
    """Returns zone name and id for specific zone

    Args:
        name (String): Discussion zone name

    Returns:
        Tuple: (name, id)
    """

    sql = text("SELECT name, id FROM discussion_zones WHERE name=:name")
    result = db.session.execute(sql,  {"name":name})
    zone =  result.fetchone()
    return zone

def get_topics(zone_id):
    """ Given zone id returns info for all the topics
        under that discussion zone

    Args:
        zone_id (Int): Discussion zone id

    Returns:
        List: List of tuples   (topic.id,
                                topic.user_id,
                                topics.title,
                                topics.content,
                                users.username,
                                topics.created_at)
    """

    sql2 = text("""SELECT topics.id, topics.user_id, topics.title, topics.content,
                users.username, topics.created_at FROM topics LEFT JOIN users ON users.id=topics.user_id
                WHERE topics.discussion_zone_id=:zoneid ORDER BY topics.created_at DESC""")

    result2 = db.session.execute(sql2, {"zoneid":zone_id})
    topics = result2.fetchall()

    return topics

def get_first_message(topic_id):
    """ Function for getting the topics first message from db

    Args:
        topic_id (int): id of topic being retrieved

    Returns:
        Tuple: (id, title, content, created_at, username)
    """

    sql = text("""SELECT topics.id, topics.title, topics.content, topics.created_at, users.username
                FROM topics LEFT JOIN users ON users.id=topics.user_id
                WHERE topics.id=:topic_id""")
    result = db.session.execute(sql, {"topic_id":topic_id})
    topic = result.fetchone()
    return topic

def get_replies(topic_id):
    """ With parameter topic_id, returns all replies
        belonging under that topic

    Args:
        topic_id (int): id of parent topic

    Returns:
        List: List of tuples (id, username, content, created_at, username)
    """

    sql = text("""SELECT replies.id, users.username, replies.content, replies.created_at
                FROM replies
                LEFT JOIN users ON  users.id=replies.user_id WHERE topic_id=:topic_id
                ORDER BY replies.created_at""")
    result = db.session.execute(sql, {"topic_id":topic_id})
    replies = result.fetchall()
    return replies

def get_title_and_zone(topic_id):
    """ Function for retrieving topics title and zones name.

    Args:
        topic_id (int): id of parent topic

    Returns:
        Tuple: (title, name)
    """

    sql = text("""SELECT t.title, d.name FROM topics t
                LEFT JOIN discussion_zones d ON t.discussion_zone_id=d.id 
                WHERE t.id=:topic_id""")
    result = db.session.execute(sql, {"topic_id":topic_id})
    title_and_zone = result.fetchone()
    return title_and_zone
