============================================
v1.feature_profile.mobility.global_.ethernet
============================================


Operation: POST /dataservice/v1/feature-profile/mobility/global/{profileId}/ethernet
------------------------------------------------------------------------------------


Create an ethernet Profile Parcel for Mobility Global Feature Profile

.. code:: python

    def post(
        profile_id: str,
        payload: CreateEthernetProfileParcelForMobilityPostRequest,
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
        client.v1.feature_profile.mobility.global_.ethernet.post()


Operation: PUT /dataservice/v1/feature-profile/mobility/global/{profileId}/ethernet/{ethernetId}
------------------------------------------------------------------------------------------------


Update a Ethernet Profile Parcel for feature profile

.. code:: python

    def put(
        profile_id: str,
        ethernet_id: str,
        payload: EditEthernetProfileParcelForSystemPutRequest,
    ) -> None: ...


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
        client.v1.feature_profile.mobility.global_.ethernet.put()


Operation: DELETE /dataservice/v1/feature-profile/mobility/global/{profileId}/ethernet/{ethernetId}
---------------------------------------------------------------------------------------------------


Delete a Ethernet Profile Parcel for feature profile

.. code:: python

    def delete(profile_id: str, ethernet_id: str) -> None: ...


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
        client.v1.feature_profile.mobility.global_.ethernet.delete()


Operation: GET /dataservice/v1/feature-profile/mobility/global/{profileId}/ethernet
-----------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(profile_id: str) -> GetListMobilityGlobalEthernetPayload: ...


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
        client.v1.feature_profile.mobility.global_.ethernet.get()


Operation: GET /dataservice/v1/feature-profile/mobility/global/{profileId}/ethernet/{ethernetId}
------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        profile_id: str, ethernet_id: str
    ) -> GetEthernetProfileParcelGetResponse: ...


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
        client.v1.feature_profile.mobility.global_.ethernet.get()


.. toctree::
    :maxdepth: 1

    models

