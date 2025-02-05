==================
device.qfp.memstat
==================


Operation: GET /dataservice/device/qfp/memstat
----------------------------------------------


Get QFP memory status

.. code:: python

    def memstat(device_id: str) -> QfpMemoryState: ...


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
        client.device.qfp.memstat.memstat()


.. toctree::
    :maxdepth: 1

    models

