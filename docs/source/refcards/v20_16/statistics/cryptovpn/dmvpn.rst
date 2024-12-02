==========================
statistics.cryptovpn.dmvpn
==========================


Operation: POST /dataservice/statistics/cryptovpn/dmvpn
-------------------------------------------------------


Get crypto vpn dmvpn data

.. code:: python

    def get_post_crypto_dmvpn_data_by_query(
        payload: Optional[Any] = None,
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
        client.statistics.cryptovpn.dmvpn.get_post_crypto_dmvpn_data_by_query()


