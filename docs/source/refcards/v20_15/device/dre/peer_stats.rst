=====================
device.dre.peer_stats
=====================


Operation: GET /dataservice/device/dre/peer-stats
-------------------------------------------------


Get DRE peer statistics

.. code:: python

    def get(
        device_id: str,
        appqoe_dre_stats_peer_system_ip: Optional[str] = None,
        appqoe_dre_stats_peer_peer_no: Optional[int] = None,
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
        client.device.dre.peer_stats.get()


