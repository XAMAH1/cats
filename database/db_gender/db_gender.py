from sqlalchemy.orm import relationship

from database.base import base
from sqlalchemy import *


class gender(base):
    __tablename__ = 'gender'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    gender_realt = relationship("cats")
