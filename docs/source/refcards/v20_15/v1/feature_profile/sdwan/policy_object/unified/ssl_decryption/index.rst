=============================================================
v1.feature_profile.sdwan.policy_object.unified.ssl_decryption
=============================================================


Operation: POST /dataservice/v1/feature-profile/sdwan/policy-object/{policyObjectId}/unified/ssl-decryption
-----------------------------------------------------------------------------------------------------------


Create Parcel for Security Policy

.. code:: python

    def create_security_profile_parcel(
        policy_object_id: str,
        payload: Optional[
            Union[
                CreateSecurityProfileParcelPostRequest1,
                CreateSecurityProfileParcelPostRequest2,
            ]
        ] = None,
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
        client.v1.feature_profile.sdwan.policy_object.unified.ssl_decryption.create_security_profile_parcel()


Operation: GET /dataservice/v1/feature-profile/sdwan/policy-object/{policyObjectId}/unified/ssl-decryption/{parcelId}
---------------------------------------------------------------------------------------------------------------------


Get Security Profile Parcels for a given ParcelType

.. code:: python

    def get_security_profile_parcel(
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
        client.v1.feature_profile.sdwan.policy_object.unified.ssl_decryption.get_security_profile_parcel()


.. toctree::
    :maxdepth: 1

    models

