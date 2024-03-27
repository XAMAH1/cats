from sqlalchemy.orm import relationship

from database.base import base
from sqlalchemy import *


class breed(base):
    __tablename__ = 'breed'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    bread_realt = relationship("cats")
