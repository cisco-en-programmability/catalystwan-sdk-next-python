=================================
v1.cloudonramp.saas.configuration
=================================


Operation: GET /dataservice/v1/cloudonramp/saas/configuration
-------------------------------------------------------------


Get Policy Groups that are deployed with Cloud on Ramp for Saas intent

.. code:: python

    def get_policy_groups_with_cor_saas_apps() -> None: ...


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
        client.v1.cloudonramp.saas.configuration.get_policy_groups_with_cor_saas_apps()


