===========================
device.multicast.replicator
===========================


Operation: GET /dataservice/device/multicast/replicator
-------------------------------------------------------


Get replicator list from device

.. code:: python

    def create_replicator_list(device_id: str) -> Any: ...


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
        client.device.multicast.replicator.create_replicator_list()


