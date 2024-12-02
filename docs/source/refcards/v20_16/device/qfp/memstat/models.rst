======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class QfpMemoryState:
        dram_free: Optional[int]
        dram_in_use: Optional[int]
        dram_lowest_free_water_mark: Optional[int]
        dram_total: Optional[int]
        iram_free: Optional[int]
        iram_in_use: Optional[int]
        iram_lowest_free_water_mark: Optional[int]
        iram_total: Optional[int]
        lastupdated: Optional[int]
        sram_free: Optional[int]
        sram_in_use: Optional[int]
        sram_lowest_free_water_mark: Optional[int]
        sram_total: Optional[int]
        vdevice_data_key: Optional[str]
        vdevice_host_name: Optional[str]
        vdevice_name: Optional[str]


