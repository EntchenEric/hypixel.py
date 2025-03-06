"""
This module contains the Player class which represents a Hypixel player.
"""

from dataclasses import dataclass
from datetime import datetime
from typing import Dict, Optional
from .rank import Rank
from .games.skywars import SkyWarsStats
from .games.bedwars import BedWarsStats
from .games.murder_mystery import MurderMysteryStats
from .achievement_progress import AchievementProgress
from .achievements import Achievements
from .pet_consumables import PetConsumables


@dataclass
class PlayerStats:
    """Class representing player statistics for various game modes"""

    skywars: Optional[SkyWarsStats] = None
    bedwars: Optional[BedWarsStats] = None
    murder_mystery: Optional[MurderMysteryStats] = None
    arcade: Optional[Dict] = None
    duels: Optional[Dict] = None
    uhc: Optional[Dict] = None
    tnt_games: Optional[Dict] = None
    pit: Optional[Dict] = None
    skyblock: Optional[Dict] = None

    def __init__(self, stats_data: Dict):
        """Initialize player stats from raw stats data"""
        self.skywars = (
            SkyWarsStats(stats_data["SkyWars"])
            if "SkyWars" in stats_data else None
        )
        self.bedwars = (
            BedWarsStats(stats_data["Bedwars"])
            if "Bedwars" in stats_data else None
        )
        self.murder_mystery = (
            MurderMysteryStats(stats_data["MurderMystery"])
            if "MurderMystery" in stats_data
            else None
        )

        self.arcade = stats_data.get("Arcade")
        self.duels = stats_data.get("Duels")
        self.uhc = stats_data.get("UHC")
        self.tnt_games = stats_data.get("TNTGames")
        self.pit = stats_data.get("Pit")
        self.skyblock = stats_data.get("SkyBlock")


class Player:
    """
    Class representing a Hypixel player with all
    their attributes and statistics.
    """

    def __init__(
        self,
        _id: str,
        uuid: str,
        display_name: str,
        rank: str,
        package_rank: str,
        new_package_rank: str,
        monthly_package_rank: str,
        first_login: int,
        last_login: int,
        last_logout: int,
        stats: dict,
        achievement_progress: dict,
        achievements: dict,
        networkExp: int,
        spec_auto_teleport: bool,
        spec_always_flying: bool,
        karma: int,
        pet_consumables: dict,
        network_update_book: str,
        last_adsense_generate_time: int,
        achievement_points: int,
        user_language: str,
        last_claimed_reward: int,
        reward_high_score: int,
        reward_score: int,
        reward_streak: int,
        total_daily_rewards: int,
        total_rewards: int,
        level_up_vip: int,
        claimed_potato_talisman: int,
        adsense_tokens: int,
        skyblock_free_cookie: int,
        scorpius_bribe_96: int,
        claimed_century_cake: int,
        level_up_vip_plus: int,
        vanity_favorites: str,
        level_up_mvp_plus: int,
        rank_plus_color: str,
        current_pet: str,
        claimed_year143_cake: int,
        channel: str,
        fortuneBuff: int,
        claimed_century_cake2000: int,
        most_recent_game_type: str,
    ):
        self._id = _id
        self.uuid = uuid
        self.display_name = display_name
        self._rank = Rank.from_api(rank)
        self._package_rank = package_rank
        self._new_package_rank = new_package_rank
        self._monthly_package_rank = monthly_package_rank
        self.first_login = datetime.fromtimestamp(first_login / 1000)
        self.last_login = datetime.fromtimestamp(last_login / 1000)
        self.last_logout = datetime.fromtimestamp(last_logout / 1000)
        self.stats = PlayerStats(stats)
        self.achievement_progress = AchievementProgress(achievement_progress)
        self.achievements = Achievements(achievements)
        self.networkExp = networkExp
        self.spec_auto_teleport = spec_auto_teleport
        self.spec_always_flying = spec_always_flying
        self.karma = karma
        self.pet_consumables = PetConsumables(pet_consumables)
        self.network_update_book = network_update_book
        self.last_adsense_generate_time = last_adsense_generate_time
        self.achievement_points = achievement_points
        self.user_language = user_language
        self.last_claimed_reward = datetime.fromtimestamp(
            last_claimed_reward / 1000
        )
        self.reward_high_score = reward_high_score
        self.reward_score = reward_score
        self.reward_streak = reward_streak
        self.total_daily_rewards = total_daily_rewards
        self.total_rewards = total_rewards
        self.level_up_vip = datetime.fromtimestamp(level_up_vip / 1000)
        self.claimed_potato_talisman = datetime.fromtimestamp(
            claimed_potato_talisman / 1000
        )
        self.adsense_tokens = adsense_tokens
        self.skyblock_free_cookie = datetime.fromtimestamp(
            skyblock_free_cookie / 1000
        )
        self.scorpius_bribe_96 = datetime.fromtimestamp(
            scorpius_bribe_96 / 1000
        )
        self.claimed_century_cake = datetime.fromtimestamp(
            claimed_century_cake / 1000
        )
        self.level_up_vip_plus = datetime.fromtimestamp(
            level_up_vip_plus / 1000
        )
        self.vanity_favorites = vanity_favorites
        self.level_up_mvp_plus = level_up_mvp_plus
        self.rank_plus_color = rank_plus_color
        self.current_pet = current_pet
        self.claimed_year143_cake = datetime.fromtimestamp(
            claimed_year143_cake / 1000
        )
        self.channel = channel
        self.fortuneBuff = datetime.fromtimestamp(fortuneBuff / 1000)
        self.claimed_century_cake2000 = datetime.fromtimestamp(
            claimed_century_cake2000 / 1000
        )
        self.most_recent_game_type = most_recent_game_type

    @property
    def rank(self) -> Rank:
        """Get the player's highest rank"""
        ranks = [
            self._rank,
            self._package_rank,
            self._new_package_rank,
            self._monthly_package_rank,
        ]
        ranks = [r for r in ranks if r and r != "NONE"]
        if not ranks:
            return Rank.DEFAULT
        return max(ranks, key=lambda r: Rank.from_api(r).name)

    @property
    def is_online(self) -> bool:
        """Check if the player is currently online"""
        return self.last_login > self.last_logout

    @property
    def playtime(self) -> float:
        """Get the player's total playtime in hours"""
        return (self.last_logout - self.first_login).total_seconds() / 3600

    def get_uuid(self) -> str:
        """Get the player's UUID"""
        return self.uuid

    def __str__(self) -> str:
        """String representation of the player"""
        return f"{self.rank}{self.display_name}"

    def __repr__(self) -> str:
        """Detailed string representation of the player"""
        return (
            f"Player(uuid={self.uuid}, name={self.display_name}, "
            f"rank={self.rank})"
        )

    def get_achievement_progress(self, achievement_name: str) -> int:
        """Get the progress of a specific achievement"""
        return self.achievement_progress.get(achievement_name, 0)
