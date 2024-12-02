======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class InlineResponse20013TopologyCriteria:
        # Name of attribute type
        attribute: Optional[str]
        # Value of attribute
        value: Optional[str]


    class InlineResponse20013TopologyUnsupportedFeatures:
        # Config-Group Parcel Id
        parcel_id: Optional[str]
        # Config-Group Parcel Type
        parcel_type: Optional[str]


    class InlineResponse20013TopologyDevices:
        criteria: Optional[InlineResponse20013TopologyCriteria]
        unsupported_features: Optional[
            InlineResponse20013TopologyUnsupportedFeatures
        ]


    class InlineResponse20013Topology:
        devices: Optional[List[InlineResponse20013TopologyDevices]]


    class InlineResponse20013:
        topology: Optional[InlineResponse20013Topology]


