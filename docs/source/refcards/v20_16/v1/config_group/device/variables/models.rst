======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    SolutionDef = Literal[
        "cellulargateway",
        "mobility",
        "nfvirtual",
        "sd-routing",
        "sdwan",
        "service-insertion",
    ]


    class Variables:
        # Name of the variable
        name: str
        # List of suggestions for the variable
        suggestions: Optional[List[str]]
        # Value of the variable
        value: Optional[str]


    class Devices:
        # Unique identifier for the device
        device_id: str
        variables: List[Variables]


    class Groups:
        # Variables associated with the group
        group_variables: List[Any]
        # Name of the group
        name: str


    class GetConfigGroupDeviceVariablesGetResponse:
        """
        Schema for the response of a GET request to retrieve config group variables
        """

        devices: List[Devices]
        # Family of the configuration
        family: str
        groups: List[Groups]


    class VariablesVariables:
        name: str
        value: Union[str, int, int, bool, List[None]]


    class DevicesDef:
        # Device unique id
        device_id: str
        # Variable object for the device
        variables: List[VariablesVariables]


    class GroupVariables:
        name: str
        value: Union[str, int, int, bool, List[None]]


    class VariablesGroups:
        # global variables object for the group
        group_variables: List[GroupVariables]
        name: str


    class CreateConfigGroupDeviceVariablesPutRequest:
        """
        Variables PUT request Schema
        """

        # Variables for devices
        devices: List[DevicesDef]
        solution: SolutionDef  # pytype: disable=annotation-type-mismatch
        # Variables for groups
        groups: Optional[List[VariablesGroups]]


    class FetchConfigGroupDeviceVariablesPostRequest:
        """
        Variables POST request Schema
        """

        # ID of devices for which Variables need to be fetched
        device_ids: Optional[List[str]]
        # Variable object for the device
        suggestions: Optional[bool]


