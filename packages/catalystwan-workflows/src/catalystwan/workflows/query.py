from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field as _field
from typing import Any, List, Literal, Optional, Union

Order = Literal["asc", "desc"]

OrderType = Literal["count", "key"]

TimeType = Literal["day", "hour", "minute", "month", "quater", "second", "week", "year"]

AggregationMetricType = Literal[
    "argMax", "avg", "cardinality", "count", "max", "min", "sum", "top_hits"
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

FieldType = Literal[
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


@dataclass
class QueryAggregationField:
    property: Any
    size: int
    order: Optional[Order] = _field(default=None)
    order_type: Optional[OrderType] = _field(
        default=None, metadata={"alias": "orderType"}
    )
    sequence: Optional[int] = _field(default=None)
    type_: Optional[str] = _field(default=None, metadata={"alias": "type"})


@dataclass
class QueryAggregationHistogram:
    order: Order
    property: Any
    type_: TimeType = _field(metadata={"alias": "type"})
    interval: Optional[int] = _field(default=None)
    mindoccount: Optional[int] = _field(default=None)


@dataclass
class QueryAggregationMetric:
    property: Any
    type_: AggregationMetricType = _field(metadata={"alias": "type"})
    order: Optional[str] = _field(default=None)
    sequence: Optional[str] = _field(default=None)
    size: Optional[str] = _field(default=None)


@dataclass
class QueryAggregation:
    field: Optional[List[QueryAggregationField]] = _field(default=None)
    histogram: Optional[QueryAggregationHistogram] = _field(default=None)
    metrics: Optional[List[QueryAggregationMetric]] = _field(default=None)


@dataclass
class QueryRule:
    field: str
    operator: Operator
    type_: FieldType = _field(metadata={"alias": "type"})
    value: List[str]


@dataclass
class QuerySpec:
    condition: Condition
    rules: List[Union[QueryRule, QuerySpec]] = _field(default_factory=list)

    def add_query_rule(
        self, field: str, operator: Operator, field_type: FieldType, value: List[str]
    ) -> QueryRule:
        query_rule = QueryRule(
            field=field, operator=operator, type_=field_type, value=value
        )
        self.rules.append(query_rule)
        return query_rule

    def add_query_spec_rule(self, condition: Condition):
        query_spec = QuerySpec(rules=[], condition=condition)
        self.rules.append(query_spec)
        return query_spec


@dataclass
class QuerySort:
    field: str
    order: Order
    type_: Optional[FieldType] = _field(default=None, metadata={"alias": "type"})


@dataclass
class Query:
    aggregation: Optional[QueryAggregation] = _field(default=None)
    category: Optional[str] = _field(default=None)
    fields: Optional[List[Any]] = _field(default=None)
    plot_data: Optional[List[str]] = _field(default=None)
    query: Optional[QuerySpec] = _field(default=None)
    size: Optional[int] = _field(default=None)
    sort: Optional[List[QuerySort]] = _field(default=None)

    def add_query(self, condition: Condition) -> QuerySpec:
        query = QuerySpec(rules=[], condition=condition)
        self.query = query
        return query

    def add_sort(self, field: str, order: Order, field_type: FieldType) -> QuerySort:
        if not self.sort:
            self.sort = []

        query_sort = QuerySort(field=field, order=order, type_=field_type)
        self.sort.append(query_sort)
        return query_sort
