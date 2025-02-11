======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class GetImagePropertiesImagePropertiesJsonImageProperties:
        application_description: Optional[str]
        application_max_instances: Optional[int]
        application_vendor: Optional[str]
        arch: Optional[str]
        image_type: Optional[str]
        name: Optional[str]
        version: Optional[str]
        vnf_type: Optional[str]


    class GetImagePropertiesImagePropertiesJson:
        image_properties: Optional[
            GetImagePropertiesImagePropertiesJsonImageProperties
        ]


    class GetImagePropertiesData:
        image_properties_json: Optional[
            GetImagePropertiesImagePropertiesJson
        ]


    class GetImageProperties:
        data: Optional[List[GetImagePropertiesData]]


