============================================================
v1.feature_profile.sdwan.policy_object.security_protocolname
============================================================


Operation: POST /dataservice/v1/feature-profile/sdwan/policy-object/{policyObjectId}/security-protocolname
----------------------------------------------------------------------------------------------------------


Create a Data Prefix Profile Parcel for Security Policy Object feature profile

.. code:: python

    def create_data_prefix_profile_parcel_for_security_policy_object(
        policy_object_id: str,
        payload: Optional[
            CreateDataPrefixProfileParcelForSecurityPolicyObjectPostRequest
        ] = None,
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
        client.v1.feature_profile.sdwan.policy_object.security_protocolname.create_data_prefix_profile_parcel_for_security_policy_object()


Operation: GET /dataservice/v1/feature-profile/sdwan/policy-object/{policyObjectId}/security-protocolname/{parcelId}
--------------------------------------------------------------------------------------------------------------------


Get Data Prefix Profile Parcels for Policy Object feature profile

.. code:: python

    def get_data_prefix_profile_parcel_for_policy_object(
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
        client.v1.feature_profile.sdwan.policy_object.security_protocolname.get_data_prefix_profile_parcel_for_policy_object()


.. toctree::
    :maxdepth: 1

    models

