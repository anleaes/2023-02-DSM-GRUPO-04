from models.client import Client
from models.socialnetwork import Socialnetwork


class ClientSocialnetwork:
     def __init__(
        self,
        *,
        client: Client,
        socialnetwork: Socialnetwork,
    ):
        self.client = client
        self.socialnetwork = socialnetwork