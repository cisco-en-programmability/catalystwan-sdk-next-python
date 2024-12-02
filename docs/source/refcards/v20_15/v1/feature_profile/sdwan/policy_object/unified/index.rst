==============================================
v1.feature_profile.sdwan.policy_object.unified
==============================================


Operation: GET /dataservice/v1/feature-profile/sdwan/policy-object/{policyObjectId}/unified/{securityProfileParcelType}
-----------------------------------------------------------------------------------------------------------------------


Get Security Profile Parcels for a given ParcelType

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


Create Parcel for Security Policy

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


Get Security Profile Parcel by parcelId

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


Update a Security Profile Parcel

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


Delete a Security Profile Parcel

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

    models

