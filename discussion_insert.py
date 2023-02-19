from db import db
from sqlalchemy.sql import text

def post_new_topic(zone_id, title, content, user_id):

    # Function to insert new topic into database

    if len(content) > 0 and 100 >= len(title) > 0:
        sql = text("""INSERT INTO topics (discussion_zone_id, user_id, title, content) 
                    VALUES (:zone_id, :user_id, :title, :content)""")
        db.session.execute(sql, {"zone_id":zone_id, "user_id":user_id, "title":title, "content":content})
        db.session.commit()
        return True
    return False

def reply_to_topic(user_id, content, topic_id):

    # insert reply to database

    if len(content) > 0:
        sql = text("""INSERT INTO replies (topic_id, user_id, content) 
                    VALUES (:topic_id, :user_id, :content)""")
        db.session.execute(sql, {"topic_id":topic_id, "user_id":user_id, "content":content})
        db.session.commit()
        return True
    return False

