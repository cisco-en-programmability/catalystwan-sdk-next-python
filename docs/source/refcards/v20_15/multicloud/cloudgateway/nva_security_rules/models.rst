======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class NvaRulesListRequestSecurityRulesList:
        destination_port_range: str
        protocol: str
        source_address_prefix: str


    class NvaRulesListRequest:
        security_rules_list: Optional[
            List[NvaRulesListRequestSecurityRulesList]
        ]


    class NvaRulesResponse:
        account_id: Optional[str]
        account_name: Optional[str]
        cloud_type: Optional[str]
        expiration_time: Optional[str]
        nva_id: Optional[str]
        resource_group_name: Optional[str]
        rule_name: Optional[str]
        security_rules_list: Optional[NvaRulesListRequest]


    class Taskid:
        """
        Task id for polling status
        """

        id: Optional[str]


