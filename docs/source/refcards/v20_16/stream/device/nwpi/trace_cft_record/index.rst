===================================
stream.device.nwpi.trace_cft_record
===================================


Operation: GET /dataservice/stream/device/nwpi/traceCftRecord
-------------------------------------------------------------


Deprecated!!!

Get Trace CFT record

.. code:: python

    def get_trace_cft_record(
        trace_id: int,
        entry_time: int,
        trace_state: str,
        vpn_ids: Optional[List[int]] = None,
        local_colors: Optional[List[str]] = None,
        devices: Optional[List[str]] = None,
        vrf_names: Optional[List[str]] = None,
    ) -> TraceCftRecordResponsePayload: ...


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
        client.stream.device.nwpi.trace_cft_record.get_trace_cft_record()


.. toctree::
    :maxdepth: 1

    models

