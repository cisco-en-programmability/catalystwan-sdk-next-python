# Copyright 2024 Cisco Systems, Inc. and its affiliates
from __future__ import annotations
from typing import Optional, Type, TYPE_CHECKING
from catalystwan.abc import RequestAdapterInterface
from .models import PolicyObjectListTypeParam

if TYPE_CHECKING:
    from .unified.unified_builder import UnifiedBuilder
    from .schema.schema_builder import SchemaBuilder


class PolicyObjectBuilder:
    """
    Builds and executes requests for operations under /v1/feature-profile/sdwan/policy-object
    """

    def __init__(self, request_adapter: RequestAdapterInterface) -> None:
        self._request_adapter = request_adapter

    def get_data_prefix_profile_parcel_for_policy_object(
        self,
        policy_object_id: str,
        policy_object_list_type: PolicyObjectListTypeParam,
        reference_count: Optional[bool] = False,
        **kw,
    ) -> str:
        """
        Get Data Prefix Profile Parcels for Policy Object feature profile

        :param policy_object_id: Feature Profile ID
        :param policy_object_list_type: Policy Object ListType
        :param reference_count: get reference count
        :returns: str
        """
        params = {
            "policyObjectId": policy_object_id,
            "policyObjectListType": policy_object_list_type,
            "referenceCount": reference_count,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sdwan/policy-object/{policyObjectId}/{policyObjectListType}",
            return_type=str,
            params=params,
            **kw,
        )

    @property
    def create_data_prefix_profile_parcel_for_security_policy_object(self):
        class create_data_prefix_profile_parcel_for_security_policy_object_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self,
                policy_object_id: str,
                policy_object_list_type: PolicyObjectListTypeParam,
                payload: Optional[str] = None,
                **kw,
            ) -> str:
                """
                Create a Data Prefix Profile Parcel for Security Policy Object feature profile

                :param policy_object_id: Feature Profile ID
                :param policy_object_list_type: Policy Object ListType
                :param payload: Data Prefix Profile Parcel
                :returns: str
                """
                params = {
                    "policyObjectId": policy_object_id,
                    "policyObjectListType": policy_object_list_type,
                }
                return self._request_adapter.request(
                    "POST",
                    "/dataservice/v1/feature-profile/sdwan/policy-object/{policyObjectId}/{policyObjectListType}",
                    return_type=str,
                    params=params,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> str:
                return str(*args, **kwargs)

            @property
            def payload_model(self) -> Type[str]:
                return str

        return create_data_prefix_profile_parcel_for_security_policy_object_(
            self._request_adapter
        )

    def get_data_prefix_profile_parcel_by_parcel_id_for_policy_object(
        self,
        policy_object_id: str,
        policy_object_list_type: PolicyObjectListTypeParam,
        list_object_id: str,
        references: Optional[bool] = False,
        **kw,
    ) -> str:
        """
        Get Data Prefix Profile Parcel by parcelId for Policy Object feature profile

        :param policy_object_id: Feature Profile ID
        :param policy_object_list_type: Policy Object ListType
        :param list_object_id: Profile Parcel ID
        :param references: get referred profile/parcel details
        :returns: str
        """
        params = {
            "policyObjectId": policy_object_id,
            "policyObjectListType": policy_object_list_type,
            "listObjectId": list_object_id,
            "references": references,
        }
        return self._request_adapter.request(
            "GET",
            "/dataservice/v1/feature-profile/sdwan/policy-object/{policyObjectId}/{policyObjectListType}/{listObjectId}",
            return_type=str,
            params=params,
            **kw,
        )

    @property
    def edit_data_prefix_profile_parcel_for_policy_object(self):
        class edit_data_prefix_profile_parcel_for_policy_object_:
            def __init__(self, request_adapter: RequestAdapterInterface) -> None:
                self._request_adapter = request_adapter

            def __call__(
                self,
                policy_object_id: str,
                policy_object_list_type: PolicyObjectListTypeParam,
                list_object_id: str,
                payload: Optional[str] = None,
                **kw,
            ) -> str:
                """
                Update a Data Prefix Profile Parcel for Policy Object feature profile

                :param policy_object_id: Feature Profile ID
                :param policy_object_list_type: Policy Object ListType
                :param list_object_id: Profile Parcel ID
                :param payload: Data Prefix Profile Parcel
                :returns: str
                """
                params = {
                    "policyObjectId": policy_object_id,
                    "policyObjectListType": policy_object_list_type,
                    "listObjectId": list_object_id,
                }
                return self._request_adapter.request(
                    "PUT",
                    "/dataservice/v1/feature-profile/sdwan/policy-object/{policyObjectId}/{policyObjectListType}/{listObjectId}",
                    return_type=str,
                    params=params,
                    payload=payload,
                    **kw,
                )

            def create_payload(self, *args, **kwargs) -> str:
                return str(*args, **kwargs)

            @property
            def payload_model(self) -> Type[str]:
                return str

        return edit_data_prefix_profile_parcel_for_policy_object_(self._request_adapter)

    def delete_data_prefix_profile_parcel_for_policy_object(
        self,
        policy_object_id: str,
        policy_object_list_type: PolicyObjectListTypeParam,
        list_object_id: str,
        **kw,
    ):
        """
        Delete a Data Prefix Profile Parcel for Policy Object feature profile

        :param policy_object_id: Feature Profile ID
        :param policy_object_list_type: Policy Object ListType
        :param list_object_id: Profile Parcel ID
        :returns: None
        """
        params = {
            "policyObjectId": policy_object_id,
            "policyObjectListType": policy_object_list_type,
            "listObjectId": list_object_id,
        }
        return self._request_adapter.request(
            "DELETE",
            "/dataservice/v1/feature-profile/sdwan/policy-object/{policyObjectId}/{policyObjectListType}/{listObjectId}",
            params=params,
            **kw,
        )

    @property
    def schema(self) -> SchemaBuilder:
        """
        The schema property
        """
        from .schema.schema_builder import SchemaBuilder

        return SchemaBuilder(self._request_adapter)

    @property
    def unified(self) -> UnifiedBuilder:
        """
        The unified property
        """
        from .unified.unified_builder import UnifiedBuilder

        return UnifiedBuilder(self._request_adapter)
