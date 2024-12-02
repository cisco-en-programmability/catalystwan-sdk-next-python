========================
template.policy.security
========================


Operation: GET /dataservice/template/policy/security
----------------------------------------------------


Generate template list

.. code:: python

    def generate_security_template_list(
        mode: Optional[str] = None,
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
        client.template.policy.security.generate_security_template_list()


Operation: POST /dataservice/template/policy/security
-----------------------------------------------------


Create Template

.. code:: python

    def create_security_template(
        payload: Optional[Any] = None,
    ) -> None: ...


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
        client.template.policy.security.create_security_template()


Operation: GET /dataservice/template/policy/security/{deviceModel}
------------------------------------------------------------------


Get templates that map a device model

.. code:: python

    def get_security_templates_for_device(
        device_model: DeviceModel,
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
        client.template.policy.security.get_security_templates_for_device()


Operation: PUT /dataservice/template/policy/security/{policyId}
---------------------------------------------------------------


Edit Template

.. code:: python

    def edit_security_template(
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
        client.template.policy.security.edit_security_template()


Operation: DELETE /dataservice/template/policy/security/{policyId}
------------------------------------------------------------------


Delete Template

.. code:: python

    def delete_security_template(policy_id: str) -> None: ...


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
        client.template.policy.security.delete_security_template()


.. toctree::
    :maxdepth: 1

    definition
    devices
    staging
    summary
    models

