from sqlalchemy.sql import text
from db import db


def post_new_topic(zone_id, title, content, user_id):
    """Posts new topic

    Args:
        zone_id (Int): Discussion zone id
        title (String): New topics title
        content (String): Message attached to first forum post
        user_id (Int): User id

    Returns:
        Boolean: True if content and title OK
    """

    if len(content) > 0 and 100 >= len(title) > 0:
        sql = text("""INSERT INTO topics (discussion_zone_id, user_id, title, content)
                    VALUES (:zone_id, :user_id, :title, :content)""")
        db.session.execute(sql,
                        {"zone_id":zone_id, "user_id":user_id, "title":title, "content":content})
        db.session.commit()
        return True
    return False

def reply_to_topic(user_id, content, topic_id):
    """Posts new reply

    Args:
        topic_id (Int): Topic id
        content (String): reply message
        user_id (Int): User id

    Returns:
        Boolean: True if content OK
    """

    if len(content) > 0:
        sql = text("""INSERT INTO replies (topic_id, user_id, content)
                    VALUES (:topic_id, :user_id, :content)""")
        db.session.execute(sql, {"topic_id":topic_id, "user_id":user_id, "content":content})
        db.session.commit()
        return True
    return False

def like_post(user_id, reply_id):
    sql = text("""INSERT INTO votes (user_id, reply_id)
                VALUES (:user_id, :reply_id)""")
    db.session.execute(sql, {"user_id":user_id, "reply_id":reply_id})
    db.session.commit()
