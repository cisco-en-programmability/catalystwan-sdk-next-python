================================
template.policy.ise.identity.sgt
================================


Operation: GET /dataservice/template/policy/ise/identity/sgt
------------------------------------------------------------


Get trustsec Scalable Group Tags

.. code:: python

    def sgts() -> SgtResponse: ...


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
        client.template.policy.ise.identity.sgt.sgts()


.. toctree::
    :maxdepth: 1

    models

