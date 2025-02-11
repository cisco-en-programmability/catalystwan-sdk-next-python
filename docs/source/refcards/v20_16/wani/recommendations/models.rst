======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class RecommendationsResponseRecommendations:
        count: Optional[int]
        site_id: Optional[str]
        site_name: Optional[str]


    class RecommendationsResponse:
        recommendations: List[RecommendationsResponseRecommendations]
        total_recommendation_count: Optional[int]


