==================
partner.aci.policy
==================


Operation: GET /dataservice/partner/aci/policy
----------------------------------------------


Get ACI definitions

.. code:: python

    def get_aci_definitions() -> Any: ...


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
        client.partner.aci.policy.get_aci_definitions()


.. toctree::
    :maxdepth: 1

    dscpmapping
    events
    prefixmapping
    sequences

