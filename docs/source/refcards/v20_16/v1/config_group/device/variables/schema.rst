=======================================
v1.config_group.device.variables.schema
=======================================


Operation: GET /dataservice/v1/config-group/{configGroupId}/device/variables/schema
-----------------------------------------------------------------------------------


get device variables schema

.. code:: python

    def get_config_group_device_variables_schema(
        config_group_id: str, all: Optional[bool] = False
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
        client.v1.config_group.device.variables.schema.get_config_group_device_variables_schema()


