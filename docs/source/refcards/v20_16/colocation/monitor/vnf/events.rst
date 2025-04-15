=============================
colocation.monitor.vnf.events
=============================


Operation: GET /dataservice/colocation/monitor/vnf/events
---------------------------------------------------------


Deprecated!!!

Get event detail of VNF

.. code:: python

    def get(vnf_name: str) -> None: ...


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
        client.colocation.monitor.vnf.events.get()


