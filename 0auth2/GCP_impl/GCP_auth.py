from dotenv import load_dotenv
load_dotenv() 

import os


GCP_CLIENT_ID = os.getenv('GCP_CLIENT_ID') or None
GCP_CLIENT_SECRET = os.getenv('GCP_CLIENT_SECRET') or None
if GCP_CLIENT_ID is None or GCP_CLIENT_SECRET is None:
    raise BaseException('Missing env variables')


print("GCP token: {}".format(GCP_CLIENT_ID))