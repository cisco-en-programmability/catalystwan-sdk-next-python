==============================
template.policy.vsmart.central
==============================


Operation: PUT /dataservice/template/policy/vsmart/central/{policyId}
---------------------------------------------------------------------


Edit template for given policy id to allow for multiple component edits

.. code:: python

    def edit_template_without_lock_checks(
        policy_id: str, payload: Optional[Any] = None
    ) -> List[Any]: ...


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
        client.template.policy.vsmart.central.edit_template_without_lock_checks()


