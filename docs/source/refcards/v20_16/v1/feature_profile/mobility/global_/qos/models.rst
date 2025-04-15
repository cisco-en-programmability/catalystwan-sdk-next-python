======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    VariableOptionTypeDef = Literal["variable"]

    GlobalOptionTypeDef = Literal["global"]

    DefaultOptionTypeDef = Literal["default"]


    class OneOfOnBooleanDefaultFalseOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfOnBooleanDefaultFalseOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfOnBooleanDefaultFalseOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: bool


    class OneOfGigInterfaceRateDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfGigInterfaceRateDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfGigInterfaceRateDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class GigabitEthernet00QosConfig:
        """
        GigabitEthernet0/0 IEEE 802.3z interface QOS configuration
        """

        rate: Union[
            OneOfGigInterfaceRateDef1,
            OneOfGigInterfaceRateDef2,
            OneOfGigInterfaceRateDef3,
        ]


    class OneOfCellularInterfaceRateDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfCellularInterfaceRateDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfCellularInterfaceRateDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class Cellular1QosConfig:
        """
        Cellular1 interface QOS configuration
        """

        rate: Union[
            OneOfCellularInterfaceRateDef1,
            OneOfCellularInterfaceRateDef2,
            OneOfCellularInterfaceRateDef3,
        ]


    class QosData:
        # Cellular1 interface QOS configuration
        cellular1_qos_config: Cellular1QosConfig
        enable_qos: Union[
            OneOfOnBooleanDefaultFalseOptionsDef1,
            OneOfOnBooleanDefaultFalseOptionsDef2,
            OneOfOnBooleanDefaultFalseOptionsDef3,
        ]
        # GigabitEthernet0/0 IEEE 802.3z interface QOS configuration
        gigabit_ethernet00_qos_config: GigabitEthernet00QosConfig


    class Payload:
        """
        AON QOS profile parcel schema for post and put requests
        """

        data: QosData
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
        # AON QOS profile parcel schema for post and put requests
        payload: Optional[Payload]


    class GetListMobilityGlobalQosPayload:
        data: Optional[List[Data]]


    class CreateQosFeatureForGlobalPostResponse:
        """
        Profile Parcel POST Response schema
        """

        parcel_id: str
        metadata: Optional[Any]


    class GlobalQosData:
        # Cellular1 interface QOS configuration
        cellular1_qos_config: Cellular1QosConfig
        enable_qos: Union[
            OneOfOnBooleanDefaultFalseOptionsDef1,
            OneOfOnBooleanDefaultFalseOptionsDef2,
            OneOfOnBooleanDefaultFalseOptionsDef3,
        ]
        # GigabitEthernet0/0 IEEE 802.3z interface QOS configuration
        gigabit_ethernet00_qos_config: GigabitEthernet00QosConfig


    class CreateQosFeatureForGlobalPostRequest:
        """
        AON QOS profile parcel schema for post and put requests
        """

        data: GlobalQosData
        name: str
        # Set the parcel description
        description: Optional[str]
        metadata: Optional[Any]


    class GetSingleMobilityGlobalQosPayload:
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
        # AON QOS profile parcel schema for post and put requests
        payload: Optional[Payload]


    class EditQosFeatureForGlobalPutResponse:
        """
        Profile Parcel PUT Response schema
        """

        id: str
        metadata: Optional[Any]


    class MobilityGlobalQosData:
        # Cellular1 interface QOS configuration
        cellular1_qos_config: Cellular1QosConfig
        enable_qos: Union[
            OneOfOnBooleanDefaultFalseOptionsDef1,
            OneOfOnBooleanDefaultFalseOptionsDef2,
            OneOfOnBooleanDefaultFalseOptionsDef3,
        ]
        # GigabitEthernet0/0 IEEE 802.3z interface QOS configuration
        gigabit_ethernet00_qos_config: GigabitEthernet00QosConfig


    class EditQosFeatureForGlobalPutRequest:
        """
        AON QOS profile parcel schema for post and put requests
        """

        data: MobilityGlobalQosData
        name: str
        # Set the parcel description
        description: Optional[str]
        metadata: Optional[Any]


