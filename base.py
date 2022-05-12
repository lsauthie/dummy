from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

dbuser = os.getenv('DBUSER')
dbpass = os.getenv('DBPASS')
dbserver = os.getenv('DBSERVER')


if dbserver != 'localhost':#running on azure
    connstr = 'postgresql://{}:{}@{}.postgres.database.azure.compostgres?sslmode=require'.format(dbuser, dbpass, dbserver)
else:
    connstr = 'postgresql://{}:{}@{}:5432'.format(dbuser, dbpass, dbserver)

#DBCON = 'postgresql://postgres:admin@localhost:5432'
#"postgres://adminTerraform:QAZwsx123@swissre-server.postgres.database.azure.com/postgres?sslmode=require"

print(connstr)

engine = create_engine(connstr)
Session = sessionmaker(bind=engine)

Base = declarative_base()