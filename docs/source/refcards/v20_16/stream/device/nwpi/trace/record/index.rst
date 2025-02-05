===============================
stream.device.nwpi.trace.record
===============================


Operation: POST /dataservice/stream/device/nwpi/trace/record/{deviceUUID}
-------------------------------------------------------------------------


Deprecated!!!

post flow data

.. code:: python

    def nwpi_post_flow_data(
        device_uuid: str, payload: str
    ) -> NwpiResponsePayload: ...


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
        client.stream.device.nwpi.trace.record.nwpi_post_flow_data()


.. toctree::
    :maxdepth: 1

    models

