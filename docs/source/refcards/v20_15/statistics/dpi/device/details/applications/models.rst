======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class DeviceAppDetailResponseData:
        application: Optional[str]
        create_time: Optional[int]
        dest_ip: Optional[str]
        dest_port: Optional[int]
        device_model: Optional[str]
        entry_time: Optional[int]
        expire_time: Optional[int]
        family: Optional[str]
        host_name: Optional[str]
        id: Optional[str]
        ip_proto: Optional[int]
        octets: Optional[int]
        packets: Optional[int]
        source_ip: Optional[str]
        source_port: Optional[int]
        vdevice_name: Optional[str]
        vip_idx: Optional[int]
        vpn_id: Optional[int]


    class DeviceAppDetailResponseHeaderChart:
        series: Optional[List[str]]
        title: Optional[str]
        x_axis: Optional[List[str]]
        x_axis_label: Optional[str]
        y_axis: Optional[List[str]]
        y_axis_label: Optional[str]


    class DeviceAppResponseHeaderColumns:
        data_type: Optional[str]
        property: Optional[str]
        title: Optional[str]


    class DeviceAppResponseHeaderFields:
        data_type: Optional[str]
        property: Optional[str]


    class DeviceAppDetailResponseHeaderViewKeys:
        preference_key: Optional[str]
        unique_key: Optional[List[str]]


    class DeviceAppDetailResponseHeader:
        chart: Optional[DeviceAppDetailResponseHeaderChart]
        columns: Optional[List[DeviceAppResponseHeaderColumns]]
        fields: Optional[List[DeviceAppResponseHeaderFields]]
        generated_on: Optional[int]
        view_keys: Optional[DeviceAppDetailResponseHeaderViewKeys]


    class DeviceAppDetailResponsePageInfo:
        count: Optional[int]
        end_time: Optional[str]
        start_time: Optional[str]


    class DeviceAppDetailResponse:
        data: Optional[List[DeviceAppDetailResponseData]]
        header: Optional[DeviceAppDetailResponseHeader]
        page_info: Optional[DeviceAppDetailResponsePageInfo]


