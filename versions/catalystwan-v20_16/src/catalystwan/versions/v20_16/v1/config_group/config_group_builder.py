# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from catalystwan.abc import RequestAdapterInterface

from . import models
from .models import ConfigGroup

if TYPE_CHECKING:
    from .device.device_builder import DeviceBuilder
    from .rules.rules_builder import RulesBuilder


class ConfigGroupBuilder:
    """
    Builds and executes requests for operations under /v1/config-group
    """

    m = models

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_config_group_by_solution(
        self, solution: Optional[str] = None, name: Optional[str] = None, **kw
    ) -> List[ConfigGroup]:
        """
        Get a Configuration Group by Solution

        :param solution: Solution
        :param name: Name
        :returns: List[ConfigGroup]
        """
        params = {
            "solution": solution,
            "name": name,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/config-group",
            return_type=List[ConfigGroup],
            params=params,
            **kw,
        )

    def create_config_group(self, payload: Optional[str] = None, **kw) -> str:
        """
        Create a new Configuration Group

        :param payload: Config Group
        :returns: str
        """
        return self._request_adapter.request(
            "POST", "/dataservice/v1/config-group", return_type=str, payload=payload, **kw
        )

    def get_config_group(
        self, config_group_id: str, device_list: Optional[bool] = True, **kw
    ) -> ConfigGroup:
        """
        Get a Configuration Group by ID

        :param config_group_id: Config group id
        :param device_list: Including associated devices list
        :returns: ConfigGroup
        """
        params = {
            "configGroupId": config_group_id,
            "deviceList": device_list,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/config-group/{configGroupId}",
            return_type=ConfigGroup,
            params=params,
            **kw,
        )

    def edit_config_group(self, config_group_id: str, payload: Optional[str] = None, **kw) -> str:
        """
        Edit a Configuration Group

        :param config_group_id: Config group id
        :param payload: Config Group
        :returns: str
        """
        params = {
            "configGroupId": config_group_id,
        }
        return self._request_adapter.request(
            "PUT",
            "/dataservice/v1/config-group/{configGroupId}",
            return_type=str,
            params=params,
            payload=payload,
            **kw,
        )

    def delete_config_group(
        self, config_group_id: str, delete_profiles: Optional[bool] = None, **kw
    ):
        """
        Delete Config Group

        :param config_group_id: Config group id
        :param delete_profiles: Delete profiles
        :returns: None
        """
        params = {
            "configGroupId": config_group_id,
            "deleteProfiles": delete_profiles,
        }
        return self._request_adapter.request(
            "DELETE", "/dataservice/v1/config-group/{configGroupId}", params=params, **kw
        )

    @property
    def device(self) -> DeviceBuilder:
        """
        The device property
        """
        from .device.device_builder import DeviceBuilder

        return DeviceBuilder(self._request_adapter)

    @property
    def rules(self) -> RulesBuilder:
        """
        The rules property
        """
        from .rules.rules_builder import RulesBuilder

        return RulesBuilder(self._request_adapter)
