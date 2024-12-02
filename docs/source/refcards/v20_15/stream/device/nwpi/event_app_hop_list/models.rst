======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class EventAppHopListResponsePayloadInner:
        """
        Application and HopList schema for GET response
        """

        application: Optional[str]
        down_hop_list_info: Optional[List[Any]]
        down_max_hop_num: Optional[int]
        entry_time: Optional[int]
        server_side_key: Optional[str]
        trace_id: Optional[int]
        type_: Optional[str]
        up_hop_list_info: Optional[List[Any]]
        up_max_hop_num: Optional[int]
        vpn_id: Optional[str]


