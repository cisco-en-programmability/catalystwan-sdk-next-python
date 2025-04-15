===========================================
v1.feature_profile.sdwan.other.thousandeyes
===========================================


Operation: POST /dataservice/v1/feature-profile/sdwan/other/{otherId}/thousandeyes
----------------------------------------------------------------------------------


Create a Thousandeyes Profile Parcel for Other feature profile

.. code:: python

    def post(
        other_id: str,
        payload: CreateThousandeyesProfileParcelForOtherPostRequest,
    ) -> CreateThousandeyesProfileParcelForOtherPostResponse: ...


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
        client.v1.feature_profile.sdwan.other.thousandeyes.post()


Operation: PUT /dataservice/v1/feature-profile/sdwan/other/{otherId}/thousandeyes/{thousandeyesId}
--------------------------------------------------------------------------------------------------


Update a Thousandeyes Profile Parcel for Other feature profile

.. code:: python

    def put(
        other_id: str,
        thousandeyes_id: str,
        payload: EditThousandeyesProfileParcelForOtherPutRequest,
    ) -> EditThousandeyesProfileParcelForOtherPutResponse: ...


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
        client.v1.feature_profile.sdwan.other.thousandeyes.put()


Operation: DELETE /dataservice/v1/feature-profile/sdwan/other/{otherId}/thousandeyes/{thousandeyesId}
-----------------------------------------------------------------------------------------------------


Delete a Thousandeyes Profile Parcel for Other feature profile

.. code:: python

    def delete(other_id: str, thousandeyes_id: str) -> None: ...


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
        client.v1.feature_profile.sdwan.other.thousandeyes.delete()


Operation: GET /dataservice/v1/feature-profile/sdwan/other/{otherId}/thousandeyes
---------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(other_id: str) -> GetListSdwanOtherThousandeyesPayload: ...


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
        client.v1.feature_profile.sdwan.other.thousandeyes.get()


Operation: GET /dataservice/v1/feature-profile/sdwan/other/{otherId}/thousandeyes/{thousandeyesId}
--------------------------------------------------------------------------------------------------


.. code:: python

    @overload
    def get(
        other_id: str, thousandeyes_id: str
    ) -> GetSingleSdwanOtherThousandeyesPayload: ...


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
        client.v1.feature_profile.sdwan.other.thousandeyes.get()


.. toctree::
    :maxdepth: 1

    schema/index
    models

