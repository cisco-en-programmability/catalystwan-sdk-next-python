======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class SecurityGroup:
        description: Optional[str]
        id: Optional[str]
        name: Optional[str]
        tag: Optional[int]


    class SgtResponse:
        """
        Security Groups Returned from ISE
        """

        security_groups: Optional[List[SecurityGroup]]


