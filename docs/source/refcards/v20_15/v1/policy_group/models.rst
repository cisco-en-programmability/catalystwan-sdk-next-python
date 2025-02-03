======
Models
======


.. code:: python

    from typing import Any, List, Dict, Literal, Optional, Union

    Solution = Literal[
        "cellulargateway",
        "common",
        "mobility",
        "nfvirtual",
        "sd-routing",
        "sdwan",
        "service-insertion",
    ]

    ProfileType = Literal["global"]

    PolicyGroupSolution = Literal["sd-routing", "sdwan"]


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


    class PolicyGroup:
        # Name of the  Group. Must be unique.
        name: str
        # Specify one of the device platform solution
        solution: Solution  # pytype: disable=annotation-type-mismatch
        #  Group Deployment state
        state: str
        #  Group Version Flag
        version: int
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


    class ProfileObjDef:
        id: str
        profile_type: ProfileType


    class CreatePolicyGroupPostResponse:
        """
        Policy Group POST Response schema
        """

        id: str
        # This is the documentation for POST response schema for policy group.
        documentation: Optional[Any]
        # (Optional - only applicable for AON) List of profile ids that belongs to the policy group
        profiles: Optional[List[ProfileObjDef]]


    class ProfileIdObjDef:
        id: str


    class FromPolicyGroupDef:
        copy: str


    class CreatePolicyGroupPostRequest:
        """
        Policy Group POST Request schema
        """

        description: str
        name: str
        solution: PolicyGroupSolution  # pytype: disable=annotation-type-mismatch
        # This is the documentation for POST request api schema for policy group
        documentation: Optional[Any]
        from_policy_group: Optional[FromPolicyGroupDef]
        # list of profile ids that belongs to the policy group
        profiles: Optional[List[ProfileIdObjDef]]


    class PolicyGroupProfileObjDef:
        id: str
        profile_type: ProfileType


    class EditPolicyGroupPutResponse:
        """
        Policy Group PUT Response schema
        """

        id: str
        # This is the documentation for PUT response schema for Policy group.
        documentation: Optional[Any]
        # (Optional - only applicable for AON) List of profile ids that belongs to the Policy group
        profiles: Optional[List[PolicyGroupProfileObjDef]]


    class PolicyGroupProfileIdObjDef:
        id: str


    class EditPolicyGroupPutRequest:
        """
        Policy Group PUT Request schema
        """

        description: str
        name: str
        solution: PolicyGroupSolution  # pytype: disable=annotation-type-mismatch
        # This is the documentation for PUT request api schema for policy group
        documentation: Optional[Any]
        # list of profile ids that belongs to the policy group
        profiles: Optional[List[PolicyGroupProfileIdObjDef]]


