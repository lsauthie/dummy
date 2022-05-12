from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
load_dotenv()

DBHOST = os.getenv('DBHOST')
DBNAME = os.getenv('DBNAME')
DBUSER = os.getenv('DBUSER')
DBPASS = os.getenv('DBPASS')

connstr = 'postgresql://{}:{}@{}/{}'.format(DBUSER,DBPASS,DBHOST, DBNAME)

print(connstr)

engine = create_engine(connstr)
Session = sessionmaker(bind=engine)

Base = declarative_base()