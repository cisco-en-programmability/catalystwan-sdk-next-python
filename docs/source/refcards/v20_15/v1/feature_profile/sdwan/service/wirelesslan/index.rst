============================================
v1.feature_profile.sdwan.service.wirelesslan
============================================


Operation: POST /dataservice/v1/feature-profile/sdwan/service/{serviceId}/wirelesslan
-------------------------------------------------------------------------------------


Create a Wirelesslan Profile Parcel for Service feature profile

.. code:: python

    def post(
        service_id: str,
        payload: CreateWirelesslanProfileParcelForServicePostRequest,
    ) -> CreateWirelesslanProfileParcelForServicePostResponse: ...


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
        client.v1.feature_profile.sdwan.service.wirelesslan.post()


Operation: PUT /dataservice/v1/feature-profile/sdwan/service/{serviceId}/wirelesslan/{wirelesslanId}
----------------------------------------------------------------------------------------------------


Update a Wirelesslan Profile Parcel for Service feature profile

.. code:: python

    def put(
        service_id: str,
        wirelesslan_id: str,
        payload: EditWirelesslanProfileParcelForServicePutRequest,
    ) -> EditWirelesslanProfileParcelForServicePutResponse: ...


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
        client.v1.feature_profile.sdwan.service.wirelesslan.put()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/service/{serviceId}/wirelesslan/{wirelesslanId}
-------------------------------------------------------------------------------------------------------


Delete a Wirelesslan Profile Parcel for Service feature profile

.. code:: python

    def delete(service_id: str, wirelesslan_id: str) -> None: ...


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
        client.v1.feature_profile.sdwan.service.wirelesslan.delete()


Operation: GET /dataservice/v1/feature-profile/sdwan/service/{serviceId}/wirelesslan
------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(service_id: str) -> GetListSdwanServiceWirelesslanPayload: ...


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
        client.v1.feature_profile.sdwan.service.wirelesslan.get()


Operation: GET /dataservice/v1/feature-profile/sdwan/service/{serviceId}/wirelesslan/{wirelesslanId}
----------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        service_id: str, wirelesslan_id: str
    ) -> GetSingleSdwanServiceWirelesslanPayload: ...


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
        client.v1.feature_profile.sdwan.service.wirelesslan.get()


.. toctree::
    :maxdepth: 1

    schema/index
    models

