================================
template.policy.security.staging
================================


Operation: PUT /dataservice/template/policy/security/staging/{policyId}
-----------------------------------------------------------------------


Edit Template

.. code:: python

    def edit_template_with_lenient_lock(
        policy_id: str, payload: Optional[Any] = None
    ) -> Any: ...


Example:
^^^^^^^^


.. code:: python

    from catalyswan.core import create_client

    url = "example.com"
    username = "admin"
    password = "password123"

    with create_client(
        url=url, username=username, password=password
    ) as client:
        client.template.policy.security.staging.edit_template_with_lenient_lock()


