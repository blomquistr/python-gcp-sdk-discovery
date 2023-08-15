import os

from google.auth import default as google_auth_default
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.cloud import (
    containerv1,
)  # this is just a demo call for the GCP SDK, replace with Containers

KCS_SOURCE_DIR = os.path.expanduser("~/.kcs")

KCS_GCP_TOKEN_FILE = "token_gcp.json"
KCS_GCP_TOKEN_PATH = os.path.join(KCS_SOURCE_DIR, KCS_GCP_TOKEN_FILE)
KCS_GCP_CREDENTIAL_JSON = "credentials_gcp.json"
KCS_GCP_CREDENTIAL_PATH = os.path.join(KCS_SOURCE_DIR, KCS_GCP_CREDENTIAL_JSON)


# We'll need to figure out what the actual scopes are for the Kubernetes clusters.
# this scope is directly from the auth demo project
SCOPES = ["https://www.googleapis.com/auth/documents.readonly"]


# TODO: write a method to test for the presence of
# credentials.json or to write it from command line
# arguments
def fetch_gcp_oauth2_creds():
    """
    Writes a file, credentials.json, to the .kcs directory of the
    user running the KCS. This file holds the OAuth2.0 token the
    user generated from the Google Cloud Console.
    """
    raise NotImplementedError()


# A modified version of quickstart.py for the future KCS implementation
def login_to_gcp_oauth2():
    """
    Shows basic usage of Auth via Oath2.0 tokens
    """

    # We'll start with an empty creds object - we can determine where to put
    # it later
    creds = None

    # Unlike in the Auth demo we'll store the creds for the KCS in the KCS
    # user directory otherwise, this flow will be the saem - we'll use
    if os.path.exists(KCS_GCP_TOKEN_PATH):
        creds = Credentials.from_authorized_user_file(
            KCS_GCP_TOKEN_PATH,
            SCOPES,
        )

    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                KCS_GCP_CREDENTIAL_PATH, SCOPES
            )
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(KCS_GCP_TOKEN_PATH, "w") as token:
            token.write(creds.to_json())


# A sample of logging in via the ADC grant pattern; this would be the way
# local users would authenticate in GCP with the k8s-cloud-system CLI.
def login_to_gcp_adc(google_application_credentials: str = None):
    """
    Snippet demonstrating basic auth for the ADC grant - this will be the
    default pattern that end-users of the KCS will want to use to log in,
    because it'll pick up their gcloud CLI credentials and save them passing
    values in.

    :param google_application_credentials: if auth is being performed by
    serviceaccount, this value should be provided or set in the environment
    asthe path to a valid service account JSON file obtained from the Google
    Cloud Console.
    """

    # If the user has provided a path to a service account JSON file, we'll
    # set the environment variable accordingly. If not, we're trusting that
    # the user intended to either use their existing gcloud CLI auth or has
    # already set the value in the environment.
    if google_application_credentials:
        os.environ.setdefault(
            "GOOGLE_APPLICATION_CREDENTIALS", google_application_credentials
        )

    # With the environment variable either set or ignored because you're on
    # your local machine, we'll use the google default ADC auth method to
    # authenticate with GCP.
    credentials, projectId = google_auth_default()

    # Here's a sample call to validate that we successfully did the thing
    client = containerv1.ClusterManagerClient(credentials=credentials)
    client.list_clusters(projectId)


# A little test for our two methods, to do some BS work against the clusters
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()

    parser.add_argument()