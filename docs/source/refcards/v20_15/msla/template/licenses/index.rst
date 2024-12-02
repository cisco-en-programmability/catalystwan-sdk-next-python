======================
msla.template.licenses
======================


Operation: POST /dataservice/msla/template/licenses
---------------------------------------------------


Deprecated!!!

Retrieve MSLA subscription/licenses

.. code:: python

    def get_subscriptions_1(
        payload: Optional[GetSubscriptions1PostRequest] = None,
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
        client.msla.template.licenses.get_subscriptions_1()


.. toctree::
    :maxdepth: 1

    models

