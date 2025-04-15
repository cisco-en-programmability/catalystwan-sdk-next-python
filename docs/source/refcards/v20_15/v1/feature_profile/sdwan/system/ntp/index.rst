===================================
v1.feature_profile.sdwan.system.ntp
===================================


Operation: POST /dataservice/v1/feature-profile/sdwan/system/{systemId}/ntp
---------------------------------------------------------------------------


Create a Ntp Profile Parcel for System feature profile

.. code:: python

    def post(
        system_id: str,
        payload: CreateNtpProfileParcelForSystemPostRequest,
    ) -> CreateNtpProfileParcelForSystemPostResponse: ...


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
        client.v1.feature_profile.sdwan.system.ntp.post()


Operation: PUT /dataservice/v1/feature-profile/sdwan/system/{systemId}/ntp/{ntpId}
----------------------------------------------------------------------------------


Update a Ntp Profile Parcel for System feature profile

.. code:: python

    def put(
        system_id: str,
        ntp_id: str,
        payload: EditNtpProfileParcelForSystemPutRequest,
    ) -> EditNtpProfileParcelForSystemPutResponse: ...


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
        client.v1.feature_profile.sdwan.system.ntp.put()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/system/{systemId}/ntp/{ntpId}
-------------------------------------------------------------------------------------


Delete a Ntp Profile Parcel for System feature profile

.. code:: python

    def delete(system_id: str, ntp_id: str) -> None: ...


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
        client.v1.feature_profile.sdwan.system.ntp.delete()


Operation: GET /dataservice/v1/feature-profile/sdwan/system/{systemId}/ntp
--------------------------------------------------------------------------


.. code:: python

    @overload
    def get(system_id: str) -> GetListSdwanSystemNtpPayload: ...


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
        client.v1.feature_profile.sdwan.system.ntp.get()


Operation: GET /dataservice/v1/feature-profile/sdwan/system/{systemId}/ntp/{ntpId}
----------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        system_id: str, ntp_id: str
    ) -> GetSingleSdwanSystemNtpPayload: ...


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
        client.v1.feature_profile.sdwan.system.ntp.get()


.. toctree::
    :maxdepth: 1

    schema/index
    models

