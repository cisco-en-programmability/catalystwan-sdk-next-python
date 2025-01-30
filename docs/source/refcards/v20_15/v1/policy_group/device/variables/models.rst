======
Models
======


.. code:: python

    from typing import Literal, Any, Union, Dict, Optional, List

    Solution = Literal["sd-routing", "sdwan"]


    class Variables:
        name: str
        value: Union[str, int, int, bool, List[None]]


    class Devices:
        # Device unique id
        device_id: str
        # Variable object for the device
        variables: List[Variables]


    class CreatePolicyGroupDeviceVariablesPutRequest:
        """
        Variables PUT request Schema
        """

        # Variables for devices
        devices: List[Devices]
        solution: Solution  # pytype: disable=annotation-type-mismatch


    class VariablesVariables:
        # Name of the variable
        name: str
        # List of suggestions for the variable
        suggestions: Optional[List[str]]
        # Value of the variable
        value: Optional[str]


    class VariablesDevices:
        # Unique identifier for the device
        device_id: str
        variables: List[VariablesVariables]


    class Groups:
        # Variables associated with the group
        group_variables: List[Any]
        # Name of the group
        name: str


    class FetchPolicyGroupDeviceVariablesPostResponse:
        """
        Schema for the response of a GET request to retrieve config group variables
        """

        devices: List[VariablesDevices]
        # Family of the configuration
        family: str
        groups: List[Groups]


    class FetchPolicyGroupDeviceVariablesPostRequest:
        """
        Variables POST request Schema
        """

        # ID of devices for which Variables need to be fetched
        device_ids: Optional[List[str]]
        # Variable object for the device
        suggestions: Optional[bool]


