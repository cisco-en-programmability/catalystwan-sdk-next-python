=================
device.block_sync
=================


Operation: POST /dataservice/device/blockSync
---------------------------------------------


Set collection manager block set flag

.. code:: python

    def post(block_sync: str) -> Any: ...


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
        client.device.block_sync.post()


