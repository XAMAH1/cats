from sqlalchemy import *
from sqlalchemy import exc as sa_exc
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
import warnings

from config import BASE_CONFIG
from database.db_autme.db_autme import *
from database.db_role.db_role import *
from database.db_autme_token.db_autme_token import *
from database.db_user.db_user import *
from database.db_cats.db_cats import *
from database.db_breed.db_breed import *
from database.db_color.db_color import *
from database.db_gender.db_gender import *
from database.db_cart.db_cart import *
from database.base import base


warnings.filterwarnings('ignore', category=sa_exc.SAWarning)


timeout = 10
engine = create_engine(f'mysql+pymysql://{BASE_CONFIG["BASE_USER"]}:{BASE_CONFIG["BASE_PASSWORD"]}@{BASE_CONFIG["BASE_HOST"]}/{BASE_CONFIG["BASE_TABLE"]}', connect_args={'connect_timeout': timeout})


base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()