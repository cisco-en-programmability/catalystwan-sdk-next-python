===============
msla.va.license
===============


Operation: GET /dataservice/msla/va/License
-------------------------------------------


Deprecated!!!

Retrieve MSLA subscription/licenses

.. code:: python

    def get_subscriptions(
        virtual_account_id: Optional[str] = None,
        license_type: Optional[str] = None,
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
        client.msla.va.license.get_subscriptions()


