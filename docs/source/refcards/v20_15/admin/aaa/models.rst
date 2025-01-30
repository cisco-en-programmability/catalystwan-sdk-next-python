======
Models
======


.. code:: python

    from typing import List, Dict, Optional, Union, Any, Literal

    AuthOrder = Literal["local", "radius", "tacacs"]


    class Aaa:
        accounting: Optional[bool]
        admin_auth_order: Optional[bool]
        audit_disable: Optional[bool]
        auth_fallback: Optional[bool]
        auth_order: Optional[List[AuthOrder]]


