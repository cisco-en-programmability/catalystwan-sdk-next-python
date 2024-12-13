======
Models
======


.. code:: python

    from typing import List, Dict, Union, Literal, Optional, Any

    AppsHealth = Literal["fair", "good", "poor"]

    HealthParam = Literal["FAIR", "GOOD", "POOR"]

    DeviceTypeParam = Literal["all", "controller", "vedge"]


    class SiteHealthItem:
        apps_health: (
            AppsHealth  # pytype: disable=annotation-type-mismatch
        )
        apps_usage: int
        devices_health: (
            AppsHealth  # pytype: disable=annotation-type-mismatch
        )
        site_health: (
            AppsHealth  # pytype: disable=annotation-type-mismatch
        )
        site_id: str
        tunnels_health: (
            AppsHealth  # pytype: disable=annotation-type-mismatch
        )


