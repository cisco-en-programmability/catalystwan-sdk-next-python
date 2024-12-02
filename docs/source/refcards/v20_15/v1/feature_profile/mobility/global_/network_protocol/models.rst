======
Models
======


.. code:: python

    from typing import Literal, Optional, List, Union, Dict, Any

    Type = Literal[
        "cellular",
        "ethernet",
        "globalSettings",
        "networkProtocol",
        "securityPolicy",
        "wifi",
    ]


    class Variable:
        json_path: str
        var_name: str


    class DhcpPool:
        lease_time_day: int
        lease_time_hour: int
        lease_time_min: int
        pool_network: str


    class NatRule:
        description: str
        in_port: int
        inside_ip: str
        interface: str
        out_port: int
        protocol: str


    class CreateNetworkProtocolProfileParcelForMobilityPostRequest:
        # Name of the Profile Parcel. Must be unique.
        name: str
        type_: Type
        # User who last created this.
        created_by: Optional[str]
        # Timestamp of creation
        created_on: Optional[int]
        # Description of the Profile Parcel.
        description: Optional[str]
        dhcp_pool: Optional[DhcpPool]
        dns_settings: Optional[str]
        # System generated unique identifier of the Profile Parcel in UUID format.
        id: Optional[str]
        # User who last updated this.
        last_updated_by: Optional[str]
        # Timestamp of last update
        last_updated_on: Optional[int]
        nat_rules: Optional[List[NatRule]]
        ntp_inherit: Optional[bool]
        ntp_settings: Optional[List[str]]
        variables: Optional[List[Variable]]


