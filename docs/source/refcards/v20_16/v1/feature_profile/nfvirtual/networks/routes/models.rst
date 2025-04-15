======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    GlobalOptionTypeDef = Literal["global"]

    VariableOptionTypeDef = Literal["variable"]


    class CreateNfvirtualRoutesParcelPostResponse:
        """
        Profile Parcel POST Response schema
        """

        parcel_id: str
        metadata: Optional[Any]


    class OneOfRoutesNetworkAddressOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfRoutesNetworkAddressOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfRoutesNexthopAddressOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: Any


    class OneOfRoutesNexthopAddressOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class Routes:
        network_address: Optional[
            Union[
                OneOfRoutesNetworkAddressOptionsDef1,
                OneOfRoutesNetworkAddressOptionsDef2,
            ]
        ]
        nexthop_address: Optional[
            Union[
                OneOfRoutesNexthopAddressOptionsDef1,
                OneOfRoutesNexthopAddressOptionsDef2,
            ]
        ]


    class Data:
        # List of Routes
        routes: Optional[List[Routes]]


    class CreateNfvirtualRoutesParcelPostRequest:
        """
        Routes profile parcel schema for POST request
        """

        data: Data
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


    class RoutesOneOfRoutesNetworkAddressOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class RoutesOneOfRoutesNexthopAddressOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: Any


    class RoutesRoutes:
        network_address: Optional[
            Union[
                RoutesOneOfRoutesNetworkAddressOptionsDef1,
                OneOfRoutesNetworkAddressOptionsDef2,
            ]
        ]
        nexthop_address: Optional[
            Union[
                RoutesOneOfRoutesNexthopAddressOptionsDef1,
                OneOfRoutesNexthopAddressOptionsDef2,
            ]
        ]


    class RoutesData:
        # List of Routes
        routes: Optional[List[RoutesRoutes]]


    class Payload:
        """
        Routes profile parcel schema for PUT request
        """

        data: RoutesData
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


    class GetSingleNfvirtualNetworksRoutesPayload:
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
        # Routes profile parcel schema for PUT request
        payload: Optional[Payload]


    class EditNfvirtualRoutesParcelPutResponse:
        """
        Profile Parcel PUT Response schema
        """

        id: str
        metadata: Optional[Any]


    class NetworksRoutesOneOfRoutesNetworkAddressOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class NetworksRoutesOneOfRoutesNexthopAddressOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: Any


    class NetworksRoutesRoutes:
        network_address: Optional[
            Union[
                NetworksRoutesOneOfRoutesNetworkAddressOptionsDef1,
                OneOfRoutesNetworkAddressOptionsDef2,
            ]
        ]
        nexthop_address: Optional[
            Union[
                NetworksRoutesOneOfRoutesNexthopAddressOptionsDef1,
                OneOfRoutesNexthopAddressOptionsDef2,
            ]
        ]


    class NetworksRoutesData:
        # List of Routes
        routes: Optional[List[NetworksRoutesRoutes]]


    class EditNfvirtualRoutesParcelPutRequest:
        """
        Routes profile parcel schema for PUT request
        """

        data: NetworksRoutesData
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


