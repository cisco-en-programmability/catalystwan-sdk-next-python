# Copyright 2024 Cisco Systems, Inc. and its affiliates
from typing import Literal

SecurityProfileParcelTypeParam = Literal[
    "advanced-inspection-profile",
    "advanced-malware-protection",
    "intrusion-prevention",
    "ssl-decryption",
    "ssl-decryption-profile",
    "url-filtering",
]
