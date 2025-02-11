======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class AuditReportAuditReport:
        err_string: Optional[str]
        region: Optional[str]
        report_type: Optional[str]
        resource_name: Optional[str]
        status: Optional[str]


    class AuditReport:
        audit_report: Optional[List[AuditReportAuditReport]]
        audit_status: Optional[str]


