======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    Type = Literal[
        "cellular",
        "ethernet",
        "globalSettings",
        "networkProtocol",
        "securityPolicy",
        "wifi",
    ]


    class Variable:
        json_path: str
        var_name: str


    class PolicyRule:
        action: Optional[str]
        dest_ip: Optional[str]
        dest_port: Optional[int]
        protocol_type: Optional[List[str]]
        source_ip: Optional[str]
        source_port: Optional[int]


    class SecurityPolicy:
        # Name of the Profile Parcel. Must be unique.
        name: str
        type_: Type
        # User who last created this.
        created_by: Optional[str]
        # Timestamp of creation
        created_on: Optional[int]
        default_action: Optional[str]
        # Description of the Profile Parcel.
        description: Optional[str]
        # System generated unique identifier of the Profile Parcel in UUID format.
        id: Optional[str]
        # User who last updated this.
        last_updated_by: Optional[str]
        # Timestamp of last update
        last_updated_on: Optional[int]
        policy_name: Optional[str]
        policy_rules: Optional[List[PolicyRule]]
        variables: Optional[List[Variable]]


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
        payload: Optional[SecurityPolicy]


    class GetListMobilityGlobalSecuritypolicyPayload:
        data: Optional[List[Data]]


    class CreateSecurityPolicyProfileParcelForMobilityPostRequest:
        # Name of the Profile Parcel. Must be unique.
        name: str
        type_: Type
        # User who last created this.
        created_by: Optional[str]
        # Timestamp of creation
        created_on: Optional[int]
        default_action: Optional[str]
        # Description of the Profile Parcel.
        description: Optional[str]
        # System generated unique identifier of the Profile Parcel in UUID format.
        id: Optional[str]
        # User who last updated this.
        last_updated_by: Optional[str]
        # Timestamp of last update
        last_updated_on: Optional[int]
        policy_name: Optional[str]
        policy_rules: Optional[List[PolicyRule]]
        variables: Optional[List[Variable]]


    class GetSingleMobilityGlobalSecuritypolicyPayload:
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
        payload: Optional[SecurityPolicy]


    class EditSecurityPolicyProfileParcelForMobilityPutRequest:
        # Name of the Profile Parcel. Must be unique.
        name: str
        type_: Type
        # User who last created this.
        created_by: Optional[str]
        # Timestamp of creation
        created_on: Optional[int]
        default_action: Optional[str]
        # Description of the Profile Parcel.
        description: Optional[str]
        # System generated unique identifier of the Profile Parcel in UUID format.
        id: Optional[str]
        # User who last updated this.
        last_updated_by: Optional[str]
        # Timestamp of last update
        last_updated_on: Optional[int]
        policy_name: Optional[str]
        policy_rules: Optional[List[PolicyRule]]
        variables: Optional[List[Variable]]


