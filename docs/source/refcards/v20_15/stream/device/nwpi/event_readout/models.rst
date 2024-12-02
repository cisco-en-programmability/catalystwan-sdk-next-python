======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class EventReadoutResponsePayloadInner:
        """
        Event Readout schema for GET response
        """

        application: Optional[str]
        drop_send_pkts: Optional[List[Any]]
        entry_time: Optional[int]
        event_hop_policy_info: Optional[List[Any]]
        event_hop_statistics: Optional[List[Any]]
        event_hop_time_info: Optional[List[Any]]
        event_impacted_flow_num: Optional[List[Any]]
        event_list: Optional[List[Any]]
        event_num: Optional[List[Any]]
        readout_agg_flag: Optional[bool]
        total_flow_num: Optional[int]
        trace_id: Optional[int]


