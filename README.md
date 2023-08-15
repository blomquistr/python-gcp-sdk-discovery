# Python Google Quickstart

A repo to hold the code from the [Python quick start for the Google Python SDK](https://developers.google.com/docs/api/quickstart/python).

## Discovery Links

- [Google Python API docs landing page](https://cloud.google.com/python/docs/)
- [Google Python Auth client](https://github.com/googleapis/google-auth-library-python)
- [Google Python container client (the one for Kubernetes)](https://github.com/googleapis/python-container)
- [Google Python quickstart exercise](https://developers.google.com/docs/api/quickstart/python)

## Setup - Enabling the Oauth Scopes for GCP

```text/html
OAuth consent screen
User type
Internal
App name
rcb-python-quickstart-app
Support email
ryan.blomquist@datasite.com
App logo
Not provided
Application homepage link
Not provided
Application privacy policy link
Not provided
Application terms of service link
Not provided
Authorized domains
Not provided
Contact email addresses
ryan.blomquist@datasite.com
```

## Design Notes

We have essentially two possible use cases - one for local users and another for operator-less environments like Jenkins and Kubernetes jobs/containers. ADC and the `gcloud` CLI will work for local users, and we'll need to devise another scheme for headless environments. In the Azure CLI, that can be accomplished by a single track that also theoretically works in a local device by setting specific environment variables. In GCP, it looks like that's done via an environment variable plus the file system.

ADC will execute through the [explicit grant pattern](https://github.com/googleapis/google-auth-library-python/blob/a4ec88c5526d300eeebbc82337780b04a20f1f37/samples/cloud-client/snippets/authenticate_explicit_with_adc.py) and is the default. For headless or operator-less environments we can provision [OAuth2.0 tokens](https://developers.google.com/docs/api/quickstart/python) for the environment in question.
