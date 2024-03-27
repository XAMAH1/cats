from sqlalchemy.orm import relationship

from database.base import base
from sqlalchemy import *


class autme(base):
    __tablename__ = 'autme'

    login = Column(String(30), primary_key=True)
    password = Column(String(255), nullable=False)
    role = Column(Integer, ForeignKey('role.id'))
    role_realt = relationship("role")
    user_realt = relationship("user", uselist=False, back_populates="autme_realt")
