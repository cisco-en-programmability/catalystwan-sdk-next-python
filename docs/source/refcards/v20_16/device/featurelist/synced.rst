=========================
device.featurelist.synced
=========================


Operation: GET /dataservice/device/featurelist/synced
-----------------------------------------------------


Get feature lists synchronously from device

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
        client.device.featurelist.synced.get()


