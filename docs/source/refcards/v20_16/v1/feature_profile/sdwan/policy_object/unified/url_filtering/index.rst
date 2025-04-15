============================================================
v1.feature_profile.sdwan.policy_object.unified.url_filtering
============================================================


Operation: POST /dataservice/v1/feature-profile/sdwan/policy-object/{policyObjectId}/unified/url-filtering
----------------------------------------------------------------------------------------------------------


Create Feature for Security Policy

.. code:: python

    def post(
        policy_object_id: str,
        payload: Union[
            Union[
                CreateSdwanSecurityFeaturePostRequest11,
                CreateSdwanSecurityFeaturePostRequest12,
            ],
            Union[
                CreateSdwanSecurityFeaturePostRequest21,
                CreateSdwanSecurityFeaturePostRequest22,
            ],
            Union[
                CreateSdwanSecurityFeaturePostRequest31,
                CreateSdwanSecurityFeaturePostRequest32,
            ],
            Union[
                CreateSdwanSecurityFeaturePostRequest41,
                CreateSdwanSecurityFeaturePostRequest42,
            ],
            Union[
                CreateSdwanSecurityFeaturePostRequest51,
                CreateSdwanSecurityFeaturePostRequest52,
            ],
            Union[
                CreateSdwanSecurityFeaturePostRequest61,
                CreateSdwanSecurityFeaturePostRequest62,
            ],
            Union[
                CreateSdwanSecurityFeaturePostRequest71,
                CreateSdwanSecurityFeaturePostRequest72,
            ],
        ],
    ) -> CreateSdwanSecurityFeaturePostResponse: ...


Example:
^^^^^^^^


.. code:: python

    from catalyswan.core import create_client

    url = "example.com"
    username = "admin"
    password = "password123"

    with create_client(
        url=url, username=username, password=password
    ) as client:
        client.v1.feature_profile.sdwan.policy_object.unified.url_filtering.post()


Operation: GET /dataservice/v1/feature-profile/sdwan/policy-object/{policyObjectId}/unified/url-filtering/{parcelId}
--------------------------------------------------------------------------------------------------------------------


Get Security Features for a given ParcelType

.. code:: python

    def get(
        policy_object_id: str,
        parcel_id: str,
        reference_count: Optional[bool] = False,
    ) -> GetSdwanSecurityFeatureGetResponse: ...


Example:
^^^^^^^^


.. code:: python

    from catalyswan.core import create_client

    url = "example.com"
    username = "admin"
    password = "password123"

    with create_client(
        url=url, username=username, password=password
    ) as client:
        client.v1.feature_profile.sdwan.policy_object.unified.url_filtering.get()


.. toctree::
    :maxdepth: 1

    models

