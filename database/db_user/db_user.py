from sqlalchemy.orm import relationship

from database.base import base
from sqlalchemy import *


class user(base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    profile_picture = Column(String(2555))
    firstname = Column(String(255), nullable=False)
    surname = Column(String(255), nullable=False)
    patronymicname = Column(String(255), nullable=True)
    age = Column(Date, nullable=False)
    mail = Column(String(320), nullable=False, unique=True)
    login = Column(String(30), ForeignKey('autme.login'))
    show_cart = Column(Boolean, nullable=False, default=False)
    create_date = Column(DateTime, nullable=False)
    autme_realt = relationship("autme", uselist=False, back_populates="user_realt")
    # cart_realt = relationship("cart")