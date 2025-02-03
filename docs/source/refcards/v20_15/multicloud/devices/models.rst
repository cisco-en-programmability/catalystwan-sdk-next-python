======
Models
======


.. code:: python

    from typing import List, Any, Optional, Literal, Dict, Union

    CloudTypeParam = Literal[
        "AWS", "AWS_GOVCLOUD", "AZURE", "AZURE_GOVCLOUD", "GCP"
    ]


    class DeviceInfoExtendedResponse:
        cloud_gateway_name: Optional[str]
        config_status_message: Optional[str]
        configured_system_ip: Optional[str]
        device_model: Optional[str]
        device_type: Optional[str]
        host_name: Optional[str]
        last_updated: Optional[int]
        local_system_ip: Optional[str]
        reachability: Optional[str]
        site_id: Optional[str]
        status: Optional[str]
        system_ip: Optional[str]
        uptime_date: Optional[int]
        uuid: Optional[str]
        version: Optional[str]


