==================
device.nms.running
==================


Operation: GET /dataservice/device/nms/running
----------------------------------------------


Get nms running state from device

.. code:: python

    def get_running(device_id: str) -> List[Any]: ...


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
        client.device.nms.running.get_running()


