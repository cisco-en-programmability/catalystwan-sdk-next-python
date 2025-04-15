======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    VariableOptionTypeDef = Literal["variable"]

    GlobalOptionTypeDef = Literal["global"]

    DefaultOptionTypeDef = Literal["default"]

    EndpointTrackerTypeDef = Literal["interface", "interface-icmp"]

    DefaultEndpointTrackerTypeDef = Literal["interface"]

    TrackerTypeDef = Literal["endpoint", "object"]

    DefaultTrackerTypeDef = Literal["endpoint"]


    class OneOfTrackerNameOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfTrackerNameOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfEndpointApiUrlOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfEndpointApiUrlOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfEndpointDnsNameOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfEndpointDnsNameOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfEndpointIpOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfEndpointIpOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfIntervalOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfIntervalOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfIntervalOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class OneOfIcmpIntervalOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfIcmpIntervalOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfIcmpIntervalOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class OneOfMultiplierOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfMultiplierOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfMultiplierOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class OneOfThresholdOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfThresholdOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfThresholdOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class OneOfEndpointTrackerTypeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: EndpointTrackerTypeDef


    class OneOfEndpointTrackerTypeOptionsDef2:
        option_type: DefaultOptionTypeDef
        value: DefaultEndpointTrackerTypeDef  # pytype: disable=annotation-type-mismatch


    class OneOfTrackerTypeOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfTrackerTypeOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: TrackerTypeDef


    class OneOfTrackerTypeOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: DefaultTrackerTypeDef  # pytype: disable=annotation-type-mismatch


    class Data:
        endpoint_api_url: Optional[
            Union[
                OneOfEndpointApiUrlOptionsDef1,
                OneOfEndpointApiUrlOptionsDef2,
            ]
        ]
        endpoint_dns_name: Optional[
            Union[
                OneOfEndpointDnsNameOptionsDef1,
                OneOfEndpointDnsNameOptionsDef2,
            ]
        ]
        endpoint_ip: Optional[
            Union[OneOfEndpointIpOptionsDef1, OneOfEndpointIpOptionsDef2]
        ]
        endpoint_tracker_type: Optional[
            Union[
                OneOfEndpointTrackerTypeOptionsDef1,
                OneOfEndpointTrackerTypeOptionsDef2,
            ]
        ]
        icmp_interval: Optional[
            Union[
                OneOfIcmpIntervalOptionsDef1,
                OneOfIcmpIntervalOptionsDef2,
                OneOfIcmpIntervalOptionsDef3,
            ]
        ]
        interval: Optional[
            Union[
                OneOfIntervalOptionsDef1,
                OneOfIntervalOptionsDef2,
                OneOfIntervalOptionsDef3,
            ]
        ]
        multiplier: Optional[
            Union[
                OneOfMultiplierOptionsDef1,
                OneOfMultiplierOptionsDef2,
                OneOfMultiplierOptionsDef3,
            ]
        ]
        threshold: Optional[
            Union[
                OneOfThresholdOptionsDef1,
                OneOfThresholdOptionsDef2,
                OneOfThresholdOptionsDef3,
            ]
        ]
        tracker_name: Optional[
            Union[
                OneOfTrackerNameOptionsDef1, OneOfTrackerNameOptionsDef2
            ]
        ]
        tracker_type: Optional[
            Union[
                OneOfTrackerTypeOptionsDef1,
                OneOfTrackerTypeOptionsDef2,
                OneOfTrackerTypeOptionsDef3,
            ]
        ]


    class Payload:
        """
        Tracker profile parcel schema for common request
        """

        data: Data
        name: str
        # Set the parcel description
        description: Optional[str]
        metadata: Optional[Any]


    class GetWanVpnInterfaceIpsecAssociatedTrackerParcelsForTransportGetResponse:
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
        # Tracker profile parcel schema for common request
        payload: Optional[Payload]


    class GetSingleSdwanTransportWanVpnInterfaceIpsecTrackerPayload:
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
        # Tracker profile parcel schema for common request
        payload: Optional[Payload]


    class EditWanVpnInterfaceIpsecAndTrackerParcelAssociationForTransportPutResponse:
        """
        Profile Parcel PUT Response schema
        """

        id: str
        metadata: Optional[Any]


    class EditWanVpnInterfaceIpsecAndTrackerParcelAssociationForTransportPutRequest:
        """
        Profile Parcel POST Request schema
        """

        parcel_id: str
        metadata: Optional[Any]


    class CreateWanVpnInterfaceIpsecAndTrackerParcelAssociationForTransportPostResponse:
        """
        Profile Parcel POST Response schema
        """

        parcel_id: str
        metadata: Optional[Any]


    class CreateWanVpnInterfaceIpsecAndTrackerParcelAssociationForTransportPostRequest:
        """
        Profile Parcel POST Request schema
        """

        parcel_id: str
        metadata: Optional[Any]


