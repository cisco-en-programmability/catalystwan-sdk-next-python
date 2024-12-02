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


    class Taskid:
        """
        Task id for polling status
        """

        id: Optional[str]


    class TunnelScalingRequestPayloadBranchEndpoints:
        accelerated_vpn: str
        cloud_type: str
        color: str
        site_id: str
        system_ip: str
        tunnel_count: str
        host_name: Optional[str]
        interface: Optional[str]
        preferred_interface: Optional[str]
        public_ip: Optional[str]
        solution: Optional[str]
        status: Optional[str]
        uuid: Optional[str]


    class TunnelScalingRequestPayload:
        cloud_type: str
        branch_endpoints: Optional[
            List[TunnelScalingRequestPayloadBranchEndpoints]
        ]


    class AttachSitesRequestPayloadInner:
        color: str
        site_id: str
        # Multicloud Branch Connect Solution type
        solution: str
        system_ip: str
        tunnel_count: str
        accelerated_vpn: Optional[str]
        interface: Optional[str]
        preferred_interface: Optional[str]
        public_ip: Optional[str]


    class DetachSitesRequestPayloadInner:
        site_id: str
        system_ip: str
        color: Optional[str]
        interface: Optional[str]
        solution: Optional[str]


