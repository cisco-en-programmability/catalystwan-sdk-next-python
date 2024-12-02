======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class LinkObject:
        href: Optional[str]
        rel: Optional[str]
        type_: Optional[str]


    class VersionInformation:
        current_server_version: Optional[str]
        link: Optional[LinkObject]
        supported_versions: Optional[str]


    class ConnectResponse:
        """
        Response from ISE ERS version info api
        """

        version_info: Optional[VersionInformation]


