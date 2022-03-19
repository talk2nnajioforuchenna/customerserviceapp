import os
import json
from google.cloud import datastore
from google.oauth2 import service_account
from dotenv import load_dotenv

load_dotenv()


# GCP_CONNECT_KEY = os.environ['GCP_CONNECT_KEY']

print(os.getenv('GCP_CONNECT_KEY'))

# KEYS = json.loads(GCP_CONNECT_KEY)  # convert JSON to dictionary
#
# credentials = service_account.Credentials.from_service_account_file(KEYS)
#
# datastore_client = datastore.Client(credentials=credentials)
#
# query = datastore_client.query(kind='EndUsers')
# for entity in query.fetch(limit=5):
#     print(entity)
