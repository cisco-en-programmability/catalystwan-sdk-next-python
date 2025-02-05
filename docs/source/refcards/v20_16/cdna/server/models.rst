======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class EnrollOtpResponse:
        """
        Enroll CDNA Server Response.
        """

        auth_token: Optional[str]
        cdna_server_ip: Optional[str]
        cline_id: Optional[str]
        enrolled: Optional[bool]
        last_updated: Optional[str]
        member_id: Optional[str]
        token_url: Optional[str]


    class EnrollOtpSettings:
        token: str


