class AchievementProgress:
    """Class representing a player"s achievement progress"""

    def __init__(self, achievements: dict):
        for name, progress in achievements.items():
            safe_name = name.replace("-", "_")
            setattr(self, f"_{safe_name}", progress)

    @property
    def truecombat_kit_hoarder_solo(self) -> int:
        return getattr(self, "_truecombat_kit_hoarder_solo", 0)

    @property
    def truecombat_kit_hoarder_team(self) -> int:
        return getattr(self, "_truecombat_kit_hoarder_team", 0)

    @property
    def truecombat_team_killer(self) -> int:
        return getattr(self, "_truecombat_team_killer", 0)

    @property
    def skywars_kits_solo(self) -> int:
        return getattr(self, "_skywars_kits_solo", 0)

    @property
    def skywars_kits_team(self) -> int:
        return getattr(self, "_skywars_kits_team", 0)

    @property
    def skywars_cages(self) -> int:
        return getattr(self, "_skywars_cages", 0)

    @property
    def skywars_kills_solo(self) -> int:
        return getattr(self, "_skywars_kills_solo", 0)

    @property
    def skywars_kills_team(self) -> int:
        return getattr(self, "_skywars_kills_team", 0)

    @property
    def skywars_wins_team(self) -> int:
        return getattr(self, "_skywars_wins_team", 0)

    @property
    def general_wins(self) -> int:
        return getattr(self, "_general_wins", 0)

    @property
    def copsandcrims_bomb_specialist(self) -> int:
        return getattr(self, "_copsandcrims_bomb_specialist", 0)

    @property
    def arcade_miniwalls_winner(self) -> int:
        return getattr(self, "_arcade_miniwalls_winner", 0)

    @property
    def arcade_arcade_winner(self) -> int:
        return getattr(self, "_arcade_arcade_winner", 0)

    @property
    def arcade_arcade_banker(self) -> int:
        return getattr(self, "_arcade_arcade_banker", 0)

    @property
    def walls3_wins(self) -> int:
        return getattr(self, "_walls3_wins", 0)

    @property
    def walls3_guardian(self) -> int:
        return getattr(self, "_walls3_guardian", 0)

    @property
    def general_coins(self) -> int:
        return getattr(self, "_general_coins", 0)

    @property
    def copsandcrims_cac_banker(self) -> int:
        return getattr(self, "_copsandcrims_cac_banker", 0)

    @property
    def copsandcrims_headshot_kills(self) -> int:
        return getattr(self, "_copsandcrims_headshot_kills", 0)

    @property
    def warlords_ctf_objective(self) -> int:
        return getattr(self, "_warlords_ctf_objective", 0)

    @property
    def warlords_assist(self) -> int:
        return getattr(self, "_warlords_assist", 0)

    @property
    def warlords_coins(self) -> int:
        return getattr(self, "_warlords_coins", 0)

    @property
    def warlords_kills(self) -> int:
        return getattr(self, "_warlords_kills", 0)

    @property
    def skyblock_minion_lover(self) -> int:
        return getattr(self, "_skyblock_minion_lover", 0)

    @property
    def copsandcrims_grenade_kills(self) -> int:
        return getattr(self, "_copsandcrims_grenade_kills", 0)

    @property
    def skyblock_gatherer(self) -> int:
        return getattr(self, "_skyblock_gatherer", 0)

    @property
    def skyblock_combat(self) -> int:
        return getattr(self, "_skyblock_combat", 0)

    @property
    def skyblock_angler(self) -> int:
        return getattr(self, "_skyblock_angler", 0)

    @property
    def murdermystery_hoarder(self) -> int:
        return getattr(self, "_murdermystery_hoarder", 0)

    @property
    def murdermystery_wins_as_survivor(self) -> int:
        return getattr(self, "_murdermystery_wins_as_survivor", 0)

    @property
    def skyblock_augmentation(self) -> int:
        return getattr(self, "_skyblock_augmentation", 0)

    @property
    def arcade_zombies_nice_shot(self) -> int:
        return getattr(self, "_arcade_zombies_nice_shot", 0)

    @property
    def arcade_zombies_round_progression(self) -> int:
        return getattr(self, "_arcade_zombies_round_progression", 0)

    @property
    def arcade_zombies_high_round(self) -> int:
        return getattr(self, "_arcade_zombies_high_round", 0)

    @property
    def bedwars_wins(self) -> int:
        return getattr(self, "_bedwars_wins", 0)

    @property
    def bedwars_loot_box(self) -> int:
        return getattr(self, "_bedwars_loot_box", 0)

    @property
    def arcade_zombie_killer(self) -> int:
        return getattr(self, "_arcade_zombie_killer", 0)

    @property
    def arcade_team_work(self) -> int:
        return getattr(self, "_arcade_team_work", 0)

    @property
    def easter_egg_finder(self) -> int:
        return getattr(self, "_easter_egg_finder", 0)

    @property
    def easter_throw_eggs(self) -> int:
        return getattr(self, "_easter_throw_eggs", 0)

    @property
    def skyblock_unique_gifts(self) -> int:
        return getattr(self, "_skyblock_unique_gifts", 0)

    @property
    def skyblock_domesticator(self) -> int:
        return getattr(self, "_skyblock_domesticator", 0)

    @property
    def skyblock_slayer(self) -> int:
        return getattr(self, "_skyblock_slayer", 0)

    @property
    def skywars_kills_mega(self) -> int:
        return getattr(self, "_skywars_kills_mega", 0)

    @property
    def summer_treasure_hoarder(self) -> int:
        return getattr(self, "_summer_treasure_hoarder", 0)

    @property
    def arena_climb_the_ranks(self) -> int:
        return getattr(self, "_arena_climb_the_ranks", 0)

    @property
    def summer_gone_fishing(self) -> int:
        return getattr(self, "_summer_gone_fishing", 0)

    @property
    def skywars_heads(self) -> int:
        return getattr(self, "_skywars_heads", 0)

    @property
    def pit_gold(self) -> int:
        return getattr(self, "_pit_gold", 0)

    @property
    def pit_kills(self) -> int:
        return getattr(self, "_pit_kills", 0)

    @property
    def skyblock_treasure_hunter(self) -> int:
        return getattr(self, "_skyblock_treasure_hunter", 0)

    @property
    def skyblock_dungeoneer(self) -> int:
        return getattr(self, "_skyblock_dungeoneer", 0)

    @property
    def christmas2017_advent_2020(self) -> int:
        return getattr(self, "_christmas2017_advent_2020", 0)

    @property
    def christmas2017_present_collector(self) -> int:
        return getattr(self, "_christmas2017_present_collector", 0)

    @property
    def bedwars_collectors_edition(self) -> int:
        return getattr(self, "_bedwars_collectors_edition", 0)

    @property
    def general_quest_master(self) -> int:
        return getattr(self, "_general_quest_master", 0)

    @property
    def bedwars_beds(self) -> int:
        return getattr(self, "_bedwars_beds", 0)

    @property
    def christmas2017_no_christmas(self) -> int:
        return getattr(self, "_christmas2017_no_christmas", 0)

    @property
    def supersmash_hero_slayer(self) -> int:
        return getattr(self, "_supersmash_hero_slayer", 0)

    @property
    def skywars_wins_lab(self) -> int:
        return getattr(self, "_skywars_wins_lab", 0)

    @property
    def duels_duels_traveller(self) -> int:
        return getattr(self, "_duels_duels_traveller", 0)

    @property
    def duels_duels_win_streak(self) -> int:
        return getattr(self, "_duels_duels_win_streak", 0)

    @property
    def arcade_hide_and_seek_hider_kills(self) -> int:
        return getattr(self, "_arcade_hide_and_seek_hider_kills", 0)

    @property
    def arcade_bounty_hunter(self) -> int:
        return getattr(self, "_arcade_bounty_hunter", 0)

    @property
    def walls3_cake_hunter_tiered(self) -> int:
        return getattr(self, "_walls3_cake_hunter_tiered", 0)

    @property
    def gingerbread_banker(self) -> int:
        return getattr(self, "_gingerbread_banker", 0)

    @property
    def gingerbread_mystery(self) -> int:
        return getattr(self, "_gingerbread_mystery", 0)

    @property
    def gingerbread_racer(self) -> int:
        return getattr(self, "_gingerbread_racer", 0)

    @property
    def quake_coins(self) -> int:
        return getattr(self, "_quake_coins", 0)

    @property
    def quake_kills(self) -> int:
        return getattr(self, "_quake_kills", 0)

    @property
    def quake_headshots(self) -> int:
        return getattr(self, "_quake_headshots", 0)

    @property
    def quake_wins(self) -> int:
        return getattr(self, "_quake_wins", 0)

    @property
    def paintball_coins(self) -> int:
        return getattr(self, "_paintball_coins", 0)

    @property
    def paintball_kills(self) -> int:
        return getattr(self, "_paintball_kills", 0)

    @property
    def halloween2017_pumpkinator(self) -> int:
        return getattr(self, "_halloween2017_pumpkinator", 0)

    @property
    def skyblock_goblin_killer(self) -> int:
        return getattr(self, "_skyblock_goblin_killer", 0)

    @property
    def christmas2017_advent_2021(self) -> int:
        return getattr(self, "_christmas2017_advent_2021", 0)

    @property
    def arcade_galaxy_wars_kills(self) -> int:
        return getattr(self, "_arcade_galaxy_wars_kills", 0)

    @property
    def skyblock_divans_treasures(self) -> int:
        return getattr(self, "_skyblock_divans_treasures", 0)

    @property
    def skyblock_crystal_nucleus(self) -> int:
        return getattr(self, "_skyblock_crystal_nucleus", 0)

    @property
    def murdermystery_brainiac(self) -> int:
        return getattr(self, "_murdermystery_brainiac", 0)

    @property
    def murdermystery_countermeasures(self) -> int:
        return getattr(self, "_murdermystery_countermeasures", 0)

    @property
    def murdermystery_kills_as_murderer(self) -> int:
        return getattr(self, "_murdermystery_kills_as_murderer", 0)

    @property
    def christmas2017_advent_2022(self) -> int:
        return getattr(self, "_christmas2017_advent_2022", 0)

    @property
    def skyblock_people_pleaser(self) -> int:
        return getattr(self, "_skyblock_people_pleaser", 0)

    @property
    def skyblock_curator(self) -> int:
        return getattr(self, "_skyblock_curator", 0)

    @property
    def skyblock_sb_levels(self) -> int:
        return getattr(self, "_skyblock_sb_levels", 0)

    @property
    def buildbattle_build_battle_voter(self) -> int:
        return getattr(self, "_buildbattle_build_battle_voter", 0)

    @property
    def buildbattle_build_battle_points(self) -> int:
        return getattr(self, "_buildbattle_build_battle_points", 0)

    @property
    def buildbattle_build_battle_score(self) -> int:
        return getattr(self, "_buildbattle_build_battle_score", 0)

    @property
    def arcade_dropper_skydiver(self) -> int:
        return getattr(self, "_arcade_dropper_skydiver", 0)

    @property
    def arcade_pixel_party_color_coordinated(self) -> int:
        return getattr(self, "_arcade_pixel_party_color_coordinated", 0)

    @property
    def murdermystery_wins_as_murderer(self) -> int:
        return getattr(self, "_murdermystery_wins_as_murderer", 0)

    @property
    def buildbattle_guess_the_build_guesses(self) -> int:
        return getattr(self, "_buildbattle_guess_the_build_guesses", 0)

    @property
    def christmas2017_advent_2023(self) -> int:
        return getattr(self, "_christmas2017_advent_2023", 0)
