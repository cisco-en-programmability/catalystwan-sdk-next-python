======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    GlobalOptionTypeDef = Literal["global"]

    DeploymentDatastoreDef = Literal[
        "datastore1", "datastore2", "datastore3"
    ]

    VariableOptionTypeDef = Literal["variable"]

    ModeDef = Literal["access", "trunk"]

    VnfDeploymentDatastoreDef = Literal[
        "datastore1", "datastore2", "datastore3"
    ]

    VnfModeDef = Literal["access", "trunk"]

    VnfAttributesVnfDeploymentDatastoreDef = Literal[
        "datastore1", "datastore2", "datastore3"
    ]

    VnfAttributesVnfModeDef = Literal["access", "trunk"]


    class CreateNfvirtualVnfParcelPostResponse:
        """
        Profile Parcel POST Response schema
        """

        parcel_id: str
        metadata: Optional[Any]


    class OneOfNameOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfImageOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfBootupTimeOptionsDef:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfDeploymentDatastoreOptionsDef:
        option_type: GlobalOptionTypeDef
        value: DeploymentDatastoreDef  # pytype: disable=annotation-type-mismatch


    class OneOfVcpusOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfVcpusOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfMemoryMbOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfMemoryMbOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfRootDiskMbOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfRootDiskMbOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfDayZeroMountPointOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfDayZeroDayZeroFileContentOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfDayZeroCustomPropertyNameOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfDayZeroCustomPropertyValOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfDayZeroCustomPropertyValOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str


    class OneOfDayZeroCustomPropertyEncryptedValOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfDayZeroCustomPropertyEncryptedValOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str


    class CustomProperty:
        encrypted_val: Optional[
            Union[
                OneOfDayZeroCustomPropertyEncryptedValOptionsDef1,
                OneOfDayZeroCustomPropertyEncryptedValOptionsDef2,
            ]
        ]
        name: Optional[OneOfDayZeroCustomPropertyNameOptionsDef]
        val: Optional[
            Union[
                OneOfDayZeroCustomPropertyValOptionsDef1,
                OneOfDayZeroCustomPropertyValOptionsDef2,
            ]
        ]


    class DayZero:
        day_zero_file_content: OneOfDayZeroDayZeroFileContentOptionsDef
        mount_point: OneOfDayZeroMountPointOptionsDef
        # custom property
        custom_property: Optional[List[CustomProperty]]


    class OneOfInterfacesNameOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfInterfacesNameOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfInterfacesNicidOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfInterfacesNicidOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfInterfacesSriovOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfInterfacesSriovOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfModeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: ModeDef  # pytype: disable=annotation-type-mismatch


    class OneOfModeOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfVlanOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfVlanOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class Interfaces:
        mode: Optional[Union[OneOfModeOptionsDef1, OneOfModeOptionsDef2]]
        name: Optional[
            Union[
                OneOfInterfacesNameOptionsDef1,
                OneOfInterfacesNameOptionsDef2,
            ]
        ]
        nicid: Optional[
            Union[
                OneOfInterfacesNicidOptionsDef1,
                OneOfInterfacesNicidOptionsDef2,
            ]
        ]
        sriov: Optional[
            Union[
                OneOfInterfacesSriovOptionsDef1,
                OneOfInterfacesSriovOptionsDef2,
            ]
        ]
        vlan: Optional[Union[OneOfVlanOptionsDef1, OneOfVlanOptionsDef2]]


    class OneOfAdditionalDisksDiskSizeOptionsDef:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfAdditionalDisksMountPathOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfAdditionalDisksMountPathOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class AdditionalDisks:
        disk_size: OneOfAdditionalDisksDiskSizeOptionsDef
        mount_path: Optional[
            Union[
                OneOfAdditionalDisksMountPathOptionsDef1,
                OneOfAdditionalDisksMountPathOptionsDef2,
            ]
        ]


    class Data:
        image: OneOfImageOptionsDef
        memory_mb: Union[
            OneOfMemoryMbOptionsDef1, OneOfMemoryMbOptionsDef2
        ]
        name: OneOfNameOptionsDef
        vcpus: Union[OneOfVcpusOptionsDef1, OneOfVcpusOptionsDef2]
        # Additional disks
        additional_disks: Optional[List[AdditionalDisks]]
        bootup_time: Optional[OneOfBootupTimeOptionsDef]
        # DayZero file
        day_zero: Optional[List[DayZero]]
        deployment_datastore: Optional[OneOfDeploymentDatastoreOptionsDef]
        # Interface name
        interfaces: Optional[List[Interfaces]]
        root_disk_mb: Optional[
            Union[OneOfRootDiskMbOptionsDef1, OneOfRootDiskMbOptionsDef2]
        ]


    class CreateNfvirtualVnfParcelPostRequest:
        """
        VNF profile parcel schema for POST request
        """

        data: Data
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


    class VnfOneOfNameOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class VnfOneOfImageOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class VnfOneOfBootupTimeOptionsDef:
        option_type: GlobalOptionTypeDef
        value: int


    class VnfOneOfDeploymentDatastoreOptionsDef:
        option_type: GlobalOptionTypeDef
        value: VnfDeploymentDatastoreDef  # pytype: disable=annotation-type-mismatch


    class VnfOneOfVcpusOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class VnfOneOfMemoryMbOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class VnfOneOfRootDiskMbOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class VnfOneOfDayZeroMountPointOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class VnfOneOfDayZeroDayZeroFileContentOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class VnfOneOfDayZeroCustomPropertyNameOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class VnfOneOfDayZeroCustomPropertyValOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class VnfOneOfDayZeroCustomPropertyValOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str


    class VnfOneOfDayZeroCustomPropertyEncryptedValOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class VnfOneOfDayZeroCustomPropertyEncryptedValOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str


    class VnfCustomProperty:
        encrypted_val: Optional[
            Union[
                VnfOneOfDayZeroCustomPropertyEncryptedValOptionsDef1,
                VnfOneOfDayZeroCustomPropertyEncryptedValOptionsDef2,
            ]
        ]
        name: Optional[VnfOneOfDayZeroCustomPropertyNameOptionsDef]
        val: Optional[
            Union[
                VnfOneOfDayZeroCustomPropertyValOptionsDef1,
                VnfOneOfDayZeroCustomPropertyValOptionsDef2,
            ]
        ]


    class VnfDayZero:
        day_zero_file_content: VnfOneOfDayZeroDayZeroFileContentOptionsDef
        mount_point: VnfOneOfDayZeroMountPointOptionsDef
        # custom property
        custom_property: Optional[List[VnfCustomProperty]]


    class VnfOneOfInterfacesNameOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class VnfOneOfInterfacesNicidOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class VnfOneOfModeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: VnfModeDef  # pytype: disable=annotation-type-mismatch


    class VnfOneOfVlanOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class VnfInterfaces:
        mode: Optional[
            Union[VnfOneOfModeOptionsDef1, OneOfModeOptionsDef2]
        ]
        name: Optional[
            Union[
                VnfOneOfInterfacesNameOptionsDef1,
                OneOfInterfacesNameOptionsDef2,
            ]
        ]
        nicid: Optional[
            Union[
                VnfOneOfInterfacesNicidOptionsDef1,
                OneOfInterfacesNicidOptionsDef2,
            ]
        ]
        sriov: Optional[
            Union[
                OneOfInterfacesSriovOptionsDef1,
                OneOfInterfacesSriovOptionsDef2,
            ]
        ]
        vlan: Optional[
            Union[VnfOneOfVlanOptionsDef1, OneOfVlanOptionsDef2]
        ]


    class VnfOneOfAdditionalDisksDiskSizeOptionsDef:
        option_type: GlobalOptionTypeDef
        value: int


    class VnfOneOfAdditionalDisksMountPathOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class VnfAdditionalDisks:
        disk_size: VnfOneOfAdditionalDisksDiskSizeOptionsDef
        mount_path: Optional[
            Union[
                VnfOneOfAdditionalDisksMountPathOptionsDef1,
                OneOfAdditionalDisksMountPathOptionsDef2,
            ]
        ]


    class VnfData:
        image: VnfOneOfImageOptionsDef
        memory_mb: Union[
            VnfOneOfMemoryMbOptionsDef1, OneOfMemoryMbOptionsDef2
        ]
        name: VnfOneOfNameOptionsDef
        vcpus: Union[VnfOneOfVcpusOptionsDef1, OneOfVcpusOptionsDef2]
        # Additional disks
        additional_disks: Optional[List[VnfAdditionalDisks]]
        bootup_time: Optional[VnfOneOfBootupTimeOptionsDef]
        # DayZero file
        day_zero: Optional[List[VnfDayZero]]
        deployment_datastore: Optional[
            VnfOneOfDeploymentDatastoreOptionsDef
        ]
        # Interface name
        interfaces: Optional[List[VnfInterfaces]]
        root_disk_mb: Optional[
            Union[
                VnfOneOfRootDiskMbOptionsDef1, OneOfRootDiskMbOptionsDef2
            ]
        ]


    class Payload:
        """
        VNF profile parcel schema for PUT request
        """

        data: VnfData
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


    class GetSingleNfvirtualNetworksVnfAttributesVnfPayload:
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
        # VNF profile parcel schema for PUT request
        payload: Optional[Payload]


    class EditNfvirtualVnfParcelPutResponse:
        """
        Profile Parcel PUT Response schema
        """

        id: str
        metadata: Optional[Any]


    class VnfAttributesVnfOneOfNameOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class VnfAttributesVnfOneOfImageOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class VnfAttributesVnfOneOfBootupTimeOptionsDef:
        option_type: GlobalOptionTypeDef
        value: int


    class VnfAttributesVnfOneOfDeploymentDatastoreOptionsDef:
        option_type: GlobalOptionTypeDef
        value: VnfAttributesVnfDeploymentDatastoreDef  # pytype: disable=annotation-type-mismatch


    class VnfAttributesVnfOneOfVcpusOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class VnfAttributesVnfOneOfMemoryMbOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class VnfAttributesVnfOneOfRootDiskMbOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class VnfAttributesVnfOneOfDayZeroMountPointOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class VnfAttributesVnfOneOfDayZeroDayZeroFileContentOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class VnfAttributesVnfOneOfDayZeroCustomPropertyNameOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class VnfAttributesVnfOneOfDayZeroCustomPropertyValOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class VnfAttributesVnfOneOfDayZeroCustomPropertyValOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str


    class VnfAttributesVnfOneOfDayZeroCustomPropertyEncryptedValOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class VnfAttributesVnfOneOfDayZeroCustomPropertyEncryptedValOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str


    class VnfAttributesVnfCustomProperty:
        encrypted_val: Optional[
            Union[
                VnfAttributesVnfOneOfDayZeroCustomPropertyEncryptedValOptionsDef1,
                VnfAttributesVnfOneOfDayZeroCustomPropertyEncryptedValOptionsDef2,
            ]
        ]
        name: Optional[
            VnfAttributesVnfOneOfDayZeroCustomPropertyNameOptionsDef
        ]
        val: Optional[
            Union[
                VnfAttributesVnfOneOfDayZeroCustomPropertyValOptionsDef1,
                VnfAttributesVnfOneOfDayZeroCustomPropertyValOptionsDef2,
            ]
        ]


    class VnfAttributesVnfDayZero:
        day_zero_file_content: (
            VnfAttributesVnfOneOfDayZeroDayZeroFileContentOptionsDef
        )
        mount_point: VnfAttributesVnfOneOfDayZeroMountPointOptionsDef
        # custom property
        custom_property: Optional[List[VnfAttributesVnfCustomProperty]]


    class VnfAttributesVnfOneOfInterfacesNameOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class VnfAttributesVnfOneOfInterfacesNicidOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class VnfAttributesVnfOneOfModeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: VnfAttributesVnfModeDef  # pytype: disable=annotation-type-mismatch


    class VnfAttributesVnfOneOfVlanOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class VnfAttributesVnfInterfaces:
        mode: Optional[
            Union[
                VnfAttributesVnfOneOfModeOptionsDef1, OneOfModeOptionsDef2
            ]
        ]
        name: Optional[
            Union[
                VnfAttributesVnfOneOfInterfacesNameOptionsDef1,
                OneOfInterfacesNameOptionsDef2,
            ]
        ]
        nicid: Optional[
            Union[
                VnfAttributesVnfOneOfInterfacesNicidOptionsDef1,
                OneOfInterfacesNicidOptionsDef2,
            ]
        ]
        sriov: Optional[
            Union[
                OneOfInterfacesSriovOptionsDef1,
                OneOfInterfacesSriovOptionsDef2,
            ]
        ]
        vlan: Optional[
            Union[
                VnfAttributesVnfOneOfVlanOptionsDef1, OneOfVlanOptionsDef2
            ]
        ]


    class VnfAttributesVnfOneOfAdditionalDisksDiskSizeOptionsDef:
        option_type: GlobalOptionTypeDef
        value: int


    class VnfAttributesVnfOneOfAdditionalDisksMountPathOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class VnfAttributesVnfAdditionalDisks:
        disk_size: VnfAttributesVnfOneOfAdditionalDisksDiskSizeOptionsDef
        mount_path: Optional[
            Union[
                VnfAttributesVnfOneOfAdditionalDisksMountPathOptionsDef1,
                OneOfAdditionalDisksMountPathOptionsDef2,
            ]
        ]


    class VnfAttributesVnfData:
        image: VnfAttributesVnfOneOfImageOptionsDef
        memory_mb: Union[
            VnfAttributesVnfOneOfMemoryMbOptionsDef1,
            OneOfMemoryMbOptionsDef2,
        ]
        name: VnfAttributesVnfOneOfNameOptionsDef
        vcpus: Union[
            VnfAttributesVnfOneOfVcpusOptionsDef1, OneOfVcpusOptionsDef2
        ]
        # Additional disks
        additional_disks: Optional[List[VnfAttributesVnfAdditionalDisks]]
        bootup_time: Optional[VnfAttributesVnfOneOfBootupTimeOptionsDef]
        # DayZero file
        day_zero: Optional[List[VnfAttributesVnfDayZero]]
        deployment_datastore: Optional[
            VnfAttributesVnfOneOfDeploymentDatastoreOptionsDef
        ]
        # Interface name
        interfaces: Optional[List[VnfAttributesVnfInterfaces]]
        root_disk_mb: Optional[
            Union[
                VnfAttributesVnfOneOfRootDiskMbOptionsDef1,
                OneOfRootDiskMbOptionsDef2,
            ]
        ]


    class EditNfvirtualVnfParcelPutRequest:
        """
        VNF profile parcel schema for PUT request
        """

        data: VnfAttributesVnfData
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


