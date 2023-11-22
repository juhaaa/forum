from sqlalchemy.sql import text
from db import db

def edit_reply(reply_id, content):

    sql = text("UPDATE replies SET content=:content WHERE id=:reply_id")
    db.session.execute(sql, {"content":content, "reply_id":reply_id})
    db.session.commit()

def edit_topic(topic_id, content, title):
    sql = text("UPDATE topics SET content=:content, title=:title WHERE id=:topic_id")
    db.session.execute(sql, {"content":content,
                            "topic_id":topic_id,
                            "title":title})
    db.session.commit()
