==============================================
v1.feature_profile.sdwan.policy_object.unified
==============================================


Operation: POST /dataservice/v1/feature-profile/sdwan/policy-object/{policyObjectId}/unified/{securityProfileParcelType}
------------------------------------------------------------------------------------------------------------------------


Create Feature for Security Policy

.. code:: python

    def post(
        policy_object_id: str,
        security_profile_parcel_type: SecurityProfileParcelTypeParam,
        payload: Union[
            CreateSdwanSecurityFeaturePostRequest1,
            CreateSdwanSecurityFeaturePostRequest2,
            CreateSdwanSecurityFeaturePostRequest3,
            CreateSdwanSecurityFeaturePostRequest4,
            CreateSdwanSecurityFeaturePostRequest5,
            Union[
                CreateSdwanSecurityFeaturePostRequest61,
                CreateSdwanSecurityFeaturePostRequest62,
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
        client.v1.feature_profile.sdwan.policy_object.unified.post()


Operation: PUT /dataservice/v1/feature-profile/sdwan/policy-object/{policyObjectId}/unified/{securityProfileParcelType}/{securityProfileParcelId}
-------------------------------------------------------------------------------------------------------------------------------------------------


Update a Security Feature

.. code:: python

    def put(
        policy_object_id: str,
        security_profile_parcel_type: SecurityProfileParcelTypeParam,
        security_profile_parcel_id: str,
        payload: Union[
            EditSdwanSecurityFeature1PutRequest1,
            EditSdwanSecurityFeature1PutRequest2,
            EditSdwanSecurityFeature1PutRequest3,
            EditSdwanSecurityFeature1PutRequest4,
            EditSdwanSecurityFeature1PutRequest5,
            Union[
                EditSdwanSecurityFeature1PutRequest61,
                EditSdwanSecurityFeature1PutRequest62,
            ],
        ],
    ) -> EditSdwanSecurityFeature1PutResponse: ...


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


Delete a Security Feature

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

