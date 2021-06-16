### messages.py ###

from sqlalchemy.orm import declarative_base
from database.models.api_table import api_table
from database.models.media_table import media_table

Base = declarative_base()

class api_table(api_table,Base):
    api_table.__tablename__ = "messages"

class media_table(media_table,Base):
    pass