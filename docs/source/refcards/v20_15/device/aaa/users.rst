================
device.aaa.users
================


Operation: GET /dataservice/device/aaa/users
--------------------------------------------


Get AAA users from device (Real Time)

.. code:: python

    def get_aaa_users(device_id: str) -> Any: ...


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
        client.device.aaa.users.get_aaa_users()


