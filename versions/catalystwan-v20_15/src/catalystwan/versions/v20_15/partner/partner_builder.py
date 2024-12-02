# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import List, Type, TYPE_CHECKING
from catalystwan.abc import RequestAdapterInterface
from .models import PartnerRes
from .models import RegisterPartnerRes
from .models import RegisterPartnerRequest
from .models import UpdatePartnerRequest
from .models import StatusResponse

if TYPE_CHECKING:
    from .aci.aci_builder import AciBuilder
    from .dnac.dnac_builder import DnacBuilder
    from .vpn.vpn_builder import VpnBuilder
    from .wcm.wcm_builder import WcmBuilder
    from .map.map_builder import MapBuilder
    from .unmap.unmap_builder import UnmapBuilder


class PartnerBuilder:
    """
    Builds and executes requests for operations under /partner
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_partners(self, **kw) -> List[PartnerRes]:
        """
        Get all NMS partners

        :returns: List[PartnerRes]
        """
        return self._request_adapter.request(
            "GET", "/dataservice/partner", return_type=List[PartnerRes], **kw
        )

    def get_partners_by_partner_type(self, partner_type: str, **kw) -> List[PartnerRes]:
        """
        Get NMS partners by partner type

        :param partner_type: Partner type
        :returns: List[PartnerRes]
        """
        params = {
            "partnerType": partner_type,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/partner/{partnerType}",
            return_type=List[PartnerRes],
            params=params,
            **kw,
        )

    @property
    def register_partner(self):
        class register_partner_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self, partner_type: str, payload: RegisterPartnerRequest, **kw
            ) -> RegisterPartnerRes:
                """
                Register NMS partner

                :param partner_type: Partner type
                :param payload: Partner
                :returns: RegisterPartnerRes
                """
                params = {
                    "partnerType": partner_type,
                }
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/partner/{partnerType}",
                    return_type=RegisterPartnerRes,
                    params=params,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> RegisterPartnerRequest:
                return RegisterPartnerRequest(*args, **kwargs)

            @property
            def payload_model(self) -> Type[RegisterPartnerRequest]:
                return RegisterPartnerRequest

        return register_partner_(self._request_adapter)

    def get_partner(self, partner_type: str, nms_id: str, **kw) -> PartnerRes:
        """
        Get NMS partners by partner type and Id

        :param partner_type: Partner type
        :param nms_id: Nms id
        :returns: PartnerRes
        """
        params = {
            "partnerType": partner_type,
            "nmsId": nms_id,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/partner/{partnerType}/{nmsId}",
            return_type=PartnerRes,
            params=params,
            **kw,
        )

    @property
    def update_partner(self):
        class update_partner_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self,
                partner_type: str,
                nms_id: str,
                payload: UpdatePartnerRequest,
                **kw,
            ):
                """
                Update NMS partner details

                :param partner_type: Partner type
                :param nms_id: Nms id
                :param payload: Partner
                :returns: None
                """
                params = {
                    "partnerType": partner_type,
                    "nmsId": nms_id,
                }
                return self._request_adapter.request(
                    "PUT",
                    "/dataservice/partner/{partnerType}/{nmsId}",
                    params=params,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> UpdatePartnerRequest:
                return UpdatePartnerRequest(*args, **kwargs)

            @property
            def payload_model(self) -> Type[UpdatePartnerRequest]:
                return UpdatePartnerRequest

        return update_partner_(self._request_adapter)

    def delete_partner(self, partner_type: str, nms_id: str, **kw) -> StatusResponse:
        """
        Delete NMS partner

        :param partner_type: Partner type
        :param nms_id: Nms id
        :returns: StatusResponse
        """
        params = {
            "partnerType": partner_type,
            "nmsId": nms_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/partner/{partnerType}/{nmsId}",
            return_type=StatusResponse,
            params=params,
            **kw,
        )

    @property
    def aci(self) -> AciBuilder:
        """
        The aci property
        """
        from .aci.aci_builder import AciBuilder

        return AciBuilder(self._request_adapter)

    @property
    def dnac(self) -> DnacBuilder:
        """
        The dnac property
        """
        from .dnac.dnac_builder import DnacBuilder

        return DnacBuilder(self._request_adapter)

    @property
    def map(self) -> MapBuilder:
        """
        The map property
        """
        from .map.map_builder import MapBuilder

        return MapBuilder(self._request_adapter)

    @property
    def unmap(self) -> UnmapBuilder:
        """
        The unmap property
        """
        from .unmap.unmap_builder import UnmapBuilder

        return UnmapBuilder(self._request_adapter)

    @property
    def vpn(self) -> VpnBuilder:
        """
        The vpn property
        """
        from .vpn.vpn_builder import VpnBuilder

        return VpnBuilder(self._request_adapter)

    @property
    def wcm(self) -> WcmBuilder:
        """
        The wcm property
        """
        from .wcm.wcm_builder import WcmBuilder

        return WcmBuilder(self._request_adapter)
