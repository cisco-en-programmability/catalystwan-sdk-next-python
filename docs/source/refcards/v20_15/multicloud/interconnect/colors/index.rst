==============================
multicloud.interconnect.colors
==============================


Operation: GET /dataservice/multicloud/interconnect/colors/{tunnel-type}
------------------------------------------------------------------------


API to retrieve supported Colors for Interconnect tunnel type.

.. code:: python

    def get(tunnel_type: TunnelTypeParam) -> InlineResponse2002: ...


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
        client.multicloud.interconnect.colors.get()


.. toctree::
    :maxdepth: 1

    models

