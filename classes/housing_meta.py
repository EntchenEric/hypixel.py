class HousingMeta:
    """Class representing a player's housing meta data.
    """

    def __init__(self, housing_meta: dict):
        self._allowed_blocks: list[str] = housing_meta.get("allowedBlocks", [])
        self._tutorial_step: str = housing_meta.get("tutorialStep", "")
        self._packages: list[str] = housing_meta.get("packages", [])
        self._player_settings: dict = housing_meta.get("playerSettings", {})
        self._plot_size: str = housing_meta.get("plotSize", "")
        self._first_house_join_ms: int = housing_meta.get(
            "firstHouseJoinMs",
            0,
        )

        # Store cookie tracking data
        self._given_cookies = {}
        for key, value in housing_meta.items():
            if key.startswith("given_cookies_"):
                self._given_cookies[key] = value

    @property
    def allowed_blocks(self) -> list[str]:
        return self._allowed_blocks

    @property
    def tutorial_step(self) -> str:
        return self._tutorial_step

    @property
    def packages(self) -> list[str]:
        return self._packages

    @property
    def player_settings(self) -> dict:
        return self._player_settings

    @property
    def plot_size(self) -> str:
        return self._plot_size

    @property
    def first_house_join_ms(self) -> int:
        return self._first_house_join_ms

    @property
    def given_cookies(self) -> dict:
        return self._given_cookies

    def has_package(self, package_id: str) -> bool:
        return package_id in self._packages

    def has_block(self, block_id: str) -> bool:
        return block_id in self._allowed_blocks

    def get_setting(self, setting_key: str) -> str:
        return self._player_settings.get(setting_key, "")
