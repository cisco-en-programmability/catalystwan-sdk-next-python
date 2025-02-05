===================================
colocation.monitor.vnf.alarms.count
===================================


Operation: GET /dataservice/colocation/monitor/vnf/alarms/count
---------------------------------------------------------------


Deprecated!!!

Get alarm count of VNF

.. code:: python

    def get_vnf_alarm_count(user_group: str) -> None: ...


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
        client.colocation.monitor.vnf.alarms.count.get_vnf_alarm_count()


