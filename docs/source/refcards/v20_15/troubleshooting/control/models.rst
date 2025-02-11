======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    LocalStatus = Literal["green", "red"]

    PeerType = Literal[
        "nonSDWAN", "vbond", "vedge", "vedge-vbond", "vmanage", "vsmart"
    ]

    State = Literal["down", "up"]


    class TlocControl:
        host_name: Optional[str]
        is_preferred: Optional[bool]
        local_status: Optional[LocalStatus]
        local_status_info: Optional[str]
        peer_type: Optional[PeerType]
        remote_status: Optional[LocalStatus]
        remote_status_info: Optional[str]
        state: Optional[State]
        system_ip: Optional[str]


    class ControlConnectionInfo:
        actual_connections: Optional[int]
        color: Optional[str]
        control: Optional[List[TlocControl]]
        expected_connections: Optional[int]
        interface: Optional[str]
        nat_type: Optional[str]
        private_ip: Optional[str]
        private_port: Optional[str]
        public_ip: Optional[str]
        public_port: Optional[str]
        tloc_status: Optional[LocalStatus]
        tloc_type: Optional[str]


    class GetControlConnections:
        actual_control_connections_to_vsmart: Optional[int]
        data: Optional[List[ControlConnectionInfo]]
        expected_control_connections_to_vsmart: Optional[int]


