# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import List, TYPE_CHECKING
from catalystwan.abc import RequestAdapterInterface
from .models import AdminTechsRes

if TYPE_CHECKING:
    from .inprogress.inprogress_builder import InprogressBuilder
    from .upload.upload_builder import UploadBuilder


class AdmintechsBuilder:
    """
    Builds and executes requests for operations under /device/tools/admintechs
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def list_admin_techs(self, **kw) -> List[AdminTechsRes]:
        """
        Get device admin-tech information

        :returns: List[AdminTechsRes]
        """
        return self._request_adapter.request(
            "GET",
            "/dataservice/device/tools/admintechs",
            return_type=List[AdminTechsRes],
            **kw,
        )

    @property
    def inprogress(self) -> InprogressBuilder:
        """
        The inprogress property
        """
        from .inprogress.inprogress_builder import InprogressBuilder

        return InprogressBuilder(self._request_adapter)

    @property
    def upload(self) -> UploadBuilder:
        """
        The upload property
        """
        from .upload.upload_builder import UploadBuilder

        return UploadBuilder(self._request_adapter)
