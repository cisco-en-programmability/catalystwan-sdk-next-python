======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class TraceCftRecordResponsePayloadData:
        agg_total_bytes: Optional[int]
        agg_total_fif_bytes: Optional[int]
        agg_total_fif_packets: Optional[int]
        agg_total_fin_flows: Optional[int]
        agg_total_flows: Optional[int]
        agg_total_packets: Optional[int]
        agg_total_ttl_ms: Optional[int]
        app_group: Optional[str]
        app_name: Optional[str]
        avg_bps: Optional[int]
        avg_concurrent_flows: Optional[int]
        avg_cps: Optional[int]
        avg_pps: Optional[int]
        avg_ttl_ms: Optional[int]
        bps: Optional[int]
        concurrent_flows: Optional[int]
        cps: Optional[int]
        device_name: Optional[str]
        device_trace_id: Optional[int]
        device_uuid: Optional[str]
        if_name: Optional[str]
        last_report_ts: Optional[int]
        local_color: Optional[str]
        max_bps: Optional[int]
        max_concurrent_flows: Optional[int]
        max_cps: Optional[int]
        max_pps: Optional[int]
        max_ttl_ms: Optional[int]
        min_bps: Optional[int]
        min_concurrent_flows: Optional[int]
        min_cps: Optional[int]
        min_pps: Optional[int]
        min_ttl_ms: Optional[int]
        model: Optional[str]
        pps: Optional[int]
        received_timestamp: Optional[int]
        system_ip: Optional[str]
        vpn_id: Optional[str]


    class TraceCftRecordResponsePayload:
        """
        Get cft record for GET response
        """

        data: Optional[TraceCftRecordResponsePayloadData]
        entry_time: Optional[int]
        tenant: Optional[str]
        trace_id: Optional[int]
        type_: Optional[str]


