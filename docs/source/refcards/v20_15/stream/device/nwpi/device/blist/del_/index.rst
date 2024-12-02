====================================
stream.device.nwpi.device.blist.del_
====================================


Operation: DELETE /dataservice/stream/device/nwpi/device/blist/del
------------------------------------------------------------------


Deprecated!!!

Delete Device BlackList for NWPI.

.. code:: python

    def del_device_black(
        system_ip: str,
    ) -> DeviceBlistDeleteResponsePayload: ...


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
        client.stream.device.nwpi.device.blist.del_.del_device_black()


.. toctree::
    :maxdepth: 1

    models

