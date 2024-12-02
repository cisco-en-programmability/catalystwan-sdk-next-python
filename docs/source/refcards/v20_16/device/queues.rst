=============
device.queues
=============


Operation: GET /dataservice/device/queues
-----------------------------------------


Get synchronized queue information, returns information about syncing, queued and stuck devices

.. code:: python

    def get_sync_queues() -> Any: ...


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
        client.device.queues.get_sync_queues()


