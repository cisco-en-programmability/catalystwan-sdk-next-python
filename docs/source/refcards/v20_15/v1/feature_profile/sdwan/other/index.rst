==============================
v1.feature_profile.sdwan.other
==============================


Operation: GET /dataservice/v1/feature-profile/sdwan/other
----------------------------------------------------------


Get all SDWAN Feature Profiles with giving Family and profile type

.. code:: python

    def get_sdwan_other_feature_profiles(
        offset: Optional[int] = None, limit: Optional[int] = 0
    ) -> Any: ...


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
        client.v1.feature_profile.sdwan.other.get_sdwan_other_feature_profiles()


Operation: POST /dataservice/v1/feature-profile/sdwan/other
-----------------------------------------------------------


Create a SDWAN Other Feature Profile

.. code:: python

    def create_sdwan_other_feature_profile(
        payload: Optional[str] = None,
    ) -> str: ...


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
        client.v1.feature_profile.sdwan.other.create_sdwan_other_feature_profile()


Operation: GET /dataservice/v1/feature-profile/sdwan/other/{otherId}
--------------------------------------------------------------------


Get a SDWAN Other Feature Profile with otherId

.. code:: python

    def get_sdwan_other_feature_profile_by_profile_id(
        other_id: str,
    ) -> Any: ...


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
        client.v1.feature_profile.sdwan.other.get_sdwan_other_feature_profile_by_profile_id()


Operation: PUT /dataservice/v1/feature-profile/sdwan/other/{otherId}
--------------------------------------------------------------------


Edit a SDWAN Other Feature Profile

.. code:: python

    def edit_sdwan_other_feature_profile(
        other_id: str, payload: Optional[str] = None
    ) -> str: ...


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
        client.v1.feature_profile.sdwan.other.edit_sdwan_other_feature_profile()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/other/{otherId}
-----------------------------------------------------------------------


Delete Feature Profile

.. code:: python

    def delete_sdwan_other_feature_profile(other_id: str) -> None: ...


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
        client.v1.feature_profile.sdwan.other.delete_sdwan_other_feature_profile()


.. toctree::
    :maxdepth: 1

    thousandeyes/index
    ucse

