from sqlalchemy.orm import relationship

from database.base import base
from sqlalchemy import *


class cats(base):
    __tablename__ = 'cats'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    age = Column(Date, nullable=False)
    breed = Column(Integer, ForeignKey('breed.id'))
    color = Column(Integer, ForeignKey('color.id'))
    sings = Column(String(255), nullable=False, default="Отсутвуют")
    gender = Column(Integer, ForeignKey('gender.id'))
    price = Column(Double, nullable=False, default=0.0)
    breed_realt = relationship("breed", uselist=False, back_populates="bread_realt")
    color_realt = relationship("color", uselist=False, back_populates="color_realt")
    gender_realt = relationship("gender", uselist=False, back_populates="gender_realt")
    # cart_realt = relationship("cart")
