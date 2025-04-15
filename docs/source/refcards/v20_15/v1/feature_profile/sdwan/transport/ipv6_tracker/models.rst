======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    VariableOptionTypeDef = Literal["variable"]

    GlobalOptionTypeDef = Literal["global"]

    DefaultOptionTypeDef = Literal["default"]

    EndpointTrackerTypeDef = Literal[
        "ipv6-interface", "ipv6-interface-icmp"
    ]

    DefaultEndpointTrackerTypeDef = Literal["ipv6-interface"]

    TrackerTypeDef = Literal["endpoint"]

    DefaultTrackerTypeDef = Literal["endpoint"]

    Ipv6TrackerEndpointTrackerTypeDef = Literal[
        "ipv6-interface", "ipv6-interface-icmp"
    ]

    Ipv6TrackerDefaultEndpointTrackerTypeDef = Literal["ipv6-interface"]

    Ipv6TrackerTrackerTypeDef = Literal["endpoint"]

    Ipv6TrackerDefaultTrackerTypeDef = Literal["endpoint"]

    TransportIpv6TrackerEndpointTrackerTypeDef = Literal[
        "ipv6-interface", "ipv6-interface-icmp"
    ]

    TransportIpv6TrackerDefaultEndpointTrackerTypeDef = Literal[
        "ipv6-interface"
    ]

    TransportIpv6TrackerTrackerTypeDef = Literal["endpoint"]

    TransportIpv6TrackerDefaultTrackerTypeDef = Literal["endpoint"]


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


    class Ipv6TrackerData:
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
        IPv6 Tracker profile parcel schema for POST request
        """

        data: Ipv6TrackerData
        name: str
        # Set the parcel description
        description: Optional[str]
        metadata: Optional[Any]


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
        # IPv6 Tracker profile parcel schema for POST request
        payload: Optional[Payload]


    class GetListSdwanTransportIpv6TrackerPayload:
        data: Optional[List[Data]]


    class CreateIpv6TrackerProfileParcelForTransportPostResponse:
        """
        Profile Parcel POST Response schema
        """

        parcel_id: str
        metadata: Optional[Any]


    class TransportIpv6TrackerData:
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


    class CreateIpv6TrackerProfileParcelForTransportPostRequest:
        """
        IPv6 Tracker profile parcel schema for POST request
        """

        data: TransportIpv6TrackerData
        name: str
        # Set the parcel description
        description: Optional[str]
        metadata: Optional[Any]


    class Ipv6TrackerOneOfTrackerNameOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class Ipv6TrackerOneOfEndpointApiUrlOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class Ipv6TrackerOneOfEndpointDnsNameOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class Ipv6TrackerOneOfEndpointIpOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class Ipv6TrackerOneOfIntervalOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class Ipv6TrackerOneOfIntervalOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class Ipv6TrackerOneOfIcmpIntervalOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class Ipv6TrackerOneOfIcmpIntervalOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class Ipv6TrackerOneOfMultiplierOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class Ipv6TrackerOneOfMultiplierOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class Ipv6TrackerOneOfThresholdOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class Ipv6TrackerOneOfThresholdOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class Ipv6TrackerOneOfEndpointTrackerTypeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: Ipv6TrackerEndpointTrackerTypeDef


    class Ipv6TrackerOneOfEndpointTrackerTypeOptionsDef2:
        option_type: DefaultOptionTypeDef
        value: Ipv6TrackerDefaultEndpointTrackerTypeDef  # pytype: disable=annotation-type-mismatch


    class Ipv6TrackerOneOfTrackerTypeOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: Ipv6TrackerTrackerTypeDef


    class Ipv6TrackerOneOfTrackerTypeOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: Ipv6TrackerDefaultTrackerTypeDef  # pytype: disable=annotation-type-mismatch


    class SdwanTransportIpv6TrackerData:
        endpoint_api_url: Optional[
            Union[
                OneOfEndpointApiUrlOptionsDef1,
                Ipv6TrackerOneOfEndpointApiUrlOptionsDef2,
            ]
        ]
        endpoint_dns_name: Optional[
            Union[
                OneOfEndpointDnsNameOptionsDef1,
                Ipv6TrackerOneOfEndpointDnsNameOptionsDef2,
            ]
        ]
        endpoint_ip: Optional[
            Union[
                OneOfEndpointIpOptionsDef1,
                Ipv6TrackerOneOfEndpointIpOptionsDef2,
            ]
        ]
        endpoint_tracker_type: Optional[
            Union[
                Ipv6TrackerOneOfEndpointTrackerTypeOptionsDef1,
                Ipv6TrackerOneOfEndpointTrackerTypeOptionsDef2,
            ]
        ]
        icmp_interval: Optional[
            Union[
                OneOfIcmpIntervalOptionsDef1,
                Ipv6TrackerOneOfIcmpIntervalOptionsDef2,
                Ipv6TrackerOneOfIcmpIntervalOptionsDef3,
            ]
        ]
        interval: Optional[
            Union[
                OneOfIntervalOptionsDef1,
                Ipv6TrackerOneOfIntervalOptionsDef2,
                Ipv6TrackerOneOfIntervalOptionsDef3,
            ]
        ]
        multiplier: Optional[
            Union[
                OneOfMultiplierOptionsDef1,
                Ipv6TrackerOneOfMultiplierOptionsDef2,
                Ipv6TrackerOneOfMultiplierOptionsDef3,
            ]
        ]
        threshold: Optional[
            Union[
                OneOfThresholdOptionsDef1,
                Ipv6TrackerOneOfThresholdOptionsDef2,
                Ipv6TrackerOneOfThresholdOptionsDef3,
            ]
        ]
        tracker_name: Optional[
            Union[
                OneOfTrackerNameOptionsDef1,
                Ipv6TrackerOneOfTrackerNameOptionsDef2,
            ]
        ]
        tracker_type: Optional[
            Union[
                OneOfTrackerTypeOptionsDef1,
                Ipv6TrackerOneOfTrackerTypeOptionsDef2,
                Ipv6TrackerOneOfTrackerTypeOptionsDef3,
            ]
        ]


    class Ipv6TrackerPayload:
        """
        IPv6 Tracker profile parcel schema for PUT request
        """

        data: SdwanTransportIpv6TrackerData
        name: str
        # Set the parcel description
        description: Optional[str]
        metadata: Optional[Any]


    class GetSingleSdwanTransportIpv6TrackerPayload:
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
        # IPv6 Tracker profile parcel schema for PUT request
        payload: Optional[Ipv6TrackerPayload]


    class EditIpv6TrackerProfileParcelForTransportPutResponse:
        """
        Profile Parcel PUT Response schema
        """

        id: str
        metadata: Optional[Any]


    class TransportIpv6TrackerOneOfTrackerNameOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class TransportIpv6TrackerOneOfEndpointApiUrlOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class TransportIpv6TrackerOneOfEndpointDnsNameOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class TransportIpv6TrackerOneOfEndpointIpOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class TransportIpv6TrackerOneOfIntervalOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class TransportIpv6TrackerOneOfIntervalOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class TransportIpv6TrackerOneOfIcmpIntervalOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class TransportIpv6TrackerOneOfIcmpIntervalOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class TransportIpv6TrackerOneOfMultiplierOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class TransportIpv6TrackerOneOfMultiplierOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class TransportIpv6TrackerOneOfThresholdOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class TransportIpv6TrackerOneOfThresholdOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class TransportIpv6TrackerOneOfEndpointTrackerTypeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: TransportIpv6TrackerEndpointTrackerTypeDef


    class TransportIpv6TrackerOneOfEndpointTrackerTypeOptionsDef2:
        option_type: DefaultOptionTypeDef
        value: TransportIpv6TrackerDefaultEndpointTrackerTypeDef  # pytype: disable=annotation-type-mismatch


    class TransportIpv6TrackerOneOfTrackerTypeOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: TransportIpv6TrackerTrackerTypeDef


    class TransportIpv6TrackerOneOfTrackerTypeOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: TransportIpv6TrackerDefaultTrackerTypeDef  # pytype: disable=annotation-type-mismatch


    class FeatureProfileSdwanTransportIpv6TrackerData:
        endpoint_api_url: Optional[
            Union[
                OneOfEndpointApiUrlOptionsDef1,
                TransportIpv6TrackerOneOfEndpointApiUrlOptionsDef2,
            ]
        ]
        endpoint_dns_name: Optional[
            Union[
                OneOfEndpointDnsNameOptionsDef1,
                TransportIpv6TrackerOneOfEndpointDnsNameOptionsDef2,
            ]
        ]
        endpoint_ip: Optional[
            Union[
                OneOfEndpointIpOptionsDef1,
                TransportIpv6TrackerOneOfEndpointIpOptionsDef2,
            ]
        ]
        endpoint_tracker_type: Optional[
            Union[
                TransportIpv6TrackerOneOfEndpointTrackerTypeOptionsDef1,
                TransportIpv6TrackerOneOfEndpointTrackerTypeOptionsDef2,
            ]
        ]
        icmp_interval: Optional[
            Union[
                OneOfIcmpIntervalOptionsDef1,
                TransportIpv6TrackerOneOfIcmpIntervalOptionsDef2,
                TransportIpv6TrackerOneOfIcmpIntervalOptionsDef3,
            ]
        ]
        interval: Optional[
            Union[
                OneOfIntervalOptionsDef1,
                TransportIpv6TrackerOneOfIntervalOptionsDef2,
                TransportIpv6TrackerOneOfIntervalOptionsDef3,
            ]
        ]
        multiplier: Optional[
            Union[
                OneOfMultiplierOptionsDef1,
                TransportIpv6TrackerOneOfMultiplierOptionsDef2,
                TransportIpv6TrackerOneOfMultiplierOptionsDef3,
            ]
        ]
        threshold: Optional[
            Union[
                OneOfThresholdOptionsDef1,
                TransportIpv6TrackerOneOfThresholdOptionsDef2,
                TransportIpv6TrackerOneOfThresholdOptionsDef3,
            ]
        ]
        tracker_name: Optional[
            Union[
                OneOfTrackerNameOptionsDef1,
                TransportIpv6TrackerOneOfTrackerNameOptionsDef2,
            ]
        ]
        tracker_type: Optional[
            Union[
                OneOfTrackerTypeOptionsDef1,
                TransportIpv6TrackerOneOfTrackerTypeOptionsDef2,
                TransportIpv6TrackerOneOfTrackerTypeOptionsDef3,
            ]
        ]


    class EditIpv6TrackerProfileParcelForTransportPutRequest:
        """
        IPv6 Tracker profile parcel schema for PUT request
        """

        data: FeatureProfileSdwanTransportIpv6TrackerData
        name: str
        # Set the parcel description
        description: Optional[str]
        metadata: Optional[Any]


