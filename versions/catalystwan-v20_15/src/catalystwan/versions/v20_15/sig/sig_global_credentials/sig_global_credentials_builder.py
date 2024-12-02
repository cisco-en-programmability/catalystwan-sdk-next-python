# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from catalystwan.abc import RequestAdapterInterface

from .models import FeatureTemplateType


class SigGlobalCredentialsBuilder:
    """
    Builds and executes requests for operations under /sig/sigGlobalCredentials
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_sig_global_credentials(
        self, feature_template_type: str, **kw
    ) -> FeatureTemplateType:
        """
        Get sig global credentials

        :param feature_template_type: Feature template type
        :returns: FeatureTemplateType
        """
        params = {
            "featureTemplateType": feature_template_type,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/sig/sigGlobalCredentials/{featureTemplateType}",
            return_type=FeatureTemplateType,
            params=params,
            **kw,
        )
