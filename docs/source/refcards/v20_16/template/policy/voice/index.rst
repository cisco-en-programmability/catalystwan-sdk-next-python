=====================
template.policy.voice
=====================


Operation: GET /dataservice/template/policy/voice
-------------------------------------------------


Generate template list

.. code:: python

    def generate_voice_template_list() -> List[Any]: ...


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
        client.template.policy.voice.generate_voice_template_list()


Operation: POST /dataservice/template/policy/voice
--------------------------------------------------


Create Template

.. code:: python

    def create_voice_template(payload: Optional[Any] = None) -> Any: ...


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
        client.template.policy.voice.create_voice_template()


Operation: GET /dataservice/template/policy/voice/{deviceModel}
---------------------------------------------------------------


Get templates that map a device model

.. code:: python

    def get_voice_templates_for_device(
        device_model: DeviceModel,
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
        client.template.policy.voice.get_voice_templates_for_device()


Operation: PUT /dataservice/template/policy/voice/{policyId}
------------------------------------------------------------


Edit Template

.. code:: python

    def edit_voice_template(
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
        client.template.policy.voice.edit_voice_template()


Operation: DELETE /dataservice/template/policy/voice/{policyId}
---------------------------------------------------------------


Delete Template

.. code:: python

    def delete_voice_template(policy_id: str) -> None: ...


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
        client.template.policy.voice.delete_voice_template()


.. toctree::
    :maxdepth: 1

    definition
    devices
    summary
    models

