======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class CgwVpnsResponse:
        account_name: Optional[str]
        host_vpc_id: Optional[str]
        # Returned for AWS/AWS_GOVCLOUD/GCP
        host_vpc_name: Optional[str]
        tag: Optional[str]
        # Returned for AWS/AWS_GOVCLOUD/GCP
        tunnel_count: Optional[int]
        vpn_id: Optional[str]


