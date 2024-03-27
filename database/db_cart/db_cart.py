from sqlalchemy.orm import relationship

from database.base import base
from sqlalchemy import *


class gender(base):
    __tablename__ = 'gender'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    cats_id = Column(Integer, ForeignKey("cats.id"))
    cats_realt = relationship("cats", uselist=False, back_populates="cats_realt")
    user_realt = relationship("user", uselist=False, back_populates="user_realt")
