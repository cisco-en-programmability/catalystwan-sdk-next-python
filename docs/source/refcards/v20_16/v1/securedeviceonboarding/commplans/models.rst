======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class Apn:
        """
        List of APNs associated with the Comm Plan
        """

        name: str


    class LteApn:
        """
        List of LTE APNs associated with the Comm Plan.Empty if lteEnabled is false
        """

        name: str


    class CommunicationPlan:
        # List of APNs associated with the Comm Plan
        apns: List[Apn]
        # List of LTE APNs associated with the Comm Plan.Empty if lteEnabled is false
        lte_apns: List[LteApn]
        # Specifies whether the Comm Plan has LTE enabled
        lte_enabled: bool
        # Name of the communication plan.
        name: str
        # Description of the communication plan.
        comm_plan_description: Optional[str]
        comm_plan_name: Optional[str]


    class CommunicationPlansResponse:
        # List of communication plans.
        communication_plans: List[CommunicationPlan]
        # Page Number.
        page_number: int
        comm_plans: Optional[List[CommunicationPlan]]


