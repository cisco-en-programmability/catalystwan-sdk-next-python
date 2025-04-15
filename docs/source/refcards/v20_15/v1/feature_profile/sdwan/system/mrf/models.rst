======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    GlobalOptionTypeDef = Literal["global"]

    VariableOptionTypeDef = Literal["variable"]

    DefaultOptionTypeDef = Literal["default"]

    RoleDef = Literal["border-router", "edge-router"]

    EnableMrfMigrationDef = Literal["enabled", "enabled-from-bgp-core"]


    class OneOfSecondaryRegionOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfSecondaryRegionOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfSecondaryRegionOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfRoleOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: RoleDef  # pytype: disable=annotation-type-mismatch


    class OneOfRoleOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfRoleOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfEnableMrfMigrationOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: EnableMrfMigrationDef  # pytype: disable=annotation-type-mismatch


    class OneOfEnableMrfMigrationOptionsDef2:
        option_type: DefaultOptionTypeDef


    class OneOfMigrationBgpCommunityOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfMigrationBgpCommunityOptionsDef2:
        option_type: DefaultOptionTypeDef


    class OneOfEnableManagemantRegionOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfEnableManagemantRegionOptionsDef2:
        option_type: DefaultOptionTypeDef
        value: bool


    class OneOfEnableManagemantRegionOptionsDef3:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfVrfIdOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfVrfIdOptionsDef2:
        option_type: DefaultOptionTypeDef


    class OneOfVrfIdOptionsDef3:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfGatewayPreferenceOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: List[int]


    class OneOfGatewayPreferenceOptionsDef2:
        option_type: DefaultOptionTypeDef


    class OneOfGatewayPreferenceOptionsDef3:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfManagementGatewayOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfManagementGatewayOptionsDef2:
        option_type: DefaultOptionTypeDef
        value: bool


    class OneOfManagementGatewayOptionsDef3:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class ManagementRegion:
        """
        Management Region
        """

        gateway_preference: Optional[
            Union[
                OneOfGatewayPreferenceOptionsDef1,
                OneOfGatewayPreferenceOptionsDef2,
                OneOfGatewayPreferenceOptionsDef3,
            ]
        ]
        management_gateway: Optional[
            Union[
                OneOfManagementGatewayOptionsDef1,
                OneOfManagementGatewayOptionsDef2,
                OneOfManagementGatewayOptionsDef3,
            ]
        ]
        vrf_id: Optional[
            Union[
                OneOfVrfIdOptionsDef1,
                OneOfVrfIdOptionsDef2,
                OneOfVrfIdOptionsDef3,
            ]
        ]


    class MrfData:
        enable_management_region: Optional[
            Union[
                OneOfEnableManagemantRegionOptionsDef1,
                OneOfEnableManagemantRegionOptionsDef2,
                OneOfEnableManagemantRegionOptionsDef3,
            ]
        ]
        enable_mrf_migration: Optional[
            Union[
                OneOfEnableMrfMigrationOptionsDef1,
                OneOfEnableMrfMigrationOptionsDef2,
            ]
        ]
        # Management Region
        management_region: Optional[ManagementRegion]
        migration_bgp_community: Optional[
            Union[
                OneOfMigrationBgpCommunityOptionsDef1,
                OneOfMigrationBgpCommunityOptionsDef2,
            ]
        ]
        role: Optional[
            Union[
                OneOfRoleOptionsDef1,
                OneOfRoleOptionsDef2,
                OneOfRoleOptionsDef3,
            ]
        ]
        secondary_region: Optional[
            Union[
                OneOfSecondaryRegionOptionsDef1,
                OneOfSecondaryRegionOptionsDef2,
                OneOfSecondaryRegionOptionsDef3,
            ]
        ]


    class Payload:
        """
        mrf profile parcel schema for POST request
        """

        data: MrfData
        name: str
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
        # mrf profile parcel schema for POST request
        payload: Optional[Payload]


    class GetListSdwanSystemMrfPayload:
        data: Optional[List[Data]]


    class CreateMrfProfileParcelForSystemPostResponse:
        """
        Profile Parcel POST Response schema
        """

        parcel_id: str
        metadata: Optional[Any]


    class SystemMrfData:
        enable_management_region: Optional[
            Union[
                OneOfEnableManagemantRegionOptionsDef1,
                OneOfEnableManagemantRegionOptionsDef2,
                OneOfEnableManagemantRegionOptionsDef3,
            ]
        ]
        enable_mrf_migration: Optional[
            Union[
                OneOfEnableMrfMigrationOptionsDef1,
                OneOfEnableMrfMigrationOptionsDef2,
            ]
        ]
        # Management Region
        management_region: Optional[ManagementRegion]
        migration_bgp_community: Optional[
            Union[
                OneOfMigrationBgpCommunityOptionsDef1,
                OneOfMigrationBgpCommunityOptionsDef2,
            ]
        ]
        role: Optional[
            Union[
                OneOfRoleOptionsDef1,
                OneOfRoleOptionsDef2,
                OneOfRoleOptionsDef3,
            ]
        ]
        secondary_region: Optional[
            Union[
                OneOfSecondaryRegionOptionsDef1,
                OneOfSecondaryRegionOptionsDef2,
                OneOfSecondaryRegionOptionsDef3,
            ]
        ]


    class CreateMrfProfileParcelForSystemPostRequest:
        """
        mrf profile parcel schema for POST request
        """

        data: SystemMrfData
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class GetSingleSdwanSystemMrfPayload:
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
        # mrf profile parcel schema for POST request
        payload: Optional[Payload]


    class EditMrfProfileParcelForSystemPutResponse:
        """
        Profile Parcel PUT Response schema
        """

        id: str
        metadata: Optional[Any]


    class SdwanSystemMrfData:
        enable_management_region: Optional[
            Union[
                OneOfEnableManagemantRegionOptionsDef1,
                OneOfEnableManagemantRegionOptionsDef2,
                OneOfEnableManagemantRegionOptionsDef3,
            ]
        ]
        enable_mrf_migration: Optional[
            Union[
                OneOfEnableMrfMigrationOptionsDef1,
                OneOfEnableMrfMigrationOptionsDef2,
            ]
        ]
        # Management Region
        management_region: Optional[ManagementRegion]
        migration_bgp_community: Optional[
            Union[
                OneOfMigrationBgpCommunityOptionsDef1,
                OneOfMigrationBgpCommunityOptionsDef2,
            ]
        ]
        role: Optional[
            Union[
                OneOfRoleOptionsDef1,
                OneOfRoleOptionsDef2,
                OneOfRoleOptionsDef3,
            ]
        ]
        secondary_region: Optional[
            Union[
                OneOfSecondaryRegionOptionsDef1,
                OneOfSecondaryRegionOptionsDef2,
                OneOfSecondaryRegionOptionsDef3,
            ]
        ]


    class EditMrfProfileParcelForSystemPutRequest:
        """
        mrf profile parcel schema for POST request
        """

        data: SdwanSystemMrfData
        name: str
        description: Optional[str]
        metadata: Optional[Any]


