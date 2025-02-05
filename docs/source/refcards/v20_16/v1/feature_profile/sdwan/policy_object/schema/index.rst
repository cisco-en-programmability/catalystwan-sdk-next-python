=============================================
v1.feature_profile.sdwan.policy_object.schema
=============================================


Operation: GET /dataservice/v1/feature-profile/sdwan/policy-object/{policyObjectListType}/schema
------------------------------------------------------------------------------------------------


Get a SDWAN PolicyObject DataPrefix Parcel Schema by Schema Type

.. code:: python

    def get_sdwan_policy_object_data_prefix_parcel_schema_by_schema_type(
        schema_type: SchemaTypeParam,
        policy_object_list_type: PolicyObjectListTypeParam,
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
        client.v1.feature_profile.sdwan.policy_object.schema.get_sdwan_policy_object_data_prefix_parcel_schema_by_schema_type()


.. toctree::
    :maxdepth: 1

    models

