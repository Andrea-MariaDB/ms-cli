from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Table
from sqlalchemy.orm import relationship, backref
from models import db_base as base
import os
from datetime import datetime
from models.User import User
from models.ChatThread import ChatThread

__author__ = "zadjii"


class ChatMessage(base):
    __tablename__ = "chatmessage"
    """
    Represents a single chat message
    """

    id = Column(Integer, primary_key=True)

    graph_id =  Column(Integer)
    content = Column(String)
    thread_id = Column(Integer, ForeignKey("chatthread.id"))
    from_id = Column(Integer, ForeignKey("user.id"))
    created_date_time = Column(DateTime)

    sender = relationship(
        "User",
        foreign_keys=[from_id],
        backref=backref("sent_chat_messages", remote_side=[from_id]),
    )


    @staticmethod
    def from_json(json_blob):
        result = User()
        result.graph_id = json_blob['id']
        # result.created_date_time = TODO: convert string ("2020-07-23T17:07:17.047Z") to datetime
        # result.last_updated_time = TODO: convert string ("2020-07-23T17:07:17.047Z") to datetime
        result.topic = json_blob['topic']
        return result

    # NOTE! The chat message json doesn't include the thread ID. So whoever's building this should also manually stick the thread's ID into it
