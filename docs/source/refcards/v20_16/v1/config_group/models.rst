======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    Solution = Literal[
        "cellulargateway",
        "common",
        "mobility",
        "nfvirtual",
        "sd-routing",
        "sdwan",
        "service-insertion",
    ]

    Attribute = Literal["tag"]

    ParcelType = Literal[
        "global-vrf",
        "global-vrf/routing/bgp",
        "global-vrf/wan/interface/ipsec",
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
        "vrf/lan/multicloud-connection",
        "vrf/routing/bgp",
        "vrf/wan/interface/ethernet",
        "vrf/wan/interface/gre",
        "vrf/wan/interface/ipsec",
        "vrf/wan/multicloud-connection",
        "wan/multicloud-connection",
        "wan/vpn/interface/cellular",
        "wan/vpn/interface/dsl-ipoe",
        "wan/vpn/interface/dsl-pppoa",
        "wan/vpn/interface/dsl-pppoe",
        "wan/vpn/interface/ethernet",
        "wan/vpn/interface/gre",
        "wan/vpn/interface/ipsec",
        "wan/vpn/interface/serial",
    ]

    ProfileType = Literal["global"]

    Source = Literal[
        "custom_workflow",
        "equinix_workflow",
        "nfvirtual_workflow",
        "retail_workflow",
    ]

    SolutionDef = Literal[
        "cellulargateway",
        "mobility",
        "nfvirtual",
        "sd-routing",
        "sdwan",
        "service-insertion",
    ]

    UnsupportedFeaturesEnumDef = Literal[
        "lan/multicloud-connection",
        "lan/vpn",
        "lan/vpn/interface/ethernet",
        "lan/vpn/interface/ipsec",
        "lan/vpn/interface/svi",
        "route-policy",
        "routing/bgp",
        "routing/ospf",
        "vrf",
        "vrf/lan/interface/ethernet",
        "vrf/lan/interface/ipsec",
        "vrf/lan/multicloud-connection",
        "vrf/routing/bgp",
        "vrf/wan/interface/ethernet",
        "vrf/wan/interface/gre",
        "vrf/wan/interface/ipsec",
        "vrf/wan/multicloud-connection",
        "wan/multicloud-connection",
        "wan/vpn/interface/cellular",
        "wan/vpn/interface/dsl-ipoe",
        "wan/vpn/interface/dsl-pppoa",
        "wan/vpn/interface/dsl-pppoe",
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
        copy_info: Optional[str]
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


    class ProfileObjDef:
        id: str
        profile_type: ProfileType


    class CreateConfigGroupPostResponse:
        """
        Config Group POST Response schema
        """

        id: str
        # (Optional - only applicable for AON) List of profile ids that belongs to the config group
        profiles: Optional[List[ProfileObjDef]]


    class Criteria_1:
        attribute: Attribute  # pytype: disable=annotation-type-mismatch
        value: str


    class UnsupportedFeatures:
        parcel_id: str
        parcel_type: UnsupportedFeaturesEnumDef


    class TopologyDevicePropertiesDef:
        criteria: Criteria_1
        unsupported_features: Optional[List[UnsupportedFeatures]]


    class TopologyDef:
        # list of devices in a site
        devices: List[TopologyDevicePropertiesDef]
        site_devices: Optional[int]


    class ProfileIdObjDef:
        id: str


    class FromConfigGroupDef:
        copy: str


    class CreateConfigGroupPostRequest:
        """
        Config Group POST Request schema
        """

        description: str
        name: str
        solution: SolutionDef  # pytype: disable=annotation-type-mismatch
        from_config_group: Optional[FromConfigGroupDef]
        # list of profile ids that belongs to the config group
        profiles: Optional[List[ProfileIdObjDef]]
        source: Optional[Source]
        topology: Optional[TopologyDef]


    class ConfigGroupProfileObjDef:
        id: str
        profile_type: ProfileType


    class EditConfigGroupPutResponse:
        """
        Config Group PUT Response schema
        """

        id: str
        # (Optional - only applicable for AON) List of profile ids that belongs to the config group
        profiles: Optional[List[ConfigGroupProfileObjDef]]


    class ConfigGroupTopologyDevicePropertiesDef:
        criteria: Criteria_1
        unsupported_features: Optional[List[UnsupportedFeatures]]


    class ConfigGroupTopologyDef:
        # list of devices in a site
        devices: List[ConfigGroupTopologyDevicePropertiesDef]
        site_devices: Optional[int]


    class ConfigGroupProfileIdObjDef:
        id: str


    class EditConfigGroupPutRequest:
        """
        Config Group PUT Request schema
        """

        description: str
        name: str
        solution: SolutionDef  # pytype: disable=annotation-type-mismatch
        # list of profile ids that belongs to the config group
        profiles: Optional[List[ConfigGroupProfileIdObjDef]]
        topology: Optional[ConfigGroupTopologyDef]


