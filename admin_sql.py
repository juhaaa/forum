from db import db
from sqlalchemy.sql import text

def add_new_zone(zone_name):
    if len(zone_name) <= 50:
        sql = text("INSERT INTO discussion_zones (name) VALUES (:zone_name)")
        db.session.execute(sql, {"zone_name":zone_name})
        db.session.commit()
        return True
    return False

def delete_zone(zone_id):
    sql = text("DELETE FROM discussion_zones WHERE id=:zone_id")
    db.session.execute(sql, {"zone_id":zone_id})
    db.session.commit()

def delete_topic(topic_id):
    sql = text("DELETE FROM topics WHERE id=:topic_id")
    db.session.execute(sql, {"topic_id":topic_id})
    db.session.commit()

def delete_reply(reply_id):
    sql = text("DELETE FROM replies WHERE id=:reply_id")
    db.session.execute(sql, {"reply_id":reply_id})
    db.session.commit()
