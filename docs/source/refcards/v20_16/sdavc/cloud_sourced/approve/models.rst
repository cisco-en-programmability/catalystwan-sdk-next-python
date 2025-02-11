======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class DefaultSuccessResponse:
        message: Optional[str]
        success: Optional[bool]


    class ApplicationRequestDetails:
        app_name: Optional[str]


    class ExtendedApplicationRequestData:
        data: Optional[List[ApplicationRequestDetails]]
        select_all: Optional[bool]


