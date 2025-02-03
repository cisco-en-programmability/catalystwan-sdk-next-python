======
Models
======


.. code:: python

    from typing import List, Any, Optional, Literal, Dict, Union

    GlobalOptionTypeDef = Literal["global"]

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


    class CreateSecurityProfileParcelPostResponse:
        parcel_id: Optional[str]


    class OneOfDecryptCategoriesOptionsDef:
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


    class RefIdOptionDef:
        option_type: GlobalOptionTypeDef
        value: str


    class UrlAllowedList:
        ref_id: Optional[RefIdOptionDef]


    class Data:
        decrypt_categories: OneOfDecryptCategoriesOptionsDef
        fail_decrypt: OneOfReputationOptionsDef
        never_decrypt_categories: OneOfDecryptCategoriesOptionsDef
        reputation: OneOfReputationOptionsDef
        decrypt_threshold: Optional[OneOfDecryptThresholdOptionsDef]
        skip_decrypt_categories: Optional[
            OneOfDecryptCategoriesOptionsDef
        ]
        skip_decrypt_threshold: Optional[OneOfDecryptThresholdOptionsDef]
        url_allowed_list: Optional[UrlAllowedList]
        url_blocked_list: Optional[UrlAllowedList]


    class CreateSecurityProfileParcelPostRequest:
        """
        ssl-decryption-profile profile parcel schema for POST request
        """

        data: Data
        description: str
        name: str
        # This is the documentation for POST request schema for ssl-decryption-profile profile parcel
        documentation: Optional[Any]
        metadata: Optional[Any]


    class GetSecurityProfileParcelGetResponse:
        created_by: Optional[str]
        created_on: Optional[int]
        last_updated_by: Optional[str]
        last_updated_on: Optional[int]
        parcel_id: Optional[str]
        parcel_type: Optional[str]
        # ssl-decryption-profile profile parcel schema for POST request
        payload: Optional[CreateSecurityProfileParcelPostRequest]


