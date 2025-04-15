============================
device.dre.auto_bypass_stats
============================


Operation: GET /dataservice/device/dre/auto-bypass-stats
--------------------------------------------------------


Get DRE auto-bypass statistics

.. code:: python

    def get(
        device_id: str,
        appqoe_dre_auto_bypass_server_ip: Optional[str] = None,
        appqoe_dre_auto_bypass_port: Optional[int] = None,
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
        client.device.dre.auto_bypass_stats.get()


