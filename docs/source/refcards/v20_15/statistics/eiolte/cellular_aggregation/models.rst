======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

    Order = Literal["asc", "desc"]

    OrderType = Literal["count", "key"]

    Type = Literal[
        "day",
        "hour",
        "minute",
        "month",
        "quater",
        "second",
        "week",
        "year",
    ]

    CellularAggregationType = Literal[
        "argMax",
        "avg",
        "cardinality",
        "count",
        "max",
        "min",
        "sum",
        "top_hits",
    ]

    Condition = Literal["AND", "OR"]

    Operator = Literal[
        "between",
        "equal",
        "greater",
        "greater_or_equal",
        "hasAny",
        "in",
        "last_n_days",
        "last_n_hours",
        "last_n_weeks",
        "less",
        "less_or_equal",
        "not_equal",
        "not_in",
        "starts_with",
    ]

    EiolteCellularAggregationType = Literal[
        "array",
        "boolean",
        "date",
        "double",
        "int",
        "long",
        "number",
        "specialString",
        "string",
    ]


    class DbQueryAggregationFieldObject:
        property: Any
        size: int
        order: Optional[Order]
        order_type: Optional[OrderType]
        sequence: Optional[int]
        type_: Optional[str]


    class DbQueryAggregationHistogramObject:
        order: Order  # pytype: disable=annotation-type-mismatch
        property: Any
        type_: Type
        interval: Optional[int]
        mindoccount: Optional[int]


    class DbQueryAggregationMetricObject:
        property: Any
        type_: CellularAggregationType
        order: Optional[str]
        sequence: Optional[str]
        size: Optional[str]


    class DbQueryAggregationObject:
        field: Optional[List[DbQueryAggregationFieldObject]]
        histogram: Optional[DbQueryAggregationHistogramObject]
        metrics: Optional[List[DbQueryAggregationMetricObject]]


    class DbQueryRuleObject:
        condition: Optional[Condition]
        field: Optional[Any]
        operator: Optional[Operator]
        rules: Optional[List["DbQueryRuleObject"]]
        type_: Optional[EiolteCellularAggregationType]
        value: Optional[List[str]]


    class DbQuerySpecObject:
        rules: List[DbQueryRuleObject]
        condition: Optional[Condition]
        field: Optional[Any]
        operator: Optional[Operator]
        type_: Optional[EiolteCellularAggregationType]
        value: Optional[List[str]]


    class DbQuerySortObject:
        field: Any
        order: Order  # pytype: disable=annotation-type-mismatch
        type_: Optional[EiolteCellularAggregationType]


    class StatisticsDbQueryParam:
        """
        Statistics search DB Query JSON object
        """

        aggregation: Optional[DbQueryAggregationObject]
        category: Optional[str]
        fields: Optional[List[Any]]
        plot_data: Optional[List[str]]
        query: Optional[DbQuerySpecObject]
        size: Optional[int]
        sort: Optional[List[DbQuerySortObject]]


