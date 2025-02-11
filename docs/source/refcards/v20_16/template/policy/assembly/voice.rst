==============================
template.policy.assembly.voice
==============================


Operation: POST /dataservice/template/policy/assembly/voice
-----------------------------------------------------------


Get policy assembly preview

.. code:: python

    def preview_2(payload: Optional[Any] = None) -> Any: ...


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
        client.template.policy.assembly.voice.preview_2()


Operation: GET /dataservice/template/policy/assembly/voice/{id}
---------------------------------------------------------------


Get policy assembly preview for feature policy

.. code:: python

    def preview_by_id_2(id: str) -> Any: ...


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
        client.template.policy.assembly.voice.preview_by_id_2()


