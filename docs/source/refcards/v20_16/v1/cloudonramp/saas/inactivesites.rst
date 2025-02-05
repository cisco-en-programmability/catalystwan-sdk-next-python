=================================
v1.cloudonramp.saas.inactivesites
=================================


Operation: GET /dataservice/v1/cloudonramp/saas/inactivesites
-------------------------------------------------------------


Get inactive sites

.. code:: python

    def get_inactive_cor_saas_sites() -> None: ...


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
        client.v1.cloudonramp.saas.inactivesites.get_inactive_cor_saas_sites()


