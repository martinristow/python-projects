import os
from dotenv import load_dotenv
from InstagramClass import InstaFollower

load_dotenv()

EMAIL = os.environ["INSTAGRAM_EMAIL"]
PASSWORD = os.environ["INSTAGRAM_PASSWORD"]
SIMILAR_ACC = os.environ["SIMILAR_ACCOUNT"]

instagram = InstaFollower()
instagram.login(EMAIL, PASSWORD)
