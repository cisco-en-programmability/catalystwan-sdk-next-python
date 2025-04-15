=============================
template.policy.voice.summary
=============================


Operation: GET /dataservice/template/policy/voice/summary
---------------------------------------------------------


Get templates that map a device model

.. code:: python

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
        client.template.policy.voice.summary.get()


