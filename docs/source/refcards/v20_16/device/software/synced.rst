======================
device.software.synced
======================


Operation: GET /dataservice/device/software/synced
--------------------------------------------------


Get software list from device synchronously

.. code:: python

    def create_synced_software_list(device_id: str) -> List[Any]: ...


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
        client.device.software.synced.create_synced_software_list()


