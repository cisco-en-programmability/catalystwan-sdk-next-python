========================================
stream.device.nwpi.event_readout_by_site
========================================


Operation: GET /dataservice/stream/device/nwpi/eventReadoutBySite
-----------------------------------------------------------------


Deprecated!!!

Get event Readout By Site

.. code:: python

    def get_event_readout_by_site(
        site_id: str, last_n_hours: int, mode: Optional[str] = None
    ) -> EventReadoutsResponsePayloadData: ...


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
        client.stream.device.nwpi.event_readout_by_site.get_event_readout_by_site()


.. toctree::
    :maxdepth: 1

    models

