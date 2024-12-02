======================================
v1.feature_profile.sdwan.policy_object
======================================


Operation: GET /dataservice/v1/feature-profile/sdwan/policy-object/{policyObjectId}/{policyObjectListType}
----------------------------------------------------------------------------------------------------------


Get Data Prefix Profile Parcels for Policy Object feature profile

.. code:: python

    def get_data_prefix_profile_parcel_for_policy_object(
        policy_object_id: str,
        policy_object_list_type: PolicyObjectListTypeParam,
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
        client.v1.feature_profile.sdwan.policy_object.get_data_prefix_profile_parcel_for_policy_object()


Operation: POST /dataservice/v1/feature-profile/sdwan/policy-object/{policyObjectId}/{policyObjectListType}
-----------------------------------------------------------------------------------------------------------


Create a Data Prefix Profile Parcel for Security Policy Object feature profile

.. code:: python

    def create_data_prefix_profile_parcel_for_security_policy_object(
        policy_object_id: str,
        policy_object_list_type: PolicyObjectListTypeParam,
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
        client.v1.feature_profile.sdwan.policy_object.create_data_prefix_profile_parcel_for_security_policy_object()


Operation: GET /dataservice/v1/feature-profile/sdwan/policy-object/{policyObjectId}/{policyObjectListType}/{listObjectId}
-------------------------------------------------------------------------------------------------------------------------


Get Data Prefix Profile Parcel by parcelId for Policy Object feature profile

.. code:: python

    def get_data_prefix_profile_parcel_by_parcel_id_for_policy_object(
        policy_object_id: str,
        policy_object_list_type: PolicyObjectListTypeParam,
        list_object_id: str,
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
        client.v1.feature_profile.sdwan.policy_object.get_data_prefix_profile_parcel_by_parcel_id_for_policy_object()


Operation: PUT /dataservice/v1/feature-profile/sdwan/policy-object/{policyObjectId}/{policyObjectListType}/{listObjectId}
-------------------------------------------------------------------------------------------------------------------------


Update a Data Prefix Profile Parcel for Policy Object feature profile

.. code:: python

    def edit_data_prefix_profile_parcel_for_policy_object(
        policy_object_id: str,
        policy_object_list_type: PolicyObjectListTypeParam,
        list_object_id: str,
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
        client.v1.feature_profile.sdwan.policy_object.edit_data_prefix_profile_parcel_for_policy_object()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/policy-object/{policyObjectId}/{policyObjectListType}/{listObjectId}
----------------------------------------------------------------------------------------------------------------------------


Delete a Data Prefix Profile Parcel for Policy Object feature profile

.. code:: python

    def delete_data_prefix_profile_parcel_for_policy_object(
        policy_object_id: str,
        policy_object_list_type: PolicyObjectListTypeParam,
        list_object_id: str,
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
        client.v1.feature_profile.sdwan.policy_object.delete_data_prefix_profile_parcel_for_policy_object()


.. toctree::
    :maxdepth: 1

    unified/index
    schema/index
    models

