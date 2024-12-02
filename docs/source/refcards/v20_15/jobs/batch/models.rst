======
Models
======


.. code:: python

    from typing import Literal, Optional, List, Union, Dict, Any

    Method = Literal["DELETE", "GET", "POST", "PUT"]


    class BatchFlowData:
        """
        payload for a REST API
        """

        # HTTP Method
        method: Optional[Method]
        # JSON Payload for a REST API call
        payload: Optional[Any]
        uri: Optional[str]


    class BatchFlow:
        """
        Input to multiple REST API calls
        """

        # payload for a REST API
        data: List[BatchFlowData]


