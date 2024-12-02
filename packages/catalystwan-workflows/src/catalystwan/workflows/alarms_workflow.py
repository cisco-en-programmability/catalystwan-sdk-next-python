from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, Optional

if TYPE_CHECKING:
    from catalystwan.core.loader import ApiClient


class AlarmsWorkflow:
    supported_versions = ("20.14", "20.15")

    def __init__(self, client: ApiClient):
        self.client = client
        assert self.client.api_version in self.supported_versions

    def get_alarms(self, from_time: Optional[int] = None, active: bool = True):
        if self.client.api_version == "20.15":
            endpoint = self.client.alarms.post_raw_alarm_data
        else:
            endpoint = self.client.alarms.get_raw_alarm_data

        query: Dict[str, Any] = {
            "query": {
                "condition": "AND",
                "rules": [
                    {
                        "field": "active",
                        "type": "boolean",
                        "value": [str(active).lower()],
                        "operator": "equal",
                    }
                ],
            }
        }
        if from_time:
            query["query"]["rules"].append(
                {
                    "value": [str(from_time)],
                    "field": "entry_time",
                    "type": "date",
                    "operator": "last_n_hours",
                }
            )
        response = endpoint(payload=query)
        return response.data
