======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class DpiAppResponseData:
        application: Optional[str]
        octets: Optional[int]


    class DpiAppResponseHeaderChart:
        series: Optional[List[str]]
        title: Optional[str]
        x_axis: Optional[List[str]]
        x_axis_label: Optional[str]
        y_axis: Optional[List[str]]
        y_axis_label: Optional[str]


    class DpiAppResponseHeaderColumns:
        data_type: Optional[str]
        hideable: Optional[bool]
        property: Optional[str]
        title: Optional[str]


    class DpiAppResponseHeaderFields:
        data_type: Optional[str]
        property: Optional[str]


    class DpiAppResponseHeaderViewKeys:
        preference_key: Optional[str]
        unique_key: Optional[List[str]]


    class DpiAppResponseHeader:
        chart: Optional[DpiAppResponseHeaderChart]
        columns: Optional[List[DpiAppResponseHeaderColumns]]
        fields: Optional[List[DpiAppResponseHeaderFields]]
        generated_on: Optional[int]
        view_keys: Optional[DpiAppResponseHeaderViewKeys]


    class DpiAppResponse:
        data: Optional[List[DpiAppResponseData]]
        header: Optional[DpiAppResponseHeader]


