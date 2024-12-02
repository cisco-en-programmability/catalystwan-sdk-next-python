===========================
device.orchestrator.summary
===========================


Operation: GET /dataservice/device/orchestrator/summary
-------------------------------------------------------


Get connection summary from device

.. code:: python

    def create_connection_summary(device_id: str) -> Any: ...


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
        client.device.orchestrator.summary.create_connection_summary()


