======
Models
======


.. code:: python

    from typing import Literal, Any, Union, Dict, Optional, List

    GlobalOptionTypeDef = Literal["global"]

    DecryptAndDropStringDef = Literal["decrypt", "drop"]

    CertificateRevocationStatusDef = Literal["none", "ocsp"]

    NoDecryptAndDropStringDef = Literal["drop", "no-decrypt"]

    FailureModeDef = Literal["close", "open"]

    KeyModulusDef = Literal["1024", "2048", "4096"]

    EckeyTypeDef = Literal["P256", "P384", "P521"]

    MinTlsVerDef = Literal["TLSv1", "TLSv1.1", "TLSv1.2"]

    CaTpLabelDef = Literal["PROXY-SIGNING-CA"]


    class CreateSecurityProfileParcelPostResponse:
        parcel_id: Optional[str]


    class Data:
        ca_cert_bundle: Optional[Any]


    class CreateSecurityProfileParcelPostRequest1:
        data: Data
        # Will be auto generated
        description: str
        name: str
        # This is the documentation for POST request schema for ssl-decryption profile parcel
        documentation: Optional[Any]
        metadata: Optional[Any]


    class OneOfSslEnableOptionsDef:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfExpiredCertificateOptionsDef:
        option_type: GlobalOptionTypeDef
        value: DecryptAndDropStringDef  # pytype: disable=annotation-type-mismatch


    class OneOfCertificateRevocationStatusOptionsDef:
        option_type: GlobalOptionTypeDef
        value: CertificateRevocationStatusDef  # pytype: disable=annotation-type-mismatch


    class OneOfUnsupportedProtocolVersionsOptionsDef:
        option_type: GlobalOptionTypeDef
        value: NoDecryptAndDropStringDef  # pytype: disable=annotation-type-mismatch


    class OneOfFailureModeOptionsDef:
        option_type: GlobalOptionTypeDef
        value: FailureModeDef  # pytype: disable=annotation-type-mismatch


    class DefaultDef:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfCaCertBundleOptionsDef1:
        default: DefaultDef


    class FileNameDef:
        option_type: GlobalOptionTypeDef
        value: str


    class BundleStringDef:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfCaCertBundleOptionsDef2:
        bundle_string: BundleStringDef
        default: DefaultDef
        file_name: FileNameDef


    class OneOfKeyModulusOptionsDef:
        option_type: GlobalOptionTypeDef
        value: KeyModulusDef  # pytype: disable=annotation-type-mismatch


    class OneOfEckeyTypeOptionsDef:
        option_type: GlobalOptionTypeDef
        value: EckeyTypeDef  # pytype: disable=annotation-type-mismatch


    class OneOfCertificateLifetimeOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfMinTlsVerOptionsDef:
        option_type: GlobalOptionTypeDef
        value: MinTlsVerDef  # pytype: disable=annotation-type-mismatch


    class OneOfCaTpLabelOptionsDef:
        option_type: GlobalOptionTypeDef
        value: CaTpLabelDef  # pytype: disable=annotation-type-mismatch


    class SslDecryptionData:
        ssl_enable: OneOfSslEnableOptionsDef
        ca_cert_bundle: Optional[
            Union[
                OneOfCaCertBundleOptionsDef1, OneOfCaCertBundleOptionsDef2
            ]
        ]
        ca_tp_label: Optional[OneOfCaTpLabelOptionsDef]
        certificate_lifetime: Optional[OneOfCertificateLifetimeOptionsDef]
        certificate_revocation_status: Optional[
            OneOfCertificateRevocationStatusOptionsDef
        ]
        eckey_type: Optional[OneOfEckeyTypeOptionsDef]
        expired_certificate: Optional[OneOfExpiredCertificateOptionsDef]
        failure_mode: Optional[OneOfFailureModeOptionsDef]
        key_modulus: Optional[OneOfKeyModulusOptionsDef]
        min_tls_ver: Optional[OneOfMinTlsVerOptionsDef]
        unknown_status: Optional[OneOfExpiredCertificateOptionsDef]
        unsupported_cipher_suites: Optional[
            OneOfUnsupportedProtocolVersionsOptionsDef
        ]
        unsupported_protocol_versions: Optional[
            OneOfUnsupportedProtocolVersionsOptionsDef
        ]
        untrusted_certificate: Optional[OneOfExpiredCertificateOptionsDef]


    class CreateSecurityProfileParcelPostRequest2:
        data: SslDecryptionData
        # Will be auto generated
        description: str
        name: str
        # This is the documentation for POST request schema for ssl-decryption profile parcel
        documentation: Optional[Any]
        metadata: Optional[Any]


    class GetSecurityProfileParcelGetResponse:
        created_by: Optional[str]
        created_on: Optional[int]
        last_updated_by: Optional[str]
        last_updated_on: Optional[int]
        parcel_id: Optional[str]
        parcel_type: Optional[str]
        # ssl-decryption profile parcel schema for POST request
        payload: Optional[
            Union[
                CreateSecurityProfileParcelPostRequest1,
                CreateSecurityProfileParcelPostRequest2,
            ]
        ]


