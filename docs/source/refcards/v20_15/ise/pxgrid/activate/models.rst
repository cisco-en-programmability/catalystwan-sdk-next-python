======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class ActivateResponse:
        """
        Response from PxGrid node activation on ISE, account PENDING on activated ENABLED after approve
        """

        account_state: Optional[str]
        version: Optional[str]


    class ActivateBody:
        """
        Body for PxGrid node activate on ISE
        """

        description: Optional[str]
        px_grid_password: Optional[str]
        px_grid_user_name: Optional[str]


