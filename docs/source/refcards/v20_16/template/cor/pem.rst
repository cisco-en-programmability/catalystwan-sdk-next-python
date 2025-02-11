================
template.cor.pem
================


Operation: GET /dataservice/template/cor/pem
--------------------------------------------


Deprecated!!!

Get transit VPC PEM key list

.. code:: python

    def get_pem_key_list(
        accountid: str, cloudregion: str, cloudtype: str
    ) -> List[Any]: ...


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
        client.template.cor.pem.get_pem_key_list()


