=============================
device.control.summary.device
=============================


Operation: GET /dataservice/device/control/summary/device
---------------------------------------------------------


Get device control status summary

.. code:: python

    def get_device_control_status_summary(device_id: str) -> Any: ...


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
        client.device.control.summary.device.get_device_control_status_summary()


