======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    VariableOptionTypeDef = Literal["variable"]

    GlobalOptionTypeDef = Literal["global"]

    TimezoneDef = Literal[
        "Africa/Abidjan",
        "Africa/Accra",
        "Africa/Addis_Ababa",
        "Africa/Algiers",
        "Africa/Asmara",
        "Africa/Bamako",
        "Africa/Bangui",
        "Africa/Banjul",
        "Africa/Bissau",
        "Africa/Blantyre",
        "Africa/Brazzaville",
        "Africa/Bujumbura",
        "Africa/Cairo",
        "Africa/Casablanca",
        "Africa/Ceuta",
        "Africa/Conakry",
        "Africa/Dakar",
        "Africa/Dar_es_Salaam",
        "Africa/Djibouti",
        "Africa/Douala",
        "Africa/El_Aaiun",
        "Africa/Freetown",
        "Africa/Gaborone",
        "Africa/Harare",
        "Africa/Johannesburg",
        "Africa/Juba",
        "Africa/Kampala",
        "Africa/Khartoum",
        "Africa/Kigali",
        "Africa/Kinshasa",
        "Africa/Lagos",
        "Africa/Libreville",
        "Africa/Lome",
        "Africa/Luanda",
        "Africa/Lubumbashi",
        "Africa/Lusaka",
        "Africa/Malabo",
        "Africa/Maputo",
        "Africa/Maseru",
        "Africa/Mbabane",
        "Africa/Mogadishu",
        "Africa/Monrovia",
        "Africa/Nairobi",
        "Africa/Ndjamena",
        "Africa/Niamey",
        "Africa/Nouakchott",
        "Africa/Ouagadougou",
        "Africa/Porto-Novo",
        "Africa/Sao_Tome",
        "Africa/Tripoli",
        "Africa/Tunis",
        "Africa/Windhoek",
        "America/Adak",
        "America/Anchorage",
        "America/Anguilla",
        "America/Antigua",
        "America/Araguaina",
        "America/Argentina/Buenos_Aires",
        "America/Argentina/Catamarca",
        "America/Argentina/Cordoba",
        "America/Argentina/Jujuy",
        "America/Argentina/La_Rioja",
        "America/Argentina/Mendoza",
        "America/Argentina/Rio_Gallegos",
        "America/Argentina/Salta",
        "America/Argentina/San_Juan",
        "America/Argentina/San_Luis",
        "America/Argentina/Tucuman",
        "America/Argentina/Ushuaia",
        "America/Aruba",
        "America/Asuncion",
        "America/Atikokan",
        "America/Bahia",
        "America/Bahia_Banderas",
        "America/Barbados",
        "America/Belem",
        "America/Belize",
        "America/Blanc-Sablon",
        "America/Boa_Vista",
        "America/Bogota",
        "America/Boise",
        "America/Cambridge_Bay",
        "America/Campo_Grande",
        "America/Cancun",
        "America/Caracas",
        "America/Cayenne",
        "America/Cayman",
        "America/Chicago",
        "America/Chihuahua",
        "America/Costa_Rica",
        "America/Creston",
        "America/Cuiaba",
        "America/Curacao",
        "America/Danmarkshavn",
        "America/Dawson",
        "America/Dawson_Creek",
        "America/Denver",
        "America/Detroit",
        "America/Dominica",
        "America/Edmonton",
        "America/Eirunepe",
        "America/El_Salvador",
        "America/Fortaleza",
        "America/Glace_Bay",
        "America/Godthab",
        "America/Goose_Bay",
        "America/Grand_Turk",
        "America/Grenada",
        "America/Guadeloupe",
        "America/Guatemala",
        "America/Guayaquil",
        "America/Guyana",
        "America/Halifax",
        "America/Havana",
        "America/Hermosillo",
        "America/Indiana/Indianapolis",
        "America/Indiana/Knox",
        "America/Indiana/Marengo",
        "America/Indiana/Petersburg",
        "America/Indiana/Tell_City",
        "America/Indiana/Vevay",
        "America/Indiana/Vincennes",
        "America/Indiana/Winamac",
        "America/Inuvik",
        "America/Iqaluit",
        "America/Jamaica",
        "America/Juneau",
        "America/Kentucky/Louisville",
        "America/Kentucky/Monticello",
        "America/Kralendijk",
        "America/La_Paz",
        "America/Lima",
        "America/Los_Angeles",
        "America/Lower_Princes",
        "America/Maceio",
        "America/Managua",
        "America/Manaus",
        "America/Marigot",
        "America/Martinique",
        "America/Matamoros",
        "America/Mazatlan",
        "America/Menominee",
        "America/Merida",
        "America/Metlakatla",
        "America/Mexico_City",
        "America/Miquelon",
        "America/Moncton",
        "America/Monterrey",
        "America/Montevideo",
        "America/Montserrat",
        "America/Nassau",
        "America/New_York",
        "America/Nipigon",
        "America/Nome",
        "America/Noronha",
        "America/North_Dakota/Beulah",
        "America/North_Dakota/Center",
        "America/North_Dakota/New_Salem",
        "America/Ojinaga",
        "America/Panama",
        "America/Pangnirtung",
        "America/Paramaribo",
        "America/Phoenix",
        "America/Port-au-Prince",
        "America/Port_of_Spain",
        "America/Porto_Velho",
        "America/Puerto_Rico",
        "America/Rainy_River",
        "America/Rankin_Inlet",
        "America/Recife",
        "America/Regina",
        "America/Resolute",
        "America/Rio_Branco",
        "America/Santa_Isabel",
        "America/Santarem",
        "America/Santiago",
        "America/Santo_Domingo",
        "America/Sao_Paulo",
        "America/Scoresbysund",
        "America/Sitka",
        "America/St_Barthelemy",
        "America/St_Johns",
        "America/St_Kitts",
        "America/St_Lucia",
        "America/St_Thomas",
        "America/St_Vincent",
        "America/Swift_Current",
        "America/Tegucigalpa",
        "America/Thule",
        "America/Thunder_Bay",
        "America/Tijuana",
        "America/Toronto",
        "America/Tortola",
        "America/Vancouver",
        "America/Whitehorse",
        "America/Winnipeg",
        "America/Yakutat",
        "America/Yellowknife",
        "Antarctica/Casey",
        "Antarctica/Davis",
        "Antarctica/DumontDUrville",
        "Antarctica/Macquarie",
        "Antarctica/Mawson",
        "Antarctica/McMurdo",
        "Antarctica/Palmer",
        "Antarctica/Rothera",
        "Antarctica/Syowa",
        "Antarctica/Vostok",
        "Arctic/Longyearbyen",
        "Asia/Aden",
        "Asia/Almaty",
        "Asia/Amman",
        "Asia/Anadyr",
        "Asia/Aqtau",
        "Asia/Aqtobe",
        "Asia/Ashgabat",
        "Asia/Baghdad",
        "Asia/Bahrain",
        "Asia/Baku",
        "Asia/Bangkok",
        "Asia/Beirut",
        "Asia/Bishkek",
        "Asia/Brunei",
        "Asia/Choibalsan",
        "Asia/Chongqing",
        "Asia/Colombo",
        "Asia/Damascus",
        "Asia/Dhaka",
        "Asia/Dili",
        "Asia/Dubai",
        "Asia/Dushanbe",
        "Asia/Gaza",
        "Asia/Harbin",
        "Asia/Hebron",
        "Asia/Ho_Chi_Minh",
        "Asia/Hong_Kong",
        "Asia/Hovd",
        "Asia/Irkutsk",
        "Asia/Jakarta",
        "Asia/Jayapura",
        "Asia/Jerusalem",
        "Asia/Kabul",
        "Asia/Kamchatka",
        "Asia/Karachi",
        "Asia/Kashgar",
        "Asia/Kathmandu",
        "Asia/Khandyga",
        "Asia/Kolkata",
        "Asia/Krasnoyarsk",
        "Asia/Kuala_Lumpur",
        "Asia/Kuching",
        "Asia/Kuwait",
        "Asia/Macau",
        "Asia/Magadan",
        "Asia/Makassar",
        "Asia/Manila",
        "Asia/Muscat",
        "Asia/Nicosia",
        "Asia/Novokuznetsk",
        "Asia/Novosibirsk",
        "Asia/Omsk",
        "Asia/Oral",
        "Asia/Phnom_Penh",
        "Asia/Pontianak",
        "Asia/Pyongyang",
        "Asia/Qatar",
        "Asia/Qyzylorda",
        "Asia/Rangoon",
        "Asia/Riyadh",
        "Asia/Sakhalin",
        "Asia/Samarkand",
        "Asia/Seoul",
        "Asia/Shanghai",
        "Asia/Singapore",
        "Asia/Taipei",
        "Asia/Tashkent",
        "Asia/Tbilisi",
        "Asia/Tehran",
        "Asia/Thimphu",
        "Asia/Tokyo",
        "Asia/Ulaanbaatar",
        "Asia/Urumqi",
        "Asia/Ust-Nera",
        "Asia/Vientiane",
        "Asia/Vladivostok",
        "Asia/Yakutsk",
        "Asia/Yekaterinburg",
        "Asia/Yerevan",
        "Atlantic/Azores",
        "Atlantic/Bermuda",
        "Atlantic/Canary",
        "Atlantic/Cape_Verde",
        "Atlantic/Faroe",
        "Atlantic/Madeira",
        "Atlantic/Reykjavik",
        "Atlantic/South_Georgia",
        "Atlantic/St_Helena",
        "Atlantic/Stanley",
        "Australia/Adelaide",
        "Australia/Brisbane",
        "Australia/Broken_Hill",
        "Australia/Currie",
        "Australia/Darwin",
        "Australia/Eucla",
        "Australia/Hobart",
        "Australia/Lindeman",
        "Australia/Lord_Howe",
        "Australia/Melbourne",
        "Australia/Perth",
        "Australia/Sydney",
        "Europe/Amsterdam",
        "Europe/Andorra",
        "Europe/Athens",
        "Europe/Belgrade",
        "Europe/Berlin",
        "Europe/Bratislava",
        "Europe/Brussels",
        "Europe/Bucharest",
        "Europe/Budapest",
        "Europe/Busingen",
        "Europe/Chisinau",
        "Europe/Copenhagen",
        "Europe/Dublin",
        "Europe/Gibraltar",
        "Europe/Guernsey",
        "Europe/Helsinki",
        "Europe/Isle_of_Man",
        "Europe/Istanbul",
        "Europe/Jersey",
        "Europe/Kaliningrad",
        "Europe/Kiev",
        "Europe/Lisbon",
        "Europe/Ljubljana",
        "Europe/London",
        "Europe/Luxembourg",
        "Europe/Madrid",
        "Europe/Malta",
        "Europe/Mariehamn",
        "Europe/Minsk",
        "Europe/Monaco",
        "Europe/Moscow",
        "Europe/Oslo",
        "Europe/Paris",
        "Europe/Podgorica",
        "Europe/Prague",
        "Europe/Riga",
        "Europe/Rome",
        "Europe/Samara",
        "Europe/San_Marino",
        "Europe/Sarajevo",
        "Europe/Simferopol",
        "Europe/Skopje",
        "Europe/Sofia",
        "Europe/Stockholm",
        "Europe/Tallinn",
        "Europe/Tirane",
        "Europe/Uzhgorod",
        "Europe/Vaduz",
        "Europe/Vatican",
        "Europe/Vienna",
        "Europe/Vilnius",
        "Europe/Volgograd",
        "Europe/Warsaw",
        "Europe/Zagreb",
        "Europe/Zaporozhye",
        "Europe/Zurich",
        "Indian/Antananarivo",
        "Indian/Chagos",
        "Indian/Christmas",
        "Indian/Cocos",
        "Indian/Comoro",
        "Indian/Kerguelen",
        "Indian/Mahe",
        "Indian/Maldives",
        "Indian/Mauritius",
        "Indian/Mayotte",
        "Indian/Reunion",
        "Pacific/Apia",
        "Pacific/Auckland",
        "Pacific/Chatham",
        "Pacific/Chuuk",
        "Pacific/Easter",
        "Pacific/Efate",
        "Pacific/Enderbury",
        "Pacific/Fakaofo",
        "Pacific/Fiji",
        "Pacific/Funafuti",
        "Pacific/Galapagos",
        "Pacific/Gambier",
        "Pacific/Guadalcanal",
        "Pacific/Guam",
        "Pacific/Honolulu",
        "Pacific/Johnston",
        "Pacific/Kiritimati",
        "Pacific/Kosrae",
        "Pacific/Kwajalein",
        "Pacific/Majuro",
        "Pacific/Marquesas",
        "Pacific/Midway",
        "Pacific/Nauru",
        "Pacific/Niue",
        "Pacific/Norfolk",
        "Pacific/Noumea",
        "Pacific/Pago_Pago",
        "Pacific/Palau",
        "Pacific/Pitcairn",
        "Pacific/Pohnpei",
        "Pacific/Port_Moresby",
        "Pacific/Rarotonga",
        "Pacific/Saipan",
        "Pacific/Tahiti",
        "Pacific/Tarawa",
        "Pacific/Tongatapu",
        "Pacific/Wake",
        "Pacific/Wallis",
        "UTC",
    ]

    DefaultOptionTypeDef = Literal["default"]

    UtcTimezoneDef = Literal["UTC"]

    BooleanFalseDef = Literal[False]

    BooleanTrueDef = Literal[True]

    ConsoleBaudRateDef = Literal[
        "115200",
        "1200",
        "19200",
        "2400",
        "38400",
        "4800",
        "57600",
        "9600",
    ]

    Value = Literal["9600"]

    EpfrDef = Literal[
        "aggressive", "conservative", "disabled", "moderate"
    ]

    BasicValue = Literal["disabled"]

    SiteTypeListDef = Literal[
        "br", "branch", "cloud", "spoke", "type-1", "type-2", "type-3"
    ]

    BasicConsoleBaudRateDef = Literal[
        "115200",
        "1200",
        "19200",
        "2400",
        "38400",
        "4800",
        "57600",
        "9600",
    ]

    BasicEpfrDef = Literal[
        "aggressive", "conservative", "disabled", "moderate"
    ]

    BasicSiteTypeListDef = Literal[
        "br", "branch", "cloud", "spoke", "type-1", "type-2", "type-3"
    ]

    SystemBasicConsoleBaudRateDef = Literal[
        "115200",
        "1200",
        "19200",
        "2400",
        "38400",
        "4800",
        "57600",
        "9600",
    ]

    SystemBasicEpfrDef = Literal[
        "aggressive", "conservative", "disabled", "moderate"
    ]

    SystemBasicSiteTypeListDef = Literal[
        "br", "branch", "cloud", "spoke", "type-1", "type-2", "type-3"
    ]


    class OneOfTimezoneOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfTimezoneOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: TimezoneDef  # pytype: disable=annotation-type-mismatch


    class OneOfTimezoneOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: UtcTimezoneDef  # pytype: disable=annotation-type-mismatch


    class Clock:
        timezone: Union[
            OneOfTimezoneOptionsDef1,
            OneOfTimezoneOptionsDef2,
            OneOfTimezoneOptionsDef3,
        ]


    class OneOfDescriptionOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfDescriptionOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfDescriptionOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfLocationOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfLocationOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfLocationOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfLongitudeOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfLongitudeOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfLongitudeOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfLatitudeOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfLatitudeOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfLatitudeOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfEnableOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfEnableOptionsDef2:
        option_type: DefaultOptionTypeDef
        value: BooleanFalseDef  # pytype: disable=annotation-type-mismatch


    class OneOfRangeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfRangeOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfRangeOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class OneOfMobileNumberNumberOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class OneOfMobileNumberNumberOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class MobileNumber:
        number: Union[
            OneOfMobileNumberNumberOptionsDef1,
            OneOfMobileNumberNumberOptionsDef2,
        ]


    class Sms:
        enable: Optional[
            Union[OneOfEnableOptionsDef1, OneOfEnableOptionsDef2]
        ]
        # Set device’s geo fencing SMS phone number
        mobile_number: Optional[List[MobileNumber]]


    class GeoFencing:
        enable: Optional[
            Union[OneOfEnableOptionsDef1, OneOfEnableOptionsDef2]
        ]
        range: Optional[
            Union[
                OneOfRangeOptionsDef1,
                OneOfRangeOptionsDef2,
                OneOfRangeOptionsDef3,
            ]
        ]
        sms: Optional[Sms]


    class GpsLocation:
        latitude: Union[
            OneOfLatitudeOptionsDef1,
            OneOfLatitudeOptionsDef2,
            OneOfLatitudeOptionsDef3,
        ]
        longitude: Union[
            OneOfLongitudeOptionsDef1,
            OneOfLongitudeOptionsDef2,
            OneOfLongitudeOptionsDef3,
        ]
        geo_fencing: Optional[GeoFencing]


    class OneOfDeviceGroupsOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfDeviceGroupsOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: List[str]


    class OneOfDeviceGroupsOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfControllerGroupListOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfControllerGroupListOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: List[int]


    class OneOfControllerGroupListOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfOverlayIdOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfOverlayIdOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfOverlayIdOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class OneOfPortOffsetOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfPortOffsetOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfPortOffsetOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class OneOfPortHopOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfPortHopOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfPortHopOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: BooleanTrueDef  # pytype: disable=annotation-type-mismatch


    class OneOfControlSessionPpsOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfControlSessionPpsOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfControlSessionPpsOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class OneOfTrackTransportOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfTrackTransportOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfTrackTransportOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: BooleanTrueDef  # pytype: disable=annotation-type-mismatch


    class OneOfTrackInterfaceTagOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfTrackInterfaceTagOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfTrackInterfaceTagOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfConsoleBaudRateOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfConsoleBaudRateOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: ConsoleBaudRateDef


    class OneOfConsoleBaudRateOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: Value  # pytype: disable=annotation-type-mismatch


    class OneOfMaxOmpSessionsOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfMaxOmpSessionsOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfMaxOmpSessionsOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfMultiTenantOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfMultiTenantOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfMultiTenantOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: BooleanFalseDef  # pytype: disable=annotation-type-mismatch


    class OneOfTrackDefaultGatewayOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfTrackDefaultGatewayOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfTrackDefaultGatewayOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: BooleanTrueDef  # pytype: disable=annotation-type-mismatch


    class OneOfTrackerDiaStabilizeStatusDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfTrackerDiaStabilizeStatusDef2:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfTrackerDiaStabilizeStatusDef3:
        option_type: DefaultOptionTypeDef
        value: BooleanFalseDef  # pytype: disable=annotation-type-mismatch


    class OneOfAdminTechOnFailureOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfAdminTechOnFailureOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfAdminTechOnFailureOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: BooleanTrueDef  # pytype: disable=annotation-type-mismatch


    class OneOfIdleTimeoutOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfIdleTimeoutOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfIdleTimeoutOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfOnDemandEnableOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfOnDemandEnableOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfOnDemandEnableOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: BooleanFalseDef  # pytype: disable=annotation-type-mismatch


    class OneOfOnDemandIdleTimeoutOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfOnDemandIdleTimeoutOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfOnDemandIdleTimeoutOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class OnDemand:
        on_demand_enable: Union[
            OneOfOnDemandEnableOptionsDef1,
            OneOfOnDemandEnableOptionsDef2,
            OneOfOnDemandEnableOptionsDef3,
        ]
        on_demand_idle_timeout: Union[
            OneOfOnDemandIdleTimeoutOptionsDef1,
            OneOfOnDemandIdleTimeoutOptionsDef2,
            OneOfOnDemandIdleTimeoutOptionsDef3,
        ]


    class OneOfTransportGatewayOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfTransportGatewayOptionsDef2:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfTransportGatewayOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: BooleanFalseDef  # pytype: disable=annotation-type-mismatch


    class OneOfEpfrOptions1:
        option_type: GlobalOptionTypeDef
        value: EpfrDef


    class OneOfEpfrOptions2:
        option_type: DefaultOptionTypeDef
        value: BasicValue  # pytype: disable=annotation-type-mismatch


    class OneOfEpfrOptions3:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfSiteTypeOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfSiteTypeOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: List[
            SiteTypeListDef
        ]  # pytype: disable=annotation-type-mismatch


    class OneOfSiteTypeOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfAffinityGroupNumberOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfAffinityGroupNumberOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class OneOfAffinityGroupNumberOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfAffinityGroupPreferenceOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfAffinityGroupPreferenceOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: List[int]


    class OneOfAffinityGroupPreferenceOptionsDef3:
        option_type: DefaultOptionTypeDef


    class OneOfAffinityPreferenceAutoOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfAffinityPreferenceAutoOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: bool


    class OneOfAffinityPreferenceAutoOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: BooleanFalseDef  # pytype: disable=annotation-type-mismatch


    class OneOfVrfRangeOptionsDef1:
        option_type: VariableOptionTypeDef
        value: str
        default: Optional[str]
        description: Optional[str]


    class OneOfVrfRangeOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: Any


    class OneOfVrfRangeOptionsDef3:
        option_type: DefaultOptionTypeDef


    class AffinityPerVrf:
        affinity_group_number: Optional[
            Union[
                OneOfAffinityGroupNumberOptionsDef1,
                OneOfAffinityGroupNumberOptionsDef2,
                OneOfAffinityGroupNumberOptionsDef3,
            ]
        ]
        vrf_range: Optional[
            Union[
                OneOfVrfRangeOptionsDef1,
                OneOfVrfRangeOptionsDef2,
                OneOfVrfRangeOptionsDef3,
            ]
        ]


    class BasicData:
        admin_tech_on_failure: Union[
            OneOfAdminTechOnFailureOptionsDef1,
            OneOfAdminTechOnFailureOptionsDef2,
            OneOfAdminTechOnFailureOptionsDef3,
        ]
        clock: Clock
        console_baud_rate: Union[
            OneOfConsoleBaudRateOptionsDef1,
            OneOfConsoleBaudRateOptionsDef2,
            OneOfConsoleBaudRateOptionsDef3,
        ]
        description: Union[
            OneOfDescriptionOptionsDef1,
            OneOfDescriptionOptionsDef2,
            OneOfDescriptionOptionsDef3,
        ]
        device_groups: Union[
            OneOfDeviceGroupsOptionsDef1,
            OneOfDeviceGroupsOptionsDef2,
            OneOfDeviceGroupsOptionsDef3,
        ]
        gps_location: GpsLocation
        location: Union[
            OneOfLocationOptionsDef1,
            OneOfLocationOptionsDef2,
            OneOfLocationOptionsDef3,
        ]
        max_omp_sessions: Union[
            OneOfMaxOmpSessionsOptionsDef1,
            OneOfMaxOmpSessionsOptionsDef2,
            OneOfMaxOmpSessionsOptionsDef3,
        ]
        on_demand: OnDemand
        overlay_id: Union[
            OneOfOverlayIdOptionsDef1,
            OneOfOverlayIdOptionsDef2,
            OneOfOverlayIdOptionsDef3,
        ]
        port_hop: Union[
            OneOfPortHopOptionsDef1,
            OneOfPortHopOptionsDef2,
            OneOfPortHopOptionsDef3,
        ]
        port_offset: Union[
            OneOfPortOffsetOptionsDef1,
            OneOfPortOffsetOptionsDef2,
            OneOfPortOffsetOptionsDef3,
        ]
        affinity_group_number: Optional[
            Union[
                OneOfAffinityGroupNumberOptionsDef1,
                OneOfAffinityGroupNumberOptionsDef2,
                OneOfAffinityGroupNumberOptionsDef3,
            ]
        ]
        affinity_group_preference: Optional[
            Union[
                OneOfAffinityGroupPreferenceOptionsDef1,
                OneOfAffinityGroupPreferenceOptionsDef2,
                OneOfAffinityGroupPreferenceOptionsDef3,
            ]
        ]
        # Affinity Group Number for VRFs
        affinity_per_vrf: Optional[List[AffinityPerVrf]]
        affinity_preference_auto: Optional[
            Union[
                OneOfAffinityPreferenceAutoOptionsDef1,
                OneOfAffinityPreferenceAutoOptionsDef2,
                OneOfAffinityPreferenceAutoOptionsDef3,
            ]
        ]
        control_session_pps: Optional[
            Union[
                OneOfControlSessionPpsOptionsDef1,
                OneOfControlSessionPpsOptionsDef2,
                OneOfControlSessionPpsOptionsDef3,
            ]
        ]
        controller_group_list: Optional[
            Union[
                OneOfControllerGroupListOptionsDef1,
                OneOfControllerGroupListOptionsDef2,
                OneOfControllerGroupListOptionsDef3,
            ]
        ]
        epfr: Optional[
            Union[OneOfEpfrOptions1, OneOfEpfrOptions2, OneOfEpfrOptions3]
        ]
        idle_timeout: Optional[
            Union[
                OneOfIdleTimeoutOptionsDef1,
                OneOfIdleTimeoutOptionsDef2,
                OneOfIdleTimeoutOptionsDef3,
            ]
        ]
        multi_tenant: Optional[
            Union[
                OneOfMultiTenantOptionsDef1,
                OneOfMultiTenantOptionsDef2,
                OneOfMultiTenantOptionsDef3,
            ]
        ]
        site_type: Optional[
            Union[
                OneOfSiteTypeOptionsDef1,
                OneOfSiteTypeOptionsDef2,
                OneOfSiteTypeOptionsDef3,
            ]
        ]
        track_default_gateway: Optional[
            Union[
                OneOfTrackDefaultGatewayOptionsDef1,
                OneOfTrackDefaultGatewayOptionsDef2,
                OneOfTrackDefaultGatewayOptionsDef3,
            ]
        ]
        track_interface_tag: Optional[
            Union[
                OneOfTrackInterfaceTagOptionsDef1,
                OneOfTrackInterfaceTagOptionsDef2,
                OneOfTrackInterfaceTagOptionsDef3,
            ]
        ]
        track_transport: Optional[
            Union[
                OneOfTrackTransportOptionsDef1,
                OneOfTrackTransportOptionsDef2,
                OneOfTrackTransportOptionsDef3,
            ]
        ]
        tracker_dia_stabilize_status: Optional[
            Union[
                OneOfTrackerDiaStabilizeStatusDef1,
                OneOfTrackerDiaStabilizeStatusDef2,
                OneOfTrackerDiaStabilizeStatusDef3,
            ]
        ]
        transport_gateway: Optional[
            Union[
                OneOfTransportGatewayOptionsDef1,
                OneOfTransportGatewayOptionsDef2,
                OneOfTransportGatewayOptionsDef3,
            ]
        ]


    class Payload:
        """
        Basic profile feature schema for POST request
        """

        data: BasicData
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
        # Basic profile feature schema for POST request
        payload: Optional[Payload]


    class GetListSdwanSystemBasicPayload:
        data: Optional[List[Data]]


    class CreateBasicProfileFeatureForSystemPostResponse:
        """
        Profile Parcel POST Response schema
        """

        parcel_id: str
        metadata: Optional[Any]


    class SystemBasicData:
        admin_tech_on_failure: Union[
            OneOfAdminTechOnFailureOptionsDef1,
            OneOfAdminTechOnFailureOptionsDef2,
            OneOfAdminTechOnFailureOptionsDef3,
        ]
        clock: Clock
        console_baud_rate: Union[
            OneOfConsoleBaudRateOptionsDef1,
            OneOfConsoleBaudRateOptionsDef2,
            OneOfConsoleBaudRateOptionsDef3,
        ]
        description: Union[
            OneOfDescriptionOptionsDef1,
            OneOfDescriptionOptionsDef2,
            OneOfDescriptionOptionsDef3,
        ]
        device_groups: Union[
            OneOfDeviceGroupsOptionsDef1,
            OneOfDeviceGroupsOptionsDef2,
            OneOfDeviceGroupsOptionsDef3,
        ]
        gps_location: GpsLocation
        location: Union[
            OneOfLocationOptionsDef1,
            OneOfLocationOptionsDef2,
            OneOfLocationOptionsDef3,
        ]
        max_omp_sessions: Union[
            OneOfMaxOmpSessionsOptionsDef1,
            OneOfMaxOmpSessionsOptionsDef2,
            OneOfMaxOmpSessionsOptionsDef3,
        ]
        on_demand: OnDemand
        overlay_id: Union[
            OneOfOverlayIdOptionsDef1,
            OneOfOverlayIdOptionsDef2,
            OneOfOverlayIdOptionsDef3,
        ]
        port_hop: Union[
            OneOfPortHopOptionsDef1,
            OneOfPortHopOptionsDef2,
            OneOfPortHopOptionsDef3,
        ]
        port_offset: Union[
            OneOfPortOffsetOptionsDef1,
            OneOfPortOffsetOptionsDef2,
            OneOfPortOffsetOptionsDef3,
        ]
        affinity_group_number: Optional[
            Union[
                OneOfAffinityGroupNumberOptionsDef1,
                OneOfAffinityGroupNumberOptionsDef2,
                OneOfAffinityGroupNumberOptionsDef3,
            ]
        ]
        affinity_group_preference: Optional[
            Union[
                OneOfAffinityGroupPreferenceOptionsDef1,
                OneOfAffinityGroupPreferenceOptionsDef2,
                OneOfAffinityGroupPreferenceOptionsDef3,
            ]
        ]
        # Affinity Group Number for VRFs
        affinity_per_vrf: Optional[List[AffinityPerVrf]]
        affinity_preference_auto: Optional[
            Union[
                OneOfAffinityPreferenceAutoOptionsDef1,
                OneOfAffinityPreferenceAutoOptionsDef2,
                OneOfAffinityPreferenceAutoOptionsDef3,
            ]
        ]
        control_session_pps: Optional[
            Union[
                OneOfControlSessionPpsOptionsDef1,
                OneOfControlSessionPpsOptionsDef2,
                OneOfControlSessionPpsOptionsDef3,
            ]
        ]
        controller_group_list: Optional[
            Union[
                OneOfControllerGroupListOptionsDef1,
                OneOfControllerGroupListOptionsDef2,
                OneOfControllerGroupListOptionsDef3,
            ]
        ]
        epfr: Optional[
            Union[OneOfEpfrOptions1, OneOfEpfrOptions2, OneOfEpfrOptions3]
        ]
        idle_timeout: Optional[
            Union[
                OneOfIdleTimeoutOptionsDef1,
                OneOfIdleTimeoutOptionsDef2,
                OneOfIdleTimeoutOptionsDef3,
            ]
        ]
        multi_tenant: Optional[
            Union[
                OneOfMultiTenantOptionsDef1,
                OneOfMultiTenantOptionsDef2,
                OneOfMultiTenantOptionsDef3,
            ]
        ]
        site_type: Optional[
            Union[
                OneOfSiteTypeOptionsDef1,
                OneOfSiteTypeOptionsDef2,
                OneOfSiteTypeOptionsDef3,
            ]
        ]
        track_default_gateway: Optional[
            Union[
                OneOfTrackDefaultGatewayOptionsDef1,
                OneOfTrackDefaultGatewayOptionsDef2,
                OneOfTrackDefaultGatewayOptionsDef3,
            ]
        ]
        track_interface_tag: Optional[
            Union[
                OneOfTrackInterfaceTagOptionsDef1,
                OneOfTrackInterfaceTagOptionsDef2,
                OneOfTrackInterfaceTagOptionsDef3,
            ]
        ]
        track_transport: Optional[
            Union[
                OneOfTrackTransportOptionsDef1,
                OneOfTrackTransportOptionsDef2,
                OneOfTrackTransportOptionsDef3,
            ]
        ]
        tracker_dia_stabilize_status: Optional[
            Union[
                OneOfTrackerDiaStabilizeStatusDef1,
                OneOfTrackerDiaStabilizeStatusDef2,
                OneOfTrackerDiaStabilizeStatusDef3,
            ]
        ]
        transport_gateway: Optional[
            Union[
                OneOfTransportGatewayOptionsDef1,
                OneOfTransportGatewayOptionsDef2,
                OneOfTransportGatewayOptionsDef3,
            ]
        ]


    class CreateBasicProfileFeatureForSystemPostRequest:
        """
        Basic profile feature schema for POST request
        """

        data: SystemBasicData
        name: str
        # Set the feature description
        description: Optional[str]
        metadata: Optional[Any]


    class BasicClock:
        timezone: Union[
            OneOfTimezoneOptionsDef1,
            OneOfTimezoneOptionsDef2,
            OneOfTimezoneOptionsDef3,
        ]


    class BasicOneOfRangeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class BasicOneOfRangeOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class BasicOneOfMobileNumberNumberOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class BasicMobileNumber:
        number: Union[
            BasicOneOfMobileNumberNumberOptionsDef1,
            OneOfMobileNumberNumberOptionsDef2,
        ]


    class BasicSms:
        enable: Optional[
            Union[OneOfEnableOptionsDef1, OneOfEnableOptionsDef2]
        ]
        # Set device’s geo fencing SMS phone number
        mobile_number: Optional[List[BasicMobileNumber]]


    class BasicGeoFencing:
        enable: Optional[
            Union[OneOfEnableOptionsDef1, OneOfEnableOptionsDef2]
        ]
        range: Optional[
            Union[
                BasicOneOfRangeOptionsDef1,
                OneOfRangeOptionsDef2,
                BasicOneOfRangeOptionsDef3,
            ]
        ]
        sms: Optional[BasicSms]


    class BasicGpsLocation:
        latitude: Union[
            OneOfLatitudeOptionsDef1,
            OneOfLatitudeOptionsDef2,
            OneOfLatitudeOptionsDef3,
        ]
        longitude: Union[
            OneOfLongitudeOptionsDef1,
            OneOfLongitudeOptionsDef2,
            OneOfLongitudeOptionsDef3,
        ]
        geo_fencing: Optional[BasicGeoFencing]


    class BasicOneOfDeviceGroupsOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: List[str]


    class BasicOneOfControllerGroupListOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: List[int]


    class BasicOneOfOverlayIdOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class BasicOneOfPortOffsetOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class BasicOneOfControlSessionPpsOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class BasicOneOfTrackInterfaceTagOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class BasicOneOfConsoleBaudRateOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: BasicConsoleBaudRateDef


    class BasicOneOfMaxOmpSessionsOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class BasicOneOfIdleTimeoutOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class BasicOneOfOnDemandIdleTimeoutOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class BasicOnDemand:
        on_demand_enable: Union[
            OneOfOnDemandEnableOptionsDef1,
            OneOfOnDemandEnableOptionsDef2,
            OneOfOnDemandEnableOptionsDef3,
        ]
        on_demand_idle_timeout: Union[
            OneOfOnDemandIdleTimeoutOptionsDef1,
            BasicOneOfOnDemandIdleTimeoutOptionsDef2,
            OneOfOnDemandIdleTimeoutOptionsDef3,
        ]


    class BasicOneOfEpfrOptions1:
        option_type: GlobalOptionTypeDef
        value: BasicEpfrDef


    class BasicOneOfSiteTypeOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: List[
            BasicSiteTypeListDef
        ]  # pytype: disable=annotation-type-mismatch


    class BasicOneOfAffinityGroupNumberOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class BasicOneOfAffinityGroupPreferenceOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: List[int]


    class SystemBasicOneOfAffinityGroupNumberOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class BasicOneOfVrfRangeOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: Any


    class BasicAffinityPerVrf:
        affinity_group_number: Optional[
            Union[
                OneOfAffinityGroupNumberOptionsDef1,
                SystemBasicOneOfAffinityGroupNumberOptionsDef2,
                OneOfAffinityGroupNumberOptionsDef3,
            ]
        ]
        vrf_range: Optional[
            Union[
                OneOfVrfRangeOptionsDef1,
                BasicOneOfVrfRangeOptionsDef2,
                OneOfVrfRangeOptionsDef3,
            ]
        ]


    class SdwanSystemBasicData:
        admin_tech_on_failure: Union[
            OneOfAdminTechOnFailureOptionsDef1,
            OneOfAdminTechOnFailureOptionsDef2,
            OneOfAdminTechOnFailureOptionsDef3,
        ]
        clock: BasicClock
        console_baud_rate: Union[
            OneOfConsoleBaudRateOptionsDef1,
            BasicOneOfConsoleBaudRateOptionsDef2,
            OneOfConsoleBaudRateOptionsDef3,
        ]
        description: Union[
            OneOfDescriptionOptionsDef1,
            OneOfDescriptionOptionsDef2,
            OneOfDescriptionOptionsDef3,
        ]
        device_groups: Union[
            OneOfDeviceGroupsOptionsDef1,
            BasicOneOfDeviceGroupsOptionsDef2,
            OneOfDeviceGroupsOptionsDef3,
        ]
        gps_location: BasicGpsLocation
        location: Union[
            OneOfLocationOptionsDef1,
            OneOfLocationOptionsDef2,
            OneOfLocationOptionsDef3,
        ]
        max_omp_sessions: Union[
            OneOfMaxOmpSessionsOptionsDef1,
            BasicOneOfMaxOmpSessionsOptionsDef2,
            OneOfMaxOmpSessionsOptionsDef3,
        ]
        on_demand: BasicOnDemand
        overlay_id: Union[
            OneOfOverlayIdOptionsDef1,
            BasicOneOfOverlayIdOptionsDef2,
            OneOfOverlayIdOptionsDef3,
        ]
        port_hop: Union[
            OneOfPortHopOptionsDef1,
            OneOfPortHopOptionsDef2,
            OneOfPortHopOptionsDef3,
        ]
        port_offset: Union[
            OneOfPortOffsetOptionsDef1,
            BasicOneOfPortOffsetOptionsDef2,
            OneOfPortOffsetOptionsDef3,
        ]
        affinity_group_number: Optional[
            Union[
                OneOfAffinityGroupNumberOptionsDef1,
                BasicOneOfAffinityGroupNumberOptionsDef2,
                OneOfAffinityGroupNumberOptionsDef3,
            ]
        ]
        affinity_group_preference: Optional[
            Union[
                OneOfAffinityGroupPreferenceOptionsDef1,
                BasicOneOfAffinityGroupPreferenceOptionsDef2,
                OneOfAffinityGroupPreferenceOptionsDef3,
            ]
        ]
        # Affinity Group Number for VRFs
        affinity_per_vrf: Optional[List[BasicAffinityPerVrf]]
        affinity_preference_auto: Optional[
            Union[
                OneOfAffinityPreferenceAutoOptionsDef1,
                OneOfAffinityPreferenceAutoOptionsDef2,
                OneOfAffinityPreferenceAutoOptionsDef3,
            ]
        ]
        control_session_pps: Optional[
            Union[
                OneOfControlSessionPpsOptionsDef1,
                BasicOneOfControlSessionPpsOptionsDef2,
                OneOfControlSessionPpsOptionsDef3,
            ]
        ]
        controller_group_list: Optional[
            Union[
                OneOfControllerGroupListOptionsDef1,
                BasicOneOfControllerGroupListOptionsDef2,
                OneOfControllerGroupListOptionsDef3,
            ]
        ]
        epfr: Optional[
            Union[
                BasicOneOfEpfrOptions1,
                OneOfEpfrOptions2,
                OneOfEpfrOptions3,
            ]
        ]
        idle_timeout: Optional[
            Union[
                OneOfIdleTimeoutOptionsDef1,
                BasicOneOfIdleTimeoutOptionsDef2,
                OneOfIdleTimeoutOptionsDef3,
            ]
        ]
        multi_tenant: Optional[
            Union[
                OneOfMultiTenantOptionsDef1,
                OneOfMultiTenantOptionsDef2,
                OneOfMultiTenantOptionsDef3,
            ]
        ]
        site_type: Optional[
            Union[
                OneOfSiteTypeOptionsDef1,
                BasicOneOfSiteTypeOptionsDef2,
                OneOfSiteTypeOptionsDef3,
            ]
        ]
        track_default_gateway: Optional[
            Union[
                OneOfTrackDefaultGatewayOptionsDef1,
                OneOfTrackDefaultGatewayOptionsDef2,
                OneOfTrackDefaultGatewayOptionsDef3,
            ]
        ]
        track_interface_tag: Optional[
            Union[
                OneOfTrackInterfaceTagOptionsDef1,
                BasicOneOfTrackInterfaceTagOptionsDef2,
                OneOfTrackInterfaceTagOptionsDef3,
            ]
        ]
        track_transport: Optional[
            Union[
                OneOfTrackTransportOptionsDef1,
                OneOfTrackTransportOptionsDef2,
                OneOfTrackTransportOptionsDef3,
            ]
        ]
        tracker_dia_stabilize_status: Optional[
            Union[
                OneOfTrackerDiaStabilizeStatusDef1,
                OneOfTrackerDiaStabilizeStatusDef2,
                OneOfTrackerDiaStabilizeStatusDef3,
            ]
        ]
        transport_gateway: Optional[
            Union[
                OneOfTransportGatewayOptionsDef1,
                OneOfTransportGatewayOptionsDef2,
                OneOfTransportGatewayOptionsDef3,
            ]
        ]


    class BasicPayload:
        """
        Basic profile feature schema for PUT request
        """

        data: SdwanSystemBasicData
        name: str
        # Set the feature description
        description: Optional[str]
        metadata: Optional[Any]


    class GetSingleSdwanSystemBasicPayload:
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
        # Basic profile feature schema for PUT request
        payload: Optional[BasicPayload]


    class EditBasicProfileFeatureForSystemPutResponse:
        """
        Profile Parcel PUT Response schema
        """

        id: str
        metadata: Optional[Any]


    class SystemBasicClock:
        timezone: Union[
            OneOfTimezoneOptionsDef1,
            OneOfTimezoneOptionsDef2,
            OneOfTimezoneOptionsDef3,
        ]


    class SystemBasicOneOfRangeOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: int


    class SystemBasicOneOfRangeOptionsDef3:
        option_type: DefaultOptionTypeDef
        value: int


    class SystemBasicOneOfMobileNumberNumberOptionsDef1:
        option_type: GlobalOptionTypeDef
        value: str


    class SystemBasicMobileNumber:
        number: Union[
            SystemBasicOneOfMobileNumberNumberOptionsDef1,
            OneOfMobileNumberNumberOptionsDef2,
        ]


    class SystemBasicSms:
        enable: Optional[
            Union[OneOfEnableOptionsDef1, OneOfEnableOptionsDef2]
        ]
        # Set device’s geo fencing SMS phone number
        mobile_number: Optional[List[SystemBasicMobileNumber]]


    class SystemBasicGeoFencing:
        enable: Optional[
            Union[OneOfEnableOptionsDef1, OneOfEnableOptionsDef2]
        ]
        range: Optional[
            Union[
                SystemBasicOneOfRangeOptionsDef1,
                OneOfRangeOptionsDef2,
                SystemBasicOneOfRangeOptionsDef3,
            ]
        ]
        sms: Optional[SystemBasicSms]


    class SystemBasicGpsLocation:
        latitude: Union[
            OneOfLatitudeOptionsDef1,
            OneOfLatitudeOptionsDef2,
            OneOfLatitudeOptionsDef3,
        ]
        longitude: Union[
            OneOfLongitudeOptionsDef1,
            OneOfLongitudeOptionsDef2,
            OneOfLongitudeOptionsDef3,
        ]
        geo_fencing: Optional[SystemBasicGeoFencing]


    class SystemBasicOneOfDeviceGroupsOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: List[str]


    class SystemBasicOneOfControllerGroupListOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: List[int]


    class SystemBasicOneOfOverlayIdOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class SystemBasicOneOfPortOffsetOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class SystemBasicOneOfControlSessionPpsOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class SystemBasicOneOfTrackInterfaceTagOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class SystemBasicOneOfConsoleBaudRateOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: SystemBasicConsoleBaudRateDef


    class SystemBasicOneOfMaxOmpSessionsOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class SystemBasicOneOfIdleTimeoutOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class SystemBasicOneOfOnDemandIdleTimeoutOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class SystemBasicOnDemand:
        on_demand_enable: Union[
            OneOfOnDemandEnableOptionsDef1,
            OneOfOnDemandEnableOptionsDef2,
            OneOfOnDemandEnableOptionsDef3,
        ]
        on_demand_idle_timeout: Union[
            OneOfOnDemandIdleTimeoutOptionsDef1,
            SystemBasicOneOfOnDemandIdleTimeoutOptionsDef2,
            OneOfOnDemandIdleTimeoutOptionsDef3,
        ]


    class SystemBasicOneOfEpfrOptions1:
        option_type: GlobalOptionTypeDef
        value: SystemBasicEpfrDef


    class SystemBasicOneOfSiteTypeOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: List[
            SystemBasicSiteTypeListDef
        ]  # pytype: disable=annotation-type-mismatch


    class SdwanSystemBasicOneOfAffinityGroupNumberOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class SystemBasicOneOfAffinityGroupPreferenceOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: List[int]


    class FeatureProfileSdwanSystemBasicOneOfAffinityGroupNumberOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: int


    class SystemBasicOneOfVrfRangeOptionsDef2:
        option_type: GlobalOptionTypeDef
        value: Any


    class SystemBasicAffinityPerVrf:
        affinity_group_number: Optional[
            Union[
                OneOfAffinityGroupNumberOptionsDef1,
                FeatureProfileSdwanSystemBasicOneOfAffinityGroupNumberOptionsDef2,
                OneOfAffinityGroupNumberOptionsDef3,
            ]
        ]
        vrf_range: Optional[
            Union[
                OneOfVrfRangeOptionsDef1,
                SystemBasicOneOfVrfRangeOptionsDef2,
                OneOfVrfRangeOptionsDef3,
            ]
        ]


    class FeatureProfileSdwanSystemBasicData:
        admin_tech_on_failure: Union[
            OneOfAdminTechOnFailureOptionsDef1,
            OneOfAdminTechOnFailureOptionsDef2,
            OneOfAdminTechOnFailureOptionsDef3,
        ]
        clock: SystemBasicClock
        console_baud_rate: Union[
            OneOfConsoleBaudRateOptionsDef1,
            SystemBasicOneOfConsoleBaudRateOptionsDef2,
            OneOfConsoleBaudRateOptionsDef3,
        ]
        description: Union[
            OneOfDescriptionOptionsDef1,
            OneOfDescriptionOptionsDef2,
            OneOfDescriptionOptionsDef3,
        ]
        device_groups: Union[
            OneOfDeviceGroupsOptionsDef1,
            SystemBasicOneOfDeviceGroupsOptionsDef2,
            OneOfDeviceGroupsOptionsDef3,
        ]
        gps_location: SystemBasicGpsLocation
        location: Union[
            OneOfLocationOptionsDef1,
            OneOfLocationOptionsDef2,
            OneOfLocationOptionsDef3,
        ]
        max_omp_sessions: Union[
            OneOfMaxOmpSessionsOptionsDef1,
            SystemBasicOneOfMaxOmpSessionsOptionsDef2,
            OneOfMaxOmpSessionsOptionsDef3,
        ]
        on_demand: SystemBasicOnDemand
        overlay_id: Union[
            OneOfOverlayIdOptionsDef1,
            SystemBasicOneOfOverlayIdOptionsDef2,
            OneOfOverlayIdOptionsDef3,
        ]
        port_hop: Union[
            OneOfPortHopOptionsDef1,
            OneOfPortHopOptionsDef2,
            OneOfPortHopOptionsDef3,
        ]
        port_offset: Union[
            OneOfPortOffsetOptionsDef1,
            SystemBasicOneOfPortOffsetOptionsDef2,
            OneOfPortOffsetOptionsDef3,
        ]
        affinity_group_number: Optional[
            Union[
                OneOfAffinityGroupNumberOptionsDef1,
                SdwanSystemBasicOneOfAffinityGroupNumberOptionsDef2,
                OneOfAffinityGroupNumberOptionsDef3,
            ]
        ]
        affinity_group_preference: Optional[
            Union[
                OneOfAffinityGroupPreferenceOptionsDef1,
                SystemBasicOneOfAffinityGroupPreferenceOptionsDef2,
                OneOfAffinityGroupPreferenceOptionsDef3,
            ]
        ]
        # Affinity Group Number for VRFs
        affinity_per_vrf: Optional[List[SystemBasicAffinityPerVrf]]
        affinity_preference_auto: Optional[
            Union[
                OneOfAffinityPreferenceAutoOptionsDef1,
                OneOfAffinityPreferenceAutoOptionsDef2,
                OneOfAffinityPreferenceAutoOptionsDef3,
            ]
        ]
        control_session_pps: Optional[
            Union[
                OneOfControlSessionPpsOptionsDef1,
                SystemBasicOneOfControlSessionPpsOptionsDef2,
                OneOfControlSessionPpsOptionsDef3,
            ]
        ]
        controller_group_list: Optional[
            Union[
                OneOfControllerGroupListOptionsDef1,
                SystemBasicOneOfControllerGroupListOptionsDef2,
                OneOfControllerGroupListOptionsDef3,
            ]
        ]
        epfr: Optional[
            Union[
                SystemBasicOneOfEpfrOptions1,
                OneOfEpfrOptions2,
                OneOfEpfrOptions3,
            ]
        ]
        idle_timeout: Optional[
            Union[
                OneOfIdleTimeoutOptionsDef1,
                SystemBasicOneOfIdleTimeoutOptionsDef2,
                OneOfIdleTimeoutOptionsDef3,
            ]
        ]
        multi_tenant: Optional[
            Union[
                OneOfMultiTenantOptionsDef1,
                OneOfMultiTenantOptionsDef2,
                OneOfMultiTenantOptionsDef3,
            ]
        ]
        site_type: Optional[
            Union[
                OneOfSiteTypeOptionsDef1,
                SystemBasicOneOfSiteTypeOptionsDef2,
                OneOfSiteTypeOptionsDef3,
            ]
        ]
        track_default_gateway: Optional[
            Union[
                OneOfTrackDefaultGatewayOptionsDef1,
                OneOfTrackDefaultGatewayOptionsDef2,
                OneOfTrackDefaultGatewayOptionsDef3,
            ]
        ]
        track_interface_tag: Optional[
            Union[
                OneOfTrackInterfaceTagOptionsDef1,
                SystemBasicOneOfTrackInterfaceTagOptionsDef2,
                OneOfTrackInterfaceTagOptionsDef3,
            ]
        ]
        track_transport: Optional[
            Union[
                OneOfTrackTransportOptionsDef1,
                OneOfTrackTransportOptionsDef2,
                OneOfTrackTransportOptionsDef3,
            ]
        ]
        tracker_dia_stabilize_status: Optional[
            Union[
                OneOfTrackerDiaStabilizeStatusDef1,
                OneOfTrackerDiaStabilizeStatusDef2,
                OneOfTrackerDiaStabilizeStatusDef3,
            ]
        ]
        transport_gateway: Optional[
            Union[
                OneOfTransportGatewayOptionsDef1,
                OneOfTransportGatewayOptionsDef2,
                OneOfTransportGatewayOptionsDef3,
            ]
        ]


    class EditBasicProfileFeatureForSystemPutRequest:
        """
        Basic profile feature schema for PUT request
        """

        data: FeatureProfileSdwanSystemBasicData
        name: str
        # Set the feature description
        description: Optional[str]
        metadata: Optional[Any]


