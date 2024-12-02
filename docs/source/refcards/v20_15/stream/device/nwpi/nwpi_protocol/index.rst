================================
stream.device.nwpi.nwpi_protocol
================================


Operation: GET /dataservice/stream/device/nwpi/nwpiProtocol
-----------------------------------------------------------


Deprecated!!!

.. code:: python

    def get_nwpi_protocol() -> List[NwpiProtocolResponsePayloadInner]: ...


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
        client.stream.device.nwpi.nwpi_protocol.get_nwpi_protocol()


.. toctree::
    :maxdepth: 1

    models

