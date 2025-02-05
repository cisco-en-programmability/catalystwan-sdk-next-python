=======================================
v1.policy_group.device.variables.schema
=======================================


Operation: GET /dataservice/v1/policy-group/{policyGroupId}/device/variables/schema
-----------------------------------------------------------------------------------


get device variables schema

.. code:: python

    def get_policy_group_device_variables_schema(
        policy_group_id: str,
    ) -> Any: ...


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
        client.v1.policy_group.device.variables.schema.get_policy_group_device_variables_schema()


