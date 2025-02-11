==================
device.qfp.cpustat
==================


Operation: GET /dataservice/device/qfp/cpustat
----------------------------------------------


Get QFP cpu status

.. code:: python

    def cpustat(device_id: str) -> QfpCpuState: ...


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
        client.device.qfp.cpustat.cpustat()


.. toctree::
    :maxdepth: 1

    models

