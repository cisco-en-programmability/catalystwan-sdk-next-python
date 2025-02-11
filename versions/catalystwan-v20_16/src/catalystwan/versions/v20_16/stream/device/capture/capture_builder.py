# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import TYPE_CHECKING

from catalystwan.abc import RequestAdapterInterface

from . import models
from .models import CreatePacketCaptureReq, FormPacketCaptureRes, PacketCaptureInfo

if TYPE_CHECKING:
    from .disable.disable_builder import DisableBuilder
    from .download.download_builder import DownloadBuilder
    from .forcedisbale.forcedisbale_builder import ForcedisbaleBuilder
    from .start.start_builder import StartBuilder
    from .status.status_builder import StatusBuilder
    from .stop.stop_builder import StopBuilder
    from .vnics_info.vnics_info_builder import VnicsInfoBuilder


class CaptureBuilder:
    """
    Builds and executes requests for operations under /stream/device/capture
    """

    m = models

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_session_info_capture(self, payload: CreatePacketCaptureReq, **kw) -> PacketCaptureInfo:
        """
        Create packet capture session

        :param payload: Packet Capture Parameters
        :returns: PacketCaptureInfo
        """
        return self._request_adapter.request(
            "POST",
            "/dataservice/stream/device/capture",
            return_type=PacketCaptureInfo,
            payload=payload,
            **kw,
        )

    def form_post_packet_capture(
        self, device_uuid: str, session_id: str, **kw
    ) -> FormPacketCaptureRes:
        """
        Form post packet capture

        :param device_uuid: Device uuid
        :param session_id: Session id
        :returns: FormPacketCaptureRes
        """
        params = {
            "deviceUUID": device_uuid,
            "sessionId": session_id,
        }
        return self._request_adapter.request(
            "POST",
            "/dataservice/stream/device/capture/{deviceUUID}/{sessionId}",
            return_type=FormPacketCaptureRes,
            params=params,
            **kw,
        )

    @property
    def disable(self) -> DisableBuilder:
        """
        The disable property
        """
        from .disable.disable_builder import DisableBuilder

        return DisableBuilder(self._request_adapter)

    @property
    def download(self) -> DownloadBuilder:
        """
        The download property
        """
        from .download.download_builder import DownloadBuilder

        return DownloadBuilder(self._request_adapter)

    @property
    def forcedisbale(self) -> ForcedisbaleBuilder:
        """
        The forcedisbale property
        """
        from .forcedisbale.forcedisbale_builder import ForcedisbaleBuilder

        return ForcedisbaleBuilder(self._request_adapter)

    @property
    def start(self) -> StartBuilder:
        """
        The start property
        """
        from .start.start_builder import StartBuilder

        return StartBuilder(self._request_adapter)

    @property
    def status(self) -> StatusBuilder:
        """
        The status property
        """
        from .status.status_builder import StatusBuilder

        return StatusBuilder(self._request_adapter)

    @property
    def stop(self) -> StopBuilder:
        """
        The stop property
        """
        from .stop.stop_builder import StopBuilder

        return StopBuilder(self._request_adapter)

    @property
    def vnics_info(self) -> VnicsInfoBuilder:
        """
        The vnicsInfo property
        """
        from .vnics_info.vnics_info_builder import VnicsInfoBuilder

        return VnicsInfoBuilder(self._request_adapter)
