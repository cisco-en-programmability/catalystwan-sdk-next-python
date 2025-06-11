======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    GlobalOptionTypeDef = Literal["global"]

    DefaultOptionTypeDef = Literal["default"]

    BooleanFalseDef = Literal[False]

    VirtualApplicationApplicationTypeDef = Literal["dreopt"]

    VirtualApplicationResourceProfileDef = Literal[
        "default", "extra-large", "large", "medium", "small"
    ]

    VariableOptionTypeDef = Literal["variable"]

    DefaultVirtualApplicationResourceProfileDef = Literal["default"]

    AppqoeDeviceRoleDef = Literal[
        "forwarder",
        "forwarderAndServiceNode",
        "forwarderAndServiceNodeWithDre",
        "serviceNode",
        "serviceNodeWithDre",
    ]

    AppqoeVpnDef = Literal[0]

    DefaultAppnavControllerGroupDef = Literal["ACG-APPQOE"]

    DefaultServiceNodeGroupDef = Literal["SNG-APPQOE"]

    AppnavControllerGroupAppnavControllersDefaultAddressDef = Literal[
        "192.168.2.1"
    ]

    BooleanTrueDef = Literal[True]

    DefaultExternalServiceNodeAddressDef = Literal["192.168.2.2"]

    DefaultExternalServiceNodeVpgIpDef = Literal["192.168.2.1/24"]


    class OneOfDreoptOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfDreoptOptionsDef2:
        option_type: DefaultOptionTypeDef
        value: BooleanFalseDef  # pytype: disable=annotation-type-mismatch


    class OneOfVirtualApplicationInstanceIdOptionsDef:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfVirtualApplicationApplicationTypeOptionsDef:
        option_type: GlobalOptionTypeDef
        value: VirtualApplicationApplicationTypeDef


    class OneOfVirtualApplicationResourceProfileOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: VirtualApplicationResourceProfileDef


    class OneOfVirtualApplicationResourceProfileOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfVirtualApplicationResourceProfileOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: DefaultVirtualApplicationResourceProfileDef  # pytype: disable=annotation-type-mismatch


    class VirtualApplication:
        instance_id: OneOfVirtualApplicationInstanceIdOptionsDef
        application_type: Optional[
            OneOfVirtualApplicationApplicationTypeOptionsDef
        ]
        resource_profile: Optional[
            Union[
                OneOfVirtualApplicationResourceProfileOptionsDef1,
                OneOfVirtualApplicationResourceProfileOptionsDef2,
                OneOfVirtualApplicationResourceProfileOptionsDef3,
            ]
        ]


    class OneOfAppqoeDeviceRoleOptionsDef:
        option_type: GlobalOptionTypeDef
        value: AppqoeDeviceRoleDef


    class OneOfAppqoeNameOptionsDef:
        option_type: DefaultOptionTypeDef
        value: str


    class OneOfAppqoeAppnavControllerGroupOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfAppqoeServiceNodeGroupOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class ServiceNodeGroups:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfAppqoeEnableOptionsDef:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfAppqoeVpnOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: AppqoeVpnDef  # pytype: disable=annotation-type-mismatch


    class OneOfAppqoeVpnOptionsDef2:
        option_type: DefaultOptionTypeDef


    class OneOfAppqoeVpnOptionsDef3:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class Appqoe:
        name: OneOfAppqoeNameOptionsDef
        appnav_controller_group: Optional[
            OneOfAppqoeAppnavControllerGroupOptionsDef
        ]
        enable: Optional[OneOfAppqoeEnableOptionsDef]
        service_node_group: Optional[
            OneOfAppqoeServiceNodeGroupOptionsDef
        ]
        # Service node group
        service_node_groups: Optional[List[ServiceNodeGroups]]
        vpn: Optional[
            Union[
                OneOfAppqoeVpnOptionsDef1,
                OneOfAppqoeVpnOptionsDef2,
                OneOfAppqoeVpnOptionsDef3,
            ]
        ]


    class ServiceContext:
        """
        Service Context
        """

        # Appqoe
        appqoe: Optional[List[Appqoe]]


    class Forwarder1:
        appnav_controller_group: Any
        service_node_group: Any
        # Service Context
        service_context: Optional[ServiceContext]


    class OneOfAppnavControllerGroupGroupNameOptionsDef:
        option_type: DefaultOptionTypeDef
        value: DefaultAppnavControllerGroupDef


    class OneOfAppnavControllerGroupAppnavControllersAddressOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: Union[Any, str]


    class OneOfAppnavControllerGroupAppnavControllersAddressOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfAppnavControllerGroupAppnavControllersVpnOptionsDef:
        option_type: GlobalOptionTypeDef
        value: int


    class AppnavControllers:
        address: Union[
            OneOfAppnavControllerGroupAppnavControllersAddressOptionsDef1,
            OneOfAppnavControllerGroupAppnavControllersAddressOptionsDef2,
        ]
        vpn: Optional[
            OneOfAppnavControllerGroupAppnavControllersVpnOptionsDef
        ]


    class AppnavControllerGroup:
        group_name: OneOfAppnavControllerGroupGroupNameOptionsDef
        # List of controllers
        appnav_controllers: Optional[List[AppnavControllers]]


    class OneOfServiceNodeGroupNameOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfServiceNodeGroupNameOptionsDef2:
        option_type: DefaultOptionTypeDef
        value: DefaultServiceNodeGroupDef  # pytype: disable=annotation-type-mismatch


    class OneOfDefaultFalseServiceNodeGroupInternalOptionsDef:
        option_type: DefaultOptionTypeDef
        value: BooleanFalseDef  # pytype: disable=annotation-type-mismatch


    class OneOfServiceNodeGroupServiceNodeAddressOptionsDef:
        option_type: GlobalOptionTypeDef
        value: Union[Any, str]


    class ServiceNode:
        address: OneOfServiceNodeGroupServiceNodeAddressOptionsDef


    class ServiceNodeGroup:
        name: Union[
            OneOfServiceNodeGroupNameOptionsDef1,
            OneOfServiceNodeGroupNameOptionsDef2,
        ]
        internal: Optional[
            OneOfDefaultFalseServiceNodeGroupInternalOptionsDef
        ]
        # Service Node Information
        service_node: Optional[List[ServiceNode]]


    class Forwarder2:
        # Appnav controller group name
        appnav_controller_group: Optional[List[AppnavControllerGroup]]
        # Service Context
        service_context: Optional[ServiceContext]
        # Name
        service_node_group: Optional[List[ServiceNodeGroup]]


    class OneOfAppnavControllerGroupAppnavControllersDefaultAddressOptionsDef:
        option_type: DefaultOptionTypeDef
        value: AppnavControllerGroupAppnavControllersDefaultAddressDef  # pytype: disable=annotation-type-mismatch


    class AppqoeAppnavControllers:
        address: OneOfAppnavControllerGroupAppnavControllersDefaultAddressOptionsDef


    class AppqoeAppnavControllerGroup:
        group_name: OneOfAppnavControllerGroupGroupNameOptionsDef
        # List of controllers
        appnav_controllers: Optional[List[AppqoeAppnavControllers]]


    class OneOfDefaultServiceNodeGroupNameOptionsDef:
        option_type: DefaultOptionTypeDef
        value: DefaultServiceNodeGroupDef  # pytype: disable=annotation-type-mismatch


    class OneOfDefaultTrueServiceNodeGroupInternalOptionsDef:
        option_type: DefaultOptionTypeDef
        value: BooleanTrueDef  # pytype: disable=annotation-type-mismatch


    class OneOfDefaultExternalServiceNodeGroupServiceNodeAddressOptionsDef:
        option_type: DefaultOptionTypeDef
        value: DefaultExternalServiceNodeAddressDef  # pytype: disable=annotation-type-mismatch


    class AppqoeServiceNode:
        address: OneOfDefaultExternalServiceNodeGroupServiceNodeAddressOptionsDef


    class AppqoeServiceNodeGroup:
        name: OneOfDefaultServiceNodeGroupNameOptionsDef
        internal: Optional[
            OneOfDefaultTrueServiceNodeGroupInternalOptionsDef
        ]
        # Service Node Information
        service_node: Optional[List[AppqoeServiceNode]]


    class ForwarderAndServiceNode:
        """
        Appqoe Device Role Forwarder And ServiceNode
        """

        # Appnav controller group name
        appnav_controller_group: Optional[
            List[AppqoeAppnavControllerGroup]
        ]
        # Service Context
        service_context: Optional[ServiceContext]
        # Name
        service_node_group: Optional[List[AppqoeServiceNodeGroup]]


    class OneOfServiceNodeGroupExternalNodeOptionsDef:
        option_type: DefaultOptionTypeDef
        value: BooleanTrueDef  # pytype: disable=annotation-type-mismatch


    class OneOfServiceNodeGroupServiceNodeVpgIpOptionsDef:
        option_type: DefaultOptionTypeDef
        value: DefaultExternalServiceNodeVpgIpDef  # pytype: disable=annotation-type-mismatch


    class SdwanServiceAppqoeServiceNode:
        address: OneOfDefaultExternalServiceNodeGroupServiceNodeAddressOptionsDef
        vpg_ip: Optional[OneOfServiceNodeGroupServiceNodeVpgIpOptionsDef]


    class ServiceAppqoeServiceNodeGroup:
        name: OneOfDefaultServiceNodeGroupNameOptionsDef
        external_node: Optional[
            OneOfServiceNodeGroupExternalNodeOptionsDef
        ]
        # Service Node Information
        service_node: Optional[List[SdwanServiceAppqoeServiceNode]]


    class ServiceAppqoeServiceNode:
        """
        Appqoe Device Role ServiceNode
        """

        # Name
        service_node_group: Optional[List[ServiceAppqoeServiceNodeGroup]]


    class AppqoeData:
        appqoe_device_role: OneOfAppqoeDeviceRoleOptionsDef
        dreopt: Optional[
            Union[OneOfDreoptOptionsDef1, OneOfDreoptOptionsDef2]
        ]
        # Appqoe Device Role Forwarder
        forwarder: Optional[Union[Forwarder1, Forwarder2]]
        # Appqoe Device Role Forwarder And ServiceNode
        forwarder_and_service_node: Optional[ForwarderAndServiceNode]
        # Appqoe Device Role ServiceNode
        service_node: Optional[ServiceAppqoeServiceNode]
        # Virtual application Instance
        virtual_application: Optional[List[VirtualApplication]]


    class Payload:
        """
        Appqoe profile feature schema for request
        """

        data: AppqoeData
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


    class Data:
        # User who last created this.
        created_by: Optional[str]
        # Timestamp of creation
        created_on: Optional[int]
        # User who last updated this.
        last_updated_by: Optional[str]
        # Timestamp of last update
        last_updated_on: Optional[int]
        parcel_id: Optional[str]
        parcel_type: Optional[str]
        # Appqoe profile feature schema for request
        payload: Optional[Payload]


    class GetListSdwanServiceAppqoePayload:
        data: Optional[List[Data]]


    class CreateAppqoeProfileParcelForServicePostResponse:
        """
        Profile Parcel POST Response schema
        """

        parcel_id: str
        metadata: Optional[Any]


    class V1FeatureProfileSdwanServiceAppqoeServiceNode:
        address: OneOfDefaultExternalServiceNodeGroupServiceNodeAddressOptionsDef
        vpg_ip: Optional[OneOfServiceNodeGroupServiceNodeVpgIpOptionsDef]


    class SdwanServiceAppqoeServiceNodeGroup:
        name: OneOfDefaultServiceNodeGroupNameOptionsDef
        external_node: Optional[
            OneOfServiceNodeGroupExternalNodeOptionsDef
        ]
        # Service Node Information
        service_node: Optional[
            List[V1FeatureProfileSdwanServiceAppqoeServiceNode]
        ]


    class FeatureProfileSdwanServiceAppqoeServiceNode:
        """
        Appqoe Device Role ServiceNode
        """

        # Name
        service_node_group: Optional[
            List[SdwanServiceAppqoeServiceNodeGroup]
        ]


    class ServiceAppqoeData:
        appqoe_device_role: OneOfAppqoeDeviceRoleOptionsDef
        dreopt: Optional[
            Union[OneOfDreoptOptionsDef1, OneOfDreoptOptionsDef2]
        ]
        # Appqoe Device Role Forwarder
        forwarder: Optional[Union[Forwarder1, Forwarder2]]
        # Appqoe Device Role Forwarder And ServiceNode
        forwarder_and_service_node: Optional[ForwarderAndServiceNode]
        # Appqoe Device Role ServiceNode
        service_node: Optional[
            FeatureProfileSdwanServiceAppqoeServiceNode
        ]
        # Virtual application Instance
        virtual_application: Optional[List[VirtualApplication]]


    class CreateAppqoeProfileParcelForServicePostRequest:
        """
        Appqoe profile feature schema for request
        """

        data: ServiceAppqoeData
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


    class GetSingleSdwanServiceAppqoePayload:
        # User who last created this.
        created_by: Optional[str]
        # Timestamp of creation
        created_on: Optional[int]
        # User who last updated this.
        last_updated_by: Optional[str]
        # Timestamp of last update
        last_updated_on: Optional[int]
        parcel_id: Optional[str]
        parcel_type: Optional[str]
        # Appqoe profile feature schema for request
        payload: Optional[Payload]


    class EditAppqoeProfileParcelForServicePutResponse:
        """
        Profile Parcel PUT Response schema
        """

        id: str
        metadata: Optional[Any]


    class ServiceNode2:
        address: OneOfDefaultExternalServiceNodeGroupServiceNodeAddressOptionsDef
        vpg_ip: Optional[OneOfServiceNodeGroupServiceNodeVpgIpOptionsDef]


    class FeatureProfileSdwanServiceAppqoeServiceNodeGroup:
        name: OneOfDefaultServiceNodeGroupNameOptionsDef
        external_node: Optional[
            OneOfServiceNodeGroupExternalNodeOptionsDef
        ]
        # Service Node Information
        service_node: Optional[List[ServiceNode2]]


    class ServiceNode1:
        """
        Appqoe Device Role ServiceNode
        """

        # Name
        service_node_group: Optional[
            List[FeatureProfileSdwanServiceAppqoeServiceNodeGroup]
        ]


    class SdwanServiceAppqoeData:
        appqoe_device_role: OneOfAppqoeDeviceRoleOptionsDef
        dreopt: Optional[
            Union[OneOfDreoptOptionsDef1, OneOfDreoptOptionsDef2]
        ]
        # Appqoe Device Role Forwarder
        forwarder: Optional[Union[Forwarder1, Forwarder2]]
        # Appqoe Device Role Forwarder And ServiceNode
        forwarder_and_service_node: Optional[ForwarderAndServiceNode]
        # Appqoe Device Role ServiceNode
        service_node: Optional[ServiceNode1]
        # Virtual application Instance
        virtual_application: Optional[List[VirtualApplication]]


    class EditAppqoeProfileParcelForServicePutRequest:
        """
        Appqoe profile feature schema for request
        """

        data: SdwanServiceAppqoeData
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


