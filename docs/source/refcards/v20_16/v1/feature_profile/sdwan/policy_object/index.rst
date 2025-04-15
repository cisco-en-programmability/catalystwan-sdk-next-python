======================================
v1.feature_profile.sdwan.policy_object
======================================


Operation: POST /dataservice/v1/feature-profile/sdwan/policy-object/{policyObjectId}/{policyObjectListType}
-----------------------------------------------------------------------------------------------------------


Create a Data Prefix Profile Parcel for Security Policy Object feature profile

.. code:: python

    def post(
        policy_object_id: str,
        policy_object_list_type: PolicyObjectListTypeParam,
        payload: Union[
            CreateDataPrefixProfileParcelForSecurityPolicyObjectPostRequest1,
            CreateDataPrefixProfileParcelForSecurityPolicyObjectPostRequest2,
            CreateDataPrefixProfileParcelForSecurityPolicyObjectPostRequest3,
            CreateDataPrefixProfileParcelForSecurityPolicyObjectPostRequest4,
            CreateDataPrefixProfileParcelForSecurityPolicyObjectPostRequest5,
            CreateDataPrefixProfileParcelForSecurityPolicyObjectPostRequest6,
            CreateDataPrefixProfileParcelForSecurityPolicyObjectPostRequest7,
            CreateDataPrefixProfileParcelForSecurityPolicyObjectPostRequest8,
            CreateDataPrefixProfileParcelForSecurityPolicyObjectPostRequest9,
            CreateDataPrefixProfileParcelForSecurityPolicyObjectPostRequest10,
            CreateDataPrefixProfileParcelForSecurityPolicyObjectPostRequest11,
            CreateDataPrefixProfileParcelForSecurityPolicyObjectPostRequest12,
            CreateDataPrefixProfileParcelForSecurityPolicyObjectPostRequest13,
            CreateDataPrefixProfileParcelForSecurityPolicyObjectPostRequest14,
            CreateDataPrefixProfileParcelForSecurityPolicyObjectPostRequest15,
            CreateDataPrefixProfileParcelForSecurityPolicyObjectPostRequest16,
            CreateDataPrefixProfileParcelForSecurityPolicyObjectPostRequest17,
            CreateDataPrefixProfileParcelForSecurityPolicyObjectPostRequest18,
            CreateDataPrefixProfileParcelForSecurityPolicyObjectPostRequest19,
            CreateDataPrefixProfileParcelForSecurityPolicyObjectPostRequest20,
            CreateDataPrefixProfileParcelForSecurityPolicyObjectPostRequest21,
            CreateDataPrefixProfileParcelForSecurityPolicyObjectPostRequest22,
            CreateDataPrefixProfileParcelForSecurityPolicyObjectPostRequest23,
            CreateDataPrefixProfileParcelForSecurityPolicyObjectPostRequest24,
            CreateDataPrefixProfileParcelForSecurityPolicyObjectPostRequest25,
            CreateDataPrefixProfileParcelForSecurityPolicyObjectPostRequest26,
            CreateDataPrefixProfileParcelForSecurityPolicyObjectPostRequest27,
            CreateDataPrefixProfileParcelForSecurityPolicyObjectPostRequest28,
            CreateDataPrefixProfileParcelForSecurityPolicyObjectPostRequest29,
            CreateDataPrefixProfileParcelForSecurityPolicyObjectPostRequest30,
            CreateDataPrefixProfileParcelForSecurityPolicyObjectPostRequest31,
            CreateDataPrefixProfileParcelForSecurityPolicyObjectPostRequest32,
        ],
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
        client.v1.feature_profile.sdwan.policy_object.post()


Operation: PUT /dataservice/v1/feature-profile/sdwan/policy-object/{policyObjectId}/{policyObjectListType}/{listObjectId}
-------------------------------------------------------------------------------------------------------------------------


Update a Data Prefix Profile Parcel for Policy Object feature profile

.. code:: python

    def put(
        policy_object_id: str,
        policy_object_list_type: PolicyObjectListTypeParam,
        list_object_id: str,
        payload: Union[
            EditDataPrefixProfileParcelForPolicyObjectPutRequest1,
            EditDataPrefixProfileParcelForPolicyObjectPutRequest2,
            EditDataPrefixProfileParcelForPolicyObjectPutRequest3,
            EditDataPrefixProfileParcelForPolicyObjectPutRequest4,
            EditDataPrefixProfileParcelForPolicyObjectPutRequest5,
            EditDataPrefixProfileParcelForPolicyObjectPutRequest6,
            EditDataPrefixProfileParcelForPolicyObjectPutRequest7,
            EditDataPrefixProfileParcelForPolicyObjectPutRequest8,
            EditDataPrefixProfileParcelForPolicyObjectPutRequest9,
            EditDataPrefixProfileParcelForPolicyObjectPutRequest10,
            EditDataPrefixProfileParcelForPolicyObjectPutRequest11,
            EditDataPrefixProfileParcelForPolicyObjectPutRequest12,
            EditDataPrefixProfileParcelForPolicyObjectPutRequest13,
            EditDataPrefixProfileParcelForPolicyObjectPutRequest14,
            EditDataPrefixProfileParcelForPolicyObjectPutRequest15,
            EditDataPrefixProfileParcelForPolicyObjectPutRequest16,
            EditDataPrefixProfileParcelForPolicyObjectPutRequest17,
            EditDataPrefixProfileParcelForPolicyObjectPutRequest18,
            EditDataPrefixProfileParcelForPolicyObjectPutRequest19,
            EditDataPrefixProfileParcelForPolicyObjectPutRequest20,
            EditDataPrefixProfileParcelForPolicyObjectPutRequest21,
            EditDataPrefixProfileParcelForPolicyObjectPutRequest22,
            EditDataPrefixProfileParcelForPolicyObjectPutRequest23,
            EditDataPrefixProfileParcelForPolicyObjectPutRequest24,
            EditDataPrefixProfileParcelForPolicyObjectPutRequest25,
            EditDataPrefixProfileParcelForPolicyObjectPutRequest26,
            EditDataPrefixProfileParcelForPolicyObjectPutRequest27,
            EditDataPrefixProfileParcelForPolicyObjectPutRequest28,
            EditDataPrefixProfileParcelForPolicyObjectPutRequest29,
            EditDataPrefixProfileParcelForPolicyObjectPutRequest30,
            EditDataPrefixProfileParcelForPolicyObjectPutRequest31,
            EditDataPrefixProfileParcelForPolicyObjectPutRequest32,
        ],
    ) -> EditDataPrefixProfileParcelForPolicyObjectPutResponse: ...


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
        client.v1.feature_profile.sdwan.policy_object.put()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/policy-object/{policyObjectId}/{policyObjectListType}/{listObjectId}
----------------------------------------------------------------------------------------------------------------------------


Delete a Data Prefix Profile Parcel for Policy Object feature profile

.. code:: python

    def delete(
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
        client.v1.feature_profile.sdwan.policy_object.delete()


Operation: GET /dataservice/v1/feature-profile/sdwan/policy-object/{policyObjectId}/{policyObjectListType}
----------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        policy_object_id: str,
        policy_object_list_type: PolicyObjectListTypeParam,
        reference_count: Optional[bool] = False,
    ) -> GetListSdwanPolicyObjectSecurityDataIpPrefixPayload: ...


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
        client.v1.feature_profile.sdwan.policy_object.get()


Operation: GET /dataservice/v1/feature-profile/sdwan/policy-object/{policyObjectId}/{policyObjectListType}/{listObjectId}
-------------------------------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        policy_object_id: str,
        policy_object_list_type: PolicyObjectListTypeParam,
        list_object_id: str,
        references: Optional[bool] = False,
    ) -> GetSingleSdwanPolicyObjectSecurityDataIpPrefixPayload: ...


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
        client.v1.feature_profile.sdwan.policy_object.get()


.. toctree::
    :maxdepth: 1

    unified/index
    security_data_ip_prefix/index
    security_fqdn/index
    security_port/index
    security_localapp/index
    security_localdomain/index
    security_ipssignature/index
    security_urllist/index
    security_protocolname/index
    security_geolocation/index
    security_identity/index
    security_scalablegrouptag/index
    security_zone/index
    app_list/index
    sla_class/index
    as_path/index
    class_/index
    data_ipv6_prefix/index
    data_prefix/index
    expanded_community/index
    ext_community/index
    ipv4_network_object_group/index
    ipv4_service_object_group/index
    ipv6_prefix/index
    mirror/index
    policer/index
    prefix/index
    standard_community/index
    vpn_group/index
    app_probe/index
    tloc/index
    color/index
    preferred_color_group/index
    schema/index
    models

