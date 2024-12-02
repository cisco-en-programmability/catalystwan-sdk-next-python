======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class NotificationsRuleData:
        _rid: Optional[int]
        account_details: Optional[str]
        alarm_name: Optional[str]
        devices_attached: Optional[str]
        email_threshold: Optional[int]
        last_updated: Optional[int]
        notification_rule_id: Optional[str]
        notification_rule_name: Optional[str]
        severity: Optional[str]
        updated_by: Optional[str]
        webhook_password: Optional[str]
        webhook_url: Optional[str]
        webhook_username: Optional[str]


    class NotificationsRulesResponse:
        data: Optional[List[NotificationsRuleData]]


