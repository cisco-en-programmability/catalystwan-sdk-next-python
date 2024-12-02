==================
multicloud.sshkeys
==================


Operation: GET /dataservice/multicloud/sshkeys
----------------------------------------------


Get ssh keyList for cloud type

.. code:: python

    def get_ssh_key_list(
        cloud_type: str, account_id: str, cloud_region: str
    ) -> List[SshKeyList]: ...


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
        client.multicloud.sshkeys.get_ssh_key_list()


.. toctree::
    :maxdepth: 1

    models

