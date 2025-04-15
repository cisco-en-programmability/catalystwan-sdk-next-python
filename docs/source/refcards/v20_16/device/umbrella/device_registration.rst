===================================
device.umbrella.device_registration
===================================


Operation: GET /dataservice/device/umbrella/device-registration
---------------------------------------------------------------


Get Umbrella device registration from device

.. code:: python

    def get(device_id: str) -> Any: ...


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
        client.device.umbrella.device_registration.get()


