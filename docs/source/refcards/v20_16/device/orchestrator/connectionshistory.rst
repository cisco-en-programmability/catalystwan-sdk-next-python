======================================
device.orchestrator.connectionshistory
======================================


Operation: GET /dataservice/device/orchestrator/connectionshistory
------------------------------------------------------------------


Get connection history list from device

.. code:: python

    def create_connection_history_list(device_id: str) -> Any: ...


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
        client.device.orchestrator.connectionshistory.create_connection_history_list()


