========================================
multicloud.interconnect.gateways.devices
========================================


Operation: GET /dataservice/multicloud/interconnect/{interconnect-type}/gateways/devices
----------------------------------------------------------------------------------------


API to retrieve available Interconnect Gateway devices.

.. code:: python

    def get(
        interconnect_type: InterconnectTypeParam,
    ) -> List[InlineResponse2003]: ...


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
        client.multicloud.interconnect.gateways.devices.get()


.. toctree::
    :maxdepth: 1

    models

