============
device.users
============


Operation: GET /dataservice/device/users
----------------------------------------


Get users from device (Real Time)

.. code:: python

    def get_users_from_device(device_id: str) -> List[Any]: ...


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
        client.device.users.get_users_from_device()


.. toctree::
    :maxdepth: 1

    list

