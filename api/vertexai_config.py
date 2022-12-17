from google.cloud import aiplatform
from google.oauth2 import service_account

creds = service_account.Credentials.from_service_account_file('creds/ta-eews-ai.json')

aiplatform.init(
    # your Google Cloud Project ID or number
    # environment default used is not set
    project='ta-eews',

    # the Vertex AI region you will use
    # defaults to us-central1
    location='us-central1',

    # Google Cloud Storage bucket in same region as location
    # used to stage artifacts
    staging_bucket='gs://bucket-model-mtr-artifacts',

    # custom google.auth.credentials.Credentials
    # environment default creds used if not set
    credentials=creds
)

endpoint = aiplatform.Endpoint(
    endpoint_name="projects/1048300824693/locations/us-central1/endpoints/6023533715282460672")
