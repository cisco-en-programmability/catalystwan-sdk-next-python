==============================================
v1.feature_profile.sdwan.policy_object.unified
==============================================


Operation: POST /dataservice/v1/feature-profile/sdwan/policy-object/{policyObjectId}/unified/{securityProfileParcelType}
------------------------------------------------------------------------------------------------------------------------


Create Parcel for Security Policy

.. code:: python

    def post(
        policy_object_id: str,
        security_profile_parcel_type: SecurityProfileParcelTypeParam,
        payload: Union[
            CreateSecurityProfileParcelPostRequest1,
            CreateSecurityProfileParcelPostRequest2,
            CreateSecurityProfileParcelPostRequest3,
            CreateSecurityProfileParcelPostRequest4,
            CreateSecurityProfileParcelPostRequest5,
            Union[
                CreateSecurityProfileParcelPostRequest61,
                CreateSecurityProfileParcelPostRequest62,
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
        client.v1.feature_profile.sdwan.policy_object.unified.post()


Operation: PUT /dataservice/v1/feature-profile/sdwan/policy-object/{policyObjectId}/unified/{securityProfileParcelType}/{securityProfileParcelId}
-------------------------------------------------------------------------------------------------------------------------------------------------


Update a Security Profile Parcel

.. code:: python

    def put(
        policy_object_id: str,
        security_profile_parcel_type: SecurityProfileParcelTypeParam,
        security_profile_parcel_id: str,
        payload: Union[
            EditSecurityProfileParcel1PutRequest1,
            EditSecurityProfileParcel1PutRequest2,
            EditSecurityProfileParcel1PutRequest3,
            EditSecurityProfileParcel1PutRequest4,
            EditSecurityProfileParcel1PutRequest5,
            Union[
                EditSecurityProfileParcel1PutRequest61,
                EditSecurityProfileParcel1PutRequest62,
            ],
        ],
    ) -> EditSecurityProfileParcel1PutResponse: ...


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
        client.v1.feature_profile.sdwan.policy_object.unified.put()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/policy-object/{policyObjectId}/unified/{securityProfileParcelType}/{securityProfileParcelId}
----------------------------------------------------------------------------------------------------------------------------------------------------


Delete a Security Profile Parcel

.. code:: python

    def delete(
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
        client.v1.feature_profile.sdwan.policy_object.unified.delete()


Operation: GET /dataservice/v1/feature-profile/sdwan/policy-object/{policyObjectId}/unified/{securityProfileParcelType}
-----------------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        policy_object_id: str,
        security_profile_parcel_type: SecurityProfileParcelTypeParam,
        reference_count: Optional[bool] = False,
    ) -> (
        GetListSdwanPolicyObjectUnifiedAdvancedInspectionProfilePayload
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
        client.v1.feature_profile.sdwan.policy_object.unified.get()


Operation: GET /dataservice/v1/feature-profile/sdwan/policy-object/{policyObjectId}/unified/{securityProfileParcelType}/{securityProfileParcelId}
-------------------------------------------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        policy_object_id: str,
        security_profile_parcel_type: SecurityProfileParcelTypeParam,
        security_profile_parcel_id: str,
        references: Optional[bool] = False,
    ) -> (
        GetSingleSdwanPolicyObjectUnifiedAdvancedInspectionProfilePayload
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
        client.v1.feature_profile.sdwan.policy_object.unified.get()


.. toctree::
    :maxdepth: 1

    advanced_inspection_profile/index
    intrusion_prevention/index
    url_filtering/index
    advanced_malware_protection/index
    ssl_decryption_profile/index
    ssl_decryption/index
    models

