======
Models
======


.. code:: python

    from typing import Any, Dict, List, Literal, Optional, Union

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


