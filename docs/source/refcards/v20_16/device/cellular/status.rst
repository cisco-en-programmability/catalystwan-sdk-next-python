======================
device.cellular.status
======================


Operation: GET /dataservice/device/cellular/status
--------------------------------------------------


Get cellular status list from device

.. code:: python

    def get_cellular_status_list(device_id: str) -> List[Any]: ...


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
        client.device.cellular.status.get_cellular_status_list()


