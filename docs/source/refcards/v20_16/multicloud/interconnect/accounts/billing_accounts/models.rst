======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class InterconnectBillingAccountInfo:
        """
        Interconnect billing account Information
        """

        # Interconnect billing account Id
        edge_billing_account_id: Optional[str]
        # Interconnect billing account name
        edge_billing_account_name: Optional[str]


    class InlineResponse2001:
        edge_billing_account_info_list: Optional[
            List[InterconnectBillingAccountInfo]
        ]


