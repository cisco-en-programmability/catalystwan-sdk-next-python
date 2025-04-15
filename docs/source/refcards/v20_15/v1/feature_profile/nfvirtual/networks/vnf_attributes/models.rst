======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    GlobalOptionTypeDef = Literal["global"]

    DefaultOptionTypeDef = Literal["default"]


    class CreateNfvirtualVnfAttributesParcelPostResponse:
        """
        Profile Parcel POST Response schema
        """

        parcel_id: str
        metadata: Optional[Any]


    class OneOfNameOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfNameOptionsDef2:
        option_type: DefaultOptionTypeDef


    class OneOfSrcOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfChecksumOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfUsernameOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfPasswordOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfVersionOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfVnfTypeOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfLowLatencyOptionsDef:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfSriovSupportedOptionsDef:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfNocloudOptionsDef:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfThickDiskProvisioningOptionsDef:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfBootstrapCloudInitDriveTypeOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfRootImageDiskFormatOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfConsoleTypeSerialOptionsDef:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfVendorOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class Data:
        image_name: Union[OneOfNameOptionsDef1, OneOfNameOptionsDef2]
        src: OneOfSrcOptionsDef
        bootstrap_cloud_init_drive_type: Optional[
            OneOfBootstrapCloudInitDriveTypeOptionsDef
        ]
        checksum: Optional[OneOfChecksumOptionsDef]
        console_type_serial: Optional[OneOfConsoleTypeSerialOptionsDef]
        low_latency: Optional[OneOfLowLatencyOptionsDef]
        nocloud: Optional[OneOfNocloudOptionsDef]
        password: Optional[OneOfPasswordOptionsDef]
        root_image_disk_format: Optional[
            OneOfRootImageDiskFormatOptionsDef
        ]
        sriov_supported: Optional[OneOfSriovSupportedOptionsDef]
        thick_disk_provisioning: Optional[
            OneOfThickDiskProvisioningOptionsDef
        ]
        username: Optional[OneOfUsernameOptionsDef]
        vendor: Optional[OneOfVendorOptionsDef]
        version: Optional[OneOfVersionOptionsDef]
        vnf_type: Optional[OneOfVnfTypeOptionsDef]


    class CreateNfvirtualVnfAttributesParcelPostRequest:
        """
        VNF Attributes profile parcel schema for POST request
        """

        data: Data
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


    class VnfAttributesOneOfNameOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class VnfAttributesOneOfSrcOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class VnfAttributesOneOfChecksumOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class VnfAttributesOneOfUsernameOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class VnfAttributesOneOfPasswordOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class VnfAttributesOneOfVersionOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class VnfAttributesOneOfVnfTypeOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class VnfAttributesOneOfBootstrapCloudInitDriveTypeOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class VnfAttributesOneOfRootImageDiskFormatOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class VnfAttributesOneOfConsoleTypeSerialOptionsDef:
        option_type: GlobalOptionTypeDef
        value: bool


    class VnfAttributesOneOfVendorOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class VnfAttributesData:
        image_name: Union[
            VnfAttributesOneOfNameOptionsDef1, OneOfNameOptionsDef2
        ]
        src: VnfAttributesOneOfSrcOptionsDef
        bootstrap_cloud_init_drive_type: Optional[
            VnfAttributesOneOfBootstrapCloudInitDriveTypeOptionsDef
        ]
        checksum: Optional[VnfAttributesOneOfChecksumOptionsDef]
        console_type_serial: Optional[
            VnfAttributesOneOfConsoleTypeSerialOptionsDef
        ]
        low_latency: Optional[OneOfLowLatencyOptionsDef]
        nocloud: Optional[OneOfNocloudOptionsDef]
        password: Optional[VnfAttributesOneOfPasswordOptionsDef]
        root_image_disk_format: Optional[
            VnfAttributesOneOfRootImageDiskFormatOptionsDef
        ]
        sriov_supported: Optional[OneOfSriovSupportedOptionsDef]
        thick_disk_provisioning: Optional[
            OneOfThickDiskProvisioningOptionsDef
        ]
        username: Optional[VnfAttributesOneOfUsernameOptionsDef]
        vendor: Optional[VnfAttributesOneOfVendorOptionsDef]
        version: Optional[VnfAttributesOneOfVersionOptionsDef]
        vnf_type: Optional[VnfAttributesOneOfVnfTypeOptionsDef]


    class Payload:
        """
        VNF Attributes profile parcel schema for PUT request
        """

        data: VnfAttributesData
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


    class GetSingleNfvirtualNetworksVnfAttributesPayload:
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
        # VNF Attributes profile parcel schema for PUT request
        payload: Optional[Payload]


    class EditNfvirtualVnfAttributesParcelPutResponse:
        """
        Profile Parcel PUT Response schema
        """

        id: str
        metadata: Optional[Any]


    class NetworksVnfAttributesOneOfNameOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class NetworksVnfAttributesOneOfSrcOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class NetworksVnfAttributesOneOfChecksumOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class NetworksVnfAttributesOneOfUsernameOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class NetworksVnfAttributesOneOfPasswordOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class NetworksVnfAttributesOneOfVersionOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class NetworksVnfAttributesOneOfVnfTypeOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class NetworksVnfAttributesOneOfBootstrapCloudInitDriveTypeOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class NetworksVnfAttributesOneOfRootImageDiskFormatOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class NetworksVnfAttributesOneOfConsoleTypeSerialOptionsDef:
        option_type: GlobalOptionTypeDef
        value: bool


    class NetworksVnfAttributesOneOfVendorOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class NetworksVnfAttributesData:
        image_name: Union[
            NetworksVnfAttributesOneOfNameOptionsDef1,
            OneOfNameOptionsDef2,
        ]
        src: NetworksVnfAttributesOneOfSrcOptionsDef
        bootstrap_cloud_init_drive_type: Optional[
            NetworksVnfAttributesOneOfBootstrapCloudInitDriveTypeOptionsDef
        ]
        checksum: Optional[NetworksVnfAttributesOneOfChecksumOptionsDef]
        console_type_serial: Optional[
            NetworksVnfAttributesOneOfConsoleTypeSerialOptionsDef
        ]
        low_latency: Optional[OneOfLowLatencyOptionsDef]
        nocloud: Optional[OneOfNocloudOptionsDef]
        password: Optional[NetworksVnfAttributesOneOfPasswordOptionsDef]
        root_image_disk_format: Optional[
            NetworksVnfAttributesOneOfRootImageDiskFormatOptionsDef
        ]
        sriov_supported: Optional[OneOfSriovSupportedOptionsDef]
        thick_disk_provisioning: Optional[
            OneOfThickDiskProvisioningOptionsDef
        ]
        username: Optional[NetworksVnfAttributesOneOfUsernameOptionsDef]
        vendor: Optional[NetworksVnfAttributesOneOfVendorOptionsDef]
        version: Optional[NetworksVnfAttributesOneOfVersionOptionsDef]
        vnf_type: Optional[NetworksVnfAttributesOneOfVnfTypeOptionsDef]


    class EditNfvirtualVnfAttributesParcelPutRequest:
        """
        VNF Attributes profile parcel schema for PUT request
        """

        data: NetworksVnfAttributesData
        description: Optional[str]
        metadata: Optional[Any]
        name: Optional[str]


