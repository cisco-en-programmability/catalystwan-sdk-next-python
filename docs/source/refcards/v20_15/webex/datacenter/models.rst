======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class Prefixinfo:
        owned: Optional[List[str]]


    class Regioninfo:
        id: Optional[int]
        name: Optional[str]
        responder_fqdn: Optional[str]


    class RegionPrefixinfo:
        prefixes: Optional[Prefixinfo]
        region: Optional[Regioninfo]


    class Configinfo:
        items: Optional[List[RegionPrefixinfo]]
        revision: Optional[str]
        version: Optional[str]


    class WebexDataCenter:
        config: Optional[Configinfo]
        e_tag: Optional[str]


