============================
partner.aci.policy.sequences
============================


Operation: GET /dataservice/partner/aci/policy/sequences
--------------------------------------------------------


Get data prefix sequence

.. code:: python

    def get_data_prefix_sequences() -> List[Any]: ...


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
        client.partner.aci.policy.sequences.get_data_prefix_sequences()


