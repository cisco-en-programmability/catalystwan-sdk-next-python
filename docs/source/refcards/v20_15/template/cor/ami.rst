================
template.cor.ami
================


Operation: GET /dataservice/template/cor/ami
--------------------------------------------


Deprecated!!!

Get AMI list

.. code:: python

    def get(
        accountid: str, cloudregion: str, cloudtype: Optional[str] = "AWS"
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
        client.template.cor.ami.get()


