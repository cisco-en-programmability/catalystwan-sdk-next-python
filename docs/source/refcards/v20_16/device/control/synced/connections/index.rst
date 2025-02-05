=================================
device.control.synced.connections
=================================


Operation: GET /dataservice/device/control/synced/connections
-------------------------------------------------------------


Get connections list from vManage

.. code:: python

    def create_synced_connection_list(
        device_id: str,
        peer_type: Optional[PeerTypeParam] = None,
        system_ip: Optional[str] = None,
    ) -> Any: ...


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
        client.device.control.synced.connections.create_synced_connection_list()


.. toctree::
    :maxdepth: 1

    models

