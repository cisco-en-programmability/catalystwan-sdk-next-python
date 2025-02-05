==================================
multicloud.interconnect.ip_transit
==================================


Operation: GET /dataservice/multicloud/interconnect/ip-transit
--------------------------------------------------------------


API to retrieve Interconnect ip transit in MB supported by an  Interconnect provider.

.. code:: python

    def get_interconnect_ip_transit(
        interconnect_service_type: str, interconnect_type: str
    ) -> InlineResponse20016: ...


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
        client.multicloud.interconnect.ip_transit.get_interconnect_ip_transit()


.. toctree::
    :maxdepth: 1

    models

