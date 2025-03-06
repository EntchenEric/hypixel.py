"""
This module contains classes for handling Murder Mystery statistics.
"""
from dataclasses import dataclass
from typing import Dict, Optional


@dataclass
class MurderMysteryStats:
    """Class representing Murder Mystery statistics"""
    coins: int = 0
    wins: int = 0
    games_played: int = 0
    kills: int = 0
    deaths: int = 0
    coins_picked_up: int = 0
    murderer_wins: int = 0
    detective_wins: int = 0
    hero_wins: int = 0
    was_hero: int = 0
    bow_kills: int = 0
    knife_kills: int = 0
    thrown_knife_kills: int = 0
    trap_kills: int = 0

    classic_wins: int = 0
    classic_games: int = 0
    classic_kills: int = 0
    classic_deaths: int = 0
    classic_coins_picked_up: int = 0
    classic_murderer_wins: int = 0
    classic_detective_wins: int = 0
    classic_hero_wins: int = 0
    classic_was_hero: int = 0

    double_up_wins: int = 0
    double_up_games: int = 0
    double_up_kills: int = 0
    double_up_deaths: int = 0
    double_up_coins_picked_up: int = 0
    double_up_murderer_wins: int = 0
    double_up_detective_wins: int = 0
    double_up_hero_wins: int = 0
    double_up_was_hero: int = 0

    assassins_wins: int = 0
    assassins_games: int = 0
    assassins_kills: int = 0
    assassins_deaths: int = 0
    assassins_coins_picked_up: int = 0

    infection_wins: int = 0
    infection_games: int = 0
    infection_kills_as_survivor: int = 0
    infection_kills_as_infected: int = 0
    infection_deaths: int = 0
    infection_coins_picked_up: int = 0
    infection_longest_survivor_time: int = 0
    infection_total_survivor_time: int = 0

    active_kill_note: Optional[str] = None
    active_last_words: Optional[str] = None
    active_victory_dance: Optional[str] = None
    active_gesture: Optional[str] = None
    active_knife_skin: Optional[str] = None
    active_death_cry: Optional[str] = None
    active_animated_hat: Optional[str] = None

    def __init__(self, stats_data: Dict):
        """Initialize Murder Mystery stats from raw stats data"""
        if not stats_data:
            return

        self.coins = stats_data.get("coins", 0)
        self.wins = stats_data.get("wins", 0)
        self.games_played = stats_data.get("games", 0)
        self.kills = stats_data.get("kills", 0)
        self.deaths = stats_data.get("deaths", 0)
        self.coins_picked_up = stats_data.get("coins_pickedup", 0)
        self.murderer_wins = stats_data.get("murderer_wins", 0)
        self.detective_wins = stats_data.get("detective_wins", 0)
        self.hero_wins = stats_data.get("hero_wins", 0)
        self.was_hero = stats_data.get("was_hero", 0)
        self.bow_kills = stats_data.get("bow_kills", 0)
        self.knife_kills = stats_data.get("knife_kills", 0)
        self.thrown_knife_kills = stats_data.get("thrown_knife_kills", 0)
        self.trap_kills = stats_data.get("trap_kills", 0)

        self.classic_wins = stats_data.get("wins_MURDER_CLASSIC", 0)
        self.classic_games = stats_data.get("games_MURDER_CLASSIC", 0)
        self.classic_kills = stats_data.get("kills_MURDER_CLASSIC", 0)
        self.classic_deaths = stats_data.get("deaths_MURDER_CLASSIC", 0)
        self.classic_coins_picked_up = stats_data.get(
            "coins_pickedup_MURDER_CLASSIC", 0
        )
        self.classic_murderer_wins = stats_data.get(
            "murderer_wins_MURDER_CLASSIC", 0
        )
        self.classic_detective_wins = stats_data.get(
            "detective_wins_MURDER_CLASSIC", 0
        )
        self.classic_was_hero = stats_data.get("was_hero_MURDER_CLASSIC", 0)

        self.double_up_wins = stats_data.get("wins_MURDER_DOUBLE_UP", 0)
        self.double_up_games = stats_data.get("games_MURDER_DOUBLE_UP", 0)
        self.double_up_kills = stats_data.get("kills_MURDER_DOUBLE_UP", 0)
        self.double_up_deaths = stats_data.get("deaths_MURDER_DOUBLE_UP", 0)
        self.double_up_coins_picked_up = stats_data.get(
            "coins_pickedup_MURDER_DOUBLE_UP", 0
        )
        self.double_up_murderer_wins = stats_data.get(
            "murderer_wins_MURDER_DOUBLE_UP", 0
        )
        self.double_up_detective_wins = stats_data.get(
            "detective_wins_MURDER_DOUBLE_UP", 0
        )
        self.double_up_was_hero = stats_data.get(
            "was_hero_MURDER_DOUBLE_UP", 0
        )

        self.assassins_wins = stats_data.get("wins_MURDER_ASSASSINS", 0)
        self.assassins_games = stats_data.get("games_MURDER_ASSASSINS", 0)
        self.assassins_kills = stats_data.get("kills_MURDER_ASSASSINS", 0)
        self.assassins_deaths = stats_data.get("deaths_MURDER_ASSASSINS", 0)
        self.assassins_coins_picked_up = stats_data.get(
            "coins_pickedup_MURDER_ASSASSINS", 0
        )

        self.infection_wins = stats_data.get("wins_MURDER_INFECTION", 0)
        self.infection_games = stats_data.get("games_MURDER_INFECTION", 0)
        self.infection_kills_as_survivor = stats_data.get(
            "kills_as_survivor_MURDER_INFECTION", 0
        )
        self.infection_kills_as_infected = stats_data.get(
            "kills_as_infected_MURDER_INFECTION", 0
        )
        self.infection_deaths = stats_data.get(
            "deaths_MURDER_INFECTION", 0
        )
        self.infection_coins_picked_up = stats_data.get(
            "coins_pickedup_MURDER_INFECTION", 0
        )
        self.infection_longest_survivor_time = stats_data.get(
            "longest_time_as_survivor_seconds_MURDER_INFECTION", 0
        )
        self.infection_total_survivor_time = stats_data.get(
            "total_time_survived_seconds_MURDER_INFECTION", 0
        )

        self.active_kill_note = stats_data.get("active_kill_note")
        self.active_last_words = stats_data.get("active_last_words")
        self.active_victory_dance = stats_data.get("active_victory_dance")
        self.active_gesture = stats_data.get("active_gesture")
        self.active_knife_skin = stats_data.get("active_knife_skin")
        self.active_death_cry = stats_data.get("active_deathcry")
        self.active_animated_hat = stats_data.get("active_animated_hat")

    @property
    def kd_ratio(self) -> float:
        """Calculate kill/death ratio"""
        return self.kills / self.deaths if self.deaths > 0 else self.kills

    @property
    def win_rate(self) -> float:
        """Calculate win rate percentage"""
        return (
            (self.wins / self.games_played) * 100
            if self.games_played > 0
            else 0
        )

    @property
    def hero_rate(self) -> float:
        """Calculate hero rate percentage"""
        return (
            (self.was_hero / self.games_played) * 100
            if self.games_played > 0
            else 0
        )

    def __str__(self) -> str:
        """String representation of Murder Mystery stats"""
        return (
            f"Wins: {self.wins}, K/D: {self.kd_ratio:.2f}, "
            f"Hero Rate: {self.hero_rate:.1f}%"
        )
