=============================
colocation.monitor.vnf.action
=============================


Operation: POST /dataservice/colocation/monitor/vnf/action
----------------------------------------------------------


Deprecated!!!

To do VNF actions such as start, stop and restart

.. code:: python

    def post(
        vm_name: str, action: str, device_id: Optional[DeviceUuid] = None
    ) -> None: ...


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
        client.colocation.monitor.vnf.action.post()


.. toctree::
    :maxdepth: 1

    models

