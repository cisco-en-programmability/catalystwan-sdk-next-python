======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class DeviceCpuCount:
        attribute_field: Optional[str]
        enable: Optional[bool]


    class DeviceInterface:
        day0: Optional[List[str]]
        lan: Optional[List[str]]
        mgmt: Optional[List[str]]
        wan: Optional[List[str]]


    class DeviceModelsData:
        cpu_count_attribute: Optional[DeviceCpuCount]
        device_class: Optional[str]
        device_type: Optional[str]
        display_name: Optional[str]
        interfaces: Optional[DeviceInterface]
        is_cli_supported: Optional[bool]
        name: Optional[str]
        onboard_cert: Optional[bool]
        template_class: Optional[str]
        template_supported: Optional[bool]


    class DeviceResponseHeader:
        generated_on: Optional[int]


    class DeviceModelsResponse:
        data: Optional[List[DeviceModelsData]]
        header: Optional[DeviceResponseHeader]


