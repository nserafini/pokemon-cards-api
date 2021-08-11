from datetime import datetime
from uuid import uuid4

from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import String

from api.db import db


def get_uuid():
    return str(uuid4())


class BaseModel(db.Model):

    __abstract__ = True

    id = Column(String(36), primary_key=True, default=get_uuid, unique=True)
    creation_date = Column(
        DateTime(timezone=True), default=datetime.utcnow, nullable=False
    )
