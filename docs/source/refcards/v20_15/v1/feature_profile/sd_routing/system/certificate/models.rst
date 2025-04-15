======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    GlobalOptionTypeDef = Literal["global"]

    VariableOptionTypeDef = Literal["variable"]

    DefaultOptionTypeDef = Literal["default"]

    Value = Literal["crl", "crl none", "none"]

    CertificateValue = Literal["none"]


    class OneOfTrustpointNameOptionDef:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfCertificateUuidOptionDef:
        option_type: GlobalOptionTypeDef
        value: str


    class Certificates:
        certificate_uuid: OneOfCertificateUuidOptionDef
        trust_point_name: OneOfTrustpointNameOptionDef


    class OneOfScepUrlOptionDef:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfScepPasswordOptionDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfScepPasswordOptionDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfScepPasswordOptionDef3:
        option_type: DefaultOptionTypeDef


    class OneOfVrfOptionsWithDefault1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfVrfOptionsWithDefault2:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfVrfOptionsWithDefault3:
        option_type: DefaultOptionTypeDef


    class OneOfSubjectNameOptionDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfSubjectNameOptionDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfCrlCheckOptionDef1:
        option_type: GlobalOptionTypeDef
        value: Value  # pytype: disable=annotation-type-mismatch


    class OneOfCrlCheckOptionDef2:
        option_type: DefaultOptionTypeDef
        value: (
            CertificateValue  # pytype: disable=annotation-type-mismatch
        )


    class ScepCertificates:
        certificate_uuid: OneOfCertificateUuidOptionDef
        crl_check: Union[OneOfCrlCheckOptionDef1, OneOfCrlCheckOptionDef2]
        scep_url: OneOfScepUrlOptionDef
        subject_name: Union[
            OneOfSubjectNameOptionDef1, OneOfSubjectNameOptionDef2
        ]
        trust_point_name: OneOfTrustpointNameOptionDef
        scep_password: Optional[
            Union[
                OneOfScepPasswordOptionDef1,
                OneOfScepPasswordOptionDef2,
                OneOfScepPasswordOptionDef3,
            ]
        ]
        scep_vrf: Optional[
            Union[
                OneOfVrfOptionsWithDefault1,
                OneOfVrfOptionsWithDefault2,
                OneOfVrfOptionsWithDefault3,
            ]
        ]


    class Data1:
        # Thirdparty CA Certificate List
        certificates: List[Certificates]
        # Feature Certificates Enrollment through SCEP
        scep_certificates: Optional[List[ScepCertificates]]


    class Data2:
        # Feature Certificates Enrollment through SCEP
        scep_certificates: List[ScepCertificates]
        # Thirdparty CA Certificate List
        certificates: Optional[List[Certificates]]


    class Payload:
        """
        Certificate feature schema for POST/PUT request
        """

        data: Union[Data1, Data2]
        name: str
        # Set the feature description
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
        # Certificate feature schema for POST/PUT request
        payload: Optional[Payload]


    class GetListSdRoutingSystemCertificatePayload:
        data: Optional[List[Data]]


    class CreateSdroutingCertificateFeaturePostResponse:
        """
        Profile Parcel POST Response schema
        """

        parcel_id: str
        metadata: Optional[Any]


    class CreateSdroutingCertificateFeaturePostRequest:
        """
        Certificate feature schema for POST/PUT request
        """

        data: Union[Data1, Data2]
        name: str
        # Set the feature description
        description: Optional[str]
        metadata: Optional[Any]


    class GetSingleSdRoutingSystemCertificatePayload:
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
        # Certificate feature schema for POST/PUT request
        payload: Optional[Payload]


    class EditSdroutingCertificateFeaturePutResponse:
        """
        Profile Parcel PUT Response schema
        """

        id: str
        metadata: Optional[Any]


    class EditSdroutingCertificateFeaturePutRequest:
        """
        Certificate feature schema for POST/PUT request
        """

        data: Union[Data1, Data2]
        name: str
        # Set the feature description
        description: Optional[str]
        metadata: Optional[Any]


