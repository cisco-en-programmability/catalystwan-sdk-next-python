======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class InterconnectSshKeyInfo:
        # Ssh Key Name
        key_name: Optional[str]
        # Ssh key Type
        key_type: Optional[str]
        # Ssh Key Value
        key_value: Optional[str]


    class InlineResponse20016:
        ssh_keys: Optional[List[InterconnectSshKeyInfo]]


