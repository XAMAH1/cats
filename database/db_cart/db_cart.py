from sqlalchemy.orm import relationship

from database.base import base
from sqlalchemy import *


class cart(base):
    __tablename__ = 'cart'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    cats_id = Column(Integer, ForeignKey("cats.id"))
