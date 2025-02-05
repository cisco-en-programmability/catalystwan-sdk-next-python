======
Models
======


.. code:: python

    from typing import Union, Dict, Optional, Literal, List, Any

    SortOrderParam = Literal["ASC", "Asc", "DESC", "Desc", "asc", "desc"]


    class PowerConsumptionRespData:
        cost: Optional[int]
        count: Optional[int]
        emission: Optional[int]
        entry_time: Optional[int]
        power_usage: Optional[int]


    class ChartObject:
        series: Optional[List[str]]
        title: Optional[str]
        x_axis: Optional[List[str]]
        x_axis_label: Optional[str]
        y_axis: Optional[List[str]]
        y_axis_label: Optional[str]


    class PowerConsumptionColumns:
        data_type: str
        property: str
        title: str
        display_format: Optional[str]
        hideable: Optional[bool]
        input_format: Optional[str]
        is_display: Optional[bool]
        min_width: Optional[int]
        width: Optional[int]


    class GetStatDataFields:
        data_type: Optional[str]
        property: Optional[str]


    class PowerConsumptionViewKeys:
        preference_key: Optional[str]
        unique_key: Optional[List[str]]


    class PowerConsumptionRespHeader:
        chart: Optional[ChartObject]
        columns: Optional[PowerConsumptionColumns]
        fields: Optional[GetStatDataFields]
        generated_on: Optional[int]
        view_keys: Optional[PowerConsumptionViewKeys]


    class PowerConsumptionResp:
        data: Optional[List[PowerConsumptionRespData]]
        entry_time_list: Optional[List[int]]
        header: Optional[PowerConsumptionRespHeader]


