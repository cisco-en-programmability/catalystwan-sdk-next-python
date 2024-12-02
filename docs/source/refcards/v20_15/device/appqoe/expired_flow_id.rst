=============================
device.appqoe.expired_flow_id
=============================


Operation: GET /dataservice/device/appqoe/expired-flow-id
---------------------------------------------------------


Get Appqoe Expired flow Id details from device

.. code:: python

    def create_appqoe_flow_id_expired_details(
        flow_id: str, device_id: str
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
        client.device.appqoe.expired_flow_id.create_appqoe_flow_id_expired_details()


