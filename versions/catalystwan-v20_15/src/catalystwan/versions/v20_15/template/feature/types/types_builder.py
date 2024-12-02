# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import List, Any, TYPE_CHECKING
from catalystwan.abc import RequestAdapterInterface
from .models import TypeParam

if TYPE_CHECKING:
    from .definition.definition_builder import DefinitionBuilder


class TypesBuilder:
    """
    Builds and executes requests for operations under /template/feature/types
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def generate_template_types(self, type_: TypeParam, **kw) -> List[Any]:
        """
        Generate template types


        Note: In a multitenant vManage system, this API is only available in the Provider view.

        :param type_: Device type
        :returns: List[Any]
        """
        params = {
            "type": type_,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/template/feature/types",
            return_type=List[Any],
            params=params,
            **kw,
        )

    @property
    def definition(self) -> DefinitionBuilder:
        """
        The definition property
        """
        from .definition.definition_builder import DefinitionBuilder

        return DefinitionBuilder(self._request_adapter)
