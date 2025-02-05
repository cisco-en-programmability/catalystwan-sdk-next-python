======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class PowerConsumptionBreakDown:
        percentage: Optional[int]
        property: Optional[str]
        usage: Optional[int]


    class PowerConsumptionEnergyMixResp:
        energy_mix: Optional[List[PowerConsumptionBreakDown]]
        low_carbon: Optional[int]


