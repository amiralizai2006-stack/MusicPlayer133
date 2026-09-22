import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    def __init__(self) -> None:
        self.API_ID: int = int(os.environ.get("API_ID", "0").strip())
        self.API_HASH: str = os.environ.get("API_HASH", "").strip()
        self.SESSION: str = os.environ.get("SESSION", "").strip()
        self.BOT_TOKEN: str = os.environ.get("BOT_TOKEN", "").strip()

        self.SUDOERS: list = [
            int(id)
            for id in os.environ.get("SUDOERS", "").split()
            if id.isnumeric()
        ]

        if not self.SESSION or not self.API_ID or not self.API_HASH:
            print("ERROR: SESSION, API_ID and API_HASH is required!")
            raise SystemExit(1)

        self.SPOTIFY: bool = False

        self.QUALITY: str = os.environ.get(
            "QUALITY", "high"
        ).lower()

        self.PREFIXES: list = os.environ.get(
            "PREFIX", "!"
        ).split()

        self.LANGUAGE: str = os.environ.get(
            "LANGUAGE", "en"
        ).lower()

        self.STREAM_MODE: str = (
            "audio"
            if os.environ.get(
                "STREAM_MODE", "audio"
            ).lower() == "audio"
            else "video"
        )

        self.ADMINS_ONLY: bool = (
            os.environ.get("ADMINS_ONLY", "false").lower()
            in ("true", "1", "yes")
        )

        self.SPOTIFY_CLIENT_ID: str = os.environ.get(
            "SPOTIFY_CLIENT_ID", ""
        ).strip()

        self.SPOTIFY_CLIENT_SECRET: str = os.environ.get(
            "SPOTIFY_CLIENT_SECRET", ""
        ).strip()


config = Config()
