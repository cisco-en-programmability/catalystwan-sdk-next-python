==============================
device.policy.zonepairsessions
==============================


Operation: GET /dataservice/device/policy/zonepairsessions
----------------------------------------------------------


Get zone pair sessions from device

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
        client.device.policy.zonepairsessions.get()


