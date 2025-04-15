====================================
stream.device.nwpi.device.blist.del_
====================================


Operation: DELETE /dataservice/stream/device/nwpi/device/blist/del
------------------------------------------------------------------


Deprecated!!!

Delete Device BlackList for NWPI.

.. code:: python

    def delete(system_ip: str) -> DeviceBlistDeleteResponsePayload: ...


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
        client.stream.device.nwpi.device.blist.del_.delete()


.. toctree::
    :maxdepth: 1

    models

