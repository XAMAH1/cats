from sqlalchemy.orm import relationship

from database.base import base
from sqlalchemy import *


class autme_token(base):
    __tablename__ = 'autme_token'

    id = Column(Integer, primary_key=True)
    login = Column(String(30), ForeignKey('autme.login'))
    token = Column(String(2555), nullable=False)
    device = Column(String(2555), nullable=False)
    type_device = Column(String(255), nullable=False)
    date = Column(DateTime(), nullable=False)
    autme_realt = relationship("autme")
