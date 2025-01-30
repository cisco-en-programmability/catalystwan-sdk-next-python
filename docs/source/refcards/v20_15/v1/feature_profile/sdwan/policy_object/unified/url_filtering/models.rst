======
Models
======


.. code:: python

    from typing import Literal, Any, Union, Dict, Optional, List

    GlobalOptionTypeDef = Literal["global"]

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


    class CreateSecurityProfileParcelPostResponse:
        parcel_id: Optional[str]


    class CreateSecurityProfileParcelPostRequest11:
        data: Any
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


    class RefIdOptionDef:
        option_type: GlobalOptionTypeDef
        value: str


    class UrlAllowedList:
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


    class Data:
        block_page_action: OneOfBlockPageActionOptionsDef
        enable_alerts: OneOfEnableAlertsOptionsDef
        web_categories_action: OneOfWebCategoriesActionOptionsDef
        web_reputation: OneOfWebReputationOptionsDef
        alerts: Optional[OneOfAlertsOptionsDef]
        block_page_contents: Optional[OneOfBlockPageContentsOptionsDef]
        redirect_url: Optional[OneOfRedirectUrlOptionsDef]
        url_allowed_list: Optional[UrlAllowedList]
        url_blocked_list: Optional[UrlAllowedList]
        web_categories: Optional[OneOfWebCategoriesOptionsDef]


    class CreateSecurityProfileParcelPostRequest12:
        data: Data
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class CreateSecurityProfileParcelPostRequest21:
        data: Any
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class CreateSecurityProfileParcelPostRequest31:
        data: Any
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class CreateSecurityProfileParcelPostRequest41:
        data: Any
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class CreateSecurityProfileParcelPostRequest61:
        data: Any
        name: str
        description: Optional[str]
        metadata: Optional[Any]


    class GetSecurityProfileParcelGetResponse:
        created_by: Optional[str]
        created_on: Optional[int]
        last_updated_by: Optional[str]
        last_updated_on: Optional[int]
        parcel_id: Optional[str]
        parcel_type: Optional[str]
        # url-filtering profile parcel schema for POST request
        payload: Optional[
            Union[
                Union[
                    CreateSecurityProfileParcelPostRequest11,
                    CreateSecurityProfileParcelPostRequest12,
                ],
                Union[
                    CreateSecurityProfileParcelPostRequest21,
                    CreateSecurityProfileParcelPostRequest12,
                ],
                Union[
                    CreateSecurityProfileParcelPostRequest31,
                    CreateSecurityProfileParcelPostRequest12,
                ],
                Union[
                    CreateSecurityProfileParcelPostRequest41,
                    CreateSecurityProfileParcelPostRequest12,
                ],
                Union[
                    CreateSecurityProfileParcelPostRequest31,
                    CreateSecurityProfileParcelPostRequest12,
                ],
                Union[
                    CreateSecurityProfileParcelPostRequest61,
                    CreateSecurityProfileParcelPostRequest12,
                ],
                Union[
                    CreateSecurityProfileParcelPostRequest31,
                    CreateSecurityProfileParcelPostRequest12,
                ],
            ]
        ]


