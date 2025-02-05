======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class CreateResponse:
        """
        Response from PxGrid node creation on ISE
        """

        node_name: Optional[str]
        password: Optional[str]
        user_name: Optional[str]


    class CreateBody:
        """
        Body for PxGrid node create on ISE
        """

        node_name: Optional[str]


