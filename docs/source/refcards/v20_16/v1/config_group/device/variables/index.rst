================================
v1.config_group.device.variables
================================


Operation: GET /dataservice/v1/config-group/{configGroupId}/device/variables
----------------------------------------------------------------------------


Get device variables

.. code:: python

    def get_config_group_device_variables(
        config_group_id: str,
        device_id: Optional[str] = None,
        suggestions: Optional[bool] = None,
    ) -> ResponseSchema2: ...


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
        client.v1.config_group.device.variables.get_config_group_device_variables()


Operation: PUT /dataservice/v1/config-group/{configGroupId}/device/variables
----------------------------------------------------------------------------


assign values to device variables

.. code:: python

    def create_config_group_device_variables(
        config_group_id: str,
        payload: Optional[
            CreateConfigGroupDeviceVariablesPutRequest
        ] = None,
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
        client.v1.config_group.device.variables.create_config_group_device_variables()


Operation: POST /dataservice/v1/config-group/{configGroupId}/device/variables
-----------------------------------------------------------------------------


Fetch device variables

.. code:: python

    def fetch_config_group_device_variables(
        config_group_id: str,
        payload: Optional[
            CreateConfigGroupDeviceVariablesPutRequest
        ] = None,
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
        client.v1.config_group.device.variables.fetch_config_group_device_variables()


.. toctree::
    :maxdepth: 1

    schema
    models

