import os

from dotenv import load_dotenv

load_dotenv()

class Credentials:

    ADMIN_LOGIN = os.getenv("ADMIN_LOGIN", "administrator")
    ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "administrator")
    FRIEND_LOGIN = os.getenv("FRIEND_LOGIN")
    FRIEND_PASSWORD = os.getenv("FRIEND_PASSWORD")
