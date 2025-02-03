======
Models
======


.. code:: python

    from typing import Any, List, Dict, Literal, Optional, Union

    GlobalOptionTypeDef = Literal["global"]

    SignatureSetDef = Literal["balanced", "connectivity", "security"]

    InspectionModeDef = Literal["detection", "protection"]

    LogLevelDef = Literal[
        "alert",
        "critical",
        "debug",
        "emergency",
        "error",
        "info",
        "notice",
        "warning",
    ]


    class CreateSecurityProfileParcelPostResponse:
        parcel_id: Optional[str]


    class OneOfSignatureSetOptionsDef:
        option_type: GlobalOptionTypeDef
        value: SignatureSetDef


    class OneOfInspectionModeOptionsDef:
        option_type: GlobalOptionTypeDef
        value: InspectionModeDef


    class RefIdOptionDef:
        option_type: GlobalOptionTypeDef
        value: str


    class SignatureAllowedList:
        """
        Valid UUID
        """

        ref_id: Optional[RefIdOptionDef]


    class OneOfLogLevelOptionsDef:
        option_type: GlobalOptionTypeDef
        value: LogLevelDef


    class OneOfCustomSignatureOptionsDef:
        option_type: GlobalOptionTypeDef
        value: bool


    class Data:
        inspection_mode: OneOfInspectionModeOptionsDef
        log_level: OneOfLogLevelOptionsDef
        signature_set: OneOfSignatureSetOptionsDef
        custom_signature: Optional[OneOfCustomSignatureOptionsDef]
        # Valid UUID
        signature_allowed_list: Optional[SignatureAllowedList]


    class CreateSecurityProfileParcelPostRequest:
        """
        Intrusion Prevention profile parcel schema for POST request
        """

        data: Data
        name: str
        description: Optional[str]
        # This is the documentation for POST request schema for Intrusion Prevention profile parcel
        documentation: Optional[Any]
        metadata: Optional[Any]


    class GetSecurityProfileParcelGetResponse:
        created_by: Optional[str]
        created_on: Optional[int]
        last_updated_by: Optional[str]
        last_updated_on: Optional[int]
        parcel_id: Optional[str]
        parcel_type: Optional[str]
        # Intrusion Prevention profile parcel schema for POST request
        payload: Optional[CreateSecurityProfileParcelPostRequest]


