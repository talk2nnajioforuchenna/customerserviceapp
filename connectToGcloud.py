import os
import json
from google.cloud import datastore
from google.oauth2 import service_account
from dotenv import load_dotenv


def getData():
    load_dotenv()
    GCP_CONNECT_KEY = os.environ['GCP_CONNECT_KEY']
    # KEYS = json.loads(GCP_CONNECT_KEY)  # convert JSON to dictionary
    credentials = service_account.Credentials.from_service_account_file('keys.json')
    datastore_client = datastore.Client(credentials=credentials)
    retValue = ''
    query = datastore_client.query(kind='EndUsers')
    for entity in query.fetch(limit=5):
        retValue += str(entity)
        # print(entity)
    return retValue


# print(getData())