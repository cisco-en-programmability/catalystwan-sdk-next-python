======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    GlobalOptionTypeDef = Literal["global"]

    TlsDecryptionActionDef = Literal[
        "decrypt", "neverDecrypt", "skipDecrypt"
    ]


    class CreateSdwanSecurityFeaturePostResponse:
        parcel_id: Optional[str]


    class OneOfTlsDecryptionActionOptionsDef:
        option_type: GlobalOptionTypeDef
        value: TlsDecryptionActionDef  # pytype: disable=annotation-type-mismatch


    class RefIdDef:
        option_type: GlobalOptionTypeDef
        value: str


    class ReferenceDef:
        ref_id: RefIdDef


    class Data1:
        intrusion_prevention: ReferenceDef
        tls_decryption_action: OneOfTlsDecryptionActionOptionsDef
        advanced_malware_protection: Optional[ReferenceDef]
        ssl_decryption_profile: Optional[ReferenceDef]
        url_filtering: Optional[ReferenceDef]


    class Data2:
        tls_decryption_action: OneOfTlsDecryptionActionOptionsDef
        url_filtering: ReferenceDef
        advanced_malware_protection: Optional[ReferenceDef]
        intrusion_prevention: Optional[ReferenceDef]
        ssl_decryption_profile: Optional[ReferenceDef]


    class Data3:
        advanced_malware_protection: ReferenceDef
        tls_decryption_action: OneOfTlsDecryptionActionOptionsDef
        intrusion_prevention: Optional[ReferenceDef]
        ssl_decryption_profile: Optional[ReferenceDef]
        url_filtering: Optional[ReferenceDef]


    class CreateSdwanSecurityFeaturePostRequest:
        """
        advanced-malware-protection profile parcel schema for POST request
        """

        # requires tlsDecryptionAction and at least one of Intrusion Prevention or URL Filtering or Advanced Malware Protection policies
        data: Union[Data1, Data2, Data3]
        description: str
        name: str
        metadata: Optional[Any]


    class Payload:
        """
        advanced-malware-protection profile parcel schema for POST request
        """

        # requires tlsDecryptionAction and at least one of Intrusion Prevention or URL Filtering or Advanced Malware Protection policies
        data: Union[Data1, Data2, Data3]
        description: str
        name: str
        metadata: Optional[Any]


    class GetSdwanSecurityFeatureGetResponse:
        created_by: Optional[str]
        created_on: Optional[int]
        last_updated_by: Optional[str]
        last_updated_on: Optional[int]
        parcel_id: Optional[str]
        parcel_type: Optional[str]
        # advanced-malware-protection profile parcel schema for POST request
        payload: Optional[Payload]


