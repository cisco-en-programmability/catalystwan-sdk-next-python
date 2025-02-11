======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class DeviceIdDef:
        id: str


    class UpdatePolicyGroupAssociationPutRequest:
        """
        Policy Group Associate Put Request schema
        """

        # list of device ids that policy group need to be associated with
        devices: List[DeviceIdDef]
        # This is the documentation for associate PUT API request schema for policy group.
        documentation: Optional[Any]


    class AssociateDeviceIdDef:
        id: str


    class CreatePolicyGroupAssociationPostRequest:
        """
        Policy Group Associate Post Request schema
        """

        # list of device ids that policy group need to be associated with
        devices: List[AssociateDeviceIdDef]
        # This is the documentation for associate POST API request schema for policy group.
        documentation: Optional[Any]


