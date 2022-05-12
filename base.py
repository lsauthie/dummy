from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
load_dotenv()


DBCON = os.getenv('DBCON')

connstr = DBCON

print(connstr)

engine = create_engine(connstr)
Session = sessionmaker(bind=engine)

Base = declarative_base()