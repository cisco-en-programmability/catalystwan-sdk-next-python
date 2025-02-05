======
Models
======


.. code:: python

    from typing import Union, Dict, Optional, Literal, List, Any

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


    class AaaServerInfo:
        aaa_servers_parcel_id: str
        radius_server_name: str


    class EthernetInterface:
        interface_name: str
        port_type: str
        aaa_server_info: Optional[AaaServerInfo]
        admin_state: Optional[str]
        corporate_lan: Optional[bool]
        ip_assignment: Optional[str]
        ipv6_assignment: Optional[str]
        static_ip_address: Optional[str]
        static_ip_address_subnet_mask: Optional[str]
        static_route_ip: Optional[str]
        wan_configuration: Optional[str]


    class CreateEthernetProfileParcelForMobilityPostRequest:
        ethernet_interface_list: List[EthernetInterface]
        # Name of the Profile Parcel. Must be unique.
        name: str
        type_: Type
        # User who last created this.
        created_by: Optional[str]
        # Timestamp of creation
        created_on: Optional[int]
        # Description of the Profile Parcel.
        description: Optional[str]
        # System generated unique identifier of the Profile Parcel in UUID format.
        id: Optional[str]
        # User who last updated this.
        last_updated_by: Optional[str]
        # Timestamp of last update
        last_updated_on: Optional[int]
        variables: Optional[List[Variable]]


