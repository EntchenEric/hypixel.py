"""
This module contains classes for handling BedWars statistics.
"""
from dataclasses import dataclass
from typing import Dict, Optional


@dataclass
class BedWarsStats:
    """Class representing BedWars statistics"""
    coins: int = 0
    wins: int = 0
    losses: int = 0
    kills: int = 0
    deaths: int = 0
    final_kills: int = 0
    final_deaths: int = 0
    beds_broken: int = 0
    beds_lost: int = 0
    games_played: int = 0
    experience: int = 0
    level: int = 1
    win_streak: int = 0

    iron_collected: int = 0
    gold_collected: int = 0
    diamond_collected: int = 0
    emerald_collected: int = 0
    items_purchased: int = 0

    solo_wins: int = 0
    solo_losses: int = 0
    solo_kills: int = 0
    solo_deaths: int = 0
    solo_final_kills: int = 0
    solo_final_deaths: int = 0
    solo_beds_broken: int = 0
    solo_beds_lost: int = 0
    solo_win_streak: int = 0

    doubles_wins: int = 0
    doubles_losses: int = 0
    doubles_kills: int = 0
    doubles_deaths: int = 0
    doubles_final_kills: int = 0
    doubles_final_deaths: int = 0
    doubles_beds_broken: int = 0
    doubles_beds_lost: int = 0
    doubles_win_streak: int = 0

    threes_wins: int = 0
    threes_losses: int = 0
    threes_kills: int = 0
    threes_deaths: int = 0
    threes_final_kills: int = 0
    threes_final_deaths: int = 0
    threes_beds_broken: int = 0
    threes_beds_lost: int = 0
    threes_win_streak: int = 0

    fours_wins: int = 0
    fours_losses: int = 0
    fours_kills: int = 0
    fours_deaths: int = 0
    fours_final_kills: int = 0
    fours_final_deaths: int = 0
    fours_beds_broken: int = 0
    fours_beds_lost: int = 0
    fours_win_streak: int = 0

    active_killeffect: Optional[str] = None
    active_deathcry: Optional[str] = None
    active_victorydance: Optional[str] = None
    active_projectiletrail: Optional[str] = None
    active_glyph: Optional[str] = None
    active_islandtopper: Optional[str] = None

    def __init__(self, stats_data: Dict):
        """Initialize BedWars stats from raw stats data"""
        if not stats_data:
            return

        self.coins = stats_data.get("coins", 0)
        self.wins = stats_data.get("wins_bedwars", 0)
        self.losses = stats_data.get("losses_bedwars", 0)
        self.kills = stats_data.get("kills_bedwars", 0)
        self.deaths = stats_data.get("deaths_bedwars", 0)
        self.final_kills = stats_data.get("final_kills_bedwars", 0)
        self.final_deaths = stats_data.get("final_deaths_bedwars", 0)
        self.beds_broken = stats_data.get("beds_broken_bedwars", 0)
        self.beds_lost = stats_data.get("beds_lost_bedwars", 0)
        self.games_played = stats_data.get("games_played_bedwars", 0)
        self.experience = stats_data.get("Experience", 0)
        self.win_streak = stats_data.get("winstreak", 0)

        self.iron_collected = stats_data.get(
            "iron_resources_collected_bedwars", 0
        )
        self.gold_collected = stats_data.get(
            "gold_resources_collected_bedwars", 0
        )
        self.diamond_collected = stats_data.get(
            "diamond_resources_collected_bedwars", 0
        )
        self.emerald_collected = stats_data.get(
            "emerald_resources_collected_bedwars", 0
        )
        self.items_purchased = stats_data.get(
            "items_purchased_bedwars", 0
        )

        self.solo_wins = stats_data.get("eight_one_wins_bedwars", 0)
        self.solo_losses = stats_data.get("eight_one_losses_bedwars", 0)
        self.solo_kills = stats_data.get("eight_one_kills_bedwars", 0)
        self.solo_deaths = stats_data.get("eight_one_deaths_bedwars", 0)
        self.solo_final_kills = stats_data.get(
            "eight_one_final_kills_bedwars", 0
        )
        self.solo_final_deaths = stats_data.get(
            "eight_one_final_deaths_bedwars", 0
        )
        self.solo_beds_broken = stats_data.get(
            "eight_one_beds_broken_bedwars", 0
        )
        self.solo_beds_lost = stats_data.get(
            "eight_one_beds_lost_bedwars", 0
        )
        self.solo_win_streak = stats_data.get("eight_one_winstreak", 0)

        self.doubles_wins = stats_data.get("eight_two_wins_bedwars", 0)
        self.doubles_losses = stats_data.get("eight_two_losses_bedwars", 0)
        self.doubles_kills = stats_data.get("eight_two_kills_bedwars", 0)
        self.doubles_deaths = stats_data.get("eight_two_deaths_bedwars", 0)
        self.doubles_final_kills = stats_data.get(
            "eight_two_final_kills_bedwars", 0
        )
        self.doubles_final_deaths = stats_data.get(
            "eight_two_final_deaths_bedwars", 0
        )
        self.doubles_beds_broken = stats_data.get(
            "eight_two_beds_broken_bedwars", 0
        )
        self.doubles_beds_lost = stats_data.get(
            "eight_two_beds_lost_bedwars", 0
        )
        self.doubles_win_streak = stats_data.get("eight_two_winstreak", 0)

        self.threes_wins = stats_data.get("four_three_wins_bedwars", 0)
        self.threes_losses = stats_data.get("four_three_losses_bedwars", 0)
        self.threes_kills = stats_data.get("four_three_kills_bedwars", 0)
        self.threes_deaths = stats_data.get("four_three_deaths_bedwars", 0)
        self.threes_final_kills = stats_data.get(
            "four_three_final_kills_bedwars", 0
        )
        self.threes_final_deaths = stats_data.get(
            "four_three_final_deaths_bedwars", 0
        )
        self.threes_beds_broken = stats_data.get(
            "four_three_beds_broken_bedwars", 0
        )
        self.threes_beds_lost = stats_data.get(
            "four_three_beds_lost_bedwars", 0
        )
        self.threes_win_streak = stats_data.get("four_three_winstreak", 0)

        self.fours_wins = stats_data.get("four_four_wins_bedwars", 0)
        self.fours_losses = stats_data.get("four_four_losses_bedwars", 0)
        self.fours_kills = stats_data.get("four_four_kills_bedwars", 0)
        self.fours_deaths = stats_data.get("four_four_deaths_bedwars", 0)
        self.fours_final_kills = stats_data.get(
            "four_four_final_kills_bedwars", 0
        )
        self.fours_final_deaths = stats_data.get(
            "four_four_final_deaths_bedwars", 0
        )
        self.fours_beds_broken = stats_data.get(
            "four_four_beds_broken_bedwars", 0
        )
        self.fours_beds_lost = stats_data.get(
            "four_four_beds_lost_bedwars", 0
        )
        self.fours_win_streak = stats_data.get("four_four_winstreak", 0)

        self.level = self._calculate_level()

        self.active_killeffect = stats_data.get("active_killeffect")
        self.active_deathcry = stats_data.get("active_deathcry")
        self.active_victorydance = stats_data.get("active_victorydance")
        self.active_projectiletrail = stats_data.get("active_projectiletrail")
        self.active_glyph = stats_data.get("active_glyph")
        self.active_islandtopper = stats_data.get("active_islandtopper")

    def _calculate_level(self) -> int:
        """Calculate BedWars level from experience"""
        exp = self.experience
        prestiges = exp // 487000
        remainder = exp % 487000

        if remainder < 500:
            level = 0
        elif remainder < 1500:
            level = 1
        elif remainder < 3500:
            level = 2
        elif remainder < 7000:
            level = 3
        else:
            level = int(remainder / 5000) + 4

        return prestiges * 100 + level

    @property
    def kd_ratio(self) -> float:
        """Calculate kill/death ratio"""
        return self.kills / self.deaths if self.deaths > 0 else self.kills

    @property
    def final_kd_ratio(self) -> float:
        """Calculate final kill/death ratio"""
        return (
            self.final_kills / self.final_deaths
            if self.final_deaths > 0
            else self.final_kills
        )

    @property
    def win_ratio(self) -> float:
        """Calculate win/loss ratio"""
        return self.wins / self.losses if self.losses > 0 else self.wins

    @property
    def bed_ratio(self) -> float:
        """Calculate bed broken/lost ratio"""
        return (
            self.beds_broken / self.beds_lost
            if self.beds_lost > 0
            else self.beds_broken
        )

    def __str__(self) -> str:
        """String representation of BedWars stats"""
        return (
            f"Level: {self.level}, Wins: {self.wins}, "
            f"Final K/D: {self.final_kd_ratio:.2f}"
        )
