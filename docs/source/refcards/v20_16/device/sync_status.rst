==================
device.sync_status
==================


Operation: GET /dataservice/device/sync_status
----------------------------------------------


Get list of currently syncing devices

.. code:: python

    def list_currently_syncing_devices(group_id: str) -> List[Any]: ...


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
        client.device.sync_status.list_currently_syncing_devices()


