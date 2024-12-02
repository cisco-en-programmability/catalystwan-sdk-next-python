======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class AnalyzeCliConfig:
        """
        Payload/body schema for analyze cli config
        """

        # device UUID
        device_uuid: str
        # modeled cli config
        cli: Optional[str]
        # unmodeled cli config
        ioscli: Optional[str]


