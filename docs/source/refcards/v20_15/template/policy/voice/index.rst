=====================
template.policy.voice
=====================


Operation: POST /dataservice/template/policy/voice
--------------------------------------------------


Create Template

.. code:: python

    def post(payload: Any) -> Any: ...


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
        client.template.policy.voice.post()


Operation: PUT /dataservice/template/policy/voice/{policyId}
------------------------------------------------------------


Edit Template

.. code:: python

    def put(policy_id: str, payload: Any) -> Any: ...


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
        client.template.policy.voice.put()


Operation: DELETE /dataservice/template/policy/voice/{policyId}
---------------------------------------------------------------


Delete Template

.. code:: python

    def delete(policy_id: str) -> None: ...


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
        client.template.policy.voice.delete()


Operation: GET /dataservice/template/policy/voice
-------------------------------------------------


.. code:: python

    @overload
    def get() -> List[Any]: ...


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
        client.template.policy.voice.get()


Operation: GET /dataservice/template/policy/voice/{deviceModel}
---------------------------------------------------------------


.. code:: python

    @overload
    def get(device_model: DeviceModel) -> List[Any]: ...


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
        client.template.policy.voice.get()


.. toctree::
    :maxdepth: 1

    definition
    devices
    summary
    models

