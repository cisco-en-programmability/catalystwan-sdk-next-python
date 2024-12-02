======
Models
======


.. code:: python

    from typing import Literal, Optional, List, Union, Dict, Any

    ActionParam = Literal["runnow", "start", "stop"]


    class UpdateReportTemplateResponse:
        # Report ID
        report_id: str


