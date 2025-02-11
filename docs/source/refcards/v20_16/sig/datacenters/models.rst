======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class MappingEntries:
        city_country: Optional[str]
        fqdn: Optional[str]
        ip: Optional[str]


    class GetDataCenters:
        mapping: Optional[List[MappingEntries]]
        title: Optional[str]


