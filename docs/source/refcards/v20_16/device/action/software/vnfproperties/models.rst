======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class GetVnfPropertiesVnfPropertiesJsonVnfProperties:
        application_description: Optional[str]
        application_max_instances: Optional[int]
        application_vendor: Optional[str]
        arch: Optional[str]
        image_type: Optional[str]
        name: Optional[str]
        version: Optional[str]
        vnf_type: Optional[str]


    class GetVnfPropertiesVnfPropertiesJson:
        vnf_properties: Optional[
            GetVnfPropertiesVnfPropertiesJsonVnfProperties
        ]


    class GetVnfPropertiesData:
        vnf_properties_json: Optional[GetVnfPropertiesVnfPropertiesJson]


    class GetVnfProperties:
        data: Optional[List[GetVnfPropertiesData]]


