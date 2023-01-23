from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import DB_USER, DB_PASS, DB_NAME, DB_HOST

engine = create_engine(f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}", echo=True)

Base = declarative_base()

sessionLocal = sessionmaker(bind=engine)
