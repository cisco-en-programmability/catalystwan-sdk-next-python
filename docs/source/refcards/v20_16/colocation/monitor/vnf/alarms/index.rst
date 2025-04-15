=============================
colocation.monitor.vnf.alarms
=============================


Operation: GET /dataservice/colocation/monitor/vnf/alarms
---------------------------------------------------------


Deprecated!!!

Get event detail of VNF

.. code:: python

    def get(user_group: str) -> None: ...


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
        client.colocation.monitor.vnf.alarms.get()


.. toctree::
    :maxdepth: 1

    count

