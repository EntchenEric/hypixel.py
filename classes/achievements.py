class Achievements:
    """Class representing a player"s achievements"""

    def __init__(self, achievements: dict):
        for name in achievements:
            safe_name = name.replace("-", "_")
            setattr(self, f"_{safe_name}", True)

    @property
    def general_first_join(self) -> bool:
        return getattr(self, "_general_first_join", False)

    @property
    def truecombat_strategist(self) -> bool:
        return getattr(self, "_truecombat_strategist", False)

    @property
    def truecombat_destiny_calls(self) -> bool:
        return getattr(self, "_truecombat_destiny_calls", False)

    @property
    def truecombat_cross_fingers(self) -> bool:
        return getattr(self, "_truecombat_cross_fingers", False)

    @property
    def truecombat_redstone_dealer(self) -> bool:
        return getattr(self, "_truecombat_redstone_dealer", False)

    @property
    def general_first_chat(self) -> bool:
        return getattr(self, "_general_first_chat", False)

    @property
    def skywars_gotcha(self) -> bool:
        return getattr(self, "_skywars_gotcha", False)

    @property
    def skywars_touch_of_death(self) -> bool:
        return getattr(self, "_skywars_touch_of_death", False)

    @property
    def general_creeperbook(self) -> bool:
        return getattr(self, "_general_creeperbook", False)

    @property
    def general_first_game(self) -> bool:
        return getattr(self, "_general_first_game", False)

    @property
    def vampirez_vampire_shop(self) -> bool:
        return getattr(self, "_vampirez_vampire_shop", False)

    @property
    def general_first_friend(self) -> bool:
        return getattr(self, "_general_first_friend", False)

    @property
    def copsandcrims_late_to_the_party(self) -> bool:
        return getattr(self, "_copsandcrims_challenge_completed", False)

    @property
    def copsandcrims_samurai_warrior(self) -> bool:
        return getattr(self, "_copsandcrims_samurai_warrior", False)

    @property
    def skyblock_your_adventure_begins(self) -> bool:
        return getattr(self, "_skyblock_your_adventure_begins", False)

    @property
    def skyblock_quest_complete(self) -> bool:
        return getattr(self, "_skyblock_quest_complete", False)

    @property
    def copsandcrims_grenade_kill(self) -> bool:
        return getattr(self, "_copsandcrims_grenade_kill", False)

    @property
    def skyblock_explorer(self) -> bool:
        return getattr(self, "_skyblock_explorer", False)

    @property
    def skyblock_lost_soul(self) -> bool:
        return getattr(self, "_skyblock_lost_soul", False)

    @property
    def skyblock_production_expanded(self) -> bool:
        return getattr(self, "_general_creeperbook", False)

    @property
    def murdermystery_be_the_hero(self) -> bool:
        return getattr(self, "_general_first_party", False)

    @property
    def skyblock_promised_fulfilled(self) -> bool:
        return getattr(self, "_skyblock_promised_fulfilled", False)

    @property
    def arcade_zombies_feels_good(self) -> bool:
        return getattr(self, "_arcade_zombies_feels_good", False)

    @property
    def bedwars_katniss_everdeen_style(self) -> bool:
        return getattr(self, "_bedwars_katniss_everdeen_style", False)

    @property
    def bedwars_its_dark_down_there(self) -> bool:
        return getattr(self, "_bedwars_its_dark_down_there", False)

    @property
    def bedwars_builder(self) -> bool:
        return getattr(self, "_bedwars_builder", False)

    @property
    def bedwars_strategist(self) -> bool:
        return getattr(self, "_bedwars_strategist", False)

    @property
    def bedwars_savvy_shopper(self) -> bool:
        return getattr(self, "_general_use_portal", False)

    @property
    def general_use_portal(self) -> bool:
        return getattr(self, "_general_use_portal", False)

    @property
    def skyblock_a_challenging_climb(self) -> bool:
        return getattr(self, "_skyblock_a_challenging_climb", False)

    @property
    def skyblock_master_enchanter(self) -> bool:
        return getattr(self, "_skyblock_master_enchanter", False)

    @property
    def skyblock_oh_shiny(self) -> bool:
        return getattr(self, "_skyblock_oh_shiny", False)

    @property
    def skyblock_dragon_slayer(self) -> bool:
        return getattr(self, "_skyblock_animal_fishing", False)

    @property
    def skyblock_soul_hunter(self) -> bool:
        return getattr(self, "_skyblock_soul_hunter", False)

    @property
    def skyblock_overkill(self) -> bool:
        return getattr(self, "_skyblock_overkill", False)

    @property
    def halloween2017_spooky_looks(self) -> bool:
        return getattr(self, "_halloween2017_spooky_looks", False)

    @property
    def skyblock_safety_first(self) -> bool:
        return getattr(self, "_skyblock_safety_first", False)

    @property
    def skyblock_dullahan(self) -> bool:
        return getattr(self, "_skyblock_dullahan", False)

    @property
    def skyblock_king_of_the_sea(self) -> bool:
        return getattr(self, "_skyblock_king_of_the_sea", False)

    @property
    def skyblock_mass_production(self) -> bool:
        return getattr(self, "_skyblock_mass_production", False)

    @property
    def copsandcrims_quad_flash(self) -> bool:
        return getattr(self, "_copsandcrims_quad_flash", False)

    @property
    def skyblock_your_big_break(self) -> bool:
        return getattr(self, "_skyblock_your_big_break", False)

    @property
    def copsandcrims_sneaky(self) -> bool:
        return getattr(self, "_copsandcrims_sneaky", False)

    @property
    def copsandcrims_run_away(self) -> bool:
        return getattr(self, "_copsandcrims_run_away", False)

    @property
    def skyblock_accessories_galore(self) -> bool:
        return getattr(self, "_skyblock_accessories_galore", False)

    @property
    def skyblock_sea_monster(self) -> bool:
        return getattr(self, "_skyblock_sea_monster", False)

    @property
    def murdermystery_first_shot_hit(self) -> bool:
        return getattr(self, "_murdermystery_first_shot_hit", False)

    @property
    def murdermystery_ride_monorail(self) -> bool:
        return getattr(self, "_murdermystery_ride_monorail", False)

    @property
    def murdermystery_blessing_and_curse(self) -> bool:
        return getattr(self, "_murdermystery_blessing_and_curse", False)

    @property
    def skyblock_happy_holidays(self) -> bool:
        return getattr(self, "_skyblock_happy_holidays", False)

    @property
    def skyblock_businessman(self) -> bool:
        return getattr(self, "_skyblock_businessman", False)

    @property
    def general_vip(self) -> bool:
        return getattr(self, "_general_vip", False)

    @property
    def skyblock_combined_efforts(self) -> bool:
        return getattr(self, "_skyblock_watch_me_shine", False)

    @property
    def housing_join_guild(self) -> bool:
        return getattr(self, "_housing_join_guild", False)

    @property
    def skyblock_sweet_tooth(self) -> bool:
        return getattr(self, "_skyblock_sweet_tooth", False)

    @property
    def skyblock_bat_pinata(self) -> bool:
        return getattr(self, "_skyblock_zookeeper", False)

    @property
    def skyblock_three_birds_one_arrow(self) -> bool:
        return getattr(self, "_skyblock_every_little_bit_helps", False)

    @property
    def skyblock_time_to_go_on_vacation(self) -> bool:
        return getattr(self, "_skyblock_time_to_go_on_vacation", False)

    @property
    def skywars_gapple(self) -> bool:
        return getattr(self, "_skywars_gapple", False)

    @property
    def skywars_well_well(self) -> bool:
        return getattr(self, "_skyblock_i_believe_i_can_fly", False)

    @property
    def skyblock_the_flint_bros(self) -> bool:
        return getattr(self, "_skyblock_the_flint_bros", False)

    @property
    def skyblock_cute_little_cube(self) -> bool:
        return getattr(self, "_skyblock_cute_little_cube", False)

    @property
    def skyblock_sirius_business(self) -> bool:
        return getattr(self, "_skyblock_im_fast_as_heck_boy", False)

    @property
    def skyblock_the_flash(self) -> bool:
        return getattr(self, "_skyblock_speedrunner", False)

    @property
    def skyblock_sacrifices_must_be_made(self) -> bool:
        return getattr(self, "_skyblock_sacrifices_must_be_made", False)

    @property
    def skyblock_caretaker(self) -> bool:
        return getattr(self, "_skyblock_i_am_superior", False)

    @property
    def skyblock_i_am_superior(self) -> bool:
        return getattr(self, "_skyblock_smell_like_roses", False)

    @property
    def skyblock_flawless(self) -> bool:
        return getattr(self, "_skyblock_flawless", False)

    @property
    def skyblock_s_plus_squad(self) -> bool:
        return getattr(self, "_skyblock_s_plus_squad", False)

    @property
    def skyblock_the_real_zoo_shady(self) -> bool:
        return getattr(self, "_skyblock_the_real_zoo_shady", False)

    @property
    def skyblock_big_game_fisher(self) -> bool:
        return getattr(self, "_skyblock_big_game_fisher", False)

    @property
    def skyblock_wonderful_treasures(self) -> bool:
        return getattr(self, "_skyblock_wonderful_treasures", False)

    @property
    def skyblock_mystical(self) -> bool:
        return getattr(self, "_skyblock_mystical", False)

    @property
    def duels_trial_by_combat(self) -> bool:
        return getattr(self, "_duels_trial_by_combat", False)

    @property
    def skyblock_though_choice(self) -> bool:
        return getattr(self, "_skyblock_though_choice", False)

    @property
    def skyblock_rainbow(self) -> bool:
        return getattr(self, "_skyblock_rainbow", False)

    @property
    def bedwars_pickaxe_challenge(self) -> bool:
        return getattr(self, "_bedwars_pickaxe_challenge", False)

    @property
    def bedwars_already_over(self) -> bool:
        return getattr(self, "_bedwars_already_over", False)

    @property
    def christmas2017_holidays_ruined(self) -> bool:
        return getattr(self, "_christmas2017_holidays_ruined", False)

    @property
    def general_friends_25(self) -> bool:
        return getattr(self, "_general_friends_25", False)

    @property
    def general_a_long_journey_begins(self) -> bool:
        return getattr(self, "_general_a_long_journey_begins", False)

    @property
    def skyblock_friend_for_life(self) -> bool:
        return getattr(self, "_skyblock_friend_for_life", False)

    @property
    def bedwars_distraction(self) -> bool:
        return getattr(self, "_bedwars_distraction", False)

    @property
    def skywars_happy_meal(self) -> bool:
        return getattr(self, "_skywars_happy_meal", False)

    @property
    def christmas2017_todays_the_day(self) -> bool:
        return getattr(self, "_christmas2017_todays_the_day", False)

    @property
    def skyblock_absorb_it_all(self) -> bool:
        return getattr(self, "_skyblock_absorb_it_all", False)

    @property
    def christmas2017_respect_your_elder(self) -> bool:
        return getattr(self, "_christmas2017_respect_your_elder", False)

    @property
    def christmas2017_not_my_mom(self) -> bool:
        return getattr(self, "_christmas2017_not_my_mom", False)

    @property
    def supersmash_botmon_challenge(self) -> bool:
        return getattr(self, "_supersmash_botmon_challenge", False)

    @property
    def skyblock_king_of_the_pets(self) -> bool:
        return getattr(self, "_skyblock_king_of_the_pets", False)

    @property
    def skyblock_to_space_we_go(self) -> bool:
        return getattr(self, "_skyblock_to_space_we_go", False)

    @property
    def skyblock_more_space(self) -> bool:
        return getattr(self, "_skyblock_more_space", False)

    @property
    def skyblock_baited(self) -> bool:
        return getattr(self, "_skyblock_baited", False)

    @property
    def bedwars_mission_control(self) -> bool:
        return getattr(self, "_bedwars_mission_control", False)

    @property
    def skyblock_declaring_allegiance(self) -> bool:
        return getattr(self, "_skyblock_declaring_allegiance", False)

    @property
    def skyblock_scam(self) -> bool:
        return getattr(self, "_skyblock_scam", False)

    @property
    def skyblock_ring_ring_whos_this(self) -> bool:
        return getattr(self, "_skyblock_ring_ring_whos_this", False)

    @property
    def skyblock_suited_up(self) -> bool:
        return getattr(self, "_skyblock_suited_up", False)

    @property
    def skyblock_this_is_the_way(self) -> bool:
        return getattr(self, "_skyblock_this_is_the_way", False)

    @property
    def skyblock_i_own_this_place(self) -> bool:
        return getattr(self, "_skyblock_i_own_this_place", False)

    @property
    def skyblock_geronimo(self) -> bool:
        return getattr(self, "_skyblock_geronimo", False)

    @property
    def skyblock_shining_scales(self) -> bool:
        return getattr(self, "_skyblock_shining_scales", False)

    @property
    def skyblock_amalgamation(self) -> bool:
        return getattr(self, "_skyblock_amalgamation", False)

    @property
    def housing_become_resident(self) -> bool:
        return getattr(self, "_housing_become_resident", False)

    @property
    def duels_speed_duel(self) -> bool:
        return getattr(self, "_duels_speed_duel", False)

    @property
    def skywars_map_select(self) -> bool:
        return getattr(self, "_skywars_map_select", False)

    @property
    def skywars_legendary(self) -> bool:
        return getattr(self, "_skywars_legendary", False)

    @property
    def arcade_no_mercy(self) -> bool:
        return getattr(self, "_arcade_no_mercy", False)

    @property
    def skyblock_dojo_grand_master(self) -> bool:
        return getattr(self, "_skyblock_dojo_grand_master", False)

    @property
    def skyblock_the_one_bottle(self) -> bool:
        return getattr(self, "_skyblock_the_one_bottle", False)

    @property
    def skyblock_hsssss(self) -> bool:
        return getattr(self, "_skyblock_hsssss", False)

    @property
    def skyblock_smells_better(self) -> bool:
        return getattr(self, "_skyblock_smells_better", False)

    @property
    def skyblock_should_have_stayed_cool(self) -> bool:
        return getattr(self, "_skyblock_should_have_stayed_cool", False)

    @property
    def christmas2017_hunt_begins_2022(self) -> bool:
        return getattr(self, "_christmas2017_hunt_begins_2022", False)

    @property
    def skyblock_humble_beginnings(self) -> bool:
        return getattr(self, "_skyblock_humble_beginnings", False)

    @property
    def skyblock_wow_useful(self) -> bool:
        return getattr(self, "_skyblock_wow_useful", False)

    @property
    def skyblock_only_be_one(self) -> bool:
        return getattr(self, "_skyblock_only_be_one", False)

    @property
    def skyblock_compost_collector(self) -> bool:
        return getattr(self, "_skyblock_compost_collector", False)

    @property
    def skyblock_bountiful_harvest(self) -> bool:
        return getattr(self, "_skyblock_bountiful_harvest", False)

    @property
    def skyblock_jakes_mystery(self) -> bool:
        return getattr(self, "_skyblock_jakes_mystery", False)

    @property
    def skywars_attention_seeking(self) -> bool:
        return getattr(self, "_skywars_attention_seeking", False)

    @property
    def skywars_open_chest(self) -> bool:
        return getattr(self, "_skywars_open_chest", False)

    @property
    def skywars_fists_of_fury(self) -> bool:
        return getattr(self, "_skywars_fists_of_fury", False)

    @property
    def murdermystery_soldiers_eliminated(self) -> bool:
        return getattr(self, "_murdermystery_soldiers_eliminated", False)

    @property
    def summer_drought(self) -> bool:
        return getattr(self, "_summer_drought", False)

    @property
    def skyblock_next_generation(self) -> bool:
        return getattr(self, "_skyblock_next_generation", False)

    @property
    def skyblock_two_out_of_nine(self) -> bool:
        return getattr(self, "_skyblock_two_out_of_nine", False)

    @property
    def skyblock_long_way_down(self) -> bool:
        return getattr(self, "_skyblock_long_way_down", False)

    @property
    def skyblock_nightmare(self) -> bool:
        return getattr(self, "_skyblock_nightmare", False)

    @property
    def skyblock_perfect_heist(self) -> bool:
        return getattr(self, "_skyblock_perfect_heist", False)

    @property
    def copsandcrims_darude_sandstorm(self) -> bool:
        return getattr(self, "_copsandcrims_darude_sandstorm", False)

    @property
    def skyblock_true_alchemist(self) -> bool:
        return getattr(self, "_skyblock_true_alchemist", False)

    @property
    def skyblock_end_race(self) -> bool:
        return getattr(self, "_skyblock_end_race", False)

    @property
    def murdermystery_kill_detective_fast(self) -> bool:
        return getattr(self, "_murdermystery_kill_detective_fast", False)

    @property
    def arcade_pixel_party_clumsy_dancer(self) -> bool:
        return getattr(self, "_arcade_pixel_party_clumsy_dancer", False)

    @property
    def murdermystery_sword_kill_long_range(self) -> bool:
        return getattr(self, "_murdermystery_sword_kill_long_range", False)

    @property
    def murdermystery_three_knife_throw_kills(self) -> bool:
        return getattr(self, "_murdermystery_three_knife_throw_kills", False)

    @property
    def murdermystery_dance(self) -> bool:
        return getattr(self, "_murdermystery_dance", False)

    @property
    def murdermystery_pickup_gold(self) -> bool:
        return getattr(self, "_murdermystery_pickup_gold", False)

    @property
    def murdermystery_kill_murderer_after_kill(self) -> bool:
        return getattr(self, "_murdermystery_kill_murderer_after_kill", False)

    @property
    def murdermystery_survive_storm_on_top(self) -> bool:
        return getattr(self, "_murdermystery_survive_storm_on_top", False)

    @property
    def bedwars_the_last_of_us(self) -> bool:
        return getattr(self, "_bedwars_the_last_of_us", False)

    @property
    def christmas2017_hunt_begins_2023(self) -> bool:
        return getattr(self, "_christmas2017_hunt_begins_2023", False)

    @property
    def christmas2017_merry_christmas(self) -> bool:
        return getattr(self, "_christmas2017_merry_christmas", False)

    @property
    def skyblock_end_credits(self) -> bool:
        return getattr(self, "_skyblock_end_credits", False)

    @property
    def skyblock_eye_for_an_i(self) -> bool:
        return getattr(self, "_skyblock_eye_for_an_i", False)

    @property
    def skyblock_no_other_choice(self) -> bool:
        return getattr(self, "_skyblock_no_other_choice", False)

    @property
    def skyblock_responsible_pet_owner(self) -> bool:
        return getattr(self, "_skyblock_responsible_pet_owner", False)

    @property
    def skyblock_snake_charmer(self) -> bool:
        return getattr(self, "_skyblock_snake_charmer", False)

    @property
    def skyblock_hes_bac(self) -> bool:
        return getattr(self, "_skyblock_hes_bac", False)

    @property
    def skyblock_see_ya_later(self) -> bool:
        return getattr(self, "_skyblock_see_ya_later", False)

    @property
    def skyblock_still_sad(self) -> bool:
        return getattr(self, "_skyblock_still_sad", False)

    @property
    def skyblock_forbidden_fruit(self) -> bool:
        return getattr(self, "_skyblock_forbidden_fruit", False)

    @property
    def skyblock_inner_machinations(self) -> bool:
        return getattr(self, "_skyblock_inner_machinations", False)

    @property
    def skyblock_diverse_destruction(self) -> bool:
        return getattr(self, "_skyblock_diverse_destruction", False)

    @property
    def arcade_avalance_waves(self) -> bool:
        return getattr(self, "_arcade_avalance_waves", False)

    @property
    def skyblock_lapidarist(self) -> bool:
        return getattr(self, "_skyblock_lapidarist", False)

    @property
    def skyblock_six_star_meal(self) -> bool:
        return getattr(self, "_skyblock_six_star_meal", False)

    @property
    def murdermystery_kali_favor(self) -> bool:
        return getattr(self, "_murdermystery_kali_favor", False)

    @property
    def murdermystery_win_survivor_due_to_time(self) -> bool:
        return getattr(self, "_murdermystery_win_survivor_due_to_time", False)

    @property
    def murdermystery_jaws(self) -> bool:
        return getattr(self, "_murdermystery_jaws", False)
