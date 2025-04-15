===================================
stream.device.nwpi.device.blist.get
===================================


Operation: GET /dataservice/stream/device/nwpi/device/blist/get
---------------------------------------------------------------


Deprecated!!!

Get Device BlackList for NWPI.

.. code:: python

    def get() -> List[DeviceBlistResponsePayloadInner]: ...


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
        client.stream.device.nwpi.device.blist.get.get()


.. toctree::
    :maxdepth: 1

    models

