======================================
template.security.encrypt_text.encrypt
======================================


Operation: POST /dataservice/template/security/encryptText/encrypt
------------------------------------------------------------------


Get Type 6 Encryptedd String for a given value

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
        client.template.security.encrypt_text.encrypt.post()


