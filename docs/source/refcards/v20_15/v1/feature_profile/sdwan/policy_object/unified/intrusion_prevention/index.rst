===================================================================
v1.feature_profile.sdwan.policy_object.unified.intrusion_prevention
===================================================================


Operation: POST /dataservice/v1/feature-profile/sdwan/policy-object/{policyObjectId}/unified/intrusion-prevention
-----------------------------------------------------------------------------------------------------------------


Create Parcel for Security Policy

.. code:: python

    def post(
        policy_object_id: str,
        payload: CreateSecurityProfileParcelPostRequest,
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
        client.v1.feature_profile.sdwan.policy_object.unified.intrusion_prevention.post()


Operation: GET /dataservice/v1/feature-profile/sdwan/policy-object/{policyObjectId}/unified/intrusion-prevention/{parcelId}
---------------------------------------------------------------------------------------------------------------------------


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
        client.v1.feature_profile.sdwan.policy_object.unified.intrusion_prevention.get()


.. toctree::
    :maxdepth: 1

    models

