======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class InterconnectServiceSwVersion:
        # Service Software Version Image Name
        image_name: Optional[str]
        # Service Software Version
        version: Optional[str]


    class InterconnectServiceTypes:
        # Name of the service package
        name: Optional[str]
        # provider assigned service package code
        package_code: Optional[str]
        service_sw_version: Optional[List[InterconnectServiceSwVersion]]


    class InlineResponse20015:
        sw_packages: Optional[List[InterconnectServiceTypes]]


