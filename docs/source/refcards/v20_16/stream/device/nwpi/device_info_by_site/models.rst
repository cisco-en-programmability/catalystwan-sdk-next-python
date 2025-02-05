======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class DeviceInfoResponsePayloadDataDevices:
        device_id: Optional[str]
        device_model: Optional[str]
        device_type: Optional[str]
        host_name: Optional[str]
        latitude: Optional[str]
        layout_level: Optional[int]
        local_system_ip: Optional[str]
        longitude: Optional[str]
        site_id: Optional[str]
        system_ip: Optional[str]
        uuid: Optional[str]
        version: Optional[str]


    class DeviceInfoResponsePayloadDataInterfaces:
        ifname: Optional[str]
        ip_address: Optional[str]
        vdevice_host_name: Optional[str]
        vdevice_name: Optional[str]
        vpn_id: Optional[str]


    class DeviceInfoResponsePayloadDataModels:
        device_class: Optional[str]
        name: Optional[str]


    class DeviceInfoResponsePayloadData:
        devices: Optional[List[DeviceInfoResponsePayloadDataDevices]]
        interfaces: Optional[
            List[DeviceInfoResponsePayloadDataInterfaces]
        ]
        models: Optional[List[DeviceInfoResponsePayloadDataModels]]


