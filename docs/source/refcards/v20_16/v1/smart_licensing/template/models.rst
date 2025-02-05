======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class SaveTemplateRequestLicenseTemplateLicenses:
        display_name: Optional[str]
        tag: Optional[str]


    class SaveTemplateRequestLicenseTemplateSubscriptionsUsed:
        subscription_id: Optional[str]


    class SaveTemplateRequestLicenseTemplate:
        license_type: Optional[str]
        licenses: Optional[
            List[SaveTemplateRequestLicenseTemplateLicenses]
        ]
        sa_account: Optional[str]
        sa_name: Optional[str]
        subscriptions_used: Optional[
            List[SaveTemplateRequestLicenseTemplateSubscriptionsUsed]
        ]
        template_name: Optional[str]
        use_existing_template: Optional[bool]
        uuid: Optional[List[str]]
        va_account: Optional[str]
        va_name: Optional[str]


    class SaveTemplateRequest:
        license_template: Optional[SaveTemplateRequestLicenseTemplate]


