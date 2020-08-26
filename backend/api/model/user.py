class UserModel:
    def __init__(self, created_at: str = None, username: str = None,
                 name: str = None, user_id: str = None):
        """User - a model defined in Swagger

        :param created_at: The created_at of this User.  # noqa: E501
        :type created_at: UTCTime
        :param username: The username of this User.  # noqa: E501
        :type username: str
        :param name: The name of this User.  # noqa: E501
        :type name: str
        :param id: The id of this User.  # noqa: E501
        :type id: str
        """
        self.created_at = created_at
        self.username = username
        self.name = name
        self.user_id = user_id
