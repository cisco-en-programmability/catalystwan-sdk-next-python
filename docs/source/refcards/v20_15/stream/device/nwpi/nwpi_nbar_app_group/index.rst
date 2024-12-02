======================================
stream.device.nwpi.nwpi_nbar_app_group
======================================


Operation: GET /dataservice/stream/device/nwpi/nwpiNbarAppGroup
---------------------------------------------------------------


Deprecated!!!

.. code:: python

    def get_nwpi_nbar_app_group() -> (
        List[NwpiNbarAppGroupResponsePayloadInner]
    ): ...


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
        client.stream.device.nwpi.nwpi_nbar_app_group.get_nwpi_nbar_app_group()


.. toctree::
    :maxdepth: 1

    models

