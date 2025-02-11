==============================================
v1.feature_profile.sdwan.policy_object.unified
==============================================


Operation: GET /dataservice/v1/feature-profile/sdwan/policy-object/{policyObjectId}/unified/{securityProfileParcelType}
-----------------------------------------------------------------------------------------------------------------------


Get Security Features for a given ParcelType

.. code:: python

    def get_security_profile_parcel(
        policy_object_id: str,
        security_profile_parcel_type: SecurityProfileParcelTypeParam,
        reference_count: Optional[bool] = False,
    ) -> str: ...


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
        client.v1.feature_profile.sdwan.policy_object.unified.get_security_profile_parcel()


Operation: POST /dataservice/v1/feature-profile/sdwan/policy-object/{policyObjectId}/unified/{securityProfileParcelType}
------------------------------------------------------------------------------------------------------------------------


Create Feature for Security Policy

.. code:: python

    def create_security_profile_parcel(
        policy_object_id: str,
        security_profile_parcel_type: SecurityProfileParcelTypeParam,
        payload: Optional[str] = None,
    ) -> str: ...


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
        client.v1.feature_profile.sdwan.policy_object.unified.create_security_profile_parcel()


Operation: GET /dataservice/v1/feature-profile/sdwan/policy-object/{policyObjectId}/unified/{securityProfileParcelType}/{securityProfileParcelId}
-------------------------------------------------------------------------------------------------------------------------------------------------


Get Security Feature by FeatureId

.. code:: python

    def get_security_profile_parcel_by_parcel_id(
        policy_object_id: str,
        security_profile_parcel_type: SecurityProfileParcelTypeParam,
        security_profile_parcel_id: str,
        references: Optional[bool] = False,
    ) -> str: ...


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
        client.v1.feature_profile.sdwan.policy_object.unified.get_security_profile_parcel_by_parcel_id()


Operation: PUT /dataservice/v1/feature-profile/sdwan/policy-object/{policyObjectId}/unified/{securityProfileParcelType}/{securityProfileParcelId}
-------------------------------------------------------------------------------------------------------------------------------------------------


Update a Security Feature

.. code:: python

    def edit_security_profile_parcel(
        policy_object_id: str,
        security_profile_parcel_type: SecurityProfileParcelTypeParam,
        security_profile_parcel_id: str,
        payload: Optional[str] = None,
    ) -> str: ...


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
        client.v1.feature_profile.sdwan.policy_object.unified.edit_security_profile_parcel()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/policy-object/{policyObjectId}/unified/{securityProfileParcelType}/{securityProfileParcelId}
----------------------------------------------------------------------------------------------------------------------------------------------------


Delete a Security Feature

.. code:: python

    def delete_security_profile_parcel(
        policy_object_id: str,
        security_profile_parcel_type: SecurityProfileParcelTypeParam,
        security_profile_parcel_id: str,
    ) -> None: ...


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
        client.v1.feature_profile.sdwan.policy_object.unified.delete_security_profile_parcel()


.. toctree::
    :maxdepth: 1

    advanced_inspection_profile/index
    intrusion_prevention/index
    url_filtering/index
    advanced_malware_protection/index
    ssl_decryption_profile/index
    ssl_decryption/index
    models

