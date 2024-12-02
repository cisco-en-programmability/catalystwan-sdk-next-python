=================
device.smu.synced
=================


Operation: GET /dataservice/device/smu/synced
---------------------------------------------


Get software list from device synchronously

.. code:: python

    def create_synced_smu_list(device_id: str) -> List[Any]: ...


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
        client.device.smu.synced.create_synced_smu_list()


