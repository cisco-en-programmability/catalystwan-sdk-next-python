======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class DataUsage:
        """
        Data usage limit info .
        """

        usage_limit: Optional[int]
        usage_limit_unit: Optional[str]
        use_default_rating: Optional[bool]


    class RatePlan:
        """
        List of rate plans.
        """

        # Name of the rate plan.
        name: str
        # Rate plan type.
        type_: str
        # Data usage limit info .
        data_usage: Optional[DataUsage]


    class RatePlansResponse:
        # Indicator whether the payload is the last payload.
        last_page: bool
        # Page Number.
        page_number: int
        # List of rate plans.
        rate_plans: List[RatePlan]


