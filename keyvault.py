import os
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential
from dotenv import load_dotenv

load_dotenv()

keyVaultName = os.environ["KEY_VAULT_NAME"]
KVUri = "https://{}.vault.azure.net".format(keyVaultName)

credential = DefaultAzureCredential()
client = SecretClient(vault_url=KVUri, credential=credential)

secretName = 'secret-sauce'
retrieved_secret = client.get_secret(secretName)
print(retrieved_secret.value)