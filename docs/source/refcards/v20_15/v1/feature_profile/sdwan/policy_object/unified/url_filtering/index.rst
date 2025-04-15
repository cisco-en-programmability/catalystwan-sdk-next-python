============================================================
v1.feature_profile.sdwan.policy_object.unified.url_filtering
============================================================


Operation: POST /dataservice/v1/feature-profile/sdwan/policy-object/{policyObjectId}/unified/url-filtering
----------------------------------------------------------------------------------------------------------


Create Parcel for Security Policy

.. code:: python

    def post(
        policy_object_id: str,
        payload: Union[
            Union[
                CreateSecurityProfileParcelPostRequest11,
                CreateSecurityProfileParcelPostRequest12,
            ],
            Union[
                CreateSecurityProfileParcelPostRequest21,
                CreateSecurityProfileParcelPostRequest22,
            ],
            Union[
                CreateSecurityProfileParcelPostRequest31,
                CreateSecurityProfileParcelPostRequest32,
            ],
            Union[
                CreateSecurityProfileParcelPostRequest41,
                CreateSecurityProfileParcelPostRequest42,
            ],
            Union[
                CreateSecurityProfileParcelPostRequest51,
                CreateSecurityProfileParcelPostRequest52,
            ],
            Union[
                CreateSecurityProfileParcelPostRequest61,
                CreateSecurityProfileParcelPostRequest62,
            ],
            Union[
                CreateSecurityProfileParcelPostRequest71,
                CreateSecurityProfileParcelPostRequest72,
            ],
        ],
    ) -> CreateSecurityProfileParcelPostResponse: ...


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


Get Security Profile Parcels for a given ParcelType

.. code:: python

    def get(
        policy_object_id: str,
        parcel_id: str,
        reference_count: Optional[bool] = False,
    ) -> GetSecurityProfileParcelGetResponse: ...


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

