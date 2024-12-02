# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Any, Type, TYPE_CHECKING
from catalystwan.abc import RequestAdapterInterface
import logging

if TYPE_CHECKING:
    from .image_properties.image_properties_builder import ImagePropertiesBuilder
    from .images.images_builder import ImagesBuilder
    from .package.package_builder import PackageBuilder
    from .remoteserver.remoteserver_builder import RemoteserverBuilder
    from .vedge.vedge_builder import VedgeBuilder
    from .version.version_builder import VersionBuilder
    from .vnfproperties.vnfproperties_builder import VnfpropertiesBuilder
    from .ztp.ztp_builder import ZtpBuilder


class SoftwareBuilder:
    """
    Builds and executes requests for operations under /device/action/software
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def find_software_images(self, **kw) -> Any:
        """
        Get software images

        :returns: Any
        """
        return self._request_adapter.request(
            "GET", "/dataservice/device/action/software", **kw
        )

    @property
    def create_image_url(self):
        class create_image_url_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[Any] = None, **kw):
                """
                Create software image URL

                :param payload: Request body for Device bootstrap configuration
                :returns: None
                """
                return self._request_adapter.request(
                    "POST", "/dataservice/device/action/software", payload=payload, **kw
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return create_image_url_(self._request_adapter)

    @property
    def update_image_url(self):
        class update_image_url_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, version_id: str, payload: Optional[Any] = None, **kw):
                """
                Update software image URL

                :param version_id: Version
                :param payload: Update software image request payload
                :returns: None
                """
                logging.warning("Operation: %s is deprecated", "updateImageURL")
                params = {
                    "versionId": version_id,
                }
                return self._request_adapter.request(
                    "PUT",
                    "/dataservice/device/action/software/{versionId}",
                    params=params,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return update_image_url_(self._request_adapter)

    def delete_image_url(self, version_id: str, **kw):
        """
        Delete software image URL

        :param version_id: Version
        :returns: None
        """
        params = {
            "versionId": version_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/device/action/software/{versionId}",
            params=params,
            **kw,
        )

    @property
    def image_properties(self) -> ImagePropertiesBuilder:
        """
        The imageProperties property
        """
        from .image_properties.image_properties_builder import ImagePropertiesBuilder

        return ImagePropertiesBuilder(self._request_adapter)

    @property
    def images(self) -> ImagesBuilder:
        """
        The images property
        """
        from .images.images_builder import ImagesBuilder

        return ImagesBuilder(self._request_adapter)

    @property
    def package(self) -> PackageBuilder:
        """
        The package property
        """
        from .package.package_builder import PackageBuilder

        return PackageBuilder(self._request_adapter)

    @property
    def remoteserver(self) -> RemoteserverBuilder:
        """
        The remoteserver property
        """
        from .remoteserver.remoteserver_builder import RemoteserverBuilder

        return RemoteserverBuilder(self._request_adapter)

    @property
    def vedge(self) -> VedgeBuilder:
        """
        The vedge property
        """
        from .vedge.vedge_builder import VedgeBuilder

        return VedgeBuilder(self._request_adapter)

    @property
    def version(self) -> VersionBuilder:
        """
        The version property
        """
        from .version.version_builder import VersionBuilder

        return VersionBuilder(self._request_adapter)

    @property
    def vnfproperties(self) -> VnfpropertiesBuilder:
        """
        The vnfproperties property
        """
        from .vnfproperties.vnfproperties_builder import VnfpropertiesBuilder

        return VnfpropertiesBuilder(self._request_adapter)

    @property
    def ztp(self) -> ZtpBuilder:
        """
        The ztp property
        """
        from .ztp.ztp_builder import ZtpBuilder

        return ZtpBuilder(self._request_adapter)
