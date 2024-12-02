===================================
device.orchestrator.localproperties
===================================


Operation: GET /dataservice/device/orchestrator/localproperties
---------------------------------------------------------------


Get local properties list from device

.. code:: python

    def create_local_properties_list_list(device_id: str) -> Any: ...


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
        client.device.orchestrator.localproperties.create_local_properties_list_list()


