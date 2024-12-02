# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Any, Type, TYPE_CHECKING
from catalystwan.abc import RequestAdapterInterface
import logging

if TYPE_CHECKING:
    from .attachment.attachment_builder import AttachmentBuilder
    from .circuit.circuit_builder import CircuitBuilder
    from .global_.global_builder import GlobalBuilder
    from .lock.lock_builder import LockBuilder
    from .mytest.mytest_builder import MytestBuilder
    from .profile.profile_builder import ProfileBuilder
    from .service_profile_config.service_profile_config_builder import (
        ServiceProfileConfigBuilder,
    )


class NetworkdesignBuilder:
    """
    Builds and executes requests for operations under /networkdesign
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_network_design(self, **kw) -> Any:
        """
        Get existing network design

        :returns: Any
        """
        logging.warning("Operation: %s is deprecated", "getNetworkDesign")
        return self._request_adapter.request("GET", "/dataservice/networkdesign", **kw)

    @property
    def edit_network_design(self):
        class edit_network_design_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, id: str, payload: Optional[Any] = None, **kw) -> Any:
                """
                Edit network segment

                :param id: Id
                :param payload: Network design payload
                :returns: Any
                """
                logging.warning("Operation: %s is deprecated", "editNetworkDesign")
                params = {
                    "id": id,
                }
                return self._request_adapter.request(
                    "PUT",
                    "/dataservice/networkdesign",
                    params=params,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return edit_network_design_(self._request_adapter)

    @property
    def create_network_design(self):
        class create_network_design_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(self, payload: Optional[Any] = None, **kw) -> Any:
                """
                Create network design

                :param payload: Network design payload
                :returns: Any
                """
                logging.warning("Operation: %s is deprecated", "createNetworkDesign")
                return self._request_adapter.request(
                    "POST", "/dataservice/networkdesign", payload=payload, **kw
                )

            def create_payload(self, *args, **kwargs) -> Any:
                return Any(*args, **kwargs)

            @property
            def payload_model(self) -> Type[Any]:
                return Any

        return create_network_design_(self._request_adapter)

    @property
    def attachment(self) -> AttachmentBuilder:
        """
        The attachment property
        """
        from .attachment.attachment_builder import AttachmentBuilder

        return AttachmentBuilder(self._request_adapter)

    @property
    def circuit(self) -> CircuitBuilder:
        """
        The circuit property
        """
        from .circuit.circuit_builder import CircuitBuilder

        return CircuitBuilder(self._request_adapter)

    @property
    def global_(self) -> GlobalBuilder:
        """
        The global property
        """
        from .global_.global_builder import GlobalBuilder

        return GlobalBuilder(self._request_adapter)

    @property
    def lock(self) -> LockBuilder:
        """
        The lock property
        """
        from .lock.lock_builder import LockBuilder

        return LockBuilder(self._request_adapter)

    @property
    def mytest(self) -> MytestBuilder:
        """
        The mytest property
        """
        from .mytest.mytest_builder import MytestBuilder

        return MytestBuilder(self._request_adapter)

    @property
    def profile(self) -> ProfileBuilder:
        """
        The profile property
        """
        from .profile.profile_builder import ProfileBuilder

        return ProfileBuilder(self._request_adapter)

    @property
    def service_profile_config(self) -> ServiceProfileConfigBuilder:
        """
        The serviceProfileConfig property
        """
        from .service_profile_config.service_profile_config_builder import (
            ServiceProfileConfigBuilder,
        )

        return ServiceProfileConfigBuilder(self._request_adapter)
