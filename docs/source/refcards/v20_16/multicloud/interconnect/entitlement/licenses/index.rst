============================================
multicloud.interconnect.entitlement.licenses
============================================


Operation: GET /dataservice/multicloud/interconnect/entitlement/licenses
------------------------------------------------------------------------


API to retrieve Interconnect licences

.. code:: python

    def get(
        interconnect_type: str,
        interconnect_account_id: str,
        refresh: Optional[str] = "false",
        product_type: Optional[str] = None,
    ) -> List[InterconnectLicense]: ...


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
        client.multicloud.interconnect.entitlement.licenses.get()


.. toctree::
    :maxdepth: 1

    models

