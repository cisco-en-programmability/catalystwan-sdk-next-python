======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    Solution = Literal[
        "cellulargateway",
        "common",
        "mobility",
        "nfvirtual",
        "sd-routing",
        "sdwan",
        "service-insertion",
    ]


    class FeatureProfile:
        """
        List of devices UUIDs associated with this group
        """

        # Name of the feature Profile. Must be unique.
        name: str
        # Solution of the feature Profile.
        solution: str
        # Type of the feature Profile.
        type_: str
        # User who last created this.
        created_by: Optional[str]
        # Timestamp of creation
        created_on: Optional[int]
        # Description of the feature Profile.
        description: Optional[str]
        # System generated unique identifier of the feature profile in UUID format.
        id: Optional[str]
        # User who last updated this.
        last_updated_by: Optional[str]
        # Timestamp of last update
        last_updated_on: Optional[int]
        # Number of Parcels attached with Feature Profile
        profile_parcel_count: Optional[int]


    class TopologyGroup:
        # Name of the  Group. Must be unique.
        name: str
        # Specify one of the device platform solution
        solution: Solution  # pytype: disable=annotation-type-mismatch
        #  Group Deployment state
        state: str
        #  Group Version Flag
        version: int
        active_status: Optional[bool]
        copy_info: Optional[str]
        # User who last created this.
        created_by: Optional[str]
        # Timestamp of creation
        created_on: Optional[int]
        # Description of the  Group.
        description: Optional[str]
        devices: Optional[List[str]]
        # System generated unique identifier of the  Group in UUID format.
        id: Optional[str]
        # User who last updated this.
        last_updated_by: Optional[str]
        # Timestamp of last update
        last_updated_on: Optional[int]
        number_of_devices: Optional[int]
        number_of_devices_up_to_date: Optional[int]
        origin: Optional[str]
        origin_info: Optional[Dict[str, str]]
        # List of devices UUIDs associated with this group
        profiles: Optional[List[FeatureProfile]]
        # Source of group
        source: Optional[str]


