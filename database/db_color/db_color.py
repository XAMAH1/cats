from sqlalchemy.orm import relationship

from database.base import base
from sqlalchemy import *


class color(base):
    __tablename__ = 'color'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    color_realt = relationship("cats")
