======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class Devices:
        # Indicates if the device was added by a rule
        added_by_rule: bool
        # Timestamp of the last update to the config group
        config_group_last_updated_on: str
        # Indicates if the config group is up to date
        config_group_up_to_date: str
        # Configuration status message
        config_status_message: str
        # IP address of the device
        device_ip: str
        # Indicates if the device is locked
        device_lock: str
        # Model of the device
        device_model: str
        # Hierarchy name path
        hierarchy_name_path: str
        # Hierarchy type path
        hierarchy_type_path: str
        # Host name of the device
        host_name: str
        # Unique identifier for the device
        id: str
        # Identifier for the site
        site_id: str
        # Name of the site
        site_name: str
        # Tags associated with the device
        tags: List[str]
        # List of unsupported features
        unsupported_features: List[str]


    class GetConfigGroupAssociationGetResponse:
        """
        Schema for the response of a GET request to associate a config group
        """

        devices: List[Devices]


    class DeviceIdDef:
        id: str


    class UpdateConfigGroupAssociationPutRequest:
        """
        Config Group Associate Put Request schema
        """

        # list of device ids that config group need to be associated with
        devices: List[DeviceIdDef]


    class AssociateDeviceIdDef:
        id: str


    class CreateConfigGroupAssociationPostRequest:
        """
        Config Group Associate Post Request schema
        """

        # list of device ids that config group need to be associated with
        devices: List[AssociateDeviceIdDef]


    class DeviceAssociateDeviceIdDef:
        id: str


    class DeleteConfigGroupAssociationDeleteRequest:
        """
        Config Group Associate Delete Request schema
        """

        # list of device ids that config group need to be associated with
        devices: List[DeviceAssociateDeviceIdDef]


