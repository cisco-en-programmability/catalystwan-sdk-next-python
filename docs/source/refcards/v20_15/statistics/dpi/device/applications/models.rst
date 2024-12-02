======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class DeviceAppResponseData:
        octets: Optional[int]
        vdevice_name: Optional[str]


    class DeviceAppResponseHeaderChart:
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


    class DeviceAppResponseHeaderViewKeys:
        preference_key: Optional[str]
        unique_key: Optional[List[str]]


    class DeviceAppResponseHeader:
        chart: Optional[DeviceAppResponseHeaderChart]
        columns: Optional[List[DeviceAppResponseHeaderColumns]]
        fields: Optional[List[DeviceAppResponseHeaderFields]]
        generated_on: Optional[int]
        view_keys: Optional[DeviceAppResponseHeaderViewKeys]


    class DeviceAppResponse:
        data: Optional[List[DeviceAppResponseData]]
        header: Optional[DeviceAppResponseHeader]


