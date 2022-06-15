from flask_sqlalchemy import SQLAlchemy
from config import Config

"""
Session(id,name)
Topic(id,session,name)
Question(id,name,topic)
Option(id,name,question,is_answer)
"""

cfg = Config()
db = SQLAlchemy()
