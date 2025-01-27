# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from catalystwan.abc import RequestAdapterInterface

from . import models
from .models import InstallPkg

if TYPE_CHECKING:
    from .image_count.image_count_builder import ImageCountBuilder
    from .metadata.metadata_builder import MetadataBuilder
    from .signature.signature_builder import SignatureBuilder
    from .utdsignature.utdsignature_builder import UtdsignatureBuilder


class PackageBuilder:
    """
    Builds and executes requests for operations under /device/action/software/package
    """

    m = models

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def install_pkg(self, payload: Optional[InstallPkg] = None, **kw):
        """
        Install software package

        :param payload: software Package File
        :returns: None
        """
        return self._request_adapter.request(
            "POST", "/dataservice/device/action/software/package", payload=payload, **kw
        )

    def download_package_file(
        self, file_name: str, image_type: Optional[str] = "software", **kw
    ) -> str:
        """
        Download software package file

        :param file_name: software package file name
        :param image_type: Image type
        :returns: str
        """
        params = {
            "fileName": file_name,
            "imageType": image_type,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/device/action/software/package/{fileName}",
            return_type=str,
            params=params,
            **kw,
        )

    def process_software_image(self, image_type: str, payload: Optional[InstallPkg] = None, **kw):
        """
        Install software image package

        :param image_type: Image type
        :param payload: image File
        :returns: None
        """
        params = {
            "imageType": image_type,
        }
        return self._request_adapter.request(
            "POST",
            "/dataservice/device/action/software/package/{imageType}",
            params=params,
            payload=payload,
            **kw,
        )

    @property
    def image_count(self) -> ImageCountBuilder:
        """
        The imageCount property
        """
        from .image_count.image_count_builder import ImageCountBuilder

        return ImageCountBuilder(self._request_adapter)

    @property
    def metadata(self) -> MetadataBuilder:
        """
        The metadata property
        """
        from .metadata.metadata_builder import MetadataBuilder

        return MetadataBuilder(self._request_adapter)

    @property
    def signature(self) -> SignatureBuilder:
        """
        The signature property
        """
        from .signature.signature_builder import SignatureBuilder

        return SignatureBuilder(self._request_adapter)

    @property
    def utdsignature(self) -> UtdsignatureBuilder:
        """
        The utdsignature property
        """
        from .utdsignature.utdsignature_builder import UtdsignatureBuilder

        return UtdsignatureBuilder(self._request_adapter)
