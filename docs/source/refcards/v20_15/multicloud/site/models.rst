======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class TunnelsInner:
        """
        CGW details relevant to AWS/AWS_GOVCLOUD
        """

        accepted_route_count: Optional[int]
        last_status_change_timestamp: Optional[str]
        outer_ip_addr: Optional[str]
        status: Optional[str]
        status_message: Optional[str]
        tunnel_id: Optional[str]
        tunnel_inner_ip: Optional[List[str]]


    class GetSitesResponse:
        accelerated_vpn: Optional[bool]
        agg_tunnel_status: Optional[str]
        attached: Optional[bool]
        color: Optional[str]
        hostname: Optional[str]
        interface: Optional[str]
        preferred_interface: Optional[bool]
        private_ip: Optional[str]
        public_ip: Optional[str]
        site_id: Optional[str]
        system_ip: Optional[str]
        tunnel_count: Optional[int]
        # CGW details relevant to AWS/AWS_GOVCLOUD
        tunnels: Optional[List[TunnelsInner]]
        uuid: Optional[str]


