"""
This module contains classes for handling SkyWars statistics.
"""

from dataclasses import dataclass
from typing import Dict, Optional


@dataclass
class SkyWarsStats:
    """Class representing SkyWars statistics"""

    coins: int = 0
    souls: int = 0
    wins: int = 0
    losses: int = 0
    kills: int = 0
    deaths: int = 0
    assists: int = 0
    games_played: int = 0
    experience: float = 0.0
    level: str = "1⋆"
    win_streak: int = 0

    blocks_broken: int = 0
    blocks_placed: int = 0
    arrows_shot: int = 0
    arrows_hit: int = 0
    egg_thrown: int = 0
    enderpearls_thrown: int = 0

    solo_wins: int = 0
    solo_losses: int = 0
    solo_kills: int = 0
    solo_deaths: int = 0
    team_wins: int = 0
    team_losses: int = 0
    team_kills: int = 0
    team_deaths: int = 0
    mega_wins: int = 0
    mega_losses: int = 0
    mega_kills: int = 0
    mega_deaths: int = 0

    active_killeffect: Optional[str] = None
    active_projectiletrail: Optional[str] = None
    active_victorydance: Optional[str] = None
    active_cage: Optional[str] = None
    active_deathcry: Optional[str] = None

    def __init__(self, stats_data: Dict):
        """Initialize SkyWars stats from raw stats data"""
        if not stats_data:
            return

        self.coins = stats_data.get("coins", 0)
        self.souls = stats_data.get("souls", 0)
        self.wins = stats_data.get("wins", 0)
        self.losses = stats_data.get("losses", 0)
        self.kills = stats_data.get("kills", 0)
        self.deaths = stats_data.get("deaths", 0)
        self.assists = stats_data.get("assists", 0)
        self.games_played = stats_data.get("games_played", 0)
        self.experience = stats_data.get("skywars_experience", 0.0)
        self.level = stats_data.get("levelFormatted", "1⋆")
        self.win_streak = stats_data.get("win_streak", 0)

        self.blocks_broken = stats_data.get("blocks_broken", 0)
        self.blocks_placed = stats_data.get("blocks_placed", 0)
        self.arrows_shot = stats_data.get("arrows_shot", 0)
        self.arrows_hit = stats_data.get("arrows_hit", 0)
        self.egg_thrown = stats_data.get("egg_thrown", 0)
        self.enderpearls_thrown = stats_data.get("enderpearls_thrown", 0)

        self.solo_wins = stats_data.get("wins_solo", 0)
        self.solo_losses = stats_data.get("losses_solo", 0)
        self.solo_kills = stats_data.get("kills_solo", 0)
        self.solo_deaths = stats_data.get("deaths_solo", 0)
        self.team_wins = stats_data.get("wins_team", 0)
        self.team_losses = stats_data.get("losses_team", 0)
        self.team_kills = stats_data.get("kills_team", 0)
        self.team_deaths = stats_data.get("deaths_team", 0)
        self.mega_wins = stats_data.get("wins_mega", 0)
        self.mega_losses = stats_data.get("losses_mega", 0)
        self.mega_kills = stats_data.get("kills_mega", 0)
        self.mega_deaths = stats_data.get("deaths_mega", 0)

        self.active_killeffect = stats_data.get("active_killeffect")
        self.active_projectiletrail = stats_data.get("active_projectiletrail")
        self.active_victorydance = stats_data.get("active_victorydance")
        self.active_cage = stats_data.get("active_cage")
        self.active_deathcry = stats_data.get("active_deathcry")

    @property
    def kd_ratio(self) -> float:
        """Calculate kill/death ratio"""
        return self.kills / self.deaths if self.deaths > 0 else self.kills

    @property
    def win_ratio(self) -> float:
        """Calculate win/loss ratio"""
        return self.wins / self.losses if self.losses > 0 else self.wins

    def __str__(self) -> str:
        """String representation of SkyWars stats"""
        return (
            f"Level: {self.level}, Wins: {self.wins}, "
            f"K/D: {self.kd_ratio:.2f}"
        )
