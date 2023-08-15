# Python Google Quickstart

A repo to hold the code from the [Python quick start for the Google Python SDK](https://developers.google.com/docs/api/quickstart/python).

## Discovery Links

- [Google Python API docs landing page](https://cloud.google.com/python/docs/)
- [Google Python Auth client](https://github.com/googleapis/google-auth-library-python)
- [Google Python container client (the one for Kubernetes)](https://github.com/googleapis/python-container)
- [Google Python quickstart exercise](https://developers.google.com/docs/api/quickstart/python)
- [Google auth using client libraries doc](https://cloud.google.com/docs/authentication/client-libraries)
- [Python ADC sample snippet](https://github.com/googleapis/python-container/blob/main/samples/generated_samples/container_v1_generated_cluster_manager_create_cluster_sync.py)
- [Google developer docs on setting up ADC credentials for a client app](https://cloud.google.com/docs/authentication/provide-credentials-adc#how-to)

Also, you'll need the [Google Cloud sign-on page](https://console.cloud.google.com/?hl=en-AU).

## Setup - Default Zones

Pick a default zone for the project in GCP from this list (thanks @AV):

```text/html
 [1] us-east1-b
 [2] us-east1-c
 [3] us-east1-d
 [4] us-east4-c
 [5] us-east4-b
 [6] us-east4-a
 [7] us-central1-c
 [8] us-central1-a
 [9] us-central1-f
 [10] us-central1-b
 [11] us-west1-b
 [12] us-west1-c
 [13] us-west1-a
 [14] europe-west4-a
 [15] europe-west4-b
 [16] europe-west4-c
 [17] europe-west1-b
 [18] europe-west1-d
 [19] europe-west1-c
 [20] europe-west3-c
 [21] europe-west3-a
 [22] europe-west3-b
 [23] europe-west2-c
 [24] europe-west2-b
 [25] europe-west2-a
 [26] asia-east1-b
 [27] asia-east1-a
 [28] asia-east1-c
 [29] asia-southeast1-b
 [30] asia-southeast1-a
 [31] asia-southeast1-c
 [32] asia-northeast1-b
 [33] asia-northeast1-c
 [34] asia-northeast1-a
 [35] asia-south1-c
 [36] asia-south1-b
 [37] asia-south1-a
 [38] australia-southeast1-b
 [39] australia-southeast1-c
 [40] australia-southeast1-a
 [41] southamerica-east1-b
 [42] southamerica-east1-c
 [43] southamerica-east1-a
 [44] asia-east2-a
 [45] asia-east2-b
 [46] asia-east2-c
 [47] asia-northeast2-a
 [48] asia-northeast2-b
 [49] asia-northeast2-c
 [50] asia-northeast3-a
 [51] asia-northeast3-b
 [52] asia-northeast3-c
 [53] asia-south2-a
 [54] asia-south2-b
 [55] asia-south2-c
 [56] asia-southeast2-a
 [57] asia-southeast2-b
 [58] asia-southeast2-c
 [59] australia-southeast2-a
 [60] australia-southeast2-b
 [61] australia-southeast2-c
 [62] europe-central2-a
 [63] europe-central2-b
 [64] europe-central2-c
 [65] europe-north1-a
 [66] europe-north1-b
 [67] europe-north1-c
 [68] europe-southwest1-a
 [69] europe-southwest1-b
 [70] europe-southwest1-c
 [71] europe-west12-a
 [72] europe-west12-b
 [73] europe-west12-c
 [74] europe-west6-a
 [75] europe-west6-b
 [76] europe-west6-c
 [77] europe-west8-a
 [78] europe-west8-b
 [79] europe-west8-c
 [80] europe-west9-a
 [81] europe-west9-b
 [82] europe-west9-c
 [83] me-central1-a
 [84] me-central1-b
 [85] me-central1-c
 [86] me-west1-a
 [87] me-west1-b
 [88] me-west1-c
 [89] northamerica-northeast1-a
 [90] northamerica-northeast1-b
 [91] northamerica-northeast1-c
 [92] northamerica-northeast2-a
 [93] northamerica-northeast2-b
 [94] northamerica-northeast2-c
 [95] southamerica-west1-a
 [96] southamerica-west1-b
 [97] southamerica-west1-c
 [98] us-east5-a
 [99] us-east5-b
 [100] us-east5-c
 [101] us-south1-a
 [102] us-south1-b
 [103] us-south1-c
 [104] us-west2-a
 [105] us-west2-b
 [106] us-west2-c
 [107] us-west3-a
 [108] us-west3-b
 [109] us-west3-c
 [110] us-west4-a
 [111] us-west4-b
 [112] us-west4-c
 [113] Do not set default zone
 ```

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
