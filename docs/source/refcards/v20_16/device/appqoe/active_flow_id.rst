============================
device.appqoe.active_flow_id
============================


Operation: GET /dataservice/device/appqoe/active-flow-id
--------------------------------------------------------


Get Appqoe Active flow Id details from device

.. code:: python

    def get(flow_id: str, device_id: str) -> Any: ...


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
        client.device.appqoe.active_flow_id.get()


