======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class Policy:
        id: Optional[str]
        name: Optional[str]
        type_: Optional[str]


    class ApplicationList:
        id: Optional[str]
        name: Optional[str]
        policies: Optional[List[Policy]]
        type_: Optional[str]


    class Application:
        application_lists: Optional[List[ApplicationList]]
        id: Optional[str]
        name: Optional[str]
        type_: Optional[str]


    class ApplicationRequestDetails:
        app_name: Optional[str]


    class ExtendedApplicationRequestData:
        data: Optional[List[ApplicationRequestDetails]]
        select_all: Optional[bool]


