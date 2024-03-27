from sqlalchemy.orm import relationship

from database.base import base
from sqlalchemy import *


class image_cats(base):
    __tablename__ = 'image_cats'

    id = Column(Integer, primary_key=True)
    path_image = Column(String(512), nullable=False)
