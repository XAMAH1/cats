from sqlalchemy.orm import relationship

from database.base import base
from sqlalchemy import *


class role(base):
    __tablename__ = 'role'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    user_realt = relationship("autme")
