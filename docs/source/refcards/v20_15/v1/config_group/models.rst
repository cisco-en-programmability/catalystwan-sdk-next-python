======
Models
======


.. code:: python

    from typing import List, Any, Optional, Literal, Dict, Union

    Solution = Literal[
        "cellulargateway",
        "common",
        "mobility",
        "nfvirtual",
        "sd-routing",
        "sdwan",
        "service-insertion",
    ]

    Attribute = Literal["rule", "tag"]

    ParcelType = Literal[
        "lan/multicloud-connection",
        "lan/vpn",
        "lan/vpn/interface/ethernet",
        "lan/vpn/interface/gre",
        "lan/vpn/interface/ipsec",
        "lan/vpn/interface/svi",
        "route-policy",
        "routing/bgp",
        "routing/ospf",
        "service-insertion-attachment",
        "vrf",
        "vrf/lan/interface/ethernet",
        "vrf/lan/interface/gre",
        "vrf/lan/interface/ipsec",
        "vrf/routing/bgp",
        "vrf/wan/interface/ethernet",
        "vrf/wan/interface/gre",
        "vrf/wan/interface/ipsec",
        "wan/multicloud-connection",
        "wan/vpn/interface/cellular",
        "wan/vpn/interface/ethernet",
        "wan/vpn/interface/gre",
        "wan/vpn/interface/ipsec",
        "wan/vpn/interface/serial",
    ]


    class FeatureProfile:
        """
        List of devices UUIDs associated with this group
        """

        # Name of the feature Profile. Must be unique.
        name: str
        # Solution of the feature Profile.
        solution: str
        # Type of the feature Profile.
        type_: str
        # User who last created this.
        created_by: Optional[str]
        # Timestamp of creation
        created_on: Optional[int]
        # Description of the feature Profile.
        description: Optional[str]
        # System generated unique identifier of the feature profile in UUID format.
        id: Optional[str]
        # User who last updated this.
        last_updated_by: Optional[str]
        # Timestamp of last update
        last_updated_on: Optional[int]
        # Number of Parcels attached with Feature Profile
        profile_parcel_count: Optional[int]


    class Criteria:
        attribute: Optional[Attribute]
        value: Optional[str]


    class UnsupportedFeature:
        parcel_id: Optional[str]
        parcel_type: Optional[ParcelType]


    class ConfigGroupDevice:
        criteria: Optional[Criteria]
        unsupported_features: Optional[List[UnsupportedFeature]]


    class Topology:
        devices: Optional[List[ConfigGroupDevice]]
        site_devices: Optional[int]


    class ConfigGroup:
        # Name of the  Group. Must be unique.
        name: str
        # Specify one of the device platform solution
        solution: Solution  # pytype: disable=annotation-type-mismatch
        #  Group Deployment state
        state: str
        #  Group Version Flag
        version: int
        # User who last created this.
        created_by: Optional[str]
        # Timestamp of creation
        created_on: Optional[int]
        # Description of the  Group.
        description: Optional[str]
        devices: Optional[List[str]]
        full_config_cli: Optional[bool]
        # System generated unique identifier of the  Group in UUID format.
        id: Optional[str]
        ios_config_cli: Optional[bool]
        # User who last updated this.
        last_updated_by: Optional[str]
        # Timestamp of last update
        last_updated_on: Optional[int]
        number_of_devices: Optional[int]
        number_of_devices_up_to_date: Optional[int]
        origin: Optional[str]
        origin_info: Optional[Dict[str, str]]
        # List of devices UUIDs associated with this group
        profiles: Optional[List[FeatureProfile]]
        # Source of group
        source: Optional[str]
        topology: Optional[Topology]
        version_increment_reason: Optional[str]


