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


    class AssociateDeviceIdDef:
        id: str


    class CreatePolicyGroupAssociationPostRequest:
        """
        Policy Group Associate Post Request schema
        """

        # list of device ids that policy group need to be associated with
        devices: List[AssociateDeviceIdDef]


    class DeviceAssociateDeviceIdDef:
        id: str


    class DeletePolicyGroupAssociationDeleteRequest:
        """
        Policy Group Associate Delete Request schema
        """

        # list of device ids that policy group need to be associated with
        devices: List[DeviceAssociateDeviceIdDef]


