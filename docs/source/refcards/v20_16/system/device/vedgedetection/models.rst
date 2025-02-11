======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class VedgeCheckResponseData:
        """
        data field
        """

        v_edge_device_present: Optional[bool]


    class VedgeCheckResponseHeaderColumnsColor:
        key: Optional[str]
        property: Optional[str]
        value: Optional[str]


    class VedgeCheckResponseHeaderColumnsKeyvalue:
        key: Optional[str]
        value: Optional[str]


    class VedgeCheckResponseHeaderColumnsSort:
        direction: Optional[str]
        priority: Optional[int]


    class VedgeCheckResponseHeaderColumns:
        action_column: Optional[bool]
        array_data_type: Optional[str]
        color: Optional[VedgeCheckResponseHeaderColumnsColor]
        color_property: Optional[str]
        data_type: Optional[str]
        default_property_key: Optional[str]
        default_property_value: Optional[str]
        display: Optional[str]
        display_format: Optional[str]
        editable: Optional[bool]
        hideable: Optional[bool]
        host_value_type: Optional[str]
        icon: Optional[List[VedgeCheckResponseHeaderColumnsKeyvalue]]
        icon_property: Optional[str]
        input_format: Optional[str]
        is_left_pinned: Optional[bool]
        is_pinned: Optional[bool]
        keyvalue: Optional[List[VedgeCheckResponseHeaderColumnsKeyvalue]]
        keyvalue_property: Optional[str]
        max_width: Optional[int]
        min_width: Optional[int]
        prepended_string: Optional[bool]
        property: Optional[str]
        sort: Optional[VedgeCheckResponseHeaderColumnsSort]
        title: Optional[str]
        tool_tip_property: Optional[str]
        visible: Optional[bool]
        width: Optional[int]


    class VedgeCheckResponseHeaderFields:
        # dataType field
        data_type: Optional[str]
        # display field
        display: Optional[str]
        # property field
        property: Optional[str]


    class VedgeCheckResponseHeaderViewKeys:
        unique_key: Optional[List[str]]


    class VedgeCheckResponseHeader:
        """
        header field
        """

        columns: Optional[List[VedgeCheckResponseHeaderColumns]]
        fields: Optional[List[VedgeCheckResponseHeaderFields]]
        generated_on: Optional[int]
        view_keys: Optional[VedgeCheckResponseHeaderViewKeys]


    class VedgeCheckResponse:
        # data field
        data: Optional[VedgeCheckResponseData]
        # header field
        header: Optional[VedgeCheckResponseHeader]


