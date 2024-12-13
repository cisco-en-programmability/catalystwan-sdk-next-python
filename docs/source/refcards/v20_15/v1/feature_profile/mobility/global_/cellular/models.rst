======
Models
======


.. code:: python

    from typing import List, Dict, Union, Literal, Optional, Any

    Type = Literal[
        "cellular",
        "ethernet",
        "globalSettings",
        "networkProtocol",
        "securityPolicy",
        "wifi",
    ]


    class CellularProfile:
        apn: Optional[str]
        auth_method: Optional[str]
        id: Optional[int]
        password: Optional[str]
        pdn_type: Optional[str]
        user_name: Optional[str]


    class Variable:
        json_path: str
        var_name: str


    class SimSlotConfig:
        attach_profile_id: int
        profile_list: List[CellularProfile]
        slot_number: int
        carrier_name: Optional[str]
        data_profile_id_list: Optional[List[int]]


    class EditCellularProfileParcelForMobilityPutRequest:
        # Name of the Profile Parcel. Must be unique.
        name: str
        primary_slot: int
        type_: Type
        # User who last created this.
        created_by: Optional[str]
        # Timestamp of creation
        created_on: Optional[int]
        # Description of the Profile Parcel.
        description: Optional[str]
        # System generated unique identifier of the Profile Parcel in UUID format.
        id: Optional[str]
        # User who last updated this.
        last_updated_by: Optional[str]
        # Timestamp of last update
        last_updated_on: Optional[int]
        sim_slot0: Optional[SimSlotConfig]
        sim_slot1: Optional[SimSlotConfig]
        variables: Optional[List[Variable]]
        wan_config: Optional[str]


