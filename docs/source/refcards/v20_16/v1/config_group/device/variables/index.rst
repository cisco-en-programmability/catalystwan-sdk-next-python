================================
v1.config_group.device.variables
================================


Operation: GET /dataservice/v1/config-group/{configGroupId}/device/variables
----------------------------------------------------------------------------


Get device variables

.. code:: python

    def get(
        config_group_id: str,
        device_id: Optional[str] = None,
        suggestions: Optional[bool] = None,
    ) -> GetConfigGroupDeviceVariablesGetResponse: ...


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
        client.v1.config_group.device.variables.get()


Operation: PUT /dataservice/v1/config-group/{configGroupId}/device/variables
----------------------------------------------------------------------------


assign values to device variables

.. code:: python

    def put(
        config_group_id: str,
        payload: CreateConfigGroupDeviceVariablesPutRequest,
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
        client.v1.config_group.device.variables.put()


Operation: POST /dataservice/v1/config-group/{configGroupId}/device/variables
-----------------------------------------------------------------------------


Fetch device variables

.. code:: python

    def post(
        config_group_id: str,
        payload: FetchConfigGroupDeviceVariablesPostRequest,
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
        client.v1.config_group.device.variables.post()


.. toctree::
    :maxdepth: 1

    schema
    models

