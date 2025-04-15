===============================
stream.device.nwpi.query.fields
===============================


Operation: GET /dataservice/stream/device/nwpi/query/fields
-----------------------------------------------------------


Deprecated!!!

Get query fields

.. code:: python

    def get() -> List[QueryFieldsResponsePayloadInner]: ...


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
        client.stream.device.nwpi.query.fields.get()


.. toctree::
    :maxdepth: 1

    models

