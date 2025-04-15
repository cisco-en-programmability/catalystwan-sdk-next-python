======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    GlobalOptionTypeDef = Literal["global"]

    PortConfigModeDef = Literal[
        "12 ports of 1/10GE + 1 port of 100GE",
        "12 ports of 1/10GE + 3 ports 40GE",
        "2 ports of 100 GE",
        "3 ports of 40GE + 1port of 100GE",
        "8 ports of 1/10GE + 1 port of 40GE + 1 port of 100GE",
        "8 ports of 1/10GE + 4 ports of 40GE",
    ]

    VariableOptionTypeDef = Literal["variable"]

    DefaultOptionTypeDef = Literal["default"]

    DefaultPortConfigModeDef = Literal[
        "12 ports of 1/10GE + 3 ports 40GE"
    ]


    class OneOfPortOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: PortConfigModeDef


    class OneOfPortOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfPortOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: DefaultPortConfigModeDef  # pytype: disable=annotation-type-mismatch


    class FlexiblePortSpeedData:
        port_type: Optional[
            Union[
                OneOfPortOptionsDef1,
                OneOfPortOptionsDef2,
                OneOfPortOptionsDef3,
            ]
        ]


    class Payload:
        """
        Flexible Port Speed profile feature schema for request
        """

        data: FlexiblePortSpeedData
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
        # Flexible Port Speed profile feature schema for request
        payload: Optional[Payload]


    class GetListSdRoutingSystemFlexiblePortSpeedPayload:
        data: Optional[List[Data]]


    class CreateSdroutingFlexiblePortSpeedFeaturePostResponse:
        """
        Profile Parcel POST Response schema
        """

        parcel_id: str
        metadata: Optional[Any]


    class SystemFlexiblePortSpeedData:
        port_type: Optional[
            Union[
                OneOfPortOptionsDef1,
                OneOfPortOptionsDef2,
                OneOfPortOptionsDef3,
            ]
        ]


    class CreateSdroutingFlexiblePortSpeedFeaturePostRequest:
        """
        Flexible Port Speed profile feature schema for request
        """

        data: SystemFlexiblePortSpeedData
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


    class GetSingleSdRoutingSystemFlexiblePortSpeedPayload:
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
        # Flexible Port Speed profile feature schema for request
        payload: Optional[Payload]


    class EditSdroutingFlexiblePortSpeedFeaturePutResponse:
        """
        Profile Parcel PUT Response schema
        """

        id: str
        metadata: Optional[Any]


    class SdRoutingSystemFlexiblePortSpeedData:
        port_type: Optional[
            Union[
                OneOfPortOptionsDef1,
                OneOfPortOptionsDef2,
                OneOfPortOptionsDef3,
            ]
        ]


    class EditSdroutingFlexiblePortSpeedFeaturePutRequest:
        """
        Flexible Port Speed profile feature schema for request
        """

        data: SdRoutingSystemFlexiblePortSpeedData
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


