from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, List, Optional, Type, overload
from uuid import UUID

from catalystwan.core.models.serialize import serialize
from catalystwan.workflows.query import Query, QuerySpec

if TYPE_CHECKING:
    from catalystwan.core.loader import ApiClient


@dataclass
class ClearedAlarm:
    alarm_uuid: UUID
    cleared: bool


class AlarmsWorkflow:
    supported_versions = ("20.14", "20.15")

    def __init__(self, client: ApiClient):
        self.client = client
        assert self.client.api_version in self.supported_versions

    @property
    def query(self) -> Type[QuerySpec]:
        return QuerySpec

    def get(self, query: Optional[QuerySpec] = None):
        if self.client.api_version == "20.15":
            endpoint = self.client.alarms.post_raw_alarm_data
        else:
            endpoint = self.client.alarms.get_raw_alarm_data

        payload = Query(query=query)
        response = endpoint(payload=serialize(payload, to_json=True))
        return response

    def get_alarms(self, from_time: Optional[int] = None, active: bool = True):
        query_spec = QuerySpec(condition="AND", rules=[])
        query_spec.add_query_rule(
            field="active",
            field_type="boolean",
            value=[str(active).lower()],
            operator="equal",
        )
        if from_time:
            query_spec.add_query_rule(
                field="entry_time",
                field_type="date",
                value=[str(from_time)],
                operator="last_n_hours",
            )
        return self.get(query_spec=query_spec)

    @overload
    def clear(self, uuid: Optional[UUID]) -> List[ClearedAlarm]: ...

    @overload
    def clear(self, *, query: Optional[Query]) -> List[ClearedAlarm]: ...

    def clear(
        self, uuid: Optional[UUID] = None, query: Optional[Query] = None
    ) -> List[ClearedAlarm]:
        ids: List[UUID] = []
        if uuid is not None:
            ids = [uuid]
        elif query is not None:
            alarms = self.get(query=query)
            if alarms is not None:
                ids = [alarm.uuid for alarm in alarms]

        api = self.client.alarms.clear

        cleared_alarms: List[ClearedAlarm] = []
        for id in ids:
            if self.client.api_version == "20.15":
                response = api.clear_stale_alarm(payload={"alarm_uuid": str(id)})
                cleared_alarms.append(
                    ClearedAlarm(
                        alarm_uuid=response.get("alarm_uuid"),
                        cleared=response.get("cleared"),
                    )
                )
            else:
                payload_model = api.m.AlarmsClearBody
                response = api.clear_stale_alarm(payload=payload_model(alarm_uuid=str(id)))
                cleared_alarms.append(
                    ClearedAlarm(alarm_uuid=response[0].alarm_uuid, cleared=response[0].cleared)
                )

        return cleared_alarms
