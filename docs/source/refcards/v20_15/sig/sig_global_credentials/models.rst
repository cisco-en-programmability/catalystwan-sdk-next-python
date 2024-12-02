======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class ApiKey:
        """
        API secret information
        """

        vip_object_type: Optional[str]
        vip_type: Optional[str]
        vip_value: Optional[str]
        vip_variable_name: Optional[str]


    class ApiSecret:
        """
        API key information
        """

        vip_needs_encryption: Optional[bool]
        vip_object_type: Optional[str]
        vip_type: Optional[str]
        vip_value: Optional[str]
        vip_variable_name: Optional[str]


    class OrgId:
        """
        Org ID
        """

        vip_object_type: Optional[str]
        vip_type: Optional[str]
        vip_value: Optional[str]
        vip_variable_name: Optional[str]


    class Umbrella:
        """
        Umbrella object
        """

        # API secret information
        api_key: Optional[ApiKey]
        # API secret information
        api_key_v2: Optional[ApiKey]
        # API key information
        api_secret: Optional[ApiSecret]
        # API key information
        api_secret_v2: Optional[ApiSecret]
        # Org ID
        org_id: Optional[OrgId]


    class FeatureTemplateType:
        """
        Response from metaDataType API
        """

        # Umbrella object
        umbrella: Optional[Umbrella]


