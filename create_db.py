from database import Base, engine
from models import *

print("Creating database ....")

Base.metadata.create_all(engine)