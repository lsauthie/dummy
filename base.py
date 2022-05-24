from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv, find_dotenv
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential

load_dotenv()

dbuser = os.getenv('DBUSER')
dbpass = os.getenv('DBPASS')
dbserver = os.getenv('DBSERVER')

#we are on localhost
if ".env" in find_dotenv():
    connstr = 'postgresql://{}:{}@{}:5432/swissre'.format(dbuser, dbpass, dbserver)
else: #we are on azure
    #if you have reached step3 - uncomment this block
    keyVaultName = os.environ["KEY_VAULT_NAME"]

    KVUri = "https://{}.vault.azure.net".format(keyVaultName)
    credential = DefaultAzureCredential()
    client = SecretClient(vault_url=KVUri, credential=credential)

    secretName = 'secret-sauce'
    dbpass = client.get_secret(secretName).value #if keyvault is configured, credential is overwritten from value in keyvault
    print(dbpass)
    # --- end keyvault

    connstr = 'postgresql://{}:{}@{}.postgres.database.azure.com/swissre-db?sslmode=require'.format(dbuser, dbpass, dbserver)


engine = create_engine(connstr)
Session = sessionmaker(bind=engine)

Base = declarative_base()