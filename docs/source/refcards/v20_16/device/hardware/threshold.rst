=========================
device.hardware.threshold
=========================


Operation: GET /dataservice/device/hardware/threshold
-----------------------------------------------------


Get hardware temperature list from device

.. code:: python

    def create_temp_threshold_list(device_id: str) -> Any: ...


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
        client.device.hardware.threshold.create_temp_threshold_list()


