=============================================================
multicloud.interconnect.connectivity.device_links.port_speeds
=============================================================


Operation: GET /dataservice/multicloud/interconnect/{interconnect-type}/connectivity/device-links/port-speeds
-------------------------------------------------------------------------------------------------------------


API to get supported port speeds for Device-Link by Interconnect provider.

.. code:: python

    def get_interconnect_device_link_port_speeds(
        interconnect_type: str,
    ) -> InlineResponse20011: ...


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
        client.multicloud.interconnect.connectivity.device_links.port_speeds.get_interconnect_device_link_port_speeds()


.. toctree::
    :maxdepth: 1

    models

