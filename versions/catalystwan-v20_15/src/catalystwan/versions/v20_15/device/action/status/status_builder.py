# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional, Type

from catalystwan.abc import RequestAdapterInterface

from .models import DeviceTaskStatus

if TYPE_CHECKING:
    from .cancel.cancel_builder import CancelBuilder
    from .clean.clean_builder import CleanBuilder
    from .clear.clear_builder import ClearBuilder
    from .mw.mw_builder import MwBuilder
    from .preupgrade.preupgrade_builder import PreupgradeBuilder
    from .tasks.tasks_builder import TasksBuilder


class StatusBuilder:
    """
    Builds and executes requests for operations under /device/action/status
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    @property
    def update_device_action_task_status(self):
        class update_device_action_task_status_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[Any] = None, **kw):
                """
                Update device action status

                :param payload: Update device action status
                :returns: None
                """
                return self._request_adapter.request(
                    "PUT", "/dataservice/device/action/status", payload=payload, **kw
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return update_device_action_task_status_(self._request_adapter)

    def find_status(self, process_id: str, **kw) -> DeviceTaskStatus:
        """
        Find status of action

        :param process_id: processId
        :returns: DeviceTaskStatus
        """
        params = {
            "processId": process_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/device/action/status/{processId}",
            return_type=DeviceTaskStatus,
            params=params,
            **kw,
        )

    @property
    def cancel(self) -> CancelBuilder:
        """
        The cancel property
        """
        from .cancel.cancel_builder import CancelBuilder

        return CancelBuilder(self._request_adapter)

    @property
    def clean(self) -> CleanBuilder:
        """
        The clean property
        """
        from .clean.clean_builder import CleanBuilder

        return CleanBuilder(self._request_adapter)

    @property
    def clear(self) -> ClearBuilder:
        """
        The clear property
        """
        from .clear.clear_builder import ClearBuilder

        return ClearBuilder(self._request_adapter)

    @property
    def mw(self) -> MwBuilder:
        """
        The mw property
        """
        from .mw.mw_builder import MwBuilder

        return MwBuilder(self._request_adapter)

    @property
    def preupgrade(self) -> PreupgradeBuilder:
        """
        The preupgrade property
        """
        from .preupgrade.preupgrade_builder import PreupgradeBuilder

        return PreupgradeBuilder(self._request_adapter)

    @property
    def tasks(self) -> TasksBuilder:
        """
        The tasks property
        """
        from .tasks.tasks_builder import TasksBuilder

        return TasksBuilder(self._request_adapter)
