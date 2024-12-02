===============================
multicloud.interconnect.sshkeys
===============================


Operation: GET /dataservice/multicloud/interconnect/sshkeys
-----------------------------------------------------------


Get ssh keys for Interconnect provider.

.. code:: python

    def get_interconnect_ssh_keys(
        interconnect_provider_name: str, interconnect_account_id: str
    ) -> InlineResponse20016: ...


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
        client.multicloud.interconnect.sshkeys.get_interconnect_ssh_keys()


.. toctree::
    :maxdepth: 1

    models

