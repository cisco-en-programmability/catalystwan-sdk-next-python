======
Models
======


.. code:: python

    from typing import Literal, Optional, List, Union, Dict, Any

    DeviceSelectionType = Literal["entire-network", "selected-devices"]

    ExecutionType = Literal["later", "now"]

    ProtocolPackType = Literal[
        "built-in-protocol-pack",
        "default-protocol-pack",
        "selected-protocol-pack",
    ]


    class ProtocolPackUpgradeRequest:
        device_selection_type: Optional[DeviceSelectionType]
        devices: Optional[List[str]]
        execution_type: Optional[ExecutionType]
        protocol_pack_type: Optional[ProtocolPackType]
        protocol_packs: Optional[List[str]]
        schedule_time: Optional[int]


