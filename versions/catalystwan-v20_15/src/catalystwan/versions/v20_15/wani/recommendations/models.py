# Copyright 2024 Cisco Systems, Inc. and its affiliates
from typing import Optional, List
from dataclasses import dataclass, field as _field


@dataclass
class RecommendationsResponseRecommendations:
    count: Optional[int] = _field(default=None)
    site_id: Optional[str] = _field(default=None, metadata={"alias": "siteId"})
    site_name: Optional[str] = _field(default=None, metadata={"alias": "siteName"})


@dataclass
class RecommendationsResponse:
    recommendations: List[RecommendationsResponseRecommendations]
    total_recommendation_count: Optional[int] = _field(
        default=None, metadata={"alias": "totalRecommendationCount"}
    )
