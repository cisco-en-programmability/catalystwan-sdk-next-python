========================
device.cellular.profiles
========================


Operation: GET /dataservice/device/cellular/profiles
----------------------------------------------------


Get cellular profile list from device

.. code:: python

    def create_profile_list(device_id: str) -> List[Any]: ...


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
        client.device.cellular.profiles.create_profile_list()


