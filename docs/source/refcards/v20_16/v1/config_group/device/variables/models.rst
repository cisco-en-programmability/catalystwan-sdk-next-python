======
Models
======


.. code:: python

    from typing import Union, Dict, Optional, Literal, List, Any

    ValueType = Literal[
        "ARRAY", "FALSE", "NULL", "NUMBER", "OBJECT", "STRING", "TRUE"
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


    class ResponseSchema2:
        """
        Schema for the response of a GET request to retrieve config group variables
        """

        devices: List[Devices]
        # Family of the configuration
        family: str
        groups: List[Groups]


    class CreateConfigGroupDeviceVariablesPutRequest:
        empty: Optional[bool]
        value_type: Optional[ValueType]


