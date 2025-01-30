======
Models
======


.. code:: python

    from typing import Literal, Any, Union, Dict, Optional, List

    CloudTypeParam = Literal[
        "AWS", "AWS_GOVCLOUD", "AZURE", "AZURE_GOVCLOUD", "GCP"
    ]


    class Taskid:
        """
        Task id for polling status
        """

        id: Optional[str]


    class AuditFixIssuesToSync:
        name: str
        region: str
        report_type: str


    class AuditFix:
        cloud_type: str
        issues_to_sync: Optional[List[AuditFixIssuesToSync]]
        region: Optional[str]


