======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class PostCgwConfigGroupResponseProfiles:
        created_by: Optional[str]
        created_on: Optional[int]
        description: Optional[str]
        id: Optional[str]
        last_updated_by: Optional[str]
        last_updated_on: Optional[int]
        name: Optional[str]
        profile_parcel_count: Optional[str]
        solution: Optional[str]
        type_: Optional[str]


    class PostCgwConfigGroupResponse:
        created_by: Optional[str]
        created_on: Optional[int]
        description: Optional[str]
        devices: Optional[List[str]]
        full_config_cli: Optional[bool]
        id: Optional[str]
        ios_config_cli: Optional[bool]
        last_updated_by: Optional[str]
        last_updated_on: Optional[int]
        name: Optional[str]
        number_of_devices: Optional[int]
        number_of_devices_up_to_date: Optional[int]
        origin: Optional[str]
        profiles: Optional[List[PostCgwConfigGroupResponseProfiles]]
        solution: Optional[str]
        source: Optional[str]
        state: Optional[str]
        topology: Optional[str]
        version: Optional[int]


    class MultiCloudGatewaysConfiggroupBody:
        config_group_name: str
        config_group_solution: Optional[str]


