======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    GlobalOptionTypeDef = Literal["global"]

    TlsDecryptionActionDef = Literal[
        "decrypt", "neverDecrypt", "skipDecrypt"
    ]

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

    WebCategoriesActionDef = Literal["allow", "block"]

    WebCategoriesDef = Literal[
        "abortion",
        "abused-drugs",
        "adult-and-pornography",
        "alcohol-and-tobacco",
        "auctions",
        "bot-nets",
        "business-and-economy",
        "cdns",
        "cheating",
        "computer-and-internet-info",
        "computer-and-internet-security",
        "confirmed-spam-sources",
        "cult-and-occult",
        "dating",
        "dead-sites",
        "dynamic-content",
        "educational-institutions",
        "entertainment-and-arts",
        "fashion-and-beauty",
        "financial-services",
        "gambling",
        "games",
        "government",
        "gross",
        "hacking",
        "hate-and-racism",
        "health-and-medicine",
        "home",
        "hunting-and-fishing",
        "illegal",
        "image-and-video-search",
        "individual-stock-advice-and-tools",
        "internet-communications",
        "internet-portals",
        "job-search",
        "keyloggers-and-monitoring",
        "kids",
        "legal",
        "local-information",
        "malware-sites",
        "marijuana",
        "military",
        "motor-vehicles",
        "music",
        "news-and-media",
        "nudity",
        "online-greeting-cards",
        "online-personal-storage",
        "open-http-proxies",
        "p2p",
        "parked-sites",
        "pay-to-surf",
        "personal-sites-and-blogs",
        "philosophy-and-political-advocacy",
        "phishing-and-other-frauds",
        "private-ip-addresses",
        "proxy-avoid-and-anonymizers",
        "questionable",
        "real-estate",
        "recreation-and-hobbies",
        "reference-and-research",
        "religion",
        "search-engines",
        "sex-education",
        "shareware-and-freeware",
        "shopping",
        "social-network",
        "society",
        "spam-urls",
        "sports",
        "spyware-and-adware",
        "streaming-media",
        "swimsuits-and-intimate-apparel",
        "training-and-tools",
        "translation",
        "travel",
        "uncategorized",
        "unconfirmed-spam-sources",
        "violence",
        "weapons",
        "web-advertisements",
        "web-based-email",
        "web-hosting",
    ]

    WebReputationDef = Literal[
        "high-risk",
        "low-risk",
        "moderate-risk",
        "suspicious",
        "trustworthy",
    ]

    BlockPageActionDef = Literal["redirect-url", "text"]

    AlertsDef = Literal["blacklist", "categories-reputation", "whitelist"]

    ServerDef = Literal["apjc", "eur", "nam"]

    AlertDef = Literal["critical", "info", "warning"]

    FileAnalysisCloudServerDef = Literal["eur", "nam"]

    CategoriesDef = Literal[
        "abortion",
        "abused-drugs",
        "adult-and-pornography",
        "alcohol-and-tobacco",
        "auctions",
        "bot-nets",
        "business-and-economy",
        "cdns",
        "cheating",
        "computer-and-internet-info",
        "computer-and-internet-security",
        "confirmed-spam-sources",
        "cult-and-occult",
        "dating",
        "dead-sites",
        "dynamic-content",
        "educational-institutions",
        "entertainment-and-arts",
        "fashion-and-beauty",
        "financial-services",
        "gambling",
        "games",
        "government",
        "gross",
        "hacking",
        "hate-and-racism",
        "health-and-medicine",
        "home",
        "hunting-and-fishing",
        "illegal",
        "image-and-video-search",
        "individual-stock-advice-and-tools",
        "internet-communications",
        "internet-portals",
        "job-search",
        "keyloggers-and-monitoring",
        "kids",
        "legal",
        "local-information",
        "malware-sites",
        "marijuana",
        "military",
        "motor-vehicles",
        "music",
        "news-and-media",
        "nudity",
        "online-greeting-cards",
        "online-personal-storage",
        "open-http-proxies",
        "p2p",
        "parked-sites",
        "pay-to-surf",
        "personal-sites-and-blogs",
        "philosophy-and-political-advocacy",
        "phishing-and-other-frauds",
        "private-ip-addresses",
        "proxy-avoid-and-anonymizers",
        "questionable",
        "real-estate",
        "recreation-and-hobbies",
        "reference-and-research",
        "religion",
        "search-engines",
        "sex-education",
        "shareware-and-freeware",
        "shopping",
        "social-network",
        "society",
        "spam-urls",
        "sports",
        "spyware-and-adware",
        "streaming-media",
        "swimsuits-and-intimate-apparel",
        "training-and-tools",
        "translation",
        "travel",
        "uncategorized",
        "unconfirmed-spam-sources",
        "violence",
        "weapons",
        "web-advertisements",
        "web-based-email",
        "web-hosting",
    ]

    ThresholdDef = Literal[
        "high-risk",
        "low-risk",
        "moderate-risk",
        "suspicious",
        "trustworthy",
    ]

    DecryptAndDropStringDef = Literal["decrypt", "drop"]

    CertificateRevocationStatusDef = Literal["none", "ocsp"]

    NoDecryptAndDropStringDef = Literal["drop", "no-decrypt"]

    FailureModeDef = Literal["close", "open"]

    KeyModulusDef = Literal["1024", "2048", "4096"]

    EckeyTypeDef = Literal["P256", "P384", "P521"]

    MinTlsVerDef = Literal["TLSv1", "TLSv1.1", "TLSv1.2"]

    CaTpLabelDef = Literal["PROXY-SIGNING-CA"]

    SecurityProfileParcelTypeParam = Literal[
        "advanced-inspection-profile",
        "advanced-malware-protection",
        "intrusion-prevention",
        "ssl-decryption",
        "ssl-decryption-profile",
        "url-filtering",
    ]

    UnifiedTlsDecryptionActionDef = Literal[
        "decrypt", "neverDecrypt", "skipDecrypt"
    ]

    PolicyObjectUnifiedTlsDecryptionActionDef = Literal[
        "decrypt", "neverDecrypt", "skipDecrypt"
    ]

    SdwanPolicyObjectUnifiedTlsDecryptionActionDef = Literal[
        "decrypt", "neverDecrypt", "skipDecrypt"
    ]

    UnifiedSignatureSetDef = Literal[
        "balanced", "connectivity", "security"
    ]

    UnifiedInspectionModeDef = Literal["detection", "protection"]

    UnifiedLogLevelDef = Literal[
        "alert",
        "critical",
        "debug",
        "emergency",
        "error",
        "info",
        "notice",
        "warning",
    ]

    UnifiedWebCategoriesActionDef = Literal["allow", "block"]

    UnifiedWebReputationDef = Literal[
        "high-risk",
        "low-risk",
        "moderate-risk",
        "suspicious",
        "trustworthy",
    ]

    UnifiedBlockPageActionDef = Literal["redirect-url", "text"]

    UnifiedServerDef = Literal["apjc", "eur", "nam"]

    PolicyObjectUnifiedServerDef = Literal["apjc", "eur", "nam"]

    UnifiedAlertDef = Literal["critical", "info", "warning"]

    UnifiedFileAnalysisCloudServerDef = Literal["eur", "nam"]

    PolicyObjectUnifiedAlertDef = Literal["critical", "info", "warning"]

    UnifiedThresholdDef = Literal[
        "high-risk",
        "low-risk",
        "moderate-risk",
        "suspicious",
        "trustworthy",
    ]

    PolicyObjectUnifiedThresholdDef = Literal[
        "high-risk",
        "low-risk",
        "moderate-risk",
        "suspicious",
        "trustworthy",
    ]

    UnifiedDecryptAndDropStringDef = Literal["decrypt", "drop"]

    PolicyObjectUnifiedDecryptAndDropStringDef = Literal[
        "decrypt", "drop"
    ]

    UnifiedCertificateRevocationStatusDef = Literal["none", "ocsp"]

    SdwanPolicyObjectUnifiedDecryptAndDropStringDef = Literal[
        "decrypt", "drop"
    ]

    UnifiedNoDecryptAndDropStringDef = Literal["drop", "no-decrypt"]

    PolicyObjectUnifiedNoDecryptAndDropStringDef = Literal[
        "drop", "no-decrypt"
    ]

    UnifiedFailureModeDef = Literal["close", "open"]

    UnifiedKeyModulusDef = Literal["1024", "2048", "4096"]

    UnifiedEckeyTypeDef = Literal["P256", "P384", "P521"]

    UnifiedMinTlsVerDef = Literal["TLSv1", "TLSv1.1", "TLSv1.2"]

    UnifiedCaTpLabelDef = Literal["PROXY-SIGNING-CA"]

    FeatureProfileSdwanPolicyObjectUnifiedTlsDecryptionActionDef = (
        Literal["decrypt", "neverDecrypt", "skipDecrypt"]
    )

    V1FeatureProfileSdwanPolicyObjectUnifiedTlsDecryptionActionDef = (
        Literal["decrypt", "neverDecrypt", "skipDecrypt"]
    )

    TlsDecryptionActionDef1 = Literal[
        "decrypt", "neverDecrypt", "skipDecrypt"
    ]

    PolicyObjectUnifiedSignatureSetDef = Literal[
        "balanced", "connectivity", "security"
    ]

    PolicyObjectUnifiedInspectionModeDef = Literal[
        "detection", "protection"
    ]

    PolicyObjectUnifiedLogLevelDef = Literal[
        "alert",
        "critical",
        "debug",
        "emergency",
        "error",
        "info",
        "notice",
        "warning",
    ]

    PolicyObjectUnifiedWebCategoriesActionDef = Literal["allow", "block"]

    PolicyObjectUnifiedWebReputationDef = Literal[
        "high-risk",
        "low-risk",
        "moderate-risk",
        "suspicious",
        "trustworthy",
    ]

    PolicyObjectUnifiedBlockPageActionDef = Literal[
        "redirect-url", "text"
    ]

    SdwanPolicyObjectUnifiedServerDef = Literal["apjc", "eur", "nam"]

    FeatureProfileSdwanPolicyObjectUnifiedServerDef = Literal[
        "apjc", "eur", "nam"
    ]

    SdwanPolicyObjectUnifiedAlertDef = Literal[
        "critical", "info", "warning"
    ]

    PolicyObjectUnifiedFileAnalysisCloudServerDef = Literal["eur", "nam"]

    FeatureProfileSdwanPolicyObjectUnifiedAlertDef = Literal[
        "critical", "info", "warning"
    ]

    SdwanPolicyObjectUnifiedThresholdDef = Literal[
        "high-risk",
        "low-risk",
        "moderate-risk",
        "suspicious",
        "trustworthy",
    ]

    FeatureProfileSdwanPolicyObjectUnifiedThresholdDef = Literal[
        "high-risk",
        "low-risk",
        "moderate-risk",
        "suspicious",
        "trustworthy",
    ]

    FeatureProfileSdwanPolicyObjectUnifiedDecryptAndDropStringDef = (
        Literal["decrypt", "drop"]
    )

    V1FeatureProfileSdwanPolicyObjectUnifiedDecryptAndDropStringDef = (
        Literal["decrypt", "drop"]
    )

    PolicyObjectUnifiedCertificateRevocationStatusDef = Literal[
        "none", "ocsp"
    ]

    DecryptAndDropStringDef1 = Literal["decrypt", "drop"]

    SdwanPolicyObjectUnifiedNoDecryptAndDropStringDef = Literal[
        "drop", "no-decrypt"
    ]

    FeatureProfileSdwanPolicyObjectUnifiedNoDecryptAndDropStringDef = (
        Literal["drop", "no-decrypt"]
    )

    PolicyObjectUnifiedFailureModeDef = Literal["close", "open"]

    PolicyObjectUnifiedKeyModulusDef = Literal["1024", "2048", "4096"]

    PolicyObjectUnifiedEckeyTypeDef = Literal["P256", "P384", "P521"]

    PolicyObjectUnifiedMinTlsVerDef = Literal[
        "TLSv1", "TLSv1.1", "TLSv1.2"
    ]

    PolicyObjectUnifiedCaTpLabelDef = Literal["PROXY-SIGNING-CA"]


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


    class Schema2HubGeneratedSecurityprofileparceltypePost1:
        """
        advanced-malware-protection profile parcel schema for POST request
        """

        # requires tlsDecryptionAction and at least one of Intrusion Prevention or URL Filtering or Advanced Malware Protection policies
        data: Union[Data1, Data2, Data3]
        description: str
        name: str
        metadata: Optional[Any]


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


    class UnifiedData:
        inspection_mode: OneOfInspectionModeOptionsDef
        log_level: OneOfLogLevelOptionsDef
        signature_set: OneOfSignatureSetOptionsDef
        custom_signature: Optional[OneOfCustomSignatureOptionsDef]
        # Valid UUID
        signature_allowed_list: Optional[SignatureAllowedList]


    class Schema2HubGeneratedSecurityprofileparceltypePost2:
        """
        Intrusion Prevention profile parcel schema for POST request
        """

        data: UnifiedData
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class OneOfWebCategoriesActionOptionsDef:
        option_type: GlobalOptionTypeDef
        value: WebCategoriesActionDef  # pytype: disable=annotation-type-mismatch


    class OneOfWebCategoriesOptionsDef:
        option_type: GlobalOptionTypeDef
        value: List[
            WebCategoriesDef
        ]  # pytype: disable=annotation-type-mismatch


    class OneOfWebReputationOptionsDef:
        option_type: GlobalOptionTypeDef
        value: (
            WebReputationDef  # pytype: disable=annotation-type-mismatch
        )


    class UrlAllowedList:
        ref_id: Optional[RefIdOptionDef]


    class UrlBlockedList:
        ref_id: Optional[RefIdOptionDef]


    class OneOfBlockPageActionOptionsDef:
        option_type: GlobalOptionTypeDef
        value: (
            BlockPageActionDef  # pytype: disable=annotation-type-mismatch
        )


    class OneOfBlockPageContentsOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfRedirectUrlOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfEnableAlertsOptionsDef:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfAlertsOptionsDef:
        option_type: GlobalOptionTypeDef
        value: List[AlertsDef]  # pytype: disable=annotation-type-mismatch


    class PolicyObjectUnifiedData:
        block_page_action: OneOfBlockPageActionOptionsDef
        enable_alerts: OneOfEnableAlertsOptionsDef
        web_categories_action: OneOfWebCategoriesActionOptionsDef
        web_reputation: OneOfWebReputationOptionsDef
        alerts: Optional[OneOfAlertsOptionsDef]
        block_page_contents: Optional[OneOfBlockPageContentsOptionsDef]
        redirect_url: Optional[OneOfRedirectUrlOptionsDef]
        url_allowed_list: Optional[UrlAllowedList]
        url_blocked_list: Optional[UrlBlockedList]
        web_categories: Optional[OneOfWebCategoriesOptionsDef]


    class Schema2HubGeneratedSecurityprofileparceltypePost3:
        """
        url-filtering profile parcel schema for POST request
        """

        data: PolicyObjectUnifiedData
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class OneOfMatchAllVpnOptionsDef:
        option_type: GlobalOptionTypeDef
        value: Any


    class OneOfFileReputationCloudServerOptionsDef:
        option_type: GlobalOptionTypeDef
        value: ServerDef  # pytype: disable=annotation-type-mismatch


    class OneOfFileReputationEstServerOptionsDef:
        option_type: GlobalOptionTypeDef
        value: ServerDef  # pytype: disable=annotation-type-mismatch


    class OneOfFileReputationAlertOptionsDef:
        option_type: GlobalOptionTypeDef
        value: AlertDef  # pytype: disable=annotation-type-mismatch


    class OneOfFileAnalysisEnabledOptionsDef:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfFileAnalysisCloudServerOptionsDef:
        option_type: GlobalOptionTypeDef
        value: FileAnalysisCloudServerDef  # pytype: disable=annotation-type-mismatch


    class OneOfFileAnalysisFileTypesOptionsDef:
        option_type: GlobalOptionTypeDef
        value: List[str]


    class OneOfFileAnalysisAlertOptionsDef:
        option_type: GlobalOptionTypeDef
        value: AlertDef  # pytype: disable=annotation-type-mismatch


    class SdwanPolicyObjectUnifiedData:
        file_analysis_enabled: OneOfFileAnalysisEnabledOptionsDef
        file_reputation_alert: OneOfFileReputationAlertOptionsDef
        file_reputation_cloud_server: (
            OneOfFileReputationCloudServerOptionsDef
        )
        file_reputation_est_server: OneOfFileReputationEstServerOptionsDef
        match_all_vpn: OneOfMatchAllVpnOptionsDef
        file_analysis_alert: Optional[OneOfFileAnalysisAlertOptionsDef]
        file_analysis_cloud_server: Optional[
            OneOfFileAnalysisCloudServerOptionsDef
        ]
        file_analysis_file_types: Optional[
            OneOfFileAnalysisFileTypesOptionsDef
        ]


    class Schema2HubGeneratedSecurityprofileparceltypePost4:
        """
        advanced-malware-protection profile parcel schema for POST request
        """

        data: SdwanPolicyObjectUnifiedData
        description: str
        name: str
        metadata: Optional[Any]


    class OneOfDecryptCategoriesOptionsDef:
        option_type: GlobalOptionTypeDef
        value: List[
            CategoriesDef
        ]  # pytype: disable=annotation-type-mismatch


    class OneOfNeverDecryptCategoriesOptionsDef:
        option_type: GlobalOptionTypeDef
        value: List[
            CategoriesDef
        ]  # pytype: disable=annotation-type-mismatch


    class OneOfSkipDecryptCategoriesOptionsDef:
        option_type: GlobalOptionTypeDef
        value: List[
            CategoriesDef
        ]  # pytype: disable=annotation-type-mismatch


    class OneOfReputationOptionsDef:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfDecryptThresholdOptionsDef:
        option_type: GlobalOptionTypeDef
        value: ThresholdDef  # pytype: disable=annotation-type-mismatch


    class OneOfSkipDecryptThresholdOptionsDef:
        option_type: GlobalOptionTypeDef
        value: ThresholdDef  # pytype: disable=annotation-type-mismatch


    class OneOfFailDecryptOptionsDef:
        option_type: GlobalOptionTypeDef
        value: bool


    class FeatureProfileSdwanPolicyObjectUnifiedData:
        decrypt_categories: OneOfDecryptCategoriesOptionsDef
        fail_decrypt: OneOfFailDecryptOptionsDef
        never_decrypt_categories: OneOfNeverDecryptCategoriesOptionsDef
        reputation: OneOfReputationOptionsDef
        decrypt_threshold: Optional[OneOfDecryptThresholdOptionsDef]
        skip_decrypt_categories: Optional[
            OneOfSkipDecryptCategoriesOptionsDef
        ]
        skip_decrypt_threshold: Optional[
            OneOfSkipDecryptThresholdOptionsDef
        ]
        url_allowed_list: Optional[UrlAllowedList]
        url_blocked_list: Optional[UrlBlockedList]


    class Schema2HubGeneratedSecurityprofileparceltypePost5:
        """
        ssl-decryption-profile profile parcel schema for POST request
        """

        data: FeatureProfileSdwanPolicyObjectUnifiedData
        description: str
        name: str
        metadata: Optional[Any]


    class V1FeatureProfileSdwanPolicyObjectUnifiedData:
        ca_cert_bundle: Optional[Any]


    class Schema2HubGeneratedSecurityprofileparceltypePost61:
        data: V1FeatureProfileSdwanPolicyObjectUnifiedData
        # Will be auto generated
        description: str
        name: str
        metadata: Optional[Any]


    class OneOfSslEnableOptionsDef:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfExpiredCertificateOptionsDef:
        option_type: GlobalOptionTypeDef
        value: DecryptAndDropStringDef  # pytype: disable=annotation-type-mismatch


    class OneOfUntrustedCertificateOptionsDef:
        option_type: GlobalOptionTypeDef
        value: DecryptAndDropStringDef  # pytype: disable=annotation-type-mismatch


    class OneOfCertificateRevocationStatusOptionsDef:
        option_type: GlobalOptionTypeDef
        value: CertificateRevocationStatusDef  # pytype: disable=annotation-type-mismatch


    class OneOfUnknownStatusOptionsDef:
        option_type: GlobalOptionTypeDef
        value: DecryptAndDropStringDef  # pytype: disable=annotation-type-mismatch


    class OneOfUnsupportedProtocolVersionsOptionsDef:
        option_type: GlobalOptionTypeDef
        value: NoDecryptAndDropStringDef  # pytype: disable=annotation-type-mismatch


    class OneOfUnsupportedCipherSuitesOptionsDef:
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


    class Data11:
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
        unknown_status: Optional[OneOfUnknownStatusOptionsDef]
        unsupported_cipher_suites: Optional[
            OneOfUnsupportedCipherSuitesOptionsDef
        ]
        unsupported_protocol_versions: Optional[
            OneOfUnsupportedProtocolVersionsOptionsDef
        ]
        untrusted_certificate: Optional[
            OneOfUntrustedCertificateOptionsDef
        ]


    class Schema2HubGeneratedSecurityprofileparceltypePost62:
        data: Data11
        # Will be auto generated
        description: str
        name: str
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
        payload: Optional[
            Union[
                Schema2HubGeneratedSecurityprofileparceltypePost1,
                Schema2HubGeneratedSecurityprofileparceltypePost2,
                Schema2HubGeneratedSecurityprofileparceltypePost3,
                Schema2HubGeneratedSecurityprofileparceltypePost4,
                Schema2HubGeneratedSecurityprofileparceltypePost5,
                Union[
                    Schema2HubGeneratedSecurityprofileparceltypePost61,
                    Schema2HubGeneratedSecurityprofileparceltypePost62,
                ],
            ]
        ]


    class GetListSdwanPolicyObjectUnifiedAdvancedInspectionProfilePayload:
        data: Optional[List[Data]]


    class CreateSecurityProfileParcelPostResponse:
        """
        Profile Parcel POST Response schema
        """

        parcel_id: str
        metadata: Optional[Any]


    class CreateSecurityProfileParcelPostRequest1:
        """
        advanced-malware-protection profile parcel schema for POST request
        """

        # requires tlsDecryptionAction and at least one of Intrusion Prevention or URL Filtering or Advanced Malware Protection policies
        data: Union[Data1, Data2, Data3]
        description: str
        name: str
        metadata: Optional[Any]


    class Data21:
        inspection_mode: OneOfInspectionModeOptionsDef
        log_level: OneOfLogLevelOptionsDef
        signature_set: OneOfSignatureSetOptionsDef
        custom_signature: Optional[OneOfCustomSignatureOptionsDef]
        # Valid UUID
        signature_allowed_list: Optional[SignatureAllowedList]


    class CreateSecurityProfileParcelPostRequest2:
        """
        Intrusion Prevention profile parcel schema for POST request
        """

        data: Data21
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class Data31:
        block_page_action: OneOfBlockPageActionOptionsDef
        enable_alerts: OneOfEnableAlertsOptionsDef
        web_categories_action: OneOfWebCategoriesActionOptionsDef
        web_reputation: OneOfWebReputationOptionsDef
        alerts: Optional[OneOfAlertsOptionsDef]
        block_page_contents: Optional[OneOfBlockPageContentsOptionsDef]
        redirect_url: Optional[OneOfRedirectUrlOptionsDef]
        url_allowed_list: Optional[UrlAllowedList]
        url_blocked_list: Optional[UrlBlockedList]
        web_categories: Optional[OneOfWebCategoriesOptionsDef]


    class CreateSecurityProfileParcelPostRequest3:
        """
        url-filtering profile parcel schema for POST request
        """

        data: Data31
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class Data4:
        file_analysis_enabled: OneOfFileAnalysisEnabledOptionsDef
        file_reputation_alert: OneOfFileReputationAlertOptionsDef
        file_reputation_cloud_server: (
            OneOfFileReputationCloudServerOptionsDef
        )
        file_reputation_est_server: OneOfFileReputationEstServerOptionsDef
        match_all_vpn: OneOfMatchAllVpnOptionsDef
        file_analysis_alert: Optional[OneOfFileAnalysisAlertOptionsDef]
        file_analysis_cloud_server: Optional[
            OneOfFileAnalysisCloudServerOptionsDef
        ]
        file_analysis_file_types: Optional[
            OneOfFileAnalysisFileTypesOptionsDef
        ]


    class CreateSecurityProfileParcelPostRequest4:
        """
        advanced-malware-protection profile parcel schema for POST request
        """

        data: Data4
        description: str
        name: str
        metadata: Optional[Any]


    class Data5:
        decrypt_categories: OneOfDecryptCategoriesOptionsDef
        fail_decrypt: OneOfFailDecryptOptionsDef
        never_decrypt_categories: OneOfNeverDecryptCategoriesOptionsDef
        reputation: OneOfReputationOptionsDef
        decrypt_threshold: Optional[OneOfDecryptThresholdOptionsDef]
        skip_decrypt_categories: Optional[
            OneOfSkipDecryptCategoriesOptionsDef
        ]
        skip_decrypt_threshold: Optional[
            OneOfSkipDecryptThresholdOptionsDef
        ]
        url_allowed_list: Optional[UrlAllowedList]
        url_blocked_list: Optional[UrlBlockedList]


    class CreateSecurityProfileParcelPostRequest5:
        """
        ssl-decryption-profile profile parcel schema for POST request
        """

        data: Data5
        description: str
        name: str
        metadata: Optional[Any]


    class Data6:
        ca_cert_bundle: Optional[Any]


    class CreateSecurityProfileParcelPostRequest61:
        data: Data6
        # Will be auto generated
        description: str
        name: str
        metadata: Optional[Any]


    class Data7:
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
        unknown_status: Optional[OneOfUnknownStatusOptionsDef]
        unsupported_cipher_suites: Optional[
            OneOfUnsupportedCipherSuitesOptionsDef
        ]
        unsupported_protocol_versions: Optional[
            OneOfUnsupportedProtocolVersionsOptionsDef
        ]
        untrusted_certificate: Optional[
            OneOfUntrustedCertificateOptionsDef
        ]


    class CreateSecurityProfileParcelPostRequest62:
        data: Data7
        # Will be auto generated
        description: str
        name: str
        metadata: Optional[Any]


    class UnifiedOneOfTlsDecryptionActionOptionsDef:
        option_type: GlobalOptionTypeDef
        value: UnifiedTlsDecryptionActionDef  # pytype: disable=annotation-type-mismatch


    class UnifiedRefIdDef:
        option_type: GlobalOptionTypeDef
        value: str


    class UnifiedReferenceDef:
        ref_id: UnifiedRefIdDef


    class PolicyObjectUnifiedRefIdDef:
        option_type: GlobalOptionTypeDef
        value: str


    class PolicyObjectUnifiedReferenceDef:
        ref_id: PolicyObjectUnifiedRefIdDef


    class SdwanPolicyObjectUnifiedRefIdDef:
        option_type: GlobalOptionTypeDef
        value: str


    class SdwanPolicyObjectUnifiedReferenceDef:
        ref_id: SdwanPolicyObjectUnifiedRefIdDef


    class FeatureProfileSdwanPolicyObjectUnifiedRefIdDef:
        option_type: GlobalOptionTypeDef
        value: str


    class FeatureProfileSdwanPolicyObjectUnifiedReferenceDef:
        ref_id: FeatureProfileSdwanPolicyObjectUnifiedRefIdDef


    class UnifiedData1:
        intrusion_prevention: UnifiedReferenceDef
        tls_decryption_action: UnifiedOneOfTlsDecryptionActionOptionsDef
        advanced_malware_protection: Optional[
            SdwanPolicyObjectUnifiedReferenceDef
        ]
        ssl_decryption_profile: Optional[
            FeatureProfileSdwanPolicyObjectUnifiedReferenceDef
        ]
        url_filtering: Optional[PolicyObjectUnifiedReferenceDef]


    class PolicyObjectUnifiedOneOfTlsDecryptionActionOptionsDef:
        option_type: GlobalOptionTypeDef
        value: PolicyObjectUnifiedTlsDecryptionActionDef  # pytype: disable=annotation-type-mismatch


    class V1FeatureProfileSdwanPolicyObjectUnifiedRefIdDef:
        option_type: GlobalOptionTypeDef
        value: str


    class V1FeatureProfileSdwanPolicyObjectUnifiedReferenceDef:
        ref_id: V1FeatureProfileSdwanPolicyObjectUnifiedRefIdDef


    class RefIdDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class ReferenceDef1:
        ref_id: RefIdDef1


    class RefIdDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class ReferenceDef2:
        ref_id: RefIdDef2


    class RefIdDef3:
        option_type: GlobalOptionTypeDef
        value: str


    class ReferenceDef3:
        ref_id: RefIdDef3


    class UnifiedData2:
        tls_decryption_action: (
            PolicyObjectUnifiedOneOfTlsDecryptionActionOptionsDef
        )
        url_filtering: ReferenceDef1
        advanced_malware_protection: Optional[ReferenceDef2]
        intrusion_prevention: Optional[
            V1FeatureProfileSdwanPolicyObjectUnifiedReferenceDef
        ]
        ssl_decryption_profile: Optional[ReferenceDef3]


    class SdwanPolicyObjectUnifiedOneOfTlsDecryptionActionOptionsDef:
        option_type: GlobalOptionTypeDef
        value: SdwanPolicyObjectUnifiedTlsDecryptionActionDef  # pytype: disable=annotation-type-mismatch


    class RefIdDef4:
        option_type: GlobalOptionTypeDef
        value: str


    class ReferenceDef4:
        ref_id: RefIdDef4


    class RefIdDef5:
        option_type: GlobalOptionTypeDef
        value: str


    class ReferenceDef5:
        ref_id: RefIdDef5


    class RefIdDef6:
        option_type: GlobalOptionTypeDef
        value: str


    class ReferenceDef6:
        ref_id: RefIdDef6


    class RefIdDef7:
        option_type: GlobalOptionTypeDef
        value: str


    class ReferenceDef7:
        ref_id: RefIdDef7


    class UnifiedData3:
        advanced_malware_protection: ReferenceDef6
        tls_decryption_action: (
            SdwanPolicyObjectUnifiedOneOfTlsDecryptionActionOptionsDef
        )
        intrusion_prevention: Optional[ReferenceDef4]
        ssl_decryption_profile: Optional[ReferenceDef7]
        url_filtering: Optional[ReferenceDef5]


    class Schema2HubGeneratedSecurityprofileparceltypePut1:
        """
        advanced-malware-protection profile parcel schema for PUT request
        """

        # requires tlsDecryptionAction and at least one of Intrusion Prevention or URL Filtering or Advanced Malware Protection policies
        data: Union[UnifiedData1, UnifiedData2, UnifiedData3]
        description: str
        name: str
        metadata: Optional[Any]


    class UnifiedOneOfSignatureSetOptionsDef:
        option_type: GlobalOptionTypeDef
        value: UnifiedSignatureSetDef


    class UnifiedOneOfInspectionModeOptionsDef:
        option_type: GlobalOptionTypeDef
        value: UnifiedInspectionModeDef


    class UnifiedOneOfLogLevelOptionsDef:
        option_type: GlobalOptionTypeDef
        value: UnifiedLogLevelDef


    class UnifiedOneOfCustomSignatureOptionsDef:
        option_type: GlobalOptionTypeDef
        value: bool


    class Data8:
        inspection_mode: UnifiedOneOfInspectionModeOptionsDef
        log_level: UnifiedOneOfLogLevelOptionsDef
        signature_set: UnifiedOneOfSignatureSetOptionsDef
        custom_signature: Optional[UnifiedOneOfCustomSignatureOptionsDef]
        # Valid UUID
        signature_allowed_list: Optional[SignatureAllowedList]


    class Schema2HubGeneratedSecurityprofileparceltypePut2:
        """
        Intrusion Prevention profile parcel schema for PUT request
        """

        data: Data8
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class UnifiedOneOfWebCategoriesActionOptionsDef:
        option_type: GlobalOptionTypeDef
        value: UnifiedWebCategoriesActionDef  # pytype: disable=annotation-type-mismatch


    class UnifiedOneOfWebCategoriesOptionsDef:
        option_type: GlobalOptionTypeDef
        value: List[
            WebCategoriesDef
        ]  # pytype: disable=annotation-type-mismatch


    class UnifiedOneOfWebReputationOptionsDef:
        option_type: GlobalOptionTypeDef
        value: UnifiedWebReputationDef  # pytype: disable=annotation-type-mismatch


    class UnifiedOneOfBlockPageActionOptionsDef:
        option_type: GlobalOptionTypeDef
        value: UnifiedBlockPageActionDef  # pytype: disable=annotation-type-mismatch


    class UnifiedOneOfBlockPageContentsOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class UnifiedOneOfRedirectUrlOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class UnifiedOneOfAlertsOptionsDef:
        option_type: GlobalOptionTypeDef
        value: List[AlertsDef]  # pytype: disable=annotation-type-mismatch


    class Data9:
        block_page_action: UnifiedOneOfBlockPageActionOptionsDef
        enable_alerts: OneOfEnableAlertsOptionsDef
        web_categories_action: UnifiedOneOfWebCategoriesActionOptionsDef
        web_reputation: UnifiedOneOfWebReputationOptionsDef
        alerts: Optional[UnifiedOneOfAlertsOptionsDef]
        block_page_contents: Optional[
            UnifiedOneOfBlockPageContentsOptionsDef
        ]
        redirect_url: Optional[UnifiedOneOfRedirectUrlOptionsDef]
        url_allowed_list: Optional[UrlAllowedList]
        url_blocked_list: Optional[UrlBlockedList]
        web_categories: Optional[UnifiedOneOfWebCategoriesOptionsDef]


    class Schema2HubGeneratedSecurityprofileparceltypePut3:
        """
        url-filtering profile parcel schema for put request
        """

        data: Data9
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class UnifiedOneOfFileReputationCloudServerOptionsDef:
        option_type: GlobalOptionTypeDef
        value: (
            UnifiedServerDef  # pytype: disable=annotation-type-mismatch
        )


    class UnifiedOneOfFileReputationEstServerOptionsDef:
        option_type: GlobalOptionTypeDef
        value: PolicyObjectUnifiedServerDef  # pytype: disable=annotation-type-mismatch


    class UnifiedOneOfFileReputationAlertOptionsDef:
        option_type: GlobalOptionTypeDef
        value: UnifiedAlertDef  # pytype: disable=annotation-type-mismatch


    class UnifiedOneOfFileAnalysisCloudServerOptionsDef:
        option_type: GlobalOptionTypeDef
        value: UnifiedFileAnalysisCloudServerDef  # pytype: disable=annotation-type-mismatch


    class UnifiedOneOfFileAnalysisFileTypesOptionsDef:
        option_type: GlobalOptionTypeDef
        value: List[str]


    class UnifiedOneOfFileAnalysisAlertOptionsDef:
        option_type: GlobalOptionTypeDef
        value: PolicyObjectUnifiedAlertDef  # pytype: disable=annotation-type-mismatch


    class Data10:
        file_analysis_enabled: OneOfFileAnalysisEnabledOptionsDef
        file_reputation_alert: UnifiedOneOfFileReputationAlertOptionsDef
        file_reputation_cloud_server: (
            UnifiedOneOfFileReputationCloudServerOptionsDef
        )
        file_reputation_est_server: (
            UnifiedOneOfFileReputationEstServerOptionsDef
        )
        match_all_vpn: OneOfMatchAllVpnOptionsDef
        file_analysis_alert: Optional[
            UnifiedOneOfFileAnalysisAlertOptionsDef
        ]
        file_analysis_cloud_server: Optional[
            UnifiedOneOfFileAnalysisCloudServerOptionsDef
        ]
        file_analysis_file_types: Optional[
            UnifiedOneOfFileAnalysisFileTypesOptionsDef
        ]


    class Schema2HubGeneratedSecurityprofileparceltypePut4:
        """
        advanced-malware-protection profile parcel schema for PUT request
        """

        data: Data10
        description: str
        name: str
        metadata: Optional[Any]


    class UnifiedOneOfDecryptCategoriesOptionsDef:
        option_type: GlobalOptionTypeDef
        value: List[
            CategoriesDef
        ]  # pytype: disable=annotation-type-mismatch


    class UnifiedOneOfNeverDecryptCategoriesOptionsDef:
        option_type: GlobalOptionTypeDef
        value: List[
            CategoriesDef
        ]  # pytype: disable=annotation-type-mismatch


    class UnifiedOneOfSkipDecryptCategoriesOptionsDef:
        option_type: GlobalOptionTypeDef
        value: List[
            CategoriesDef
        ]  # pytype: disable=annotation-type-mismatch


    class UnifiedOneOfDecryptThresholdOptionsDef:
        option_type: GlobalOptionTypeDef
        value: UnifiedThresholdDef  # pytype: disable=annotation-type-mismatch


    class UnifiedOneOfSkipDecryptThresholdOptionsDef:
        option_type: GlobalOptionTypeDef
        value: PolicyObjectUnifiedThresholdDef  # pytype: disable=annotation-type-mismatch


    class Data11_1:
        decrypt_categories: UnifiedOneOfDecryptCategoriesOptionsDef
        fail_decrypt: OneOfFailDecryptOptionsDef
        never_decrypt_categories: (
            UnifiedOneOfNeverDecryptCategoriesOptionsDef
        )
        reputation: OneOfReputationOptionsDef
        decrypt_threshold: Optional[
            UnifiedOneOfDecryptThresholdOptionsDef
        ]
        skip_decrypt_categories: Optional[
            UnifiedOneOfSkipDecryptCategoriesOptionsDef
        ]
        skip_decrypt_threshold: Optional[
            UnifiedOneOfSkipDecryptThresholdOptionsDef
        ]
        url_allowed_list: Optional[UrlAllowedList]
        url_blocked_list: Optional[UrlBlockedList]


    class Schema2HubGeneratedSecurityprofileparceltypePut5:
        """
        ssl-decryption-profile profile parcel schema for put request
        """

        data: Data11_1
        description: str
        name: str
        metadata: Optional[Any]


    class Data12:
        ca_cert_bundle: Optional[Any]


    class Schema2HubGeneratedSecurityprofileparceltypePut61:
        data: Data12
        # Will be auto generated
        description: str
        name: str
        metadata: Optional[Any]


    class UnifiedOneOfExpiredCertificateOptionsDef:
        option_type: GlobalOptionTypeDef
        value: UnifiedDecryptAndDropStringDef  # pytype: disable=annotation-type-mismatch


    class UnifiedOneOfUntrustedCertificateOptionsDef:
        option_type: GlobalOptionTypeDef
        value: PolicyObjectUnifiedDecryptAndDropStringDef  # pytype: disable=annotation-type-mismatch


    class UnifiedOneOfCertificateRevocationStatusOptionsDef:
        option_type: GlobalOptionTypeDef
        value: UnifiedCertificateRevocationStatusDef  # pytype: disable=annotation-type-mismatch


    class UnifiedOneOfUnknownStatusOptionsDef:
        option_type: GlobalOptionTypeDef
        value: SdwanPolicyObjectUnifiedDecryptAndDropStringDef  # pytype: disable=annotation-type-mismatch


    class UnifiedOneOfUnsupportedProtocolVersionsOptionsDef:
        option_type: GlobalOptionTypeDef
        value: UnifiedNoDecryptAndDropStringDef  # pytype: disable=annotation-type-mismatch


    class UnifiedOneOfUnsupportedCipherSuitesOptionsDef:
        option_type: GlobalOptionTypeDef
        value: PolicyObjectUnifiedNoDecryptAndDropStringDef  # pytype: disable=annotation-type-mismatch


    class UnifiedOneOfFailureModeOptionsDef:
        option_type: GlobalOptionTypeDef
        value: UnifiedFailureModeDef  # pytype: disable=annotation-type-mismatch


    class UnifiedDefaultDef:
        option_type: GlobalOptionTypeDef
        value: bool


    class UnifiedOneOfCaCertBundleOptionsDef1:
        default: UnifiedDefaultDef


    class PolicyObjectUnifiedDefaultDef:
        option_type: GlobalOptionTypeDef
        value: bool


    class UnifiedFileNameDef:
        option_type: GlobalOptionTypeDef
        value: str


    class UnifiedBundleStringDef:
        option_type: GlobalOptionTypeDef
        value: str


    class UnifiedOneOfCaCertBundleOptionsDef2:
        bundle_string: UnifiedBundleStringDef
        default: PolicyObjectUnifiedDefaultDef
        file_name: UnifiedFileNameDef


    class UnifiedOneOfKeyModulusOptionsDef:
        option_type: GlobalOptionTypeDef
        value: UnifiedKeyModulusDef  # pytype: disable=annotation-type-mismatch


    class UnifiedOneOfEckeyTypeOptionsDef:
        option_type: GlobalOptionTypeDef
        value: UnifiedEckeyTypeDef  # pytype: disable=annotation-type-mismatch


    class UnifiedOneOfCertificateLifetimeOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class UnifiedOneOfMinTlsVerOptionsDef:
        option_type: GlobalOptionTypeDef
        value: UnifiedMinTlsVerDef  # pytype: disable=annotation-type-mismatch


    class UnifiedOneOfCaTpLabelOptionsDef:
        option_type: GlobalOptionTypeDef
        value: UnifiedCaTpLabelDef  # pytype: disable=annotation-type-mismatch


    class Data13:
        ssl_enable: OneOfSslEnableOptionsDef
        ca_cert_bundle: Optional[
            Union[
                UnifiedOneOfCaCertBundleOptionsDef1,
                UnifiedOneOfCaCertBundleOptionsDef2,
            ]
        ]
        ca_tp_label: Optional[UnifiedOneOfCaTpLabelOptionsDef]
        certificate_lifetime: Optional[
            UnifiedOneOfCertificateLifetimeOptionsDef
        ]
        certificate_revocation_status: Optional[
            UnifiedOneOfCertificateRevocationStatusOptionsDef
        ]
        eckey_type: Optional[UnifiedOneOfEckeyTypeOptionsDef]
        expired_certificate: Optional[
            UnifiedOneOfExpiredCertificateOptionsDef
        ]
        failure_mode: Optional[UnifiedOneOfFailureModeOptionsDef]
        key_modulus: Optional[UnifiedOneOfKeyModulusOptionsDef]
        min_tls_ver: Optional[UnifiedOneOfMinTlsVerOptionsDef]
        unknown_status: Optional[UnifiedOneOfUnknownStatusOptionsDef]
        unsupported_cipher_suites: Optional[
            UnifiedOneOfUnsupportedCipherSuitesOptionsDef
        ]
        unsupported_protocol_versions: Optional[
            UnifiedOneOfUnsupportedProtocolVersionsOptionsDef
        ]
        untrusted_certificate: Optional[
            UnifiedOneOfUntrustedCertificateOptionsDef
        ]


    class Schema2HubGeneratedSecurityprofileparceltypePut62:
        data: Data13
        # Will be auto generated
        description: str
        name: str
        metadata: Optional[Any]


    class GetSingleSdwanPolicyObjectUnifiedAdvancedInspectionProfilePayload:
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
        payload: Optional[
            Union[
                Schema2HubGeneratedSecurityprofileparceltypePut1,
                Schema2HubGeneratedSecurityprofileparceltypePut2,
                Schema2HubGeneratedSecurityprofileparceltypePut3,
                Schema2HubGeneratedSecurityprofileparceltypePut4,
                Schema2HubGeneratedSecurityprofileparceltypePut5,
                Union[
                    Schema2HubGeneratedSecurityprofileparceltypePut61,
                    Schema2HubGeneratedSecurityprofileparceltypePut62,
                ],
            ]
        ]


    class EditSecurityProfileParcel1PutResponse:
        """
        Profile Parcel PUT Response schema
        """

        id: str
        metadata: Optional[Any]


    class FeatureProfileSdwanPolicyObjectUnifiedOneOfTlsDecryptionActionOptionsDef:
        option_type: GlobalOptionTypeDef
        value: FeatureProfileSdwanPolicyObjectUnifiedTlsDecryptionActionDef  # pytype: disable=annotation-type-mismatch


    class RefIdDef8:
        option_type: GlobalOptionTypeDef
        value: str


    class ReferenceDef8:
        ref_id: RefIdDef8


    class RefIdDef9:
        option_type: GlobalOptionTypeDef
        value: str


    class ReferenceDef9:
        ref_id: RefIdDef9


    class RefIdDef10:
        option_type: GlobalOptionTypeDef
        value: str


    class ReferenceDef10:
        ref_id: RefIdDef10


    class RefIdDef11:
        option_type: GlobalOptionTypeDef
        value: str


    class ReferenceDef11:
        ref_id: RefIdDef11


    class PolicyObjectUnifiedData1:
        intrusion_prevention: ReferenceDef8
        tls_decryption_action: FeatureProfileSdwanPolicyObjectUnifiedOneOfTlsDecryptionActionOptionsDef
        advanced_malware_protection: Optional[ReferenceDef10]
        ssl_decryption_profile: Optional[ReferenceDef11]
        url_filtering: Optional[ReferenceDef9]


    class V1FeatureProfileSdwanPolicyObjectUnifiedOneOfTlsDecryptionActionOptionsDef:
        option_type: GlobalOptionTypeDef
        value: V1FeatureProfileSdwanPolicyObjectUnifiedTlsDecryptionActionDef  # pytype: disable=annotation-type-mismatch


    class RefIdDef12:
        option_type: GlobalOptionTypeDef
        value: str


    class ReferenceDef12:
        ref_id: RefIdDef12


    class RefIdDef13:
        option_type: GlobalOptionTypeDef
        value: str


    class ReferenceDef13:
        ref_id: RefIdDef13


    class RefIdDef14:
        option_type: GlobalOptionTypeDef
        value: str


    class ReferenceDef14:
        ref_id: RefIdDef14


    class RefIdDef15:
        option_type: GlobalOptionTypeDef
        value: str


    class ReferenceDef15:
        ref_id: RefIdDef15


    class PolicyObjectUnifiedData2:
        tls_decryption_action: V1FeatureProfileSdwanPolicyObjectUnifiedOneOfTlsDecryptionActionOptionsDef
        url_filtering: ReferenceDef13
        advanced_malware_protection: Optional[ReferenceDef14]
        intrusion_prevention: Optional[ReferenceDef12]
        ssl_decryption_profile: Optional[ReferenceDef15]


    class OneOfTlsDecryptionActionOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: TlsDecryptionActionDef1  # pytype: disable=annotation-type-mismatch


    class RefIdDef16:
        option_type: GlobalOptionTypeDef
        value: str


    class ReferenceDef16:
        ref_id: RefIdDef16


    class RefIdDef17:
        option_type: GlobalOptionTypeDef
        value: str


    class ReferenceDef17:
        ref_id: RefIdDef17


    class RefIdDef18:
        option_type: GlobalOptionTypeDef
        value: str


    class ReferenceDef18:
        ref_id: RefIdDef18


    class RefIdDef19:
        option_type: GlobalOptionTypeDef
        value: str


    class ReferenceDef19:
        ref_id: RefIdDef19


    class PolicyObjectUnifiedData3:
        advanced_malware_protection: ReferenceDef18
        tls_decryption_action: OneOfTlsDecryptionActionOptionsDef1
        intrusion_prevention: Optional[ReferenceDef16]
        ssl_decryption_profile: Optional[ReferenceDef19]
        url_filtering: Optional[ReferenceDef17]


    class EditSecurityProfileParcel1PutRequest1:
        """
        advanced-malware-protection profile parcel schema for PUT request
        """

        # requires tlsDecryptionAction and at least one of Intrusion Prevention or URL Filtering or Advanced Malware Protection policies
        data: Union[
            PolicyObjectUnifiedData1,
            PolicyObjectUnifiedData2,
            PolicyObjectUnifiedData3,
        ]
        description: str
        name: str
        metadata: Optional[Any]


    class PolicyObjectUnifiedOneOfSignatureSetOptionsDef:
        option_type: GlobalOptionTypeDef
        value: PolicyObjectUnifiedSignatureSetDef


    class PolicyObjectUnifiedOneOfInspectionModeOptionsDef:
        option_type: GlobalOptionTypeDef
        value: PolicyObjectUnifiedInspectionModeDef


    class PolicyObjectUnifiedOneOfLogLevelOptionsDef:
        option_type: GlobalOptionTypeDef
        value: PolicyObjectUnifiedLogLevelDef


    class PolicyObjectUnifiedOneOfCustomSignatureOptionsDef:
        option_type: GlobalOptionTypeDef
        value: bool


    class Data14:
        inspection_mode: PolicyObjectUnifiedOneOfInspectionModeOptionsDef
        log_level: PolicyObjectUnifiedOneOfLogLevelOptionsDef
        signature_set: PolicyObjectUnifiedOneOfSignatureSetOptionsDef
        custom_signature: Optional[
            PolicyObjectUnifiedOneOfCustomSignatureOptionsDef
        ]
        # Valid UUID
        signature_allowed_list: Optional[SignatureAllowedList]


    class EditSecurityProfileParcel1PutRequest2:
        """
        Intrusion Prevention profile parcel schema for PUT request
        """

        data: Data14
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class PolicyObjectUnifiedOneOfWebCategoriesActionOptionsDef:
        option_type: GlobalOptionTypeDef
        value: PolicyObjectUnifiedWebCategoriesActionDef  # pytype: disable=annotation-type-mismatch


    class PolicyObjectUnifiedOneOfWebCategoriesOptionsDef:
        option_type: GlobalOptionTypeDef
        value: List[
            WebCategoriesDef
        ]  # pytype: disable=annotation-type-mismatch


    class PolicyObjectUnifiedOneOfWebReputationOptionsDef:
        option_type: GlobalOptionTypeDef
        value: PolicyObjectUnifiedWebReputationDef  # pytype: disable=annotation-type-mismatch


    class PolicyObjectUnifiedOneOfBlockPageActionOptionsDef:
        option_type: GlobalOptionTypeDef
        value: PolicyObjectUnifiedBlockPageActionDef  # pytype: disable=annotation-type-mismatch


    class PolicyObjectUnifiedOneOfBlockPageContentsOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class PolicyObjectUnifiedOneOfRedirectUrlOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class PolicyObjectUnifiedOneOfAlertsOptionsDef:
        option_type: GlobalOptionTypeDef
        value: List[AlertsDef]  # pytype: disable=annotation-type-mismatch


    class Data15:
        block_page_action: (
            PolicyObjectUnifiedOneOfBlockPageActionOptionsDef
        )
        enable_alerts: OneOfEnableAlertsOptionsDef
        web_categories_action: (
            PolicyObjectUnifiedOneOfWebCategoriesActionOptionsDef
        )
        web_reputation: PolicyObjectUnifiedOneOfWebReputationOptionsDef
        alerts: Optional[PolicyObjectUnifiedOneOfAlertsOptionsDef]
        block_page_contents: Optional[
            PolicyObjectUnifiedOneOfBlockPageContentsOptionsDef
        ]
        redirect_url: Optional[
            PolicyObjectUnifiedOneOfRedirectUrlOptionsDef
        ]
        url_allowed_list: Optional[UrlAllowedList]
        url_blocked_list: Optional[UrlBlockedList]
        web_categories: Optional[
            PolicyObjectUnifiedOneOfWebCategoriesOptionsDef
        ]


    class EditSecurityProfileParcel1PutRequest3:
        """
        url-filtering profile parcel schema for put request
        """

        data: Data15
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class PolicyObjectUnifiedOneOfFileReputationCloudServerOptionsDef:
        option_type: GlobalOptionTypeDef
        value: SdwanPolicyObjectUnifiedServerDef  # pytype: disable=annotation-type-mismatch


    class PolicyObjectUnifiedOneOfFileReputationEstServerOptionsDef:
        option_type: GlobalOptionTypeDef
        value: FeatureProfileSdwanPolicyObjectUnifiedServerDef  # pytype: disable=annotation-type-mismatch


    class PolicyObjectUnifiedOneOfFileReputationAlertOptionsDef:
        option_type: GlobalOptionTypeDef
        value: SdwanPolicyObjectUnifiedAlertDef  # pytype: disable=annotation-type-mismatch


    class PolicyObjectUnifiedOneOfFileAnalysisCloudServerOptionsDef:
        option_type: GlobalOptionTypeDef
        value: PolicyObjectUnifiedFileAnalysisCloudServerDef  # pytype: disable=annotation-type-mismatch


    class PolicyObjectUnifiedOneOfFileAnalysisFileTypesOptionsDef:
        option_type: GlobalOptionTypeDef
        value: List[str]


    class PolicyObjectUnifiedOneOfFileAnalysisAlertOptionsDef:
        option_type: GlobalOptionTypeDef
        value: FeatureProfileSdwanPolicyObjectUnifiedAlertDef  # pytype: disable=annotation-type-mismatch


    class Data16:
        file_analysis_enabled: OneOfFileAnalysisEnabledOptionsDef
        file_reputation_alert: (
            PolicyObjectUnifiedOneOfFileReputationAlertOptionsDef
        )
        file_reputation_cloud_server: (
            PolicyObjectUnifiedOneOfFileReputationCloudServerOptionsDef
        )
        file_reputation_est_server: (
            PolicyObjectUnifiedOneOfFileReputationEstServerOptionsDef
        )
        match_all_vpn: OneOfMatchAllVpnOptionsDef
        file_analysis_alert: Optional[
            PolicyObjectUnifiedOneOfFileAnalysisAlertOptionsDef
        ]
        file_analysis_cloud_server: Optional[
            PolicyObjectUnifiedOneOfFileAnalysisCloudServerOptionsDef
        ]
        file_analysis_file_types: Optional[
            PolicyObjectUnifiedOneOfFileAnalysisFileTypesOptionsDef
        ]


    class EditSecurityProfileParcel1PutRequest4:
        """
        advanced-malware-protection profile parcel schema for PUT request
        """

        data: Data16
        description: str
        name: str
        metadata: Optional[Any]


    class PolicyObjectUnifiedOneOfDecryptCategoriesOptionsDef:
        option_type: GlobalOptionTypeDef
        value: List[
            CategoriesDef
        ]  # pytype: disable=annotation-type-mismatch


    class PolicyObjectUnifiedOneOfNeverDecryptCategoriesOptionsDef:
        option_type: GlobalOptionTypeDef
        value: List[
            CategoriesDef
        ]  # pytype: disable=annotation-type-mismatch


    class PolicyObjectUnifiedOneOfSkipDecryptCategoriesOptionsDef:
        option_type: GlobalOptionTypeDef
        value: List[
            CategoriesDef
        ]  # pytype: disable=annotation-type-mismatch


    class PolicyObjectUnifiedOneOfDecryptThresholdOptionsDef:
        option_type: GlobalOptionTypeDef
        value: SdwanPolicyObjectUnifiedThresholdDef  # pytype: disable=annotation-type-mismatch


    class PolicyObjectUnifiedOneOfSkipDecryptThresholdOptionsDef:
        option_type: GlobalOptionTypeDef
        value: FeatureProfileSdwanPolicyObjectUnifiedThresholdDef  # pytype: disable=annotation-type-mismatch


    class Data17:
        decrypt_categories: (
            PolicyObjectUnifiedOneOfDecryptCategoriesOptionsDef
        )
        fail_decrypt: OneOfFailDecryptOptionsDef
        never_decrypt_categories: (
            PolicyObjectUnifiedOneOfNeverDecryptCategoriesOptionsDef
        )
        reputation: OneOfReputationOptionsDef
        decrypt_threshold: Optional[
            PolicyObjectUnifiedOneOfDecryptThresholdOptionsDef
        ]
        skip_decrypt_categories: Optional[
            PolicyObjectUnifiedOneOfSkipDecryptCategoriesOptionsDef
        ]
        skip_decrypt_threshold: Optional[
            PolicyObjectUnifiedOneOfSkipDecryptThresholdOptionsDef
        ]
        url_allowed_list: Optional[UrlAllowedList]
        url_blocked_list: Optional[UrlBlockedList]


    class EditSecurityProfileParcel1PutRequest5:
        """
        ssl-decryption-profile profile parcel schema for put request
        """

        data: Data17
        description: str
        name: str
        metadata: Optional[Any]


    class Data18:
        ca_cert_bundle: Optional[Any]


    class EditSecurityProfileParcel1PutRequest61:
        data: Data18
        # Will be auto generated
        description: str
        name: str
        metadata: Optional[Any]


    class PolicyObjectUnifiedOneOfExpiredCertificateOptionsDef:
        option_type: GlobalOptionTypeDef
        value: FeatureProfileSdwanPolicyObjectUnifiedDecryptAndDropStringDef  # pytype: disable=annotation-type-mismatch


    class PolicyObjectUnifiedOneOfUntrustedCertificateOptionsDef:
        option_type: GlobalOptionTypeDef
        value: V1FeatureProfileSdwanPolicyObjectUnifiedDecryptAndDropStringDef  # pytype: disable=annotation-type-mismatch


    class PolicyObjectUnifiedOneOfCertificateRevocationStatusOptionsDef:
        option_type: GlobalOptionTypeDef
        value: PolicyObjectUnifiedCertificateRevocationStatusDef  # pytype: disable=annotation-type-mismatch


    class PolicyObjectUnifiedOneOfUnknownStatusOptionsDef:
        option_type: GlobalOptionTypeDef
        value: DecryptAndDropStringDef1  # pytype: disable=annotation-type-mismatch


    class PolicyObjectUnifiedOneOfUnsupportedProtocolVersionsOptionsDef:
        option_type: GlobalOptionTypeDef
        value: SdwanPolicyObjectUnifiedNoDecryptAndDropStringDef  # pytype: disable=annotation-type-mismatch


    class PolicyObjectUnifiedOneOfUnsupportedCipherSuitesOptionsDef:
        option_type: GlobalOptionTypeDef
        value: FeatureProfileSdwanPolicyObjectUnifiedNoDecryptAndDropStringDef  # pytype: disable=annotation-type-mismatch


    class PolicyObjectUnifiedOneOfFailureModeOptionsDef:
        option_type: GlobalOptionTypeDef
        value: PolicyObjectUnifiedFailureModeDef  # pytype: disable=annotation-type-mismatch


    class SdwanPolicyObjectUnifiedDefaultDef:
        option_type: GlobalOptionTypeDef
        value: bool


    class PolicyObjectUnifiedOneOfCaCertBundleOptionsDef1:
        default: SdwanPolicyObjectUnifiedDefaultDef


    class FeatureProfileSdwanPolicyObjectUnifiedDefaultDef:
        option_type: GlobalOptionTypeDef
        value: bool


    class PolicyObjectUnifiedFileNameDef:
        option_type: GlobalOptionTypeDef
        value: str


    class PolicyObjectUnifiedBundleStringDef:
        option_type: GlobalOptionTypeDef
        value: str


    class PolicyObjectUnifiedOneOfCaCertBundleOptionsDef2:
        bundle_string: PolicyObjectUnifiedBundleStringDef
        default: FeatureProfileSdwanPolicyObjectUnifiedDefaultDef
        file_name: PolicyObjectUnifiedFileNameDef


    class PolicyObjectUnifiedOneOfKeyModulusOptionsDef:
        option_type: GlobalOptionTypeDef
        value: PolicyObjectUnifiedKeyModulusDef  # pytype: disable=annotation-type-mismatch


    class PolicyObjectUnifiedOneOfEckeyTypeOptionsDef:
        option_type: GlobalOptionTypeDef
        value: PolicyObjectUnifiedEckeyTypeDef  # pytype: disable=annotation-type-mismatch


    class PolicyObjectUnifiedOneOfCertificateLifetimeOptionsDef:
        option_type: GlobalOptionTypeDef
        value: str


    class PolicyObjectUnifiedOneOfMinTlsVerOptionsDef:
        option_type: GlobalOptionTypeDef
        value: PolicyObjectUnifiedMinTlsVerDef  # pytype: disable=annotation-type-mismatch


    class PolicyObjectUnifiedOneOfCaTpLabelOptionsDef:
        option_type: GlobalOptionTypeDef
        value: PolicyObjectUnifiedCaTpLabelDef  # pytype: disable=annotation-type-mismatch


    class Data19:
        ssl_enable: OneOfSslEnableOptionsDef
        ca_cert_bundle: Optional[
            Union[
                PolicyObjectUnifiedOneOfCaCertBundleOptionsDef1,
                PolicyObjectUnifiedOneOfCaCertBundleOptionsDef2,
            ]
        ]
        ca_tp_label: Optional[PolicyObjectUnifiedOneOfCaTpLabelOptionsDef]
        certificate_lifetime: Optional[
            PolicyObjectUnifiedOneOfCertificateLifetimeOptionsDef
        ]
        certificate_revocation_status: Optional[
            PolicyObjectUnifiedOneOfCertificateRevocationStatusOptionsDef
        ]
        eckey_type: Optional[PolicyObjectUnifiedOneOfEckeyTypeOptionsDef]
        expired_certificate: Optional[
            PolicyObjectUnifiedOneOfExpiredCertificateOptionsDef
        ]
        failure_mode: Optional[
            PolicyObjectUnifiedOneOfFailureModeOptionsDef
        ]
        key_modulus: Optional[
            PolicyObjectUnifiedOneOfKeyModulusOptionsDef
        ]
        min_tls_ver: Optional[PolicyObjectUnifiedOneOfMinTlsVerOptionsDef]
        unknown_status: Optional[
            PolicyObjectUnifiedOneOfUnknownStatusOptionsDef
        ]
        unsupported_cipher_suites: Optional[
            PolicyObjectUnifiedOneOfUnsupportedCipherSuitesOptionsDef
        ]
        unsupported_protocol_versions: Optional[
            PolicyObjectUnifiedOneOfUnsupportedProtocolVersionsOptionsDef
        ]
        untrusted_certificate: Optional[
            PolicyObjectUnifiedOneOfUntrustedCertificateOptionsDef
        ]


    class EditSecurityProfileParcel1PutRequest62:
        data: Data19
        # Will be auto generated
        description: str
        name: str
        metadata: Optional[Any]


