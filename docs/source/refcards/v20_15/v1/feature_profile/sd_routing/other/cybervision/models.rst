======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    GlobalOptionTypeDef = Literal["global"]

    DefaultOptionTypeDef = Literal["default"]

    Ipv4SubnetMaskDef = Literal[
        "0.0.0.0",
        "128.0.0.0",
        "192.0.0.0",
        "224.0.0.0",
        "240.0.0.0",
        "248.0.0.0",
        "252.0.0.0",
        "254.0.0.0",
        "255.0.0.0",
        "255.128.0.0",
        "255.192.0.0",
        "255.224.0.0",
        "255.240.0.0",
        "255.252.0.0",
        "255.254.0.0",
        "255.255.0.0",
        "255.255.128.0",
        "255.255.192.0",
        "255.255.224.0",
        "255.255.240.0",
        "255.255.248.0",
        "255.255.252.0",
        "255.255.254.0",
        "255.255.255.0",
        "255.255.255.128",
        "255.255.255.192",
        "255.255.255.224",
        "255.255.255.240",
        "255.255.255.248",
        "255.255.255.252",
        "255.255.255.254",
        "255.255.255.255",
    ]


    class OneOfVirtualApplicationcaptureInterfaceIpDef1:
        option_type: GlobalOptionTypeDef
        value: Any


    class OneOfVirtualApplicationcaptureInterfaceIpDef2:
        option_type: DefaultOptionTypeDef


    class OneOfVirtualApplicationIngressIfSubnetMaskDef1:
        option_type: GlobalOptionTypeDef
        value: (
            Ipv4SubnetMaskDef  # pytype: disable=annotation-type-mismatch
        )


    class OneOfVirtualApplicationIngressIfSubnetMaskDef2:
        option_type: DefaultOptionTypeDef


    class OneOfVirtualApplicationcollectionInterfaceIpDef1:
        option_type: GlobalOptionTypeDef
        value: Any


    class OneOfVirtualApplicationcollectionInterfaceIpDef2:
        option_type: DefaultOptionTypeDef


    class OneOfVirtualApplicationcollectionInterfaceSubnetMask1:
        option_type: GlobalOptionTypeDef
        value: (
            Ipv4SubnetMaskDef  # pytype: disable=annotation-type-mismatch
        )


    class OneOfVirtualApplicationcollectionInterfaceSubnetMask2:
        option_type: DefaultOptionTypeDef


    class MultipleErspanSourceInterfaces:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfVirtualApplicationvirtualPortGroup5IpDef1:
        option_type: GlobalOptionTypeDef
        value: Any


    class OneOfVirtualApplicationvirtualPortGroup5IpDef2:
        option_type: DefaultOptionTypeDef


    class OneOfVirtualApplicationvirtualPortGroup6IpDef1:
        option_type: GlobalOptionTypeDef
        value: Any


    class OneOfVirtualApplicationvirtualPortGroup6IpDef2:
        option_type: DefaultOptionTypeDef


    class OneOfVirtualApplicationerspanSourceInterfaceDef:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfcvcId:
        option_type: GlobalOptionTypeDef
        value: str


    class VirtualApplication:
        """
        Virtual application Instance
        """

        capture_interface_ip: Union[
            OneOfVirtualApplicationcaptureInterfaceIpDef1,
            OneOfVirtualApplicationcaptureInterfaceIpDef2,
        ]
        capture_interface_subnet_mask: Union[
            OneOfVirtualApplicationIngressIfSubnetMaskDef1,
            OneOfVirtualApplicationIngressIfSubnetMaskDef2,
        ]
        collection_interface_ip: Union[
            OneOfVirtualApplicationcollectionInterfaceIpDef1,
            OneOfVirtualApplicationcollectionInterfaceIpDef2,
        ]
        collection_interface_subnet_mask: Union[
            OneOfVirtualApplicationcollectionInterfaceSubnetMask1,
            OneOfVirtualApplicationcollectionInterfaceSubnetMask2,
        ]
        cvc_id: OneOfcvcId
        multiple_erspan_source_interfaces: List[
            MultipleErspanSourceInterfaces
        ]
        sensor_to_cvc_interface: (
            OneOfVirtualApplicationerspanSourceInterfaceDef
        )
        virtual_port_group5_ip: Union[
            OneOfVirtualApplicationvirtualPortGroup5IpDef1,
            OneOfVirtualApplicationvirtualPortGroup5IpDef2,
        ]
        virtual_port_group6_ip: Union[
            OneOfVirtualApplicationvirtualPortGroup6IpDef1,
            OneOfVirtualApplicationvirtualPortGroup6IpDef2,
        ]


    class CybervisionData:
        # Virtual application Instance
        virtual_application: VirtualApplication


    class Payload:
        """
        cybervision profile feature schema for POST/PUT request
        """

        data: CybervisionData
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
        # cybervision profile feature schema for POST/PUT request
        payload: Optional[Payload]


    class GetListSdRoutingOtherCybervisionPayload:
        data: Optional[List[Data]]


    class CreateCybervisionProfileFeatureForOtherPostResponse:
        """
        Profile Parcel POST Response schema
        """

        parcel_id: str
        metadata: Optional[Any]


    class OtherCybervisionData:
        # Virtual application Instance
        virtual_application: VirtualApplication


    class CreateCybervisionProfileFeatureForOtherPostRequest:
        """
        cybervision profile feature schema for POST/PUT request
        """

        data: OtherCybervisionData
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


    class GetSingleSdRoutingOtherCybervisionPayload:
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
        # cybervision profile feature schema for POST/PUT request
        payload: Optional[Payload]


    class EditCybervisionProfileFeatureForOtherPutResponse:
        """
        Profile Parcel PUT Response schema
        """

        id: str
        metadata: Optional[Any]


    class SdRoutingOtherCybervisionData:
        # Virtual application Instance
        virtual_application: VirtualApplication


    class EditCybervisionProfileFeatureForOtherPutRequest:
        """
        cybervision profile feature schema for POST/PUT request
        """

        data: SdRoutingOtherCybervisionData
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


