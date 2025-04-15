====================================
stream.device.nwpi.current_timestamp
====================================


Operation: GET /dataservice/stream/device/nwpi/currentTimestamp
---------------------------------------------------------------


Deprecated!!!

.. code:: python

    def get() -> CurrentTimestampResponsePayload: ...


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
        client.stream.device.nwpi.current_timestamp.get()


.. toctree::
    :maxdepth: 1

    models

