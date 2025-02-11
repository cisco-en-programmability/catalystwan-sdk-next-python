============================================
multicloud.interconnect.gateways.image_names
============================================


Operation: GET /dataservice/multicloud/interconnect/gateways/image-names
------------------------------------------------------------------------


API to retrieve Interconnect Gateway software image versions supported by an Interconnect Provider.

.. code:: python

    def get_interconnect_gateway_image_names(
        interconnect_type: InterconnectTypeParam,
    ) -> InlineResponse2005: ...


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
        client.multicloud.interconnect.gateways.image_names.get_interconnect_gateway_image_names()


.. toctree::
    :maxdepth: 1

    models

