======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class ActivationStatusRes:
        centralized_policy_active: bool
        is_activated_by_v_smarts: bool
        activated_centralized_policy_id: Optional[str]
        referred_in_active_wani_policy: Optional[bool]
        user_defined_policy_id: Optional[str]


