==============================================
v1.feature_profile.sdwan.policy_object.policer
==============================================


Operation: POST /dataservice/v1/feature-profile/sdwan/policy-object/{policyObjectId}/policer
--------------------------------------------------------------------------------------------


Create a Data Prefix Profile Parcel for Security Policy Object feature profile

.. code:: python

    def post(
        policy_object_id: str,
        payload: CreateDataPrefixProfileParcelForSecurityPolicyObjectPostRequest,
    ) -> (
        CreateDataPrefixProfileParcelForSecurityPolicyObjectPostResponse
    ): ...


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
        client.v1.feature_profile.sdwan.policy_object.policer.post()


Operation: GET /dataservice/v1/feature-profile/sdwan/policy-object/{policyObjectId}/policer/{parcelId}
------------------------------------------------------------------------------------------------------


Get Data Prefix Profile Parcels for Policy Object feature profile

.. code:: python

    def get(
        policy_object_id: str,
        parcel_id: str,
        reference_count: Optional[bool] = False,
    ) -> GetDataPrefixProfileParcelForPolicyObjectGetResponse: ...


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
        client.v1.feature_profile.sdwan.policy_object.policer.get()


.. toctree::
    :maxdepth: 1

    models

