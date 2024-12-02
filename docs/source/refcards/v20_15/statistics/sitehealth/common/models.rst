======
Models
======


.. code:: python

    from typing import Literal, Optional, List, Union, Dict, Any

    AppsHealth = Literal["fair", "good", "poor"]

    HealthParam = Literal["FAIR", "GOOD", "POOR"]

    DeviceTypeParam = Literal["all", "controller", "vedge"]


    class SiteHealthItem:
        apps_health: AppsHealth
        apps_usage: int
        devices_health: AppsHealth
        site_health: AppsHealth
        site_id: str
        tunnels_health: AppsHealth


