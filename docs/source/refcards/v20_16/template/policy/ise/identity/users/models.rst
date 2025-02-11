======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class UserObject:
        """
        Object containing the users name
        """

        ad_user_sam_account_name: Optional[str]


    class ErsActiveDirectoryUsers:
        users: Optional[List[UserObject]]


    class UsersDataObject:
        """
        Data Object for Users get call
        """

        ers_active_directory_users: Optional[ErsActiveDirectoryUsers]


    class HeaderObject:
        """
        Header for Response
        """

        columns: Optional[Any]
        fields: Optional[Any]
        generated_on: Optional[int]
        view_keys: Optional[Any]


    class UsersResponse:
        """
        Users returned from ISE active directory domain
        """

        # Data Object for Users get call
        data: Optional[UsersDataObject]
        # Header for Response
        header: Optional[HeaderObject]


    class UsersBody:
        """
        Users body with regex filter for which users to retrieve from ISE
        """

        filter: Optional[str]


