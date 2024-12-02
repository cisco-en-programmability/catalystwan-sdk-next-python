===========
device.tier
===========


Operation: GET /dataservice/device/tier
---------------------------------------


getTiers

.. code:: python

    def get_tiers() -> None: ...


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
        client.device.tier.get_tiers()


Operation: POST /dataservice/device/tier
----------------------------------------


add tier

.. code:: python

    def add_tier(add_tier: str) -> None: ...


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
        client.device.tier.add_tier()


Operation: DELETE /dataservice/device/tier/{tierName}
-----------------------------------------------------


deleteTier

.. code:: python

    def delete_tier(tier_name: str) -> None: ...


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
        client.device.tier.delete_tier()


