=============================================================
multicloud.interconnect.connectivity.device_links.metro_speed
=============================================================


Operation: POST /dataservice/multicloud/interconnect/{interconnect-type}/connectivity/device-links/metro-speed
--------------------------------------------------------------------------------------------------------------


API to get metro speed for Device-Link by Device-Link Configuration.

.. code:: python

    def get_interconnect_device_link_metro_speed(
        interconnect_type: InterconnectTypeParam,
        payload: Optional[InterconnectDeviceLink] = None,
    ) -> InlineResponse20012: ...


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
        client.multicloud.interconnect.connectivity.device_links.metro_speed.get_interconnect_device_link_metro_speed()


.. toctree::
    :maxdepth: 1

    models

