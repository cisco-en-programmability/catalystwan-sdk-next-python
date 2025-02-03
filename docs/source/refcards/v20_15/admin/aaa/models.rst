======
Models
======


.. code:: python

    from typing import List, Any, Optional, Literal, Dict, Union

    AuthOrder = Literal["local", "radius", "tacacs"]


    class Aaa:
        accounting: Optional[bool]
        admin_auth_order: Optional[bool]
        audit_disable: Optional[bool]
        auth_fallback: Optional[bool]
        auth_order: Optional[List[AuthOrder]]


