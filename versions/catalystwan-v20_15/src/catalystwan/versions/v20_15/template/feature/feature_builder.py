# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import TYPE_CHECKING, Any, List, Optional

from catalystwan.abc import RequestAdapterInterface

if TYPE_CHECKING:
    from .clone.clone_builder import CloneBuilder
    from .default.default_builder import DefaultBuilder
    from .definition.definition_builder import DefinitionBuilder
    from .devicetemplates.devicetemplates_builder import DevicetemplatesBuilder
    from .li.li_builder import LiBuilder
    from .master.master_builder import MasterBuilder
    from .migration.migration_builder import MigrationBuilder
    from .object.object_builder import ObjectBuilder
    from .resource_group.resource_group_builder import ResourceGroupBuilder
    from .types.types_builder import TypesBuilder


class FeatureBuilder:
    """
    Builds and executes requests for operations under /template/feature
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def generate_feature_template_list(
        self, summary: Optional[bool] = False, offset: Optional[int] = None, limit: Optional[int] = 0, **kw
    ) -> List[Any]:
        """
        Get feature template list


        Note: In a multitenant vManage system, this API is only available in the Provider view.

        :param summary: Flag to include template definition
        :param offset: Pagination offset
        :param limit: Pagination limit on templateId
        :returns: List[Any]
        """
        params = {
            "summary": summary,
            "offset": offset,
            "limit": limit,
        }
        return self._request_adapter.request(
            "GET", "/dataservice/template/feature", return_type=List[Any], params=params, **kw
        )

    def create_feature_template(self, payload: Optional[Any] = None, **kw) -> Any:
        """
        Create feature template

        :param payload: Feature template
        :returns: Any
        """
        return self._request_adapter.request("POST", "/dataservice/template/feature", payload=payload, **kw)

    def generate_template_by_device_type(self, device_type: str, **kw) -> List[Any]:
        """
        Generate template based on device


        Note: In a multitenant vManage system, this API is only available in the Provider view.

        :param device_type: Device type
        :returns: List[Any]
        """
        params = {
            "deviceType": device_type,
        }
        return self._request_adapter.request(
            "GET", "/dataservice/template/feature/{deviceType}", return_type=List[Any], params=params, **kw
        )

    def edit_feature_template(self, template_id: str, payload: Optional[Any] = None, **kw) -> Any:
        """
        Update feature template


        Note: In a multitenant vManage system, this API is only available in the Provider view.

        :param template_id: Template Id
        :param payload: Template
        :returns: Any
        """
        params = {
            "templateId": template_id,
        }
        return self._request_adapter.request(
            "PUT", "/dataservice/template/feature/{templateId}", params=params, payload=payload, **kw
        )

    def delete_general_template(self, template_id: str, **kw):
        """
        Delete feature template

        :param template_id: Template Id
        :returns: None
        """
        params = {
            "templateId": template_id,
        }
        return self._request_adapter.request(
            "DELETE", "/dataservice/template/feature/{templateId}", params=params, **kw
        )

    @property
    def clone(self) -> CloneBuilder:
        """
        The clone property
        """
        from .clone.clone_builder import CloneBuilder

        return CloneBuilder(self._request_adapter)

    @property
    def default(self) -> DefaultBuilder:
        """
        The default property
        """
        from .default.default_builder import DefaultBuilder

        return DefaultBuilder(self._request_adapter)

    @property
    def definition(self) -> DefinitionBuilder:
        """
        The definition property
        """
        from .definition.definition_builder import DefinitionBuilder

        return DefinitionBuilder(self._request_adapter)

    @property
    def devicetemplates(self) -> DevicetemplatesBuilder:
        """
        The devicetemplates property
        """
        from .devicetemplates.devicetemplates_builder import DevicetemplatesBuilder

        return DevicetemplatesBuilder(self._request_adapter)

    @property
    def li(self) -> LiBuilder:
        """
        The li property
        """
        from .li.li_builder import LiBuilder

        return LiBuilder(self._request_adapter)

    @property
    def master(self) -> MasterBuilder:
        """
        The master property
        """
        from .master.master_builder import MasterBuilder

        return MasterBuilder(self._request_adapter)

    @property
    def migration(self) -> MigrationBuilder:
        """
        The migration property
        """
        from .migration.migration_builder import MigrationBuilder

        return MigrationBuilder(self._request_adapter)

    @property
    def object(self) -> ObjectBuilder:
        """
        The object property
        """
        from .object.object_builder import ObjectBuilder

        return ObjectBuilder(self._request_adapter)

    @property
    def resource_group(self) -> ResourceGroupBuilder:
        """
        The resource-group property
        """
        from .resource_group.resource_group_builder import ResourceGroupBuilder

        return ResourceGroupBuilder(self._request_adapter)

    @property
    def types(self) -> TypesBuilder:
        """
        The types property
        """
        from .types.types_builder import TypesBuilder

        return TypesBuilder(self._request_adapter)
