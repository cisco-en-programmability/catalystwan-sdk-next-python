============================
stream.device.nwpi.nwpi_dscp
============================


Operation: GET /dataservice/stream/device/nwpi/nwpiDSCP
-------------------------------------------------------


Deprecated!!!

.. code:: python

    def get_nwpi_dscp() -> List[NwpiDscpResponsePayloadInner]: ...


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
        client.stream.device.nwpi.nwpi_dscp.get_nwpi_dscp()


.. toctree::
    :maxdepth: 1

    models

