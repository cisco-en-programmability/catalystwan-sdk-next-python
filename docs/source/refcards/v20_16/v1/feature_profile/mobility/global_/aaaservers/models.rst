======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    GlobalOptionTypeDef = Literal["global"]


    class OneOfRadiusServerNameOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfRadiusServerIpAddressOptionsDef:
        option_type: GlobalOptionTypeDef
        value: Any


    class OneOfRadiusServerPortOptionsDef:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfRadiusServerSecretOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class RadiusServers:
        ip_address: OneOfRadiusServerIpAddressOptionsDef
        name: OneOfRadiusServerNameOptionsDef
        port: OneOfRadiusServerPortOptionsDef
        secret: OneOfRadiusServerSecretOptionsDef


    class AaaserversData:
        # Radius Server Configuration
        radius_servers: List[RadiusServers]


    class Payload:
        """
        AON AAA Servers profile parcel schema for POST request
        """

        data: AaaserversData
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
        # AON AAA Servers profile parcel schema for POST request
        payload: Optional[Payload]


    class GetListMobilityGlobalAaaserversPayload:
        data: Optional[List[Data]]


    class CreateAaaServersProfileParcelForMobilityPostResponse:
        """
        Profile Parcel POST Response schema
        """

        parcel_id: str
        metadata: Optional[Any]


    class GlobalAaaserversData:
        # Radius Server Configuration
        radius_servers: List[RadiusServers]


    class CreateAaaServersProfileParcelForMobilityPostRequest:
        """
        AON AAA Servers profile parcel schema for POST request
        """

        data: GlobalAaaserversData
        name: str
        # Set the parcel description
        description: Optional[str]
        metadata: Optional[Any]


    class AaaserversOneOfRadiusServerNameOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class AaaserversOneOfRadiusServerPortOptionsDef:
        option_type: GlobalOptionTypeDef
        value: int


    class AaaserversOneOfRadiusServerSecretOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class AaaserversRadiusServers:
        ip_address: OneOfRadiusServerIpAddressOptionsDef
        name: AaaserversOneOfRadiusServerNameOptionsDef
        port: AaaserversOneOfRadiusServerPortOptionsDef
        secret: AaaserversOneOfRadiusServerSecretOptionsDef


    class MobilityGlobalAaaserversData:
        # Radius Server Configuration
        radius_servers: List[AaaserversRadiusServers]


    class AaaserversPayload:
        """
        AON AAA Servers profile parcel schema for PUT request
        """

        data: MobilityGlobalAaaserversData
        name: str
        # Set the parcel description
        description: Optional[str]
        metadata: Optional[Any]


    class GetSingleMobilityGlobalAaaserversPayload:
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
        # AON AAA Servers profile parcel schema for PUT request
        payload: Optional[AaaserversPayload]


    class EditAaaServersProfileParcelForMobilityPutResponse:
        """
        Profile Parcel PUT Response schema
        """

        id: str
        metadata: Optional[Any]


    class GlobalAaaserversOneOfRadiusServerNameOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class GlobalAaaserversOneOfRadiusServerPortOptionsDef:
        option_type: GlobalOptionTypeDef
        value: int


    class GlobalAaaserversOneOfRadiusServerSecretOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class GlobalAaaserversRadiusServers:
        ip_address: OneOfRadiusServerIpAddressOptionsDef
        name: GlobalAaaserversOneOfRadiusServerNameOptionsDef
        port: GlobalAaaserversOneOfRadiusServerPortOptionsDef
        secret: GlobalAaaserversOneOfRadiusServerSecretOptionsDef


    class FeatureProfileMobilityGlobalAaaserversData:
        # Radius Server Configuration
        radius_servers: List[GlobalAaaserversRadiusServers]


    class EditAaaServersProfileParcelForMobilityPutRequest:
        """
        AON AAA Servers profile parcel schema for PUT request
        """

        data: FeatureProfileMobilityGlobalAaaserversData
        name: str
        # Set the parcel description
        description: Optional[str]
        metadata: Optional[Any]


