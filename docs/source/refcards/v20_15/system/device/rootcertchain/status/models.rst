======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class GetRootCertStatusAllData:
        last_update_time: Optional[str]
        root_cert_md5: Optional[str]
        root_cert_status: Optional[str]


    class GetRootCertStatusAll:
        data: Optional[List[GetRootCertStatusAllData]]


