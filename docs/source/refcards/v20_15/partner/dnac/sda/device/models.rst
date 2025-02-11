======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    Reachability = Literal["reachable", "unreachable"]

    Status = Literal["error", "new", "normal", "warning"]

    Validity = Literal["invalid", "prestaging", "staging", "valid"]


    class Loopback:
        interface_ip: Optional[str]
        interface_name: Optional[str]


    class Device:
        chassis_serial_number: Optional[str]
        configured_aaa_user: Optional[List[str]]
        device_id: Optional[str]
        device_model: Optional[str]
        device_os: Optional[str]
        device_type: Optional[str]
        devices_attached: Optional[int]
        discovered_device_interfaces: Optional[List[str]]
        host_name: Optional[str]
        loopback: Optional[List[Loopback]]
        personality: Optional[str]
        platform: Optional[str]
        reachability: Optional[Reachability]
        registration_date: Optional[int]
        serial_number: Optional[str]
        site_id: Optional[str]
        state: Optional[str]
        status: Optional[Status]
        system_ip: Optional[str]
        template_status: Optional[str]
        uuid: Optional[str]
        validity: Optional[Validity]
        version: Optional[str]
        wan_interfaces: Optional[List[str]]


    class VpnListResHeader:
        generated_on: Optional[int]


    class SdaDevicesRes:
        data: Optional[List[Device]]
        header: Optional[VpnListResHeader]


