====================
device.app.log.flows
====================


Operation: GET /dataservice/device/app/log/flows
------------------------------------------------


Get App log flows from device (Real Time)

.. code:: python

    def get_app_log_flows(device_id: str) -> Any: ...


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
        client.device.app.log.flows.get_app_log_flows()


