class Achievements:
    """Class representing a player"s achievements"""

    def __init__(self, achievements: dict):
        for name in achievements:
            safe_name = name.replace("-", "_")
            setattr(self, f"_{safe_name}", True)

    @property
    def skyblock_your_big_break(self) -> bool:
        return getattr(self, "_skyblock_your_big_break", False)

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

    @property
    def arcade_bounty_hunter_target_killer(self) -> bool:
        return getattr(self, "_arcade_bounty_hunter_target_killer", False)

    @property
    def arcade_creeper_attack_iron_golem(self) -> bool:
        return getattr(self, "_arcade_creeper_attack_iron_golem", False)

    @property
    def arcade_creeper_attack_upgrades(self) -> bool:
        return getattr(self, "_arcade_creeper_attack_upgrades", False)

    @property
    def arcade_creeper_attack_waves(self) -> bool:
        return getattr(self, "_arcade_creeper_attack_waves", False)

    @property
    def arcade_dropper_wasnt_so_bad(self) -> bool:
        return getattr(self, "_arcade_dropper_wasnt_so_bad", False)

    @property
    def arcade_hole_finals(self) -> bool:
        return getattr(self, "_arcade_hole_finals", False)

    @property
    def arcade_woops_didnt_mean_to(self) -> bool:
        return getattr(self, "_arcade_woops_didnt_mean_to", False)

    @property
    def arcade_zombies_ultimate(self) -> bool:
        return getattr(self, "_arcade_zombies_ultimate", False)

    @property
    def bedwars_buggy_beds(self) -> bool:
        return getattr(self, "_bedwars_buggy_beds", False)

    @property
    def bedwars_destroy_beds(self) -> bool:
        return getattr(self, "_bedwars_destroy_beds", False)

    @property
    def bedwars_dont_need_bed(self) -> bool:
        return getattr(self, "_bedwars_dont_need_bed", False)

    @property
    def bedwars_first(self) -> bool:
        return getattr(self, "_bedwars_first", False)

    @property
    def bedwars_first_blood(self) -> bool:
        return getattr(self, "_bedwars_first_blood", False)

    @property
    def bedwars_geared_up(self) -> bool:
        return getattr(self, "_bedwars_geared_up", False)

    @property
    def bedwars_merciless(self) -> bool:
        return getattr(self, "_bedwars_merciless", False)

    @property
    def bedwars_minefield(self) -> bool:
        return getattr(self, "_bedwars_minefield", False)

    @property
    def bedwars_out_of_stock(self) -> bool:
        return getattr(self, "_bedwars_out_of_stock", False)

    @property
    def bedwars_revenge(self) -> bool:
        return getattr(self, "_bedwars_revenge", False)

    @property
    def bedwars_super_looter(self) -> bool:
        return getattr(self, "_bedwars_super_looter", False)

    @property
    def bedwars_survivor(self) -> bool:
        return getattr(self, "_bedwars_survivor", False)

    @property
    def bedwars_team_player(self) -> bool:
        return getattr(self, "_bedwars_team_player", False)

    @property
    def bedwars_thats_a_first(self) -> bool:
        return getattr(self, "_bedwars_thats_a_first", False)

    @property
    def bedwars_you_cant_do_that(self) -> bool:
        return getattr(self, "_bedwars_you_cant_do_that", False)

    @property
    def blitz_first_game(self) -> bool:
        return getattr(self, "_blitz_first_game", False)

    @property
    def buildbattle_artist(self) -> bool:
        return getattr(self, "_buildbattle_artist", False)

    @property
    def buildbattle_every_second_counts(self) -> bool:
        return getattr(self, "_buildbattle_every_second_counts", False)

    @property
    def christmas2017_new_years_celebrations(self) -> bool:
        return getattr(self, "_christmas2017_new_years_celebrations", False)

    @property
    def copsandcrims_challenge_completed(self) -> bool:
        return getattr(self, "_copsandcrims_challenge_completed", False)

    @property
    def copsandcrims_fancy_new_toys(self) -> bool:
        return getattr(self, "_copsandcrims_fancy_new_toys", False)

    @property
    def copsandcrims_flawless(self) -> bool:
        return getattr(self, "_copsandcrims_flawless", False)

    @property
    def copsandcrims_sneak_kill(self) -> bool:
        return getattr(self, "_copsandcrims_sneak_kill", False)

    @property
    def duels_one_v_one_me(self) -> bool:
        return getattr(self, "_duels_one_v_one_me", False)

    @property
    def duels_rematch(self) -> bool:
        return getattr(self, "_duels_rematch", False)

    @property
    def duels_untouchable(self) -> bool:
        return getattr(self, "_duels_untouchable", False)

    @property
    def easter_happy_easter_2020(self) -> bool:
        return getattr(self, "_easter_happy_easter_2020", False)

    @property
    def easter_happy_easter_2021(self) -> bool:
        return getattr(self, "_easter_happy_easter_2021", False)

    @property
    def easter_happy_easter_2022(self) -> bool:
        return getattr(self, "_easter_happy_easter_2022", False)

    @property
    def easter_happy_easter_2023(self) -> bool:
        return getattr(self, "_easter_happy_easter_2023", False)

    @property
    def easter_happy_easter_2024(self) -> bool:
        return getattr(self, "_easter_happy_easter_2024", False)

    @property
    def general_first_party(self) -> bool:
        return getattr(self, "_general_first_party", False)

    @property
    def general_gifting(self) -> bool:
        return getattr(self, "_general_gifting", False)

    @property
    def general_treasure_hunt_2022(self) -> bool:
        return getattr(self, "_general_treasure_hunt_2022", False)

    @property
    def general_vip_plus(self) -> bool:
        return getattr(self, "_general_vip_plus", False)

    @property
    def general_youtuber(self) -> bool:
        return getattr(self, "_general_youtuber", False)

    @property
    def gingerbread_boost_of_confidence(self) -> bool:
        return getattr(self, "_gingerbread_boost_of_confidence", False)

    @property
    def gingerbread_get_hit_by_me(self) -> bool:
        return getattr(self, "_gingerbread_get_hit_by_me", False)

    @property
    def gingerbread_getting_good(self) -> bool:
        return getattr(self, "_gingerbread_getting_good", False)

    @property
    def gingerbread_taste_my_banana(self) -> bool:
        return getattr(self, "_gingerbread_taste_my_banana", False)

    @property
    def halloween2017_hi_there(self) -> bool:
        return getattr(self, "_halloween2017_hi_there", False)

    @property
    def halloween2017_trick_or_treat_time(self) -> bool:
        return getattr(self, "_halloween2017_trick_or_treat_time", False)

    @property
    def housing_give_cookie(self) -> bool:
        return getattr(self, "_housing_give_cookie", False)

    @property
    def murdermystery_clear_cacti(self) -> bool:
        return getattr(self, "_murdermystery_clear_cacti", False)

    @property
    def murdermystery_reichenbach_fall(self) -> bool:
        return getattr(self, "_murdermystery_reichenbach_fall", False)

    @property
    def murdermystery_shoot_thrown_knife(self) -> bool:
        return getattr(self, "_murdermystery_shoot_thrown_knife", False)

    @property
    def murdermystery_special_two_in_a_row(self) -> bool:
        return getattr(self, "_murdermystery_special_two_in_a_row", False)

    @property
    def murdermystery_uncalculated(self) -> bool:
        return getattr(self, "_murdermystery_uncalculated", False)

    @property
    def murdermystery_win_murderer_fell_in_trap(self) -> bool:
        return getattr(self, "_murdermystery_win_murderer_fell_in_trap", False)

    @property
    def quake_billy_talent(self) -> bool:
        return getattr(self, "_quake_billy_talent", False)

    @property
    def quake_bogof(self) -> bool:
        return getattr(self, "_quake_bogof", False)

    @property
    def quake_good_guy_gamer(self) -> bool:
        return getattr(self, "_quake_good_guy_gamer", False)

    @property
    def quake_team_player(self) -> bool:
        return getattr(self, "_quake_team_player", False)

    @property
    def skyblock_a_face_to_remember(self) -> bool:
        return getattr(self, "_skyblock_a_face_to_remember", False)

    @property
    def skyblock_a_good_review(self) -> bool:
        return getattr(self, "_skyblock_a_good_review", False)

    @property
    def skyblock_a_good_spider_is_a_dead_spider(self) -> bool:
        return getattr(self, "_skyblock_a_good_spider_is_a_dead_spider", False)

    @property
    def skyblock_advanced_transportation(self) -> bool:
        return getattr(self, "_skyblock_advanced_transportation", False)

    @property
    def skyblock_animal_fishing(self) -> bool:
        return getattr(self, "_skyblock_animal_fishing", False)

    @property
    def skyblock_balrog_memories(self) -> bool:
        return getattr(self, "_skyblock_balrog_memories", False)

    @property
    def skyblock_beaconator_two(self) -> bool:
        return getattr(self, "_skyblock_beaconator_two", False)

    @property
    def skyblock_bigger_storage_is_seeded(self) -> bool:
        return getattr(self, "_skyblock_bigger_storage_is_seeded", False)

    @property
    def skyblock_blaze_wrangler(self) -> bool:
        return getattr(self, "_skyblock_blaze_wrangler", False)

    @property
    def skyblock_buzzkill(self) -> bool:
        return getattr(self, "_skyblock_buzzkill", False)

    @property
    def skyblock_caught_the_grinch(self) -> bool:
        return getattr(self, "_skyblock_caught_the_grinch", False)

    @property
    def skyblock_cleanup_crew(self) -> bool:
        return getattr(self, "_skyblock_cleanup_crew", False)

    @property
    def skyblock_death_from_above(self) -> bool:
        return getattr(self, "_skyblock_death_from_above", False)

    @property
    def skyblock_deep_storage(self) -> bool:
        return getattr(self, "_skyblock_deep_storage", False)

    @property
    def skyblock_defeating_death(self) -> bool:
        return getattr(self, "_skyblock_defeating_death", False)

    @property
    def skyblock_didnt_mean_to(self) -> bool:
        return getattr(self, "_skyblock_didnt_mean_to", False)

    @property
    def skyblock_do_you_even_voodoo(self) -> bool:
        return getattr(self, "_skyblock_do_you_even_voodoo", False)

    @property
    def skyblock_dojo_master(self) -> bool:
        return getattr(self, "_skyblock_dojo_master", False)

    @property
    def skyblock_dragons_egg(self) -> bool:
        return getattr(self, "_skyblock_dragons_egg", False)

    @property
    def skyblock_dungeon_explorer(self) -> bool:
        return getattr(self, "_skyblock_dungeon_explorer", False)

    @property
    def skyblock_eternal_flame_ring(self) -> bool:
        return getattr(self, "_skyblock_eternal_flame_ring", False)

    @property
    def skyblock_every_little_bit_helps(self) -> bool:
        return getattr(self, "_skyblock_every_little_bit_helps", False)

    @property
    def skyblock_existential_revelations(self) -> bool:
        return getattr(self, "_skyblock_existential_revelations", False)

    @property
    def skyblock_explosive_ending(self) -> bool:
        return getattr(self, "_skyblock_explosive_ending", False)

    @property
    def skyblock_fancy_farming(self) -> bool:
        return getattr(self, "_skyblock_fancy_farming", False)

    @property
    def skyblock_flamin_hot(self) -> bool:
        return getattr(self, "_skyblock_flamin_hot", False)

    @property
    def skyblock_fortunate(self) -> bool:
        return getattr(self, "_skyblock_fortunate", False)

    @property
    def skyblock_friar_lawrence(self) -> bool:
        return getattr(self, "_skyblock_friar_lawrence", False)

    @property
    def skyblock_frozen_monster(self) -> bool:
        return getattr(self, "_skyblock_frozen_monster", False)

    @property
    def skyblock_fully_evolved(self) -> bool:
        return getattr(self, "_skyblock_fully_evolved", False)

    @property
    def skyblock_ghost_buster(self) -> bool:
        return getattr(self, "_skyblock_ghost_buster", False)

    @property
    def skyblock_glass_cannon(self) -> bool:
        return getattr(self, "_skyblock_glass_cannon", False)

    @property
    def skyblock_goblin_slayer(self) -> bool:
        return getattr(self, "_skyblock_goblin_slayer", False)

    @property
    def skyblock_gotta_go_fast(self) -> bool:
        return getattr(self, "_skyblock_gotta_go_fast", False)

    @property
    def skyblock_happy_new_year(self) -> bool:
        return getattr(self, "_skyblock_happy_new_year", False)

    @property
    def skyblock_heart_of_the_end(self) -> bool:
        return getattr(self, "_skyblock_heart_of_the_end", False)

    @property
    def skyblock_helpful_hand(self) -> bool:
        return getattr(self, "_skyblock_helpful_hand", False)

    @property
    def skyblock_hidden_secrets(self) -> bool:
        return getattr(self, "_skyblock_hidden_secrets", False)

    @property
    def skyblock_higher_enchants(self) -> bool:
        return getattr(self, "_skyblock_higher_enchants", False)

    @property
    def skyblock_higher_than_a_rabbit(self) -> bool:
        return getattr(self, "_skyblock_higher_than_a_rabbit", False)

    @property
    def skyblock_how_to_train_your_dragon(self) -> bool:
        return getattr(self, "_skyblock_how_to_train_your_dragon", False)

    @property
    def skyblock_i_believe_i_can_fly(self) -> bool:
        return getattr(self, "_skyblock_i_believe_i_can_fly", False)

    @property
    def skyblock_i_knew_it(self) -> bool:
        return getattr(self, "_skyblock_i_knew_it", False)

    @property
    def skyblock_im_fast_as_heck_boy(self) -> bool:
        return getattr(self, "_skyblock_im_fast_as_heck_boy", False)

    @property
    def skyblock_im_not_dead(self) -> bool:
        return getattr(self, "_skyblock_im_not_dead", False)

    @property
    def skyblock_indiana_bones(self) -> bool:
        return getattr(self, "_skyblock_indiana_bones", False)

    @property
    def skyblock_into_the_deep(self) -> bool:
        return getattr(self, "_skyblock_into_the_deep", False)

    @property
    def skyblock_it_worked(self) -> bool:
        return getattr(self, "_skyblock_it_worked", False)

    @property
    def skyblock_king_of_the_chicks(self) -> bool:
        return getattr(self, "_skyblock_king_of_the_chicks", False)

    @property
    def skyblock_knowledge_is_power(self) -> bool:
        return getattr(self, "_skyblock_knowledge_is_power", False)

    @property
    def skyblock_kuudra_conundrum(self) -> bool:
        return getattr(self, "_skyblock_kuudra_conundrum", False)

    @property
    def skyblock_librarian(self) -> bool:
        return getattr(self, "_skyblock_librarian", False)

    @property
    def skyblock_long_way_gone(self) -> bool:
        return getattr(self, "_skyblock_long_way_gone", False)

    @property
    def skyblock_magical_place(self) -> bool:
        return getattr(self, "_skyblock_magical_place", False)

    @property
    def skyblock_next_level(self) -> bool:
        return getattr(self, "_skyblock_next_level", False)

    @property
    def skyblock_night_eyes(self) -> bool:
        return getattr(self, "_skyblock_night_eyes", False)

    @property
    def skyblock_peak_of_the_mountain(self) -> bool:
        return getattr(self, "_skyblock_peak_of_the_mountain", False)

    @property
    def skyblock_player_of_the_people(self) -> bool:
        return getattr(self, "_skyblock_player_of_the_people", False)

    @property
    def skyblock_prepare_for_trouble(self) -> bool:
        return getattr(self, "_skyblock_prepare_for_trouble", False)

    @property
    def skyblock_put_spell(self) -> bool:
        return getattr(self, "_skyblock_put_spell", False)

    @property
    def skyblock_quite_the_crowd(self) -> bool:
        return getattr(self, "_skyblock_quite_the_crowd", False)

    @property
    def skyblock_rebirth(self) -> bool:
        return getattr(self, "_skyblock_rebirth", False)

    @property
    def skyblock_resourceful(self) -> bool:
        return getattr(self, "_skyblock_resourceful", False)

    @property
    def skyblock_royal_meeting(self) -> bool:
        return getattr(self, "_skyblock_royal_meeting", False)

    @property
    def skyblock_royal_resident_dialogue(self) -> bool:
        return getattr(self, "_skyblock_royal_resident_dialogue", False)

    @property
    def skyblock_secret_end_place(self) -> bool:
        return getattr(self, "_skyblock_secret_end_place", False)

    @property
    def skyblock_smell_like_roses(self) -> bool:
        return getattr(self, "_skyblock_smell_like_roses", False)

    @property
    def skyblock_speedrunner(self) -> bool:
        return getattr(self, "_skyblock_speedrunner", False)

    @property
    def skyblock_spiky(self) -> bool:
        return getattr(self, "_skyblock_spiky", False)

    @property
    def skyblock_storage_forever(self) -> bool:
        return getattr(self, "_skyblock_storage_forever", False)

    @property
    def skyblock_stubborn_giver(self) -> bool:
        return getattr(self, "_skyblock_stubborn_giver", False)

    @property
    def skyblock_super_fuel(self) -> bool:
        return getattr(self, "_skyblock_super_fuel", False)

    @property
    def skyblock_swaying_the_vote(self) -> bool:
        return getattr(self, "_skyblock_swaying_the_vote", False)

    @property
    def skyblock_the_itsy_bitsy_spider(self) -> bool:
        return getattr(self, "_skyblock_the_itsy_bitsy_spider", False)

    @property
    def skyblock_time_to_start_fishing(self) -> bool:
        return getattr(self, "_skyblock_time_to_start_fishing", False)

    @property
    def skyblock_treasure_fishing(self) -> bool:
        return getattr(self, "_skyblock_treasure_fishing", False)

    @property
    def skyblock_true_adventurer(self) -> bool:
        return getattr(self, "_skyblock_true_adventurer", False)

    @property
    def skyblock_united_in_blood(self) -> bool:
        return getattr(self, "_skyblock_united_in_blood", False)

    @property
    def skyblock_upgrades_people_upgrades(self) -> bool:
        return getattr(self, "_skyblock_upgrades_people_upgrades", False)

    @property
    def skyblock_vanquished(self) -> bool:
        return getattr(self, "_skyblock_vanquished", False)

    @property
    def skyblock_watch_me_shine(self) -> bool:
        return getattr(self, "_skyblock_watch_me_shine", False)

    @property
    def skyblock_water_sword(self) -> bool:
        return getattr(self, "_skyblock_water_sword", False)

    @property
    def skyblock_welcome_to_my_factory(self) -> bool:
        return getattr(self, "_skyblock_welcome_to_my_factory", False)

    @property
    def skyblock_worth_it(self) -> bool:
        return getattr(self, "_skyblock_worth_it", False)

    @property
    def skyblock_yucky(self) -> bool:
        return getattr(self, "_skyblock_yucky", False)

    @property
    def skyblock_zookeeper(self) -> bool:
        return getattr(self, "_skyblock_zookeeper", False)

    @property
    def skywars_fast_and_furious(self) -> bool:
        return getattr(self, "_skywars_fast_and_furious", False)

    @property
    def skywars_hasta_la_vista(self) -> bool:
        return getattr(self, "_skywars_hasta_la_vista", False)

    @property
    def skywars_mob_spawner(self) -> bool:
        return getattr(self, "_skywars_mob_spawner", False)

    @property
    def skywars_rng(self) -> bool:
        return getattr(self, "_skywars_rng", False)

    @property
    def skywars_shiny_stuff(self) -> bool:
        return getattr(self, "_skywars_shiny_stuff", False)

    @property
    def skywars_siege(self) -> bool:
        return getattr(self, "_skywars_siege", False)

    @property
    def summer_cool_off(self) -> bool:
        return getattr(self, "_summer_cool_off", False)

    @property
    def walls3_find_chest(self) -> bool:
        return getattr(self, "_walls3_find_chest", False)

    @property
    def arcade_animal_slaughter(self) -> bool:
        return getattr(self, "_arcade_animal_slaughter", False)

    @property
    def arcade_blocking_dead_rescue(self) -> bool:
        return getattr(self, "_arcade_blocking_dead_rescue", False)

    @property
    def arcade_cant_hide_from_me(self) -> bool:
        return getattr(self, "_arcade_cant_hide_from_me", False)

    @property
    def arcade_creeper_attack_survival(self) -> bool:
        return getattr(self, "_arcade_creeper_attack_survival", False)

    @property
    def arcade_dragon_killer(self) -> bool:
        return getattr(self, "_arcade_dragon_killer", False)

    @property
    def arcade_dragon_slayer(self) -> bool:
        return getattr(self, "_arcade_dragon_slayer", False)

    @property
    def arcade_dragon_wars_blast(self) -> bool:
        return getattr(self, "_arcade_dragon_wars_blast", False)

    @property
    def arcade_dropper_fast_way_down(self) -> bool:
        return getattr(self, "_arcade_dropper_fast_way_down", False)

    @property
    def arcade_dropper_sheer_brilliance(self) -> bool:
        return getattr(self, "_arcade_dropper_sheer_brilliance", False)

    @property
    def arcade_dropper_versatile(self) -> bool:
        return getattr(self, "_arcade_dropper_versatile", False)

    @property
    def arcade_ender_spleef_no_powerhouse(self) -> bool:
        return getattr(self, "_arcade_ender_spleef_no_powerhouse", False)

    @property
    def arcade_farm_hunt_disguise(self) -> bool:
        return getattr(self, "_arcade_farm_hunt_disguise", False)

    @property
    def arcade_farm_hunt_killer(self) -> bool:
        return getattr(self, "_arcade_farm_hunt_killer", False)

    @property
    def arcade_football_five_goals(self) -> bool:
        return getattr(self, "_arcade_football_five_goals", False)

    @property
    def arcade_football_potm(self) -> bool:
        return getattr(self, "_arcade_football_potm", False)

    @property
    def arcade_football_speed(self) -> bool:
        return getattr(self, "_arcade_football_speed", False)

    @property
    def arcade_giddy_up_horsey(self) -> bool:
        return getattr(self, "_arcade_giddy_up_horsey", False)

    @property
    def arcade_hide_and_seek_party_pooper(self) -> bool:
        return getattr(self, "_arcade_hide_and_seek_party_pooper", False)

    @property
    def arcade_hide_and_seek_prop(self) -> bool:
        return getattr(self, "_arcade_hide_and_seek_prop", False)

    @property
    def arcade_hide_and_seek_prop_hunter(self) -> bool:
        return getattr(self, "_arcade_hide_and_seek_prop_hunter", False)

    @property
    def arcade_hoehoehoe_score(self) -> bool:
        return getattr(self, "_arcade_hoehoehoe_score", False)

    @property
    def arcade_hole_score(self) -> bool:
        return getattr(self, "_arcade_hole_score", False)

    @property
    def arcade_hypixel_says_bad_health_choices(self) -> bool:
        return getattr(self, "_arcade_hypixel_says_bad_health_choices", False)

    @property
    def arcade_hypixel_says_master(self) -> bool:
        return getattr(self, "_arcade_hypixel_says_master", False)

    @property
    def arcade_hypixel_says_pig_rider(self) -> bool:
        return getattr(self, "_arcade_hypixel_says_pig_rider", False)

    @property
    def arcade_hypixel_says_pve_expert(self) -> bool:
        return getattr(self, "_arcade_hypixel_says_pve_expert", False)

    @property
    def arcade_hypixel_says_tnt_dodger(self) -> bool:
        return getattr(self, "_arcade_hypixel_says_tnt_dodger", False)

    @property
    def arcade_lone_survivor(self) -> bool:
        return getattr(self, "_arcade_lone_survivor", False)

    @property
    def arcade_mini_hunter(self) -> bool:
        return getattr(self, "_arcade_mini_hunter", False)

    @property
    def arcade_mini_walls_last_man(self) -> bool:
        return getattr(self, "_arcade_mini_walls_last_man", False)

    @property
    def arcade_no_mutiny_today(self) -> bool:
        return getattr(self, "_arcade_no_mutiny_today", False)

    @property
    def arcade_over_here(self) -> bool:
        return getattr(self, "_arcade_over_here", False)

    @property
    def arcade_overpowered(self) -> bool:
        return getattr(self, "_arcade_overpowered", False)

    @property
    def arcade_party_games_stars(self) -> bool:
        return getattr(self, "_arcade_party_games_stars", False)

    @property
    def arcade_party_in_sync(self) -> bool:
        return getattr(self, "_arcade_party_in_sync", False)

    @property
    def arcade_party_parkour(self) -> bool:
        return getattr(self, "_arcade_party_parkour", False)

    @property
    def arcade_party_sheep_rider(self) -> bool:
        return getattr(self, "_arcade_party_sheep_rider", False)

    @property
    def arcade_pig_fishing_super_bacon(self) -> bool:
        return getattr(self, "_arcade_pig_fishing_super_bacon", False)

    @property
    def arcade_pixel_painters_one(self) -> bool:
        return getattr(self, "_arcade_pixel_painters_one", False)

    @property
    def arcade_pixel_party_crushed_disco(self) -> bool:
        return getattr(self, "_arcade_pixel_party_crushed_disco", False)

    @property
    def arcade_pixel_party_silent_disco(self) -> bool:
        return getattr(self, "_arcade_pixel_party_silent_disco", False)

    @property
    def arcade_professional_mower(self) -> bool:
        return getattr(self, "_arcade_professional_mower", False)

    @property
    def arcade_rpg_16_rocket_pig(self) -> bool:
        return getattr(self, "_arcade_rpg_16_rocket_pig", False)

    @property
    def arcade_savage(self) -> bool:
        return getattr(self, "_arcade_savage", False)

    @property
    def arcade_snake(self) -> bool:
        return getattr(self, "_arcade_snake", False)

    @property
    def arcade_team_slayer(self) -> bool:
        return getattr(self, "_arcade_team_slayer", False)

    @property
    def arcade_throw_out_powerup_kill(self) -> bool:
        return getattr(self, "_arcade_throw_out_powerup_kill", False)

    @property
    def arcade_trampolinio_red_wool(self) -> bool:
        return getattr(self, "_arcade_trampolinio_red_wool", False)

    @property
    def arcade_untouchable(self) -> bool:
        return getattr(self, "_arcade_untouchable", False)

    @property
    def arcade_world_economics(self) -> bool:
        return getattr(self, "_arcade_world_economics", False)

    @property
    def arcade_zombes_serial_killer(self) -> bool:
        return getattr(self, "_arcade_zombes_serial_killer", False)

    @property
    def arcade_zombies_electrician(self) -> bool:
        return getattr(self, "_arcade_zombies_electrician", False)

    @property
    def arcade_zombies_herobrine(self) -> bool:
        return getattr(self, "_arcade_zombies_herobrine", False)

    @property
    def arcade_zombies_perk_hoarder(self) -> bool:
        return getattr(self, "_arcade_zombies_perk_hoarder", False)

    @property
    def arcade_zombies_speed_runner(self) -> bool:
        return getattr(self, "_arcade_zombies_speed_runner", False)

    @property
    def arcade_zombies_survivor(self) -> bool:
        return getattr(self, "_arcade_zombies_survivor", False)

    @property
    def arcade_zombies_team_player(self) -> bool:
        return getattr(self, "_arcade_zombies_team_player", False)

    @property
    def arcade_zombies_time_trial_blood(self) -> bool:
        return getattr(self, "_arcade_zombies_time_trial_blood", False)

    @property
    def arcade_zombies_time_trial_dead(self) -> bool:
        return getattr(self, "_arcade_zombies_time_trial_dead", False)

    @property
    def arcade_zombies_win(self) -> bool:
        return getattr(self, "_arcade_zombies_win", False)

    @property
    def arena_cooldown(self) -> bool:
        return getattr(self, "_arena_cooldown", False)

    @property
    def arena_deadly_pumpkin(self) -> bool:
        return getattr(self, "_arena_deadly_pumpkin", False)

    @property
    def arena_dont_touch_me(self) -> bool:
        return getattr(self, "_arena_dont_touch_me", False)

    @property
    def arena_doom_shroom_gloom(self) -> bool:
        return getattr(self, "_arena_doom_shroom_gloom", False)

    @property
    def arena_dragon_within(self) -> bool:
        return getattr(self, "_arena_dragon_within", False)

    @property
    def arena_energy(self) -> bool:
        return getattr(self, "_arena_energy", False)

    @property
    def arena_environmentalist(self) -> bool:
        return getattr(self, "_arena_environmentalist", False)

    @property
    def arena_flawless(self) -> bool:
        return getattr(self, "_arena_flawless", False)

    @property
    def arena_health(self) -> bool:
        return getattr(self, "_arena_health", False)

    @property
    def arena_health_totem(self) -> bool:
        return getattr(self, "_arena_health_totem", False)

    @property
    def arena_magical(self) -> bool:
        return getattr(self, "_arena_magical", False)

    @property
    def arena_max_runic_magic(self) -> bool:
        return getattr(self, "_arena_max_runic_magic", False)

    @property
    def arena_melee(self) -> bool:
        return getattr(self, "_arena_melee", False)

    @property
    def arena_my_new_hat(self) -> bool:
        return getattr(self, "_arena_my_new_hat", False)

    @property
    def arena_new_toy(self) -> bool:
        return getattr(self, "_arena_new_toy", False)

    @property
    def arena_nice_spare(self) -> bool:
        return getattr(self, "_arena_nice_spare", False)

    @property
    def arena_not_even_close(self) -> bool:
        return getattr(self, "_arena_not_even_close", False)

    @property
    def arena_not_today(self) -> bool:
        return getattr(self, "_arena_not_today", False)

    @property
    def arena_offensive(self) -> bool:
        return getattr(self, "_arena_offensive", False)

    @property
    def arena_overkill(self) -> bool:
        return getattr(self, "_arena_overkill", False)

    @property
    def arena_pairs(self) -> bool:
        return getattr(self, "_arena_pairs", False)

    @property
    def arena_pig(self) -> bool:
        return getattr(self, "_arena_pig", False)

    @property
    def arena_pool(self) -> bool:
        return getattr(self, "_arena_pool", False)

    @property
    def arena_power_hungry(self) -> bool:
        return getattr(self, "_arena_power_hungry", False)

    @property
    def arena_punisher(self) -> bool:
        return getattr(self, "_arena_punisher", False)

    @property
    def arena_runic(self) -> bool:
        return getattr(self, "_arena_runic", False)

    @property
    def arena_smash(self) -> bool:
        return getattr(self, "_arena_smash", False)

    @property
    def arena_spirited_away(self) -> bool:
        return getattr(self, "_arena_spirited_away", False)

    @property
    def arena_support(self) -> bool:
        return getattr(self, "_arena_support", False)

    @property
    def arena_totem_destroyer(self) -> bool:
        return getattr(self, "_arena_totem_destroyer", False)

    @property
    def arena_you_shall_not_pass(self) -> bool:
        return getattr(self, "_arena_you_shall_not_pass", False)

    @property
    def bedwars_alchemist(self) -> bool:
        return getattr(self, "_bedwars_alchemist", False)

    @property
    def bedwars_bed_trap(self) -> bool:
        return getattr(self, "_bedwars_bed_trap", False)

    @property
    def bedwars_bomber(self) -> bool:
        return getattr(self, "_bedwars_bomber", False)

    @property
    def bedwars_cutting_it_close(self) -> bool:
        return getattr(self, "_bedwars_cutting_it_close", False)

    @property
    def bedwars_diamond_hoarder(self) -> bool:
        return getattr(self, "_bedwars_diamond_hoarder", False)

    @property
    def bedwars_emerald_hoarder(self) -> bool:
        return getattr(self, "_bedwars_emerald_hoarder", False)

    @property
    def bedwars_fireballs(self) -> bool:
        return getattr(self, "_bedwars_fireballs", False)

    @property
    def bedwars_getting_the_job_done_better(self) -> bool:
        return getattr(self, "_bedwars_getting_the_job_done_better", False)

    @property
    def bedwars_golem(self) -> bool:
        return getattr(self, "_bedwars_golem", False)

    @property
    def bedwars_iron_punch(self) -> bool:
        return getattr(self, "_bedwars_iron_punch", False)

    @property
    def bedwars_ninja(self) -> bool:
        return getattr(self, "_bedwars_ninja", False)

    @property
    def bedwars_rejoining_the_dream(self) -> bool:
        return getattr(self, "_bedwars_rejoining_the_dream", False)

    @property
    def bedwars_shear_luck(self) -> bool:
        return getattr(self, "_bedwars_shear_luck", False)

    @property
    def bedwars_slayer(self) -> bool:
        return getattr(self, "_bedwars_slayer", False)

    @property
    def bedwars_slumber_forged_in_fire(self) -> bool:
        return getattr(self, "_bedwars_slumber_forged_in_fire", False)

    @property
    def bedwars_slumber_hotel_regular(self) -> bool:
        return getattr(self, "_bedwars_slumber_hotel_regular", False)

    @property
    def bedwars_slumber_hotel_vip(self) -> bool:
        return getattr(self, "_bedwars_slumber_hotel_vip", False)

    @property
    def bedwars_slumber_millionaires_club(self) -> bool:
        return getattr(self, "_bedwars_slumber_millionaires_club", False)

    @property
    def bedwars_slumber_sold_the_dreamscape(self) -> bool:
        return getattr(self, "_bedwars_slumber_sold_the_dreamscape", False)

    @property
    def bedwars_slumber_you_did_it(self) -> bool:
        return getattr(self, "_bedwars_slumber_you_did_it", False)

    @property
    def bedwars_slumber_your_journey_starts_here(self) -> bool:
        return getattr(
            self,
            "_bedwars_slumber_your_journey_starts_here",
            False,
        )

    @property
    def bedwars_sneaky_rusher(self) -> bool:
        return getattr(self, "_bedwars_sneaky_rusher", False)

    @property
    def bedwars_sniper(self) -> bool:
        return getattr(self, "_bedwars_sniper", False)

    @property
    def bedwars_stay_away_from_me(self) -> bool:
        return getattr(self, "_bedwars_stay_away_from_me", False)

    @property
    def bedwars_ultimate_defense(self) -> bool:
        return getattr(self, "_bedwars_ultimate_defense", False)

    @property
    def blitz_afterburner(self) -> bool:
        return getattr(self, "_blitz_afterburner", False)

    @property
    def blitz_apocalypse(self) -> bool:
        return getattr(self, "_blitz_apocalypse", False)

    @property
    def blitz_are_you_not_entertained(self) -> bool:
        return getattr(self, "_blitz_are_you_not_entertained", False)

    @property
    def blitz_blitz_maniac(self) -> bool:
        return getattr(self, "_blitz_blitz_maniac", False)

    @property
    def blitz_bomberman(self) -> bool:
        return getattr(self, "_blitz_bomberman", False)

    @property
    def blitz_brutal_warrior(self) -> bool:
        return getattr(self, "_blitz_brutal_warrior", False)

    @property
    def blitz_champion(self) -> bool:
        return getattr(self, "_blitz_champion", False)

    @property
    def blitz_close_call(self) -> bool:
        return getattr(self, "_blitz_close_call", False)

    @property
    def blitz_coin_festival(self) -> bool:
        return getattr(self, "_blitz_coin_festival", False)

    @property
    def blitz_collector(self) -> bool:
        return getattr(self, "_blitz_collector", False)

    @property
    def blitz_cooking_expert(self) -> bool:
        return getattr(self, "_blitz_cooking_expert", False)

    @property
    def blitz_counterplay(self) -> bool:
        return getattr(self, "_blitz_counterplay", False)

    @property
    def blitz_craft_bread(self) -> bool:
        return getattr(self, "_blitz_craft_bread", False)

    @property
    def blitz_enchant_sword(self) -> bool:
        return getattr(self, "_blitz_enchant_sword", False)

    @property
    def blitz_enchanted_armor(self) -> bool:
        return getattr(self, "_blitz_enchanted_armor", False)

    @property
    def blitz_experimentation(self) -> bool:
        return getattr(self, "_blitz_experimentation", False)

    @property
    def blitz_finally(self) -> bool:
        return getattr(self, "_blitz_finally", False)

    @property
    def blitz_find_blitz(self) -> bool:
        return getattr(self, "_blitz_find_blitz", False)

    @property
    def blitz_find_head(self) -> bool:
        return getattr(self, "_blitz_find_head", False)

    @property
    def blitz_first_blood(self) -> bool:
        return getattr(self, "_blitz_first_blood", False)

    @property
    def blitz_fish_kill(self) -> bool:
        return getattr(self, "_blitz_fish_kill", False)

    @property
    def blitz_frame_of_mind(self) -> bool:
        return getattr(self, "_blitz_frame_of_mind", False)

    @property
    def blitz_full_inventory(self) -> bool:
        return getattr(self, "_blitz_full_inventory", False)

    @property
    def blitz_get_diamond_sword(self) -> bool:
        return getattr(self, "_blitz_get_diamond_sword", False)

    @property
    def blitz_kill_without_kit(self) -> bool:
        return getattr(self, "_blitz_kill_without_kit", False)

    @property
    def blitz_level_seven(self) -> bool:
        return getattr(self, "_blitz_level_seven", False)

    @property
    def blitz_lucky_minions(self) -> bool:
        return getattr(self, "_blitz_lucky_minions", False)

    @property
    def blitz_max_blitz(self) -> bool:
        return getattr(self, "_blitz_max_blitz", False)

    @property
    def blitz_nickname(self) -> bool:
        return getattr(self, "_blitz_nickname", False)

    @property
    def blitz_no_looting(self) -> bool:
        return getattr(self, "_blitz_no_looting", False)

    @property
    def blitz_no_problem(self) -> bool:
        return getattr(self, "_blitz_no_problem", False)

    @property
    def blitz_no_regrets(self) -> bool:
        return getattr(self, "_blitz_no_regrets", False)

    @property
    def blitz_not_skywars(self) -> bool:
        return getattr(self, "_blitz_not_skywars", False)

    @property
    def blitz_party_animal(self) -> bool:
        return getattr(self, "_blitz_party_animal", False)

    @property
    def blitz_pigrider(self) -> bool:
        return getattr(self, "_blitz_pigrider", False)

    @property
    def blitz_preference(self) -> bool:
        return getattr(self, "_blitz_preference", False)

    @property
    def blitz_rambo(self) -> bool:
        return getattr(self, "_blitz_rambo", False)

    @property
    def blitz_rampage(self) -> bool:
        return getattr(self, "_blitz_rampage", False)

    @property
    def blitz_safety_first(self) -> bool:
        return getattr(self, "_blitz_safety_first", False)

    @property
    def blitz_sail_away(self) -> bool:
        return getattr(self, "_blitz_sail_away", False)

    @property
    def blitz_seven_kits(self) -> bool:
        return getattr(self, "_blitz_seven_kits", False)

    @property
    def blitz_so_shiny(self) -> bool:
        return getattr(self, "_blitz_so_shiny", False)

    @property
    def blitz_spawn_horse(self) -> bool:
        return getattr(self, "_blitz_spawn_horse", False)

    @property
    def blitz_theres_levels_to_this(self) -> bool:
        return getattr(self, "_blitz_theres_levels_to_this", False)

    @property
    def blitz_titanium(self) -> bool:
        return getattr(self, "_blitz_titanium", False)

    @property
    def blitz_too_basic(self) -> bool:
        return getattr(self, "_blitz_too_basic", False)

    @property
    def blitz_ultimate_combatant(self) -> bool:
        return getattr(self, "_blitz_ultimate_combatant", False)

    @property
    def blitz_ultimate_completist(self) -> bool:
        return getattr(self, "_blitz_ultimate_completist", False)

    @property
    def blitz_ultimate_prestiger(self) -> bool:
        return getattr(self, "_blitz_ultimate_prestiger", False)

    @property
    def blitz_unstoppable(self) -> bool:
        return getattr(self, "_blitz_unstoppable", False)

    @property
    def blitz_use_wolf_tamer(self) -> bool:
        return getattr(self, "_blitz_use_wolf_tamer", False)

    @property
    def blitz_win_before_deathmatch(self) -> bool:
        return getattr(self, "_blitz_win_before_deathmatch", False)

    @property
    def bridge_community_oriented(self) -> bool:
        return getattr(self, "_bridge_community_oriented", False)

    @property
    def bridge_express_yourself(self) -> bool:
        return getattr(self, "_bridge_express_yourself", False)

    @property
    def bridge_got_ya(self) -> bool:
        return getattr(self, "_bridge_got_ya", False)

    @property
    def bridge_hat_trick(self) -> bool:
        return getattr(self, "_bridge_hat_trick", False)

    @property
    def bridge_ninja(self) -> bool:
        return getattr(self, "_bridge_ninja", False)

    @property
    def bridge_on_fire(self) -> bool:
        return getattr(self, "_bridge_on_fire", False)

    @property
    def buildbattle_braniac(self) -> bool:
        return getattr(self, "_buildbattle_braniac", False)

    @property
    def buildbattle_fancy(self) -> bool:
        return getattr(self, "_buildbattle_fancy", False)

    @property
    def buildbattle_guessing_streak(self) -> bool:
        return getattr(self, "_buildbattle_guessing_streak", False)

    @property
    def buildbattle_intuition(self) -> bool:
        return getattr(self, "_buildbattle_intuition", False)

    @property
    def buildbattle_legendary(self) -> bool:
        return getattr(self, "_buildbattle_legendary", False)

    @property
    def buildbattle_locked_in(self) -> bool:
        return getattr(self, "_buildbattle_locked_in", False)

    @property
    def buildbattle_mobster(self) -> bool:
        return getattr(self, "_buildbattle_mobster", False)

    @property
    def buildbattle_musician(self) -> bool:
        return getattr(self, "_buildbattle_musician", False)

    @property
    def buildbattle_no_mistakes(self) -> bool:
        return getattr(self, "_buildbattle_no_mistakes", False)

    @property
    def buildbattle_obvious(self) -> bool:
        return getattr(self, "_buildbattle_obvious", False)

    @property
    def buildbattle_ooo_shiny(self) -> bool:
        return getattr(self, "_buildbattle_ooo_shiny", False)

    @property
    def buildbattle_over_99(self) -> bool:
        return getattr(self, "_buildbattle_over_99", False)

    @property
    def buildbattle_perfection(self) -> bool:
        return getattr(self, "_buildbattle_perfection", False)

    @property
    def buildbattle_podium_position(self) -> bool:
        return getattr(self, "_buildbattle_podium_position", False)

    @property
    def buildbattle_professional_builder(self) -> bool:
        return getattr(self, "_buildbattle_professional_builder", False)

    @property
    def buildbattle_stenographer(self) -> bool:
        return getattr(self, "_buildbattle_stenographer", False)

    @property
    def buildbattle_superior_vote(self) -> bool:
        return getattr(self, "_buildbattle_superior_vote", False)

    @property
    def buildbattle_teamwork(self) -> bool:
        return getattr(self, "_buildbattle_teamwork", False)

    @property
    def buildbattle_that_wood_be_perfect(self) -> bool:
        return getattr(self, "_buildbattle_that_wood_be_perfect", False)

    @property
    def christmas2017_big_bag_o_gifts(self) -> bool:
        return getattr(self, "_christmas2017_big_bag_o_gifts", False)

    @property
    def christmas2017_blacksmith(self) -> bool:
        return getattr(self, "_christmas2017_blacksmith", False)

    @property
    def christmas2017_bouncy_castle(self) -> bool:
        return getattr(self, "_christmas2017_bouncy_castle", False)

    @property
    def christmas2017_christmas_is_saved(self) -> bool:
        return getattr(self, "_christmas2017_christmas_is_saved", False)

    @property
    def christmas2017_christmas_quest(self) -> bool:
        return getattr(self, "_christmas2017_christmas_quest", False)

    @property
    def christmas2017_christmas_topper(self) -> bool:
        return getattr(self, "_christmas2017_christmas_topper", False)

    @property
    def christmas2017_close_enough(self) -> bool:
        return getattr(self, "_christmas2017_close_enough", False)

    @property
    def christmas2017_dem_cows(self) -> bool:
        return getattr(self, "_christmas2017_dem_cows", False)

    @property
    def christmas2017_do_you_wanna_build_a_snowman(self) -> bool:
        return getattr(
            self,
            "_christmas2017_do_you_wanna_build_a_snowman",
            False,
        )

    @property
    def christmas2017_eat_this(self) -> bool:
        return getattr(self, "_christmas2017_eat_this", False)

    @property
    def christmas2017_empty_house(self) -> bool:
        return getattr(self, "_christmas2017_empty_house", False)

    @property
    def christmas2017_explosive_candy(self) -> bool:
        return getattr(self, "_christmas2017_explosive_candy", False)

    @property
    def christmas2017_festivities(self) -> bool:
        return getattr(self, "_christmas2017_festivities", False)

    @property
    def christmas2017_freeze_dont_move(self) -> bool:
        return getattr(self, "_christmas2017_freeze_dont_move", False)

    @property
    def christmas2017_freshly_baked(self) -> bool:
        return getattr(self, "_christmas2017_freshly_baked", False)

    @property
    def christmas2017_friendly_fire(self) -> bool:
        return getattr(self, "_christmas2017_friendly_fire", False)

    @property
    def christmas2017_greed_incarnate(self) -> bool:
        return getattr(self, "_christmas2017_greed_incarnate", False)

    @property
    def christmas2017_groopo_returns(self) -> bool:
        return getattr(self, "_christmas2017_groopo_returns", False)

    @property
    def christmas2017_holiday_miracle(self) -> bool:
        return getattr(self, "_christmas2017_holiday_miracle", False)

    @property
    def christmas2017_hunt_begins(self) -> bool:
        return getattr(self, "_christmas2017_hunt_begins", False)

    @property
    def christmas2017_hunt_begins_2018(self) -> bool:
        return getattr(self, "_christmas2017_hunt_begins_2018", False)

    @property
    def christmas2017_hunt_begins_2019(self) -> bool:
        return getattr(self, "_christmas2017_hunt_begins_2019", False)

    @property
    def christmas2017_hunt_begins_2020(self) -> bool:
        return getattr(self, "_christmas2017_hunt_begins_2020", False)

    @property
    def christmas2017_hunt_begins_2021(self) -> bool:
        return getattr(self, "_christmas2017_hunt_begins_2021", False)

    @property
    def christmas2017_hunt_begins_2024(self) -> bool:
        return getattr(self, "_christmas2017_hunt_begins_2024", False)

    @property
    def christmas2017_ice_breaker(self) -> bool:
        return getattr(self, "_christmas2017_ice_breaker", False)

    @property
    def christmas2017_ice_king(self) -> bool:
        return getattr(self, "_christmas2017_ice_king", False)

    @property
    def christmas2017_ice_spreader(self) -> bool:
        return getattr(self, "_christmas2017_ice_spreader", False)

    @property
    def christmas2017_knead_no_more(self) -> bool:
        return getattr(self, "_christmas2017_knead_no_more", False)

    @property
    def christmas2017_legendary(self) -> bool:
        return getattr(self, "_christmas2017_legendary", False)

    @property
    def christmas2017_let_it_snow(self) -> bool:
        return getattr(self, "_christmas2017_let_it_snow", False)

    @property
    def christmas2017_nom_nom(self) -> bool:
        return getattr(self, "_christmas2017_nom_nom", False)

    @property
    def christmas2017_not_so_secret_santa(self) -> bool:
        return getattr(self, "_christmas2017_not_so_secret_santa", False)

    @property
    def christmas2017_oooo_chilly(self) -> bool:
        return getattr(self, "_christmas2017_oooo_chilly", False)

    @property
    def christmas2017_real_santa_2019(self) -> bool:
        return getattr(self, "_christmas2017_real_santa_2019", False)

    @property
    def christmas2017_real_santa_2020(self) -> bool:
        return getattr(self, "_christmas2017_real_santa_2020", False)

    @property
    def christmas2017_real_santa_2021(self) -> bool:
        return getattr(self, "_christmas2017_real_santa_2021", False)

    @property
    def christmas2017_real_santa_2022(self) -> bool:
        return getattr(self, "_christmas2017_real_santa_2022", False)

    @property
    def christmas2017_real_santa_2023(self) -> bool:
        return getattr(self, "_christmas2017_real_santa_2023", False)

    @property
    def christmas2017_real_santa_2024(self) -> bool:
        return getattr(self, "_christmas2017_real_santa_2024", False)

    @property
    def christmas2017_rudolphs_favourite_carrot(self) -> bool:
        return getattr(self, "_christmas2017_rudolphs_favourite_carrot", False)

    @property
    def christmas2017_rush(self) -> bool:
        return getattr(self, "_christmas2017_rush", False)

    @property
    def christmas2017_santa_helper(self) -> bool:
        return getattr(self, "_christmas2017_santa_helper", False)

    @property
    def christmas2017_snow_wars(self) -> bool:
        return getattr(self, "_christmas2017_snow_wars", False)

    @property
    def christmas2017_spreading_love(self) -> bool:
        return getattr(self, "_christmas2017_spreading_love", False)

    @property
    def christmas2017_sugar_rush(self) -> bool:
        return getattr(self, "_christmas2017_sugar_rush", False)

    @property
    def christmas2017_swegmas(self) -> bool:
        return getattr(self, "_christmas2017_swegmas", False)

    @property
    def christmas2017_to_war(self) -> bool:
        return getattr(self, "_christmas2017_to_war", False)

    @property
    def christmas2017_uh_uh(self) -> bool:
        return getattr(self, "_christmas2017_uh_uh", False)

    @property
    def christmas2017_winter_runner(self) -> bool:
        return getattr(self, "_christmas2017_winter_runner", False)

    @property
    def copsandcrims_armed_and_dangerous(self) -> bool:
        return getattr(self, "_copsandcrims_armed_and_dangerous", False)

    @property
    def copsandcrims_blasted_to_the_moon(self) -> bool:
        return getattr(self, "_copsandcrims_blasted_to_the_moon", False)

    @property
    def copsandcrims_blind_kill(self) -> bool:
        return getattr(self, "_copsandcrims_blind_kill", False)

    @property
    def copsandcrims_character_upgrades(self) -> bool:
        return getattr(self, "_copsandcrims_character_upgrades", False)

    @property
    def copsandcrims_close_call(self) -> bool:
        return getattr(self, "_copsandcrims_close_call", False)

    @property
    def copsandcrims_comeback_story(self) -> bool:
        return getattr(self, "_copsandcrims_comeback_story", False)

    @property
    def copsandcrims_deathmatch_specialist(self) -> bool:
        return getattr(self, "_copsandcrims_deathmatch_specialist", False)

    @property
    def copsandcrims_friendly_fire(self) -> bool:
        return getattr(self, "_copsandcrims_friendly_fire", False)

    @property
    def copsandcrims_friendly_game(self) -> bool:
        return getattr(self, "_copsandcrims_friendly_game", False)

    @property
    def copsandcrims_grafitti_king(self) -> bool:
        return getattr(self, "_copsandcrims_grafitti_king", False)

    @property
    def copsandcrims_gun_master(self) -> bool:
        return getattr(self, "_copsandcrims_gun_master", False)

    @property
    def copsandcrims_half_the_battle(self) -> bool:
        return getattr(self, "_copsandcrims_half_the_battle", False)

    @property
    def copsandcrims_homing_bullets(self) -> bool:
        return getattr(self, "_copsandcrims_homing_bullets", False)

    @property
    def copsandcrims_hunting_season(self) -> bool:
        return getattr(self, "_copsandcrims_hunting_season", False)

    @property
    def copsandcrims_is_it_good_now(self) -> bool:
        return getattr(self, "_copsandcrims_is_it_good_now", False)

    @property
    def copsandcrims_legends_never_die(self) -> bool:
        return getattr(self, "_copsandcrims_legends_never_die", False)

    @property
    def copsandcrims_like_my_gun(self) -> bool:
        return getattr(self, "_copsandcrims_like_my_gun", False)

    @property
    def copsandcrims_never_too_late(self) -> bool:
        return getattr(self, "_copsandcrims_never_too_late", False)

    @property
    def copsandcrims_on_fire(self) -> bool:
        return getattr(self, "_copsandcrims_on_fire", False)

    @property
    def copsandcrims_one_shot_one_kil(self) -> bool:
        return getattr(self, "_copsandcrims_one_shot_one_kil", False)

    @property
    def copsandcrims_pentaaaa(self) -> bool:
        return getattr(self, "_copsandcrims_pentaaaa", False)

    @property
    def copsandcrims_raise_your_voice(self) -> bool:
        return getattr(self, "_copsandcrims_raise_your_voice", False)

    @property
    def copsandcrims_secret_order(self) -> bool:
        return getattr(self, "_copsandcrims_secret_order", False)

    @property
    def copsandcrims_sniper(self) -> bool:
        return getattr(self, "_copsandcrims_sniper", False)

    @property
    def copsandcrims_so_much_better(self) -> bool:
        return getattr(self, "_copsandcrims_so_much_better", False)

    @property
    def copsandcrims_street_artist(self) -> bool:
        return getattr(self, "_copsandcrims_street_artist", False)

    @property
    def copsandcrims_team_communicator(self) -> bool:
        return getattr(self, "_copsandcrims_team_communicator", False)

    @property
    def copsandcrims_the_best_around(self) -> bool:
        return getattr(self, "_copsandcrims_the_best_around", False)

    @property
    def copsandcrims_the_carrier(self) -> bool:
        return getattr(self, "_copsandcrims_the_carrier", False)

    @property
    def copsandcrims_too_easy(self) -> bool:
        return getattr(self, "_copsandcrims_too_easy", False)

    @property
    def copsandcrims_triipplee(self) -> bool:
        return getattr(self, "_copsandcrims_triipplee", False)

    @property
    def copsandcrims_umadbro(self) -> bool:
        return getattr(self, "_copsandcrims_umadbro", False)

    @property
    def copsandcrims_unstoppable(self) -> bool:
        return getattr(self, "_copsandcrims_unstoppable", False)

    @property
    def copsandcrims_warfare_stylist(self) -> bool:
        return getattr(self, "_copsandcrims_warfare_stylist", False)

    @property
    def duels_ace(self) -> bool:
        return getattr(self, "_duels_ace", False)

    @property
    def duels_axe_you_a_question(self) -> bool:
        return getattr(self, "_duels_axe_you_a_question", False)

    @property
    def duels_boxing_combo(self) -> bool:
        return getattr(self, "_duels_boxing_combo", False)

    @property
    def duels_build_battle(self) -> bool:
        return getattr(self, "_duels_build_battle", False)

    @property
    def duels_burn_baby_burn(self) -> bool:
        return getattr(self, "_duels_burn_baby_burn", False)

    @property
    def duels_carried(self) -> bool:
        return getattr(self, "_duels_carried", False)

    @property
    def duels_change_icon(self) -> bool:
        return getattr(self, "_duels_change_icon", False)

    @property
    def duels_clean_sweep(self) -> bool:
        return getattr(self, "_duels_clean_sweep", False)

    @property
    def duels_close_call(self) -> bool:
        return getattr(self, "_duels_close_call", False)

    @property
    def duels_community_oriented(self) -> bool:
        return getattr(self, "_duels_community_oriented", False)

    @property
    def duels_competitor(self) -> bool:
        return getattr(self, "_duels_competitor", False)

    @property
    def duels_domination(self) -> bool:
        return getattr(self, "_duels_domination", False)

    @property
    def duels_express_yourself(self) -> bool:
        return getattr(self, "_duels_express_yourself", False)

    @property
    def duels_fortification(self) -> bool:
        return getattr(self, "_duels_fortification", False)

    @property
    def duels_getting_loot(self) -> bool:
        return getattr(self, "_duels_getting_loot", False)

    @property
    def duels_gg(self) -> bool:
        return getattr(self, "_duels_gg", False)

    @property
    def duels_gone_fishing(self) -> bool:
        return getattr(self, "_duels_gone_fishing", False)

    @property
    def duels_got_ya(self) -> bool:
        return getattr(self, "_duels_got_ya", False)

    @property
    def duels_hat_trick(self) -> bool:
        return getattr(self, "_duels_hat_trick", False)

    @property
    def duels_hawk_eye(self) -> bool:
        return getattr(self, "_duels_hawk_eye", False)

    @property
    def duels_heart_hoarder(self) -> bool:
        return getattr(self, "_duels_heart_hoarder", False)

    @property
    def duels_hungry(self) -> bool:
        return getattr(self, "_duels_hungry", False)

    @property
    def duels_jack_of_all_trades(self) -> bool:
        return getattr(self, "_duels_jack_of_all_trades", False)

    @property
    def duels_last_stand(self) -> bool:
        return getattr(self, "_duels_last_stand", False)

    @property
    def duels_lobby_slayer(self) -> bool:
        return getattr(self, "_duels_lobby_slayer", False)

    @property
    def duels_master_builders(self) -> bool:
        return getattr(self, "_duels_master_builders", False)

    @property
    def duels_my_preference(self) -> bool:
        return getattr(self, "_duels_my_preference", False)

    @property
    def duels_ninja(self) -> bool:
        return getattr(self, "_duels_ninja", False)

    @property
    def duels_not_close_at_all(self) -> bool:
        return getattr(self, "_duels_not_close_at_all", False)

    @property
    def duels_not_hungary(self) -> bool:
        return getattr(self, "_duels_not_hungary", False)

    @property
    def duels_on_fire(self) -> bool:
        return getattr(self, "_duels_on_fire", False)

    @property
    def duels_replay(self) -> bool:
        return getattr(self, "_duels_replay", False)

    @property
    def duels_revenge(self) -> bool:
        return getattr(self, "_duels_revenge", False)

    @property
    def duels_shut_down(self) -> bool:
        return getattr(self, "_duels_shut_down", False)

    @property
    def duels_speedster(self) -> bool:
        return getattr(self, "_duels_speedster", False)

    @property
    def duels_speedy_sumo(self) -> bool:
        return getattr(self, "_duels_speedy_sumo", False)

    @property
    def duels_summoner(self) -> bool:
        return getattr(self, "_duels_summoner", False)

    @property
    def duels_team_player(self) -> bool:
        return getattr(self, "_duels_team_player", False)

    @property
    def duels_the_waiting_game(self) -> bool:
        return getattr(self, "_duels_the_waiting_game", False)

    @property
    def duels_void_archer(self) -> bool:
        return getattr(self, "_duels_void_archer", False)

    @property
    def duels_well_rounded(self) -> bool:
        return getattr(self, "_duels_well_rounded", False)

    @property
    def easter_all_eggs_2020(self) -> bool:
        return getattr(self, "_easter_all_eggs_2020", False)

    @property
    def easter_all_eggs_2021(self) -> bool:
        return getattr(self, "_easter_all_eggs_2021", False)

    @property
    def easter_all_eggs_2022(self) -> bool:
        return getattr(self, "_easter_all_eggs_2022", False)

    @property
    def easter_all_eggs_2023(self) -> bool:
        return getattr(self, "_easter_all_eggs_2023", False)

    @property
    def easter_all_eggs_2024(self) -> bool:
        return getattr(self, "_easter_all_eggs_2024", False)

    @property
    def easter_blitz_spawn_rabbit(self) -> bool:
        return getattr(self, "_easter_blitz_spawn_rabbit", False)

    @property
    def easter_bw_jump_boost(self) -> bool:
        return getattr(self, "_easter_bw_jump_boost", False)

    @property
    def easter_close_enough(self) -> bool:
        return getattr(self, "_easter_close_enough", False)

    @property
    def easter_cvc_grenades(self) -> bool:
        return getattr(self, "_easter_cvc_grenades", False)

    @property
    def easter_easter_egg(self) -> bool:
        return getattr(self, "_easter_easter_egg", False)

    @property
    def easter_egg_assault(self) -> bool:
        return getattr(self, "_easter_egg_assault", False)

    @property
    def easter_egg_betrayer(self) -> bool:
        return getattr(self, "_easter_egg_betrayer", False)

    @property
    def easter_egg_layer(self) -> bool:
        return getattr(self, "_easter_egg_layer", False)

    @property
    def easter_environment_protection(self) -> bool:
        return getattr(self, "_easter_environment_protection", False)

    @property
    def easter_faster_than_wind(self) -> bool:
        return getattr(self, "_easter_faster_than_wind", False)

    @property
    def easter_first_egg_2019(self) -> bool:
        return getattr(self, "_easter_first_egg_2019", False)

    @property
    def easter_first_egg_2020(self) -> bool:
        return getattr(self, "_easter_first_egg_2020", False)

    @property
    def easter_first_egg_2021(self) -> bool:
        return getattr(self, "_easter_first_egg_2021", False)

    @property
    def easter_first_egg_2022(self) -> bool:
        return getattr(self, "_easter_first_egg_2022", False)

    @property
    def easter_first_egg_2023(self) -> bool:
        return getattr(self, "_easter_first_egg_2023", False)

    @property
    def easter_first_egg_2024(self) -> bool:
        return getattr(self, "_easter_first_egg_2024", False)

    @property
    def easter_happy_easter_2019(self) -> bool:
        return getattr(self, "_easter_happy_easter_2019", False)

    @property
    def easter_hop_to_it(self) -> bool:
        return getattr(self, "_easter_hop_to_it", False)

    @property
    def easter_inner_rabbit(self) -> bool:
        return getattr(self, "_easter_inner_rabbit", False)

    @property
    def easter_megawalls_jockey(self) -> bool:
        return getattr(self, "_easter_megawalls_jockey", False)

    @property
    def easter_midspring_nights_dream(self) -> bool:
        return getattr(self, "_easter_midspring_nights_dream", False)

    @property
    def easter_mm_carrot_kills(self) -> bool:
        return getattr(self, "_easter_mm_carrot_kills", False)

    @property
    def easter_paintball_leeroy(self) -> bool:
        return getattr(self, "_easter_paintball_leeroy", False)

    @property
    def easter_pep_in_your_step(self) -> bool:
        return getattr(self, "_easter_pep_in_your_step", False)

    @property
    def easter_pit_dragon_egg(self) -> bool:
        return getattr(self, "_easter_pit_dragon_egg", False)

    @property
    def easter_saving_the_planet(self) -> bool:
        return getattr(self, "_easter_saving_the_planet", False)

    @property
    def easter_smash_cluck_kills(self) -> bool:
        return getattr(self, "_easter_smash_cluck_kills", False)

    @property
    def easter_spring_fishing(self) -> bool:
        return getattr(self, "_easter_spring_fishing", False)

    @property
    def easter_spring_maiden(self) -> bool:
        return getattr(self, "_easter_spring_maiden", False)

    @property
    def easter_spring_water(self) -> bool:
        return getattr(self, "_easter_spring_water", False)

    @property
    def easter_springtime_match_ups(self) -> bool:
        return getattr(self, "_easter_springtime_match_ups", False)

    @property
    def easter_sw_egg_void(self) -> bool:
        return getattr(self, "_easter_sw_egg_void", False)

    @property
    def easter_towerwars_chickens(self) -> bool:
        return getattr(self, "_easter_towerwars_chickens", False)

    @property
    def easter_uhc_golden_carrot(self) -> bool:
        return getattr(self, "_easter_uhc_golden_carrot", False)

    @property
    def easter_vampirez_carrot(self) -> bool:
        return getattr(self, "_easter_vampirez_carrot", False)

    @property
    def easter_whats_this(self) -> bool:
        return getattr(self, "_easter_whats_this", False)

    @property
    def easter_you_didnt_see_that_coming(self) -> bool:
        return getattr(self, "_easter_you_didnt_see_that_coming", False)

    @property
    def general_achievement_npc(self) -> bool:
        return getattr(self, "_general_achievement_npc", False)

    @property
    def general_bingo_jackpot(self) -> bool:
        return getattr(self, "_general_bingo_jackpot", False)

    @property
    def general_code_breaker(self) -> bool:
        return getattr(self, "_general_code_breaker", False)

    @property
    def general_crash_landed(self) -> bool:
        return getattr(self, "_general_crash_landed", False)

    @property
    def general_deep_sea_expert(self) -> bool:
        return getattr(self, "_general_deep_sea_expert", False)

    @property
    def general_doing_my_part(self) -> bool:
        return getattr(self, "_general_doing_my_part", False)

    @property
    def general_fishing_hobbyist(self) -> bool:
        return getattr(self, "_general_fishing_hobbyist", False)

    @property
    def general_grapple_pro(self) -> bool:
        return getattr(self, "_general_grapple_pro", False)

    @property
    def general_happiest_anniversary(self) -> bool:
        return getattr(self, "_general_happiest_anniversary", False)

    @property
    def general_hot_potato(self) -> bool:
        return getattr(self, "_general_hot_potato", False)

    @property
    def general_keep_quiet(self) -> bool:
        return getattr(self, "_general_keep_quiet", False)

    @property
    def general_labyrinthine_collector(self) -> bool:
        return getattr(self, "_general_labyrinthine_collector", False)

    @property
    def general_lobby_explorer(self) -> bool:
        return getattr(self, "_general_lobby_explorer", False)

    @property
    def general_old_farmers_almanac(self) -> bool:
        return getattr(self, "_general_old_farmers_almanac", False)

    @property
    def general_tips_and_tricks(self) -> bool:
        return getattr(self, "_general_tips_and_tricks", False)

    @property
    def general_treasure_hunt_2021(self) -> bool:
        return getattr(self, "_general_treasure_hunt_2021", False)

    @property
    def general_treasure_hunt_2023(self) -> bool:
        return getattr(self, "_general_treasure_hunt_2023", False)

    @property
    def gingerbread_cant_see_anything(self) -> bool:
        return getattr(self, "_gingerbread_cant_see_anything", False)

    @property
    def gingerbread_chill_out(self) -> bool:
        return getattr(self, "_gingerbread_chill_out", False)

    @property
    def gingerbread_coins_please(self) -> bool:
        return getattr(self, "_gingerbread_coins_please", False)

    @property
    def gingerbread_eat_my_dust(self) -> bool:
        return getattr(self, "_gingerbread_eat_my_dust", False)

    @property
    def gingerbread_eternally_awesome(self) -> bool:
        return getattr(self, "_gingerbread_eternally_awesome", False)

    @property
    def gingerbread_flower_power(self) -> bool:
        return getattr(self, "_gingerbread_flower_power", False)

    @property
    def gingerbread_front_man(self) -> bool:
        return getattr(self, "_gingerbread_front_man", False)

    @property
    def gingerbread_gettin_paid(self) -> bool:
        return getattr(self, "_gingerbread_gettin_paid", False)

    @property
    def gingerbread_honking_amazing(self) -> bool:
        return getattr(self, "_gingerbread_honking_amazing", False)

    @property
    def gingerbread_honking_mad(self) -> bool:
        return getattr(self, "_gingerbread_honking_mad", False)

    @property
    def gingerbread_im_lucky(self) -> bool:
        return getattr(self, "_gingerbread_im_lucky", False)

    @property
    def gingerbread_is_this_survival_games(self) -> bool:
        return getattr(self, "_gingerbread_is_this_survival_games", False)

    @property
    def gingerbread_javelins_rocket(self) -> bool:
        return getattr(self, "_gingerbread_javelins_rocket", False)

    @property
    def gingerbread_lapped(self) -> bool:
        return getattr(self, "_gingerbread_lapped", False)

    @property
    def gingerbread_mechanic(self) -> bool:
        return getattr(self, "_gingerbread_mechanic", False)

    @property
    def gingerbread_missile_mayhem(self) -> bool:
        return getattr(self, "_gingerbread_missile_mayhem", False)

    @property
    def gingerbread_modular(self) -> bool:
        return getattr(self, "_gingerbread_modular", False)

    @property
    def gingerbread_never_lucky(self) -> bool:
        return getattr(self, "_gingerbread_never_lucky", False)

    @property
    def gingerbread_new_style(self) -> bool:
        return getattr(self, "_gingerbread_new_style", False)

    @property
    def gingerbread_nope(self) -> bool:
        return getattr(self, "_gingerbread_nope", False)

    @property
    def gingerbread_shut_down(self) -> bool:
        return getattr(self, "_gingerbread_shut_down", False)

    @property
    def gingerbread_sleeper_agent(self) -> bool:
        return getattr(self, "_gingerbread_sleeper_agent", False)

    @property
    def gingerbread_surface_to_air_missile(self) -> bool:
        return getattr(self, "_gingerbread_surface_to_air_missile", False)

    @property
    def gingerbread_tryharder(self) -> bool:
        return getattr(self, "_gingerbread_tryharder", False)

    @property
    def gingerbread_victors_prize(self) -> bool:
        return getattr(self, "_gingerbread_victors_prize", False)

    @property
    def gingerbread_well_versed(self) -> bool:
        return getattr(self, "_gingerbread_well_versed", False)

    @property
    def halloween2017_all_baskets(self) -> bool:
        return getattr(self, "_halloween2017_all_baskets", False)

    @property
    def halloween2017_all_baskets_2020(self) -> bool:
        return getattr(self, "_halloween2017_all_baskets_2020", False)

    @property
    def halloween2017_all_baskets_2021(self) -> bool:
        return getattr(self, "_halloween2017_all_baskets_2021", False)

    @property
    def halloween2017_all_baskets_2022(self) -> bool:
        return getattr(self, "_halloween2017_all_baskets_2022", False)

    @property
    def halloween2017_all_baskets_2023(self) -> bool:
        return getattr(self, "_halloween2017_all_baskets_2023", False)

    @property
    def halloween2017_all_baskets_2024(self) -> bool:
        return getattr(self, "_halloween2017_all_baskets_2024", False)

    @property
    def halloween2017_all_ghosts(self) -> bool:
        return getattr(self, "_halloween2017_all_ghosts", False)

    @property
    def halloween2017_be_free(self) -> bool:
        return getattr(self, "_halloween2017_be_free", False)

    @property
    def halloween2017_blame_your_team(self) -> bool:
        return getattr(self, "_halloween2017_blame_your_team", False)

    @property
    def halloween2017_burning_touch(self) -> bool:
        return getattr(self, "_halloween2017_burning_touch", False)

    @property
    def halloween2017_classy_wither(self) -> bool:
        return getattr(self, "_halloween2017_classy_wither", False)

    @property
    def halloween2017_devils_ride(self) -> bool:
        return getattr(self, "_halloween2017_devils_ride", False)

    @property
    def halloween2017_fear_the_pumpkinator(self) -> bool:
        return getattr(self, "_halloween2017_fear_the_pumpkinator", False)

    @property
    def halloween2017_feline_fortune(self) -> bool:
        return getattr(self, "_halloween2017_feline_fortune", False)

    @property
    def halloween2017_fire_from_hell(self) -> bool:
        return getattr(self, "_halloween2017_fire_from_hell", False)

    @property
    def halloween2017_five_baskets(self) -> bool:
        return getattr(self, "_halloween2017_five_baskets", False)

    @property
    def halloween2017_five_baskets_2020(self) -> bool:
        return getattr(self, "_halloween2017_five_baskets_2020", False)

    @property
    def halloween2017_five_baskets_2021(self) -> bool:
        return getattr(self, "_halloween2017_five_baskets_2021", False)

    @property
    def halloween2017_five_baskets_2022(self) -> bool:
        return getattr(self, "_halloween2017_five_baskets_2022", False)

    @property
    def halloween2017_five_baskets_2023(self) -> bool:
        return getattr(self, "_halloween2017_five_baskets_2023", False)

    @property
    def halloween2017_five_baskets_2024(self) -> bool:
        return getattr(self, "_halloween2017_five_baskets_2024", False)

    @property
    def halloween2017_full_bat_mode(self) -> bool:
        return getattr(self, "_halloween2017_full_bat_mode", False)

    @property
    def halloween2017_good_try(self) -> bool:
        return getattr(self, "_halloween2017_good_try", False)

    @property
    def halloween2017_gravedigger(self) -> bool:
        return getattr(self, "_halloween2017_gravedigger", False)

    @property
    def halloween2017_haunted_maps(self) -> bool:
        return getattr(self, "_halloween2017_haunted_maps", False)

    @property
    def halloween2017_howl_o_ween(self) -> bool:
        return getattr(self, "_halloween2017_howl_o_ween", False)

    @property
    def halloween2017_killer_loot(self) -> bool:
        return getattr(self, "_halloween2017_killer_loot", False)

    @property
    def halloween2017_loose_floorboard(self) -> bool:
        return getattr(self, "_halloween2017_loose_floorboard", False)

    @property
    def halloween2017_master_alchemist(self) -> bool:
        return getattr(self, "_halloween2017_master_alchemist", False)

    @property
    def halloween2017_my_halloween_costume(self) -> bool:
        return getattr(self, "_halloween2017_my_halloween_costume", False)

    @property
    def halloween2017_october_betrayal(self) -> bool:
        return getattr(self, "_halloween2017_october_betrayal", False)

    @property
    def halloween2017_pumpkin_dancer(self) -> bool:
        return getattr(self, "_halloween2017_pumpkin_dancer", False)

    @property
    def halloween2017_pumpkin_death(self) -> bool:
        return getattr(self, "_halloween2017_pumpkin_death", False)

    @property
    def halloween2017_pumpkin_vision(self) -> bool:
        return getattr(self, "_halloween2017_pumpkin_vision", False)

    @property
    def halloween2017_pumpkins_will_rise(self) -> bool:
        return getattr(self, "_halloween2017_pumpkins_will_rise", False)

    @property
    def halloween2017_rising_dead(self) -> bool:
        return getattr(self, "_halloween2017_rising_dead", False)

    @property
    def halloween2017_second_ghost(self) -> bool:
        return getattr(self, "_halloween2017_second_ghost", False)

    @property
    def halloween2017_second_ghost_2018(self) -> bool:
        return getattr(self, "_halloween2017_second_ghost_2018", False)

    @property
    def halloween2017_see_through(self) -> bool:
        return getattr(self, "_halloween2017_see_through", False)

    @property
    def halloween2017_smoking_veil(self) -> bool:
        return getattr(self, "_halloween2017_smoking_veil", False)

    @property
    def halloween2017_spooktacular_bingo(self) -> bool:
        return getattr(self, "_halloween2017_spooktacular_bingo", False)

    @property
    def halloween2017_spooky_chest(self) -> bool:
        return getattr(self, "_halloween2017_spooky_chest", False)

    @property
    def halloween2017_spooky_victory(self) -> bool:
        return getattr(self, "_halloween2017_spooky_victory", False)

    @property
    def halloween2017_sugar_rush_2(self) -> bool:
        return getattr(self, "_halloween2017_sugar_rush_2", False)

    @property
    def halloween2017_survivors_be_gone(self) -> bool:
        return getattr(self, "_halloween2017_survivors_be_gone", False)

    @property
    def halloween2017_tbr_clock_tower_trip(self) -> bool:
        return getattr(self, "_halloween2017_tbr_clock_tower_trip", False)

    @property
    def halloween2017_tbr_clock_tower_trip_fast(self) -> bool:
        return getattr(self, "_halloween2017_tbr_clock_tower_trip_fast", False)

    @property
    def halloween2017_tbr_cryptic_castle(self) -> bool:
        return getattr(self, "_halloween2017_tbr_cryptic_castle", False)

    @property
    def halloween2017_tbr_farmland_circle(self) -> bool:
        return getattr(self, "_halloween2017_tbr_farmland_circle", False)

    @property
    def halloween2017_tbr_farmland_circle_fast(self) -> bool:
        return getattr(self, "_halloween2017_tbr_farmland_circle_fast", False)

    @property
    def halloween2017_tbr_forest_fright(self) -> bool:
        return getattr(self, "_halloween2017_tbr_forest_fright", False)

    @property
    def halloween2017_tbr_forest_fright_fast(self) -> bool:
        return getattr(self, "_halloween2017_tbr_forest_fright_fast", False)

    @property
    def halloween2017_tbr_pumpkin_jump(self) -> bool:
        return getattr(self, "_halloween2017_tbr_pumpkin_jump", False)

    @property
    def halloween2017_tbr_riverside_revenge(self) -> bool:
        return getattr(self, "_halloween2017_tbr_riverside_revenge", False)

    @property
    def halloween2017_tbr_riverside_revenge_fast(self) -> bool:
        return getattr(
            self,
            "_halloween2017_tbr_riverside_revenge_fast",
            False,
        )

    @property
    def halloween2017_tbr_seaside_drive(self) -> bool:
        return getattr(self, "_halloween2017_tbr_seaside_drive", False)

    @property
    def halloween2017_tbr_territorial_tour(self) -> bool:
        return getattr(self, "_halloween2017_tbr_territorial_tour", False)

    @property
    def halloween2017_tbr_village_sweep(self) -> bool:
        return getattr(self, "_halloween2017_tbr_village_sweep", False)

    @property
    def halloween2017_tbr_village_sweep_fast(self) -> bool:
        return getattr(self, "_halloween2017_tbr_village_sweep_fast", False)

    @property
    def halloween2017_that_time_of_year(self) -> bool:
        return getattr(self, "_halloween2017_that_time_of_year", False)

    @property
    def halloween2017_that_was_easy(self) -> bool:
        return getattr(self, "_halloween2017_that_was_easy", False)

    @property
    def halloween2017_the_crawling_dead(self) -> bool:
        return getattr(self, "_halloween2017_the_crawling_dead", False)

    @property
    def halloween2017_tricked(self) -> bool:
        return getattr(self, "_halloween2017_tricked", False)

    @property
    def halloween2017_undead_target_practice(self) -> bool:
        return getattr(self, "_halloween2017_undead_target_practice", False)

    @property
    def halloween2017_vampires_be_gone(self) -> bool:
        return getattr(self, "_halloween2017_vampires_be_gone", False)

    @property
    def halloween2017_withering_heights(self) -> bool:
        return getattr(self, "_halloween2017_withering_heights", False)

    @property
    def housing_grand_opening(self) -> bool:
        return getattr(self, "_housing_grand_opening", False)

    @property
    def housing_join_friend(self) -> bool:
        return getattr(self, "_housing_join_friend", False)

    @property
    def housing_join_random(self) -> bool:
        return getattr(self, "_housing_join_random", False)

    @property
    def housing_join_staff(self) -> bool:
        return getattr(self, "_housing_join_staff", False)

    @property
    def housing_join_youtube(self) -> bool:
        return getattr(self, "_housing_join_youtube", False)

    @property
    def housing_make_resident(self) -> bool:
        return getattr(self, "_housing_make_resident", False)

    @property
    def housing_new_look(self) -> bool:
        return getattr(self, "_housing_new_look", False)

    @property
    def housing_recieve_cookie(self) -> bool:
        return getattr(self, "_housing_recieve_cookie", False)

    @property
    def murdermystery_all_directions(self) -> bool:
        return getattr(self, "_murdermystery_all_directions", False)

    @property
    def murdermystery_block_with_barrier(self) -> bool:
        return getattr(self, "_murdermystery_block_with_barrier", False)

    @property
    def murdermystery_bow_kill_on_detective(self) -> bool:
        return getattr(self, "_murdermystery_bow_kill_on_detective", False)

    @property
    def murdermystery_disinfectant(self) -> bool:
        return getattr(self, "_murdermystery_disinfectant", False)

    @property
    def murdermystery_emp(self) -> bool:
        return getattr(self, "_murdermystery_emp", False)

    @property
    def murdermystery_five_curses(self) -> bool:
        return getattr(self, "_murdermystery_five_curses", False)

    @property
    def murdermystery_hit_by_sword_while_invinc(self) -> bool:
        return getattr(self, "_murdermystery_hit_by_sword_while_invinc", False)

    @property
    def murdermystery_kill_murderer_as_last_alive(self) -> bool:
        return getattr(
            self,
            "_murdermystery_kill_murderer_as_last_alive",
            False,
        )

    @property
    def murdermystery_kill_on_horse(self) -> bool:
        return getattr(self, "_murdermystery_kill_on_horse", False)

    @property
    def murdermystery_killstreak(self) -> bool:
        return getattr(self, "_murdermystery_killstreak", False)

    @property
    def murdermystery_last_survivor(self) -> bool:
        return getattr(self, "_murdermystery_last_survivor", False)

    @property
    def murdermystery_longrange_shot(self) -> bool:
        return getattr(self, "_murdermystery_longrange_shot", False)

    @property
    def murdermystery_murderer_first_kill(self) -> bool:
        return getattr(self, "_murdermystery_murderer_first_kill", False)

    @property
    def murdermystery_no_gold_pickup(self) -> bool:
        return getattr(self, "_murdermystery_no_gold_pickup", False)

    @property
    def murdermystery_paranoid(self) -> bool:
        return getattr(self, "_murdermystery_paranoid", False)

    @property
    def murdermystery_play_both_games(self) -> bool:
        return getattr(self, "_murdermystery_play_both_games", False)

    @property
    def murdermystery_play_game_in_lobby(self) -> bool:
        return getattr(self, "_murdermystery_play_game_in_lobby", False)

    @property
    def murdermystery_return_from_dead_win(self) -> bool:
        return getattr(self, "_murdermystery_return_from_dead_win", False)

    @property
    def murdermystery_secret_chamber(self) -> bool:
        return getattr(self, "_murdermystery_secret_chamber", False)

    @property
    def murdermystery_sixth_sense(self) -> bool:
        return getattr(self, "_murdermystery_sixth_sense", False)

    @property
    def murdermystery_thirty_gold_picked_up(self) -> bool:
        return getattr(self, "_murdermystery_thirty_gold_picked_up", False)

    @property
    def murdermystery_three_arrows(self) -> bool:
        return getattr(self, "_murdermystery_three_arrows", False)

    @property
    def murdermystery_top_zombie(self) -> bool:
        return getattr(self, "_murdermystery_top_zombie", False)

    @property
    def murdermystery_trigger_happy_havoc(self) -> bool:
        return getattr(self, "_murdermystery_trigger_happy_havoc", False)

    @property
    def murdermystery_watson(self) -> bool:
        return getattr(self, "_murdermystery_watson", False)

    @property
    def murdermystery_win_as_murderer_short_time(self) -> bool:
        return getattr(
            self,
            "_murdermystery_win_as_murderer_short_time",
            False,
        )

    @property
    def murdermystery_win_inno_monorail(self) -> bool:
        return getattr(self, "_murdermystery_win_inno_monorail", False)

    @property
    def murdermystery_win_while_invincible(self) -> bool:
        return getattr(self, "_murdermystery_win_while_invincible", False)

    @property
    def murdermystery_xom_b(self) -> bool:
        return getattr(self, "_murdermystery_xom_b", False)

    @property
    def paintball_activate_killstreaks(self) -> bool:
        return getattr(self, "_paintball_activate_killstreaks", False)

    @property
    def paintball_activate_leeroy_jenkins(self) -> bool:
        return getattr(self, "_paintball_activate_leeroy_jenkins", False)

    @property
    def paintball_activate_plus_ten(self) -> bool:
        return getattr(self, "_paintball_activate_plus_ten", False)

    @property
    def paintball_admin_hat(self) -> bool:
        return getattr(self, "_paintball_admin_hat", False)

    @property
    def paintball_cheating_death(self) -> bool:
        return getattr(self, "_paintball_cheating_death", False)

    @property
    def paintball_combo(self) -> bool:
        return getattr(self, "_paintball_combo", False)

    @property
    def paintball_energy_drink(self) -> bool:
        return getattr(self, "_paintball_energy_drink", False)

    @property
    def paintball_espionage(self) -> bool:
        return getattr(self, "_paintball_espionage", False)

    @property
    def paintball_explosive_death(self) -> bool:
        return getattr(self, "_paintball_explosive_death", False)

    @property
    def paintball_first_kill(self) -> bool:
        return getattr(self, "_paintball_first_kill", False)

    @property
    def paintball_go_home_youre_drunk(self) -> bool:
        return getattr(self, "_paintball_go_home_youre_drunk", False)

    @property
    def paintball_god_killer(self) -> bool:
        return getattr(self, "_paintball_god_killer", False)

    @property
    def paintball_how_does_it_feel(self) -> bool:
        return getattr(self, "_paintball_how_does_it_feel", False)

    @property
    def paintball_jackson_pollock(self) -> bool:
        return getattr(self, "_paintball_jackson_pollock", False)

    @property
    def paintball_last_kill(self) -> bool:
        return getattr(self, "_paintball_last_kill", False)

    @property
    def paintball_no_killstreaks(self) -> bool:
        return getattr(self, "_paintball_no_killstreaks", False)

    @property
    def paintball_now_you_see_me(self) -> bool:
        return getattr(self, "_paintball_now_you_see_me", False)

    @property
    def paintball_on_the_brink_of_defeat(self) -> bool:
        return getattr(self, "_paintball_on_the_brink_of_defeat", False)

    @property
    def paintball_sarcrifice(self) -> bool:
        return getattr(self, "_paintball_sarcrifice", False)

    @property
    def paintball_thunder_struck(self) -> bool:
        return getattr(self, "_paintball_thunder_struck", False)

    @property
    def paintball_trigger_happy(self) -> bool:
        return getattr(self, "_paintball_trigger_happy", False)

    @property
    def paintball_undercover_sloth(self) -> bool:
        return getattr(self, "_paintball_undercover_sloth", False)

    @property
    def paintball_unlock_hat(self) -> bool:
        return getattr(self, "_paintball_unlock_hat", False)

    @property
    def paintball_unlock_killstreaks(self) -> bool:
        return getattr(self, "_paintball_unlock_killstreaks", False)

    @property
    def paintball_warfare_time(self) -> bool:
        return getattr(self, "_paintball_warfare_time", False)

    @property
    def pit_bake_cake(self) -> bool:
        return getattr(self, "_pit_bake_cake", False)

    @property
    def pit_bid_auction(self) -> bool:
        return getattr(self, "_pit_bid_auction", False)

    @property
    def pit_claim_bounty(self) -> bool:
        return getattr(self, "_pit_claim_bounty", False)

    @property
    def pit_collect_from_care_package(self) -> bool:
        return getattr(self, "_pit_collect_from_care_package", False)

    @property
    def pit_complete_contract_fast(self) -> bool:
        return getattr(self, "_pit_complete_contract_fast", False)

    @property
    def pit_do_a_trade(self) -> bool:
        return getattr(self, "_pit_do_a_trade", False)

    @property
    def pit_earn_mystic_item(self) -> bool:
        return getattr(self, "_pit_earn_mystic_item", False)

    @property
    def pit_fall_in_void(self) -> bool:
        return getattr(self, "_pit_fall_in_void", False)

    @property
    def pit_full_storage(self) -> bool:
        return getattr(self, "_pit_full_storage", False)

    @property
    def pit_have_cobblestone(self) -> bool:
        return getattr(self, "_pit_have_cobblestone", False)

    @property
    def pit_high_killstreak(self) -> bool:
        return getattr(self, "_pit_high_killstreak", False)

    @property
    def pit_kill_two_beasts(self) -> bool:
        return getattr(self, "_pit_kill_two_beasts", False)

    @property
    def pit_kill_with_strength(self) -> bool:
        return getattr(self, "_pit_kill_with_strength", False)

    @property
    def pit_many_clicks_dragon_egg(self) -> bool:
        return getattr(self, "_pit_many_clicks_dragon_egg", False)

    @property
    def pit_max_out_el_gato(self) -> bool:
        return getattr(self, "_pit_max_out_el_gato", False)

    @property
    def pit_pentakill(self) -> bool:
        return getattr(self, "_pit_pentakill", False)

    @property
    def pit_place_obsidian(self) -> bool:
        return getattr(self, "_pit_place_obsidian", False)

    @property
    def pit_reach_level_100(self) -> bool:
        return getattr(self, "_pit_reach_level_100", False)

    @property
    def pit_small_streak(self) -> bool:
        return getattr(self, "_pit_small_streak", False)

    @property
    def pit_time_on_kotl(self) -> bool:
        return getattr(self, "_pit_time_on_kotl", False)

    @property
    def pit_top_three_in_event(self) -> bool:
        return getattr(self, "_pit_top_three_in_event", False)

    @property
    def pit_use_golden_heads(self) -> bool:
        return getattr(self, "_pit_use_golden_heads", False)

    @property
    def quake_baking_a_dozen(self) -> bool:
        return getattr(self, "_quake_baking_a_dozen", False)

    @property
    def quake_beyond_incredible(self) -> bool:
        return getattr(self, "_quake_beyond_incredible", False)

    @property
    def quake_bubbly(self) -> bool:
        return getattr(self, "_quake_bubbly", False)

    @property
    def quake_buffing_up(self) -> bool:
        return getattr(self, "_quake_buffing_up", False)

    @property
    def quake_diamonds_to_you(self) -> bool:
        return getattr(self, "_quake_diamonds_to_you", False)

    @property
    def quake_double_trouble(self) -> bool:
        return getattr(self, "_quake_double_trouble", False)

    @property
    def quake_doubling_up(self) -> bool:
        return getattr(self, "_quake_doubling_up", False)

    @property
    def quake_fabulous_win(self) -> bool:
        return getattr(self, "_quake_fabulous_win", False)

    @property
    def quake_fanatic(self) -> bool:
        return getattr(self, "_quake_fanatic", False)

    @property
    def quake_first_kill(self) -> bool:
        return getattr(self, "_quake_first_kill", False)

    @property
    def quake_fly(self) -> bool:
        return getattr(self, "_quake_fly", False)

    @property
    def quake_frog(self) -> bool:
        return getattr(self, "_quake_frog", False)

    @property
    def quake_going_up_in_life(self) -> bool:
        return getattr(self, "_quake_going_up_in_life", False)

    @property
    def quake_heart_stopper(self) -> bool:
        return getattr(self, "_quake_heart_stopper", False)

    @property
    def quake_heavy_shoulders(self) -> bool:
        return getattr(self, "_quake_heavy_shoulders", False)

    @property
    def quake_how_did_that_happen(self) -> bool:
        return getattr(self, "_quake_how_did_that_happen", False)

    @property
    def quake_humiliation(self) -> bool:
        return getattr(self, "_quake_humiliation", False)

    @property
    def quake_i_liek_turtles(self) -> bool:
        return getattr(self, "_quake_i_liek_turtles", False)

    @property
    def quake_in_my_way(self) -> bool:
        return getattr(self, "_quake_in_my_way", False)

    @property
    def quake_incredible(self) -> bool:
        return getattr(self, "_quake_incredible", False)

    @property
    def quake_its_so_shiny(self) -> bool:
        return getattr(self, "_quake_its_so_shiny", False)

    @property
    def quake_looking_fancy(self) -> bool:
        return getattr(self, "_quake_looking_fancy", False)

    @property
    def quake_love_is_in_the_air(self) -> bool:
        return getattr(self, "_quake_love_is_in_the_air", False)

    @property
    def quake_minigun(self) -> bool:
        return getattr(self, "_quake_minigun", False)

    @property
    def quake_my_precious(self) -> bool:
        return getattr(self, "_quake_my_precious", False)

    @property
    def quake_my_way(self) -> bool:
        return getattr(self, "_quake_my_way", False)

    @property
    def quake_not_today(self) -> bool:
        return getattr(self, "_quake_not_today", False)

    @property
    def quake_not_working(self) -> bool:
        return getattr(self, "_quake_not_working", False)

    @property
    def quake_oh_baby_a_triple(self) -> bool:
        return getattr(self, "_quake_oh_baby_a_triple", False)

    @property
    def quake_one_in_the_chamber(self) -> bool:
        return getattr(self, "_quake_one_in_the_chamber", False)

    @property
    def quake_one_shot(self) -> bool:
        return getattr(self, "_quake_one_shot", False)

    @property
    def quake_perfection(self) -> bool:
        return getattr(self, "_quake_perfection", False)

    @property
    def quake_perfectionnist(self) -> bool:
        return getattr(self, "_quake_perfectionnist", False)

    @property
    def quake_presidential(self) -> bool:
        return getattr(self, "_quake_presidential", False)

    @property
    def quake_redstoner(self) -> bool:
        return getattr(self, "_quake_redstoner", False)

    @property
    def quake_show_me_the_money(self) -> bool:
        return getattr(self, "_quake_show_me_the_money", False)

    @property
    def quake_simple_things(self) -> bool:
        return getattr(self, "_quake_simple_things", False)

    @property
    def quake_squish(self) -> bool:
        return getattr(self, "_quake_squish", False)

    @property
    def quake_think_fast(self) -> bool:
        return getattr(self, "_quake_think_fast", False)

    @property
    def quake_tubular(self) -> bool:
        return getattr(self, "_quake_tubular", False)

    @property
    def quake_untouchable(self) -> bool:
        return getattr(self, "_quake_untouchable", False)

    @property
    def quake_want_a_wardrobe(self) -> bool:
        return getattr(self, "_quake_want_a_wardrobe", False)

    @property
    def quake_what_have_i_done(self) -> bool:
        return getattr(self, "_quake_what_have_i_done", False)

    @property
    def quake_what_just_happened(self) -> bool:
        return getattr(self, "_quake_what_just_happened", False)

    @property
    def skyblock_agile(self) -> bool:
        return getattr(self, "_skyblock_agile", False)

    @property
    def skyblock_always_sunny_in_sb(self) -> bool:
        return getattr(self, "_skyblock_always_sunny_in_sb", False)

    @property
    def skyblock_arcadia(self) -> bool:
        return getattr(self, "_skyblock_arcadia", False)

    @property
    def skyblock_brain_power(self) -> bool:
        return getattr(self, "_skyblock_brain_power", False)

    @property
    def skyblock_empty_flower_pot(self) -> bool:
        return getattr(self, "_skyblock_empty_flower_pot", False)

    @property
    def skyblock_expensive_brew(self) -> bool:
        return getattr(self, "_skyblock_expensive_brew", False)

    @property
    def skyblock_fallen_star_cult(self) -> bool:
        return getattr(self, "_skyblock_fallen_star_cult", False)

    @property
    def skyblock_gottagofast(self) -> bool:
        return getattr(self, "_skyblock_gottagofast", False)

    @property
    def skyblock_i_am_groot(self) -> bool:
        return getattr(self, "_skyblock_i_am_groot", False)

    @property
    def skyblock_i_call_that_mercy(self) -> bool:
        return getattr(self, "_skyblock_i_call_that_mercy", False)

    @property
    def skyblock_infinite_darkness(self) -> bool:
        return getattr(self, "_skyblock_infinite_darkness", False)

    @property
    def skyblock_it_never_ends(self) -> bool:
        return getattr(self, "_skyblock_it_never_ends", False)

    @property
    def skyblock_jerry(self) -> bool:
        return getattr(self, "_skyblock_jerry", False)

    @property
    def skyblock_legendary_rod(self) -> bool:
        return getattr(self, "_skyblock_legendary_rod", False)

    @property
    def skyblock_lifelong_contract(self) -> bool:
        return getattr(self, "_skyblock_lifelong_contract", False)

    @property
    def skyblock_meal_fit_for_a_king(self) -> bool:
        return getattr(self, "_skyblock_meal_fit_for_a_king", False)

    @property
    def skyblock_no_enchants_needed(self) -> bool:
        return getattr(self, "_skyblock_no_enchants_needed", False)

    @property
    def skyblock_precious_minerals(self) -> bool:
        return getattr(self, "_skyblock_precious_minerals", False)

    @property
    def skyblock_saddle_up(self) -> bool:
        return getattr(self, "_skyblock_saddle_up", False)

    @property
    def skyblock_second_chance(self) -> bool:
        return getattr(self, "_skyblock_second_chance", False)

    @property
    def skyblock_seriously(self) -> bool:
        return getattr(self, "_skyblock_seriously", False)

    @property
    def skyblock_shrimp(self) -> bool:
        return getattr(self, "_skyblock_shrimp", False)

    @property
    def skyblock_speed_of_light(self) -> bool:
        return getattr(self, "_skyblock_speed_of_light", False)

    @property
    def skyblock_supreme_farmer(self) -> bool:
        return getattr(self, "_skyblock_supreme_farmer", False)

    @property
    def skyblock_this_is_fair(self) -> bool:
        return getattr(self, "_skyblock_this_is_fair", False)

    @property
    def skywars_ashes_to_ashes(self) -> bool:
        return getattr(self, "_skywars_ashes_to_ashes", False)

    @property
    def skywars_baller(self) -> bool:
        return getattr(self, "_skywars_baller", False)

    @property
    def skywars_challenge_archer(self) -> bool:
        return getattr(self, "_skywars_challenge_archer", False)

    @property
    def skywars_challenge_half_health(self) -> bool:
        return getattr(self, "_skywars_challenge_half_health", False)

    @property
    def skywars_challenge_master(self) -> bool:
        return getattr(self, "_skywars_challenge_master", False)

    @property
    def skywars_challenge_no_block(self) -> bool:
        return getattr(self, "_skywars_challenge_no_block", False)

    @property
    def skywars_challenge_no_chest(self) -> bool:
        return getattr(self, "_skywars_challenge_no_chest", False)

    @property
    def skywars_challenge_paper(self) -> bool:
        return getattr(self, "_skywars_challenge_paper", False)

    @property
    def skywars_challenge_pro(self) -> bool:
        return getattr(self, "_skywars_challenge_pro", False)

    @property
    def skywars_challenge_rookie(self) -> bool:
        return getattr(self, "_skywars_challenge_rookie", False)

    @property
    def skywars_challenge_uhc(self) -> bool:
        return getattr(self, "_skywars_challenge_uhc", False)

    @property
    def skywars_challenge_ultimate_warrior(self) -> bool:
        return getattr(self, "_skywars_challenge_ultimate_warrior", False)

    @property
    def skywars_corruption_lord(self) -> bool:
        return getattr(self, "_skywars_corruption_lord", False)

    @property
    def skywars_criminal(self) -> bool:
        return getattr(self, "_skywars_criminal", False)

    @property
    def skywars_donator(self) -> bool:
        return getattr(self, "_skywars_donator", False)

    @property
    def skywars_ender_party(self) -> bool:
        return getattr(self, "_skywars_ender_party", False)

    @property
    def skywars_enderdragon(self) -> bool:
        return getattr(self, "_skywars_enderdragon", False)

    @property
    def skywars_fear_me(self) -> bool:
        return getattr(self, "_skywars_fear_me", False)

    @property
    def skywars_going_ham(self) -> bool:
        return getattr(self, "_skywars_going_ham", False)

    @property
    def skywars_gone_fishing(self) -> bool:
        return getattr(self, "_skywars_gone_fishing", False)

    @property
    def skywars_kill_streak(self) -> bool:
        return getattr(self, "_skywars_kill_streak", False)

    @property
    def skywars_killstolen(self) -> bool:
        return getattr(self, "_skywars_killstolen", False)

    @property
    def skywars_lucky_charm(self) -> bool:
        return getattr(self, "_skywars_lucky_charm", False)

    @property
    def skywars_lucky_souls(self) -> bool:
        return getattr(self, "_skywars_lucky_souls", False)

    @property
    def skywars_max_perk(self) -> bool:
        return getattr(self, "_skywars_max_perk", False)

    @property
    def skywars_max_well(self) -> bool:
        return getattr(self, "_skywars_max_well", False)

    @property
    def skywars_mythical(self) -> bool:
        return getattr(self, "_skywars_mythical", False)

    @property
    def skywars_nick_cage(self) -> bool:
        return getattr(self, "_skywars_nick_cage", False)

    @property
    def skywars_now_im_enchanted(self) -> bool:
        return getattr(self, "_skywars_now_im_enchanted", False)

    @property
    def skywars_peacemaker(self) -> bool:
        return getattr(self, "_skywars_peacemaker", False)

    @property
    def skywars_portal_game(self) -> bool:
        return getattr(self, "_skywars_portal_game", False)

    @property
    def skywars_slow_steady(self) -> bool:
        return getattr(self, "_skywars_slow_steady", False)

    @property
    def skywars_sniper(self) -> bool:
        return getattr(self, "_skywars_sniper", False)

    @property
    def skywars_speed_run(self) -> bool:
        return getattr(self, "_skywars_speed_run", False)

    @property
    def skywars_speed_runner(self) -> bool:
        return getattr(self, "_skywars_speed_runner", False)

    @property
    def skywars_teamwork_makes_the_dream_work(self) -> bool:
        return getattr(self, "_skywars_teamwork_makes_the_dream_work", False)

    @property
    def skywars_trolol(self) -> bool:
        return getattr(self, "_skywars_trolol", False)

    @property
    def skywars_well_deserved(self) -> bool:
        return getattr(self, "_skywars_well_deserved", False)

    @property
    def skywars_who_needs_teammates(self) -> bool:
        return getattr(self, "_skywars_who_needs_teammates", False)

    @property
    def speeduhc_brave_new_world(self) -> bool:
        return getattr(self, "_speeduhc_brave_new_world", False)

    @property
    def speeduhc_domination(self) -> bool:
        return getattr(self, "_speeduhc_domination", False)

    @property
    def speeduhc_enchanted_armor(self) -> bool:
        return getattr(self, "_speeduhc_enchanted_armor", False)

    @property
    def speeduhc_god_apple(self) -> bool:
        return getattr(self, "_speeduhc_god_apple", False)

    @property
    def speeduhc_golden_apple(self) -> bool:
        return getattr(self, "_speeduhc_golden_apple", False)

    @property
    def speeduhc_hot_hog(self) -> bool:
        return getattr(self, "_speeduhc_hot_hog", False)

    @property
    def speeduhc_kill_ghast(self) -> bool:
        return getattr(self, "_speeduhc_kill_ghast", False)

    @property
    def speeduhc_kit_specialist(self) -> bool:
        return getattr(self, "_speeduhc_kit_specialist", False)

    @property
    def speeduhc_kit_unlock(self) -> bool:
        return getattr(self, "_speeduhc_kit_unlock", False)

    @property
    def speeduhc_melon_smasher(self) -> bool:
        return getattr(self, "_speeduhc_melon_smasher", False)

    @property
    def speeduhc_my_way(self) -> bool:
        return getattr(self, "_speeduhc_my_way", False)

    @property
    def speeduhc_potion_brewer(self) -> bool:
        return getattr(self, "_speeduhc_potion_brewer", False)

    @property
    def speeduhc_ride_pig(self) -> bool:
        return getattr(self, "_speeduhc_ride_pig", False)

    @property
    def speeduhc_rusher(self) -> bool:
        return getattr(self, "_speeduhc_rusher", False)

    @property
    def speeduhc_tears_of_loneliness(self) -> bool:
        return getattr(self, "_speeduhc_tears_of_loneliness", False)

    @property
    def summer_beat_the_heat(self) -> bool:
        return getattr(self, "_summer_beat_the_heat", False)

    @property
    def summer_collectors_edition(self) -> bool:
        return getattr(self, "_summer_collectors_edition", False)

    @property
    def summer_expert_diver(self) -> bool:
        return getattr(self, "_summer_expert_diver", False)

    @property
    def summer_grillmaster(self) -> bool:
        return getattr(self, "_summer_grillmaster", False)

    @property
    def summer_home_run(self) -> bool:
        return getattr(self, "_summer_home_run", False)

    @property
    def summer_kind_refreshment(self) -> bool:
        return getattr(self, "_summer_kind_refreshment", False)

    @property
    def summer_lightning_rod(self) -> bool:
        return getattr(self, "_summer_lightning_rod", False)

    @property
    def summer_ocean_in_a_bucket(self) -> bool:
        return getattr(self, "_summer_ocean_in_a_bucket", False)

    @property
    def summer_out_fishing(self) -> bool:
        return getattr(self, "_summer_out_fishing", False)

    @property
    def summer_over_heated(self) -> bool:
        return getattr(self, "_summer_over_heated", False)

    @property
    def summer_pool_party(self) -> bool:
        return getattr(self, "_summer_pool_party", False)

    @property
    def summer_punch_out(self) -> bool:
        return getattr(self, "_summer_punch_out", False)

    @property
    def summer_relaxing_bingo(self) -> bool:
        return getattr(self, "_summer_relaxing_bingo", False)

    @property
    def summer_roasted(self) -> bool:
        return getattr(self, "_summer_roasted", False)

    @property
    def summer_rule_the_heat(self) -> bool:
        return getattr(self, "_summer_rule_the_heat", False)

    @property
    def summer_shockwave(self) -> bool:
        return getattr(self, "_summer_shockwave", False)

    @property
    def summer_small_sea_sailor(self) -> bool:
        return getattr(self, "_summer_small_sea_sailor", False)

    @property
    def summer_stay_hydrated(self) -> bool:
        return getattr(self, "_summer_stay_hydrated", False)

    @property
    def summer_sun_denial(self) -> bool:
        return getattr(self, "_summer_sun_denial", False)

    @property
    def summer_this_isnt_the_lobby(self) -> bool:
        return getattr(self, "_summer_this_isnt_the_lobby", False)

    @property
    def summer_win_pink_sheep(self) -> bool:
        return getattr(self, "_summer_win_pink_sheep", False)

    @property
    def summer_wrong_season(self) -> bool:
        return getattr(self, "_summer_wrong_season", False)

    @property
    def supersmash_botmon_vs_spooderman(self) -> bool:
        return getattr(self, "_supersmash_botmon_vs_spooderman", False)

    @property
    def supersmash_cake_challenge(self) -> bool:
        return getattr(self, "_supersmash_cake_challenge", False)

    @property
    def supersmash_domination(self) -> bool:
        return getattr(self, "_supersmash_domination", False)

    @property
    def supersmash_experience_express(self) -> bool:
        return getattr(self, "_supersmash_experience_express", False)

    @property
    def supersmash_get_over_here(self) -> bool:
        return getattr(self, "_supersmash_get_over_here", False)

    @property
    def supersmash_need_all(self) -> bool:
        return getattr(self, "_supersmash_need_all", False)

    @property
    def supersmash_second_round(self) -> bool:
        return getattr(self, "_supersmash_second_round", False)

    @property
    def supersmash_supremacy(self) -> bool:
        return getattr(self, "_supersmash_supremacy", False)

    @property
    def supersmash_too_easy(self) -> bool:
        return getattr(self, "_supersmash_too_easy", False)

    @property
    def supersmash_two_for_one(self) -> bool:
        return getattr(self, "_supersmash_two_for_one", False)

    @property
    def tntgames_beyond_expectations(self) -> bool:
        return getattr(self, "_tntgames_beyond_expectations", False)

    @property
    def tntgames_bow_spleef_double_jump_upgrade(self) -> bool:
        return getattr(self, "_tntgames_bow_spleef_double_jump_upgrade", False)

    @property
    def tntgames_bow_spleef_first_double_jump(self) -> bool:
        return getattr(self, "_tntgames_bow_spleef_first_double_jump", False)

    @property
    def tntgames_bow_spleef_first_win(self) -> bool:
        return getattr(self, "_tntgames_bow_spleef_first_win", False)

    @property
    def tntgames_bow_spleef_repulsor_upgrade(self) -> bool:
        return getattr(self, "_tntgames_bow_spleef_repulsor_upgrade", False)

    @property
    def tntgames_bow_spleef_triple_shot_upgrade(self) -> bool:
        return getattr(self, "_tntgames_bow_spleef_triple_shot_upgrade", False)

    @property
    def tntgames_bye_bye(self) -> bool:
        return getattr(self, "_tntgames_bye_bye", False)

    @property
    def tntgames_cant_stop_wont_stop(self) -> bool:
        return getattr(self, "_tntgames_cant_stop_wont_stop", False)

    @property
    def tntgames_dont_get_close(self) -> bool:
        return getattr(self, "_tntgames_dont_get_close", False)

    @property
    def tntgames_extrme_speed(self) -> bool:
        return getattr(self, "_tntgames_extrme_speed", False)

    @property
    def tntgames_flying_madman(self) -> bool:
        return getattr(self, "_tntgames_flying_madman", False)

    @property
    def tntgames_free_points(self) -> bool:
        return getattr(self, "_tntgames_free_points", False)

    @property
    def tntgames_freeze(self) -> bool:
        return getattr(self, "_tntgames_freeze", False)

    @property
    def tntgames_healer(self) -> bool:
        return getattr(self, "_tntgames_healer", False)

    @property
    def tntgames_hole_in_my_pocket(self) -> bool:
        return getattr(self, "_tntgames_hole_in_my_pocket", False)

    @property
    def tntgames_lucky(self) -> bool:
        return getattr(self, "_tntgames_lucky", False)

    @property
    def tntgames_mega_tank(self) -> bool:
        return getattr(self, "_tntgames_mega_tank", False)

    @property
    def tntgames_no_you(self) -> bool:
        return getattr(self, "_tntgames_no_you", False)

    @property
    def tntgames_overpowered_archery(self) -> bool:
        return getattr(self, "_tntgames_overpowered_archery", False)

    @property
    def tntgames_potion_shower(self) -> bool:
        return getattr(self, "_tntgames_potion_shower", False)

    @property
    def tntgames_pro_surfer(self) -> bool:
        return getattr(self, "_tntgames_pro_surfer", False)

    @property
    def tntgames_pvp_run_first_win(self) -> bool:
        return getattr(self, "_tntgames_pvp_run_first_win", False)

    @property
    def tntgames_pvp_run_flying(self) -> bool:
        return getattr(self, "_tntgames_pvp_run_flying", False)

    @property
    def tntgames_pvp_run_potions(self) -> bool:
        return getattr(self, "_tntgames_pvp_run_potions", False)

    @property
    def tntgames_pvp_run_sabotage(self) -> bool:
        return getattr(self, "_tntgames_pvp_run_sabotage", False)

    @property
    def tntgames_quarantine(self) -> bool:
        return getattr(self, "_tntgames_quarantine", False)

    @property
    def tntgames_run_potions(self) -> bool:
        return getattr(self, "_tntgames_run_potions", False)

    @property
    def tntgames_second_chance(self) -> bool:
        return getattr(self, "_tntgames_second_chance", False)

    @property
    def tntgames_sniper(self) -> bool:
        return getattr(self, "_tntgames_sniper", False)

    @property
    def tntgames_spleef_exhausted(self) -> bool:
        return getattr(self, "_tntgames_spleef_exhausted", False)

    @property
    def tntgames_spleef_hits(self) -> bool:
        return getattr(self, "_tntgames_spleef_hits", False)

    @property
    def tntgames_spleef_noperks(self) -> bool:
        return getattr(self, "_tntgames_spleef_noperks", False)

    @property
    def tntgames_spleef_repulsor(self) -> bool:
        return getattr(self, "_tntgames_spleef_repulsor", False)

    @property
    def tntgames_spleef_shots(self) -> bool:
        return getattr(self, "_tntgames_spleef_shots", False)

    @property
    def tntgames_spleef_triple(self) -> bool:
        return getattr(self, "_tntgames_spleef_triple", False)

    @property
    def tntgames_spooky(self) -> bool:
        return getattr(self, "_tntgames_spooky", False)

    @property
    def tntgames_that_was_close(self) -> bool:
        return getattr(self, "_tntgames_that_was_close", False)

    @property
    def tntgames_timer(self) -> bool:
        return getattr(self, "_tntgames_timer", False)

    @property
    def tntgames_tnt_npcs(self) -> bool:
        return getattr(self, "_tntgames_tnt_npcs", False)

    @property
    def tntgames_tnt_parkour(self) -> bool:
        return getattr(self, "_tntgames_tnt_parkour", False)

    @property
    def tntgames_tnt_run_effects(self) -> bool:
        return getattr(self, "_tntgames_tnt_run_effects", False)

    @property
    def tntgames_tnt_run_first_win(self) -> bool:
        return getattr(self, "_tntgames_tnt_run_first_win", False)

    @property
    def tntgames_tnt_run_firstlayer(self) -> bool:
        return getattr(self, "_tntgames_tnt_run_firstlayer", False)

    @property
    def tntgames_tnt_run_flying(self) -> bool:
        return getattr(self, "_tntgames_tnt_run_flying", False)

    @property
    def tntgames_tnt_run_no_sprinting(self) -> bool:
        return getattr(self, "_tntgames_tnt_run_no_sprinting", False)

    @property
    def tntgames_tnt_run_nodjs(self) -> bool:
        return getattr(self, "_tntgames_tnt_run_nodjs", False)

    @property
    def tntgames_tnt_run_purchase_potion(self) -> bool:
        return getattr(self, "_tntgames_tnt_run_purchase_potion", False)

    @property
    def tntgames_tnt_run_short(self) -> bool:
        return getattr(self, "_tntgames_tnt_run_short", False)

    @property
    def tntgames_tnt_tag_aww(self) -> bool:
        return getattr(self, "_tntgames_tnt_tag_aww", False)

    @property
    def tntgames_tnt_tag_blownup(self) -> bool:
        return getattr(self, "_tntgames_tnt_tag_blownup", False)

    @property
    def tntgames_tnt_tag_close(self) -> bool:
        return getattr(self, "_tntgames_tnt_tag_close", False)

    @property
    def tntgames_tnt_tag_differenttags(self) -> bool:
        return getattr(self, "_tntgames_tnt_tag_differenttags", False)

    @property
    def tntgames_tnt_tag_dm(self) -> bool:
        return getattr(self, "_tntgames_tnt_tag_dm", False)

    @property
    def tntgames_tnt_tag_first_win(self) -> bool:
        return getattr(self, "_tntgames_tnt_tag_first_win", False)

    @property
    def tntgames_tnt_tag_snowball(self) -> bool:
        return getattr(self, "_tntgames_tnt_tag_snowball", False)

    @property
    def tntgames_tnt_tag_tagger(self) -> bool:
        return getattr(self, "_tntgames_tnt_tag_tagger", False)

    @property
    def tntgames_tnt_tag_traveller(self) -> bool:
        return getattr(self, "_tntgames_tnt_tag_traveller", False)

    @property
    def tntgames_tnt_wins_in_a_row(self) -> bool:
        return getattr(self, "_tntgames_tnt_wins_in_a_row", False)

    @property
    def tntgames_wizards_blood_wizard_regen(self) -> bool:
        return getattr(self, "_tntgames_wizards_blood_wizard_regen", False)

    @property
    def tntgames_wizards_caphelp(self) -> bool:
        return getattr(self, "_tntgames_wizards_caphelp", False)

    @property
    def tntgames_wizards_fire_wizard_explode(self) -> bool:
        return getattr(self, "_tntgames_wizards_fire_wizard_explode", False)

    @property
    def tntgames_wizards_first_win(self) -> bool:
        return getattr(self, "_tntgames_wizards_first_win", False)

    @property
    def tntgames_wizards_hurts(self) -> bool:
        return getattr(self, "_tntgames_wizards_hurts", False)

    @property
    def tntgames_wizards_jumper(self) -> bool:
        return getattr(self, "_tntgames_wizards_jumper", False)

    @property
    def tntgames_wizards_lead(self) -> bool:
        return getattr(self, "_tntgames_wizards_lead", False)

    @property
    def tntgames_wizards_leaderboard(self) -> bool:
        return getattr(self, "_tntgames_wizards_leaderboard", False)

    @property
    def tntgames_wizards_nogood(self) -> bool:
        return getattr(self, "_tntgames_wizards_nogood", False)

    @property
    def tntgames_wizards_triple(self) -> bool:
        return getattr(self, "_tntgames_wizards_triple", False)

    @property
    def truecombat_deadly_donation(self) -> bool:
        return getattr(self, "_truecombat_deadly_donation", False)

    @property
    def truecombat_dominating(self) -> bool:
        return getattr(self, "_truecombat_dominating", False)

    @property
    def truecombat_golden_bounty(self) -> bool:
        return getattr(self, "_truecombat_golden_bounty", False)

    @property
    def uhc_ace_kit(self) -> bool:
        return getattr(self, "_uhc_ace_kit", False)

    @property
    def uhc_adrenaline(self) -> bool:
        return getattr(self, "_uhc_adrenaline", False)

    @property
    def uhc_bye_cruel_world(self) -> bool:
        return getattr(self, "_uhc_bye_cruel_world", False)

    @property
    def uhc_chest_of_fate(self) -> bool:
        return getattr(self, "_uhc_chest_of_fate", False)

    @property
    def uhc_crafting_revolution(self) -> bool:
        return getattr(self, "_uhc_crafting_revolution", False)

    @property
    def uhc_dice_of_god(self) -> bool:
        return getattr(self, "_uhc_dice_of_god", False)

    @property
    def uhc_dong(self) -> bool:
        return getattr(self, "_uhc_dong", False)

    @property
    def uhc_drink_with_caution(self) -> bool:
        return getattr(self, "_uhc_drink_with_caution", False)

    @property
    def uhc_eldorado(self) -> bool:
        return getattr(self, "_uhc_eldorado", False)

    @property
    def uhc_elite_prestige(self) -> bool:
        return getattr(self, "_uhc_elite_prestige", False)

    @property
    def uhc_enderkind(self) -> bool:
        return getattr(self, "_uhc_enderkind", False)

    @property
    def uhc_extra_powerful(self) -> bool:
        return getattr(self, "_uhc_extra_powerful", False)

    @property
    def uhc_ghast(self) -> bool:
        return getattr(self, "_uhc_ghast", False)

    @property
    def uhc_ghost_rider(self) -> bool:
        return getattr(self, "_uhc_ghost_rider", False)

    @property
    def uhc_kit_mastery(self) -> bool:
        return getattr(self, "_uhc_kit_mastery", False)

    @property
    def uhc_no_problem_here(self) -> bool:
        return getattr(self, "_uhc_no_problem_here", False)

    @property
    def uhc_parkour_master(self) -> bool:
        return getattr(self, "_uhc_parkour_master", False)

    @property
    def uhc_prestigious(self) -> bool:
        return getattr(self, "_uhc_prestigious", False)

    @property
    def uhc_production_ender(self) -> bool:
        return getattr(self, "_uhc_production_ender", False)

    @property
    def uhc_puppy(self) -> bool:
        return getattr(self, "_uhc_puppy", False)

    @property
    def uhc_ride_a_horse(self) -> bool:
        return getattr(self, "_uhc_ride_a_horse", False)

    @property
    def uhc_seafood(self) -> bool:
        return getattr(self, "_uhc_seafood", False)

    @property
    def uhc_shiny_rock(self) -> bool:
        return getattr(self, "_uhc_shiny_rock", False)

    @property
    def uhc_ultimate_crafting(self) -> bool:
        return getattr(self, "_uhc_ultimate_crafting", False)

    @property
    def uhc_ultimate_recipe(self) -> bool:
        return getattr(self, "_uhc_ultimate_recipe", False)

    @property
    def uhc_ultimately_wealthy(self) -> bool:
        return getattr(self, "_uhc_ultimately_wealthy", False)

    @property
    def uhc_warming_up(self) -> bool:
        return getattr(self, "_uhc_warming_up", False)

    @property
    def uhc_wealthy_champion(self) -> bool:
        return getattr(self, "_uhc_wealthy_champion", False)

    @property
    def vampirez_blood(self) -> bool:
        return getattr(self, "_vampirez_blood", False)

    @property
    def vampirez_blood_thirsty(self) -> bool:
        return getattr(self, "_vampirez_blood_thirsty", False)

    @property
    def vampirez_close_call(self) -> bool:
        return getattr(self, "_vampirez_close_call", False)

    @property
    def vampirez_first_wave_kill(self) -> bool:
        return getattr(self, "_vampirez_first_wave_kill", False)

    @property
    def vampirez_gold(self) -> bool:
        return getattr(self, "_vampirez_gold", False)

    @property
    def vampirez_kill_zombies(self) -> bool:
        return getattr(self, "_vampirez_kill_zombies", False)

    @property
    def vampirez_last_chance(self) -> bool:
        return getattr(self, "_vampirez_last_chance", False)

    @property
    def vampirez_nightmare(self) -> bool:
        return getattr(self, "_vampirez_nightmare", False)

    @property
    def vampirez_pest(self) -> bool:
        return getattr(self, "_vampirez_pest", False)

    @property
    def vampirez_potions(self) -> bool:
        return getattr(self, "_vampirez_potions", False)

    @property
    def vampirez_purchase_armor(self) -> bool:
        return getattr(self, "_vampirez_purchase_armor", False)

    @property
    def vampirez_purchase_blood(self) -> bool:
        return getattr(self, "_vampirez_purchase_blood", False)

    @property
    def vampirez_purchase_food(self) -> bool:
        return getattr(self, "_vampirez_purchase_food", False)

    @property
    def vampirez_purchase_gold(self) -> bool:
        return getattr(self, "_vampirez_purchase_gold", False)

    @property
    def vampirez_purchase_sword(self) -> bool:
        return getattr(self, "_vampirez_purchase_sword", False)

    @property
    def vampirez_purified(self) -> bool:
        return getattr(self, "_vampirez_purified", False)

    @property
    def vampirez_robbed(self) -> bool:
        return getattr(self, "_vampirez_robbed", False)

    @property
    def vampirez_sole_survivor(self) -> bool:
        return getattr(self, "_vampirez_sole_survivor", False)

    @property
    def vampirez_survivor_kills_one_round(self) -> bool:
        return getattr(self, "_vampirez_survivor_kills_one_round", False)

    @property
    def vampirez_tastes_funny(self) -> bool:
        return getattr(self, "_vampirez_tastes_funny", False)

    @property
    def vampirez_undefeatable(self) -> bool:
        return getattr(self, "_vampirez_undefeatable", False)

    @property
    def vampirez_upgraded(self) -> bool:
        return getattr(self, "_vampirez_upgraded", False)

    @property
    def vampirez_vampire_fang_kill(self) -> bool:
        return getattr(self, "_vampirez_vampire_fang_kill", False)

    @property
    def vampirez_vampire_kills_one_round(self) -> bool:
        return getattr(self, "_vampirez_vampire_kills_one_round", False)

    @property
    def vampirez_word_puns(self) -> bool:
        return getattr(self, "_vampirez_word_puns", False)

    @property
    def vampirez_zombie_slayer(self) -> bool:
        return getattr(self, "_vampirez_zombie_slayer", False)

    @property
    def vampirez_zombie_whisperer(self) -> bool:
        return getattr(self, "_vampirez_zombie_whisperer", False)

    @property
    def walls3_at_least_he_tried(self) -> bool:
        return getattr(self, "_walls3_at_least_he_tried", False)

    @property
    def walls3_attack_wither(self) -> bool:
        return getattr(self, "_walls3_attack_wither", False)

    @property
    def walls3_first_gathering_skill_upgrade(self) -> bool:
        return getattr(self, "_walls3_first_gathering_skill_upgrade", False)

    @property
    def walls3_first_skill_upgrade(self) -> bool:
        return getattr(self, "_walls3_first_skill_upgrade", False)

    @property
    def walls3_happy(self) -> bool:
        return getattr(self, "_walls3_happy", False)

    @property
    def walls3_max_skills(self) -> bool:
        return getattr(self, "_walls3_max_skills", False)

    @property
    def walls3_save_your_stuff(self) -> bool:
        return getattr(self, "_walls3_save_your_stuff", False)

    @property
    def walls3_this_is_my_final_form(self) -> bool:
        return getattr(self, "_walls3_this_is_my_final_form", False)

    @property
    def walls3_to_infinity(self) -> bool:
        return getattr(self, "_walls3_to_infinity", False)

    @property
    def walls3_win_before_deathmatch(self) -> bool:
        return getattr(self, "_walls3_win_before_deathmatch", False)

    @property
    def walls3_win_with_living_wither(self) -> bool:
        return getattr(self, "_walls3_win_with_living_wither", False)

    @property
    def walls_berserk(self) -> bool:
        return getattr(self, "_walls_berserk", False)

    @property
    def walls_burning(self) -> bool:
        return getattr(self, "_walls_burning", False)

    @property
    def walls_catch_fish(self) -> bool:
        return getattr(self, "_walls_catch_fish", False)

    @property
    def walls_craft_boat(self) -> bool:
        return getattr(self, "_walls_craft_boat", False)

    @property
    def walls_craft_flint(self) -> bool:
        return getattr(self, "_walls_craft_flint", False)

    @property
    def walls_create_portal(self) -> bool:
        return getattr(self, "_walls_create_portal", False)

    @property
    def walls_customized(self) -> bool:
        return getattr(self, "_walls_customized", False)

    @property
    def walls_engineer(self) -> bool:
        return getattr(self, "_walls_engineer", False)

    @property
    def walls_finding_nemo(self) -> bool:
        return getattr(self, "_walls_finding_nemo", False)

    @property
    def walls_first_kit(self) -> bool:
        return getattr(self, "_walls_first_kit", False)

    @property
    def walls_first_perk(self) -> bool:
        return getattr(self, "_walls_first_perk", False)

    @property
    def walls_get_diamond_sword(self) -> bool:
        return getattr(self, "_walls_get_diamond_sword", False)

    @property
    def walls_kill_cliff(self) -> bool:
        return getattr(self, "_walls_kill_cliff", False)

    @property
    def walls_no_team_deaths(self) -> bool:
        return getattr(self, "_walls_no_team_deaths", False)

    @property
    def walls_not_a_fish(self) -> bool:
        return getattr(self, "_walls_not_a_fish", False)

    @property
    def walls_not_today(self) -> bool:
        return getattr(self, "_walls_not_today", False)

    @property
    def walls_record_label(self) -> bool:
        return getattr(self, "_walls_record_label", False)

    @property
    def walls_revenge(self) -> bool:
        return getattr(self, "_walls_revenge", False)

    @property
    def walls_ride_horse(self) -> bool:
        return getattr(self, "_walls_ride_horse", False)

    @property
    def walls_robin_hood(self) -> bool:
        return getattr(self, "_walls_robin_hood", False)

    @property
    def walls_sole_survivor(self) -> bool:
        return getattr(self, "_walls_sole_survivor", False)

    @property
    def walls_starter_kits(self) -> bool:
        return getattr(self, "_walls_starter_kits", False)

    @property
    def walls_ten_kills(self) -> bool:
        return getattr(self, "_walls_ten_kills", False)

    @property
    def walls_true_power(self) -> bool:
        return getattr(self, "_walls_true_power", False)

    @property
    def walls_untouchable(self) -> bool:
        return getattr(self, "_walls_untouchable", False)

    @property
    def walls_vampirism(self) -> bool:
        return getattr(self, "_walls_vampirism", False)

    @property
    def walls_wiped_out(self) -> bool:
        return getattr(self, "_walls_wiped_out", False)

    @property
    def warlords_avengers_wrath(self) -> bool:
        return getattr(self, "_warlords_avengers_wrath", False)

    @property
    def warlords_chain_kill(self) -> bool:
        return getattr(self, "_warlords_chain_kill", False)

    @property
    def warlords_coming_through(self) -> bool:
        return getattr(self, "_warlords_coming_through", False)

    @property
    def warlords_eagle_eyed(self) -> bool:
        return getattr(self, "_warlords_eagle_eyed", False)

    @property
    def warlords_feeling_special(self) -> bool:
        return getattr(self, "_warlords_feeling_special", False)

    @property
    def warlords_first_of_many(self) -> bool:
        return getattr(self, "_warlords_first_of_many", False)

    @property
    def warlords_giddy_up(self) -> bool:
        return getattr(self, "_warlords_giddy_up", False)

    @property
    def warlords_i_have_to_concentrate(self) -> bool:
        return getattr(self, "_warlords_i_have_to_concentrate", False)

    @property
    def warlords_i_must_resist(self) -> bool:
        return getattr(self, "_warlords_i_must_resist", False)

    @property
    def warlords_juiced_up(self) -> bool:
        return getattr(self, "_warlords_juiced_up", False)

    @property
    def warlords_legendary(self) -> bool:
        return getattr(self, "_warlords_legendary", False)

    @property
    def warlords_makin_some_room(self) -> bool:
        return getattr(self, "_warlords_makin_some_room", False)

    @property
    def warlords_medium_rare(self) -> bool:
        return getattr(self, "_warlords_medium_rare", False)

    @property
    def warlords_my_pleasure(self) -> bool:
        return getattr(self, "_warlords_my_pleasure", False)

    @property
    def warlords_on_top(self) -> bool:
        return getattr(self, "_warlords_on_top", False)

    @property
    def warlords_power_up(self) -> bool:
        return getattr(self, "_warlords_power_up", False)

    @property
    def warlords_purple_power(self) -> bool:
        return getattr(self, "_warlords_purple_power", False)

    @property
    def warlords_right_on_time(self) -> bool:
        return getattr(self, "_warlords_right_on_time", False)

    @property
    def warlords_super_soaker(self) -> bool:
        return getattr(self, "_warlords_super_soaker", False)

    @property
    def warlords_that_was_easy(self) -> bool:
        return getattr(self, "_warlords_that_was_easy", False)

    @property
    def woolgames_ace(self) -> bool:
        return getattr(self, "_woolgames_ace", False)

    @property
    def woolgames_all_aboard(self) -> bool:
        return getattr(self, "_woolgames_all_aboard", False)

    @property
    def woolgames_chromatic(self) -> bool:
        return getattr(self, "_woolgames_chromatic", False)

    @property
    def woolgames_comeback(self) -> bool:
        return getattr(self, "_woolgames_comeback", False)

    @property
    def woolgames_enderman(self) -> bool:
        return getattr(self, "_woolgames_enderman", False)

    @property
    def woolgames_fashionably_late(self) -> bool:
        return getattr(self, "_woolgames_fashionably_late", False)

    @property
    def woolgames_first(self) -> bool:
        return getattr(self, "_woolgames_first", False)

    @property
    def woolgames_first_blood(self) -> bool:
        return getattr(self, "_woolgames_first_blood", False)

    @property
    def woolgames_hey_there(self) -> bool:
        return getattr(self, "_woolgames_hey_there", False)

    @property
    def woolgames_i_can_be_anything(self) -> bool:
        return getattr(self, "_woolgames_i_can_be_anything", False)

    @property
    def woolgames_its_dark_down_there(self) -> bool:
        return getattr(self, "_woolgames_its_dark_down_there", False)

    @property
    def woolgames_keystone(self) -> bool:
        return getattr(self, "_woolgames_keystone", False)

    @property
    def woolgames_merciless(self) -> bool:
        return getattr(self, "_woolgames_merciless", False)

    @property
    def woolgames_mvp(self) -> bool:
        return getattr(self, "_woolgames_mvp", False)

    @property
    def woolgames_ninja(self) -> bool:
        return getattr(self, "_woolgames_ninja", False)

    @property
    def woolgames_no_need_bro(self) -> bool:
        return getattr(self, "_woolgames_no_need_bro", False)

    @property
    def woolgames_resilient(self) -> bool:
        return getattr(self, "_woolgames_resilient", False)

    @property
    def woolgames_right_place_right_time(self) -> bool:
        return getattr(self, "_woolgames_right_place_right_time", False)

    @property
    def woolgames_safety_is_an_illusion(self) -> bool:
        return getattr(self, "_woolgames_safety_is_an_illusion", False)

    @property
    def woolgames_stock_pile(self) -> bool:
        return getattr(self, "_woolgames_stock_pile", False)

    @property
    def woolgames_survivor(self) -> bool:
        return getattr(self, "_woolgames_survivor", False)

    @property
    def woolgames_the_best_offense(self) -> bool:
        return getattr(self, "_woolgames_the_best_offense", False)

    @property
    def woolgames_top_killer(self) -> bool:
        return getattr(self, "_woolgames_top_killer", False)

    @property
    def woolgames_true_leader(self) -> bool:
        return getattr(self, "_woolgames_true_leader", False)

    @property
    def arcade_ctw_comeback(self) -> bool:
        return getattr(self, "_arcade_ctw_comeback", False)

    @property
    def arcade_ctw_first(self) -> bool:
        return getattr(self, "_arcade_ctw_first", False)

    @property
    def arcade_ctw_hey_there(self) -> bool:
        return getattr(self, "_arcade_ctw_hey_there", False)

    @property
    def arcade_ctw_i_can_be_anything(self) -> bool:
        return getattr(self, "_arcade_ctw_i_can_be_anything", False)

    @property
    def arcade_ctw_no_need(self) -> bool:
        return getattr(self, "_arcade_ctw_no_need", False)

    @property
    def arcade_ctw_safety_is_an_illusion(self) -> bool:
        return getattr(self, "_arcade_ctw_safety_is_an_illusion", False)

    @property
    def arcade_dropper_speedfaller(self) -> bool:
        return getattr(self, "_arcade_dropper_speedfaller", False)

    @property
    def arcade_galaxy_wars_aimed(self) -> bool:
        return getattr(self, "_arcade_galaxy_wars_aimed", False)

    @property
    def arcade_hide_and_seek_close_call(self) -> bool:
        return getattr(self, "_arcade_hide_and_seek_close_call", False)

    @property
    def arcade_hypixel_says_movement(self) -> bool:
        return getattr(self, "_arcade_hypixel_says_movement", False)

    @property
    def arcade_party_fast_hands(self) -> bool:
        return getattr(self, "_arcade_party_fast_hands", False)

    @property
    def arcade_party_perfection(self) -> bool:
        return getattr(self, "_arcade_party_perfection", False)

    @property
    def arcade_party_picasso(self) -> bool:
        return getattr(self, "_arcade_party_picasso", False)

    @property
    def arcade_party_survivor(self) -> bool:
        return getattr(self, "_arcade_party_survivor", False)

    @property
    def arcade_pixel_party_expert_dancer(self) -> bool:
        return getattr(self, "_arcade_pixel_party_expert_dancer", False)

    @property
    def arcade_ptb_ride_bat(self) -> bool:
        return getattr(self, "_arcade_ptb_ride_bat", False)

    @property
    def arcade_shooting_range_explosive_arrow(self) -> bool:
        return getattr(self, "_arcade_shooting_range_explosive_arrow", False)

    @property
    def arcade_zombies_prison_escape(self) -> bool:
        return getattr(self, "_arcade_zombies_prison_escape", False)

    @property
    def arcade_zombies_prison_secret_beyond(self) -> bool:
        return getattr(self, "_arcade_zombies_prison_secret_beyond", False)

    @property
    def blitz_invincible(self) -> bool:
        return getattr(self, "_blitz_invincible", False)

    @property
    def blitz_under_the_sea(self) -> bool:
        return getattr(self, "_blitz_under_the_sea", False)

    @property
    def bridge_carried(self) -> bool:
        return getattr(self, "_bridge_carried", False)

    @property
    def bridge_clean_sweep(self) -> bool:
        return getattr(self, "_bridge_clean_sweep", False)

    @property
    def bridge_heart_hoarder(self) -> bool:
        return getattr(self, "_bridge_heart_hoarder", False)

    @property
    def bridge_jumping_to_conclusions(self) -> bool:
        return getattr(self, "_bridge_jumping_to_conclusions", False)

    @property
    def bridge_last_stand(self) -> bool:
        return getattr(self, "_bridge_last_stand", False)

    @property
    def bridge_one_v_one_me(self) -> bool:
        return getattr(self, "_bridge_one_v_one_me", False)

    @property
    def buildbattle_classic_man(self) -> bool:
        return getattr(self, "_buildbattle_classic_man", False)

    @property
    def buildbattle_fast_typer(self) -> bool:
        return getattr(self, "_buildbattle_fast_typer", False)

    @property
    def buildbattle_perfect_harmony(self) -> bool:
        return getattr(self, "_buildbattle_perfect_harmony", False)

    @property
    def buildbattle_perfectception(self) -> bool:
        return getattr(self, "_buildbattle_perfectception", False)

    @property
    def buildbattle_pro_winner(self) -> bool:
        return getattr(self, "_buildbattle_pro_winner", False)

    @property
    def buildbattle_the_hat_master(self) -> bool:
        return getattr(self, "_buildbattle_the_hat_master", False)

    @property
    def christmas2017_sharing_is_caring(self) -> bool:
        return getattr(self, "_christmas2017_sharing_is_caring", False)

    @property
    def christmas2017_slice_and_ice(self) -> bool:
        return getattr(self, "_christmas2017_slice_and_ice", False)

    @property
    def christmas2017_snowball_sniper(self) -> bool:
        return getattr(self, "_christmas2017_snowball_sniper", False)

    @property
    def christmas2017_very_merry_bingo(self) -> bool:
        return getattr(self, "_christmas2017_very_merry_bingo", False)

    @property
    def copsandcrims_oh_baby_a_triple(self) -> bool:
        return getattr(self, "_copsandcrims_oh_baby_a_triple", False)

    @property
    def duels_arena_master(self) -> bool:
        return getattr(self, "_duels_arena_master", False)

    @property
    def duels_silent_thief(self) -> bool:
        return getattr(self, "_duels_silent_thief", False)

    @property
    def duels_smash_your_keyboard(self) -> bool:
        return getattr(self, "_duels_smash_your_keyboard", False)

    @property
    def duels_we_are_number_one(self) -> bool:
        return getattr(self, "_duels_we_are_number_one", False)

    @property
    def easter_all_eggs_2019(self) -> bool:
        return getattr(self, "_easter_all_eggs_2019", False)

    @property
    def easter_arcade_chicken_race(self) -> bool:
        return getattr(self, "_easter_arcade_chicken_race", False)

    @property
    def easter_egg_master(self) -> bool:
        return getattr(self, "_easter_egg_master", False)

    @property
    def easter_springy_bingo(self) -> bool:
        return getattr(self, "_easter_springy_bingo", False)

    @property
    def easter_what_have_we_done(self) -> bool:
        return getattr(self, "_easter_what_have_we_done", False)

    @property
    def easter_what_is_this(self) -> bool:
        return getattr(self, "_easter_what_is_this", False)

    @property
    def general_hypixel_historian(self) -> bool:
        return getattr(self, "_general_hypixel_historian", False)

    @property
    def gingerbread_coin_magnet(self) -> bool:
        return getattr(self, "_gingerbread_coin_magnet", False)

    @property
    def gingerbread_contender(self) -> bool:
        return getattr(self, "_gingerbread_contender", False)

    @property
    def gingerbread_seasonal_racer(self) -> bool:
        return getattr(self, "_gingerbread_seasonal_racer", False)

    @property
    def gingerbread_seen_it_all(self) -> bool:
        return getattr(self, "_gingerbread_seen_it_all", False)

    @property
    def gingerbread_show_off(self) -> bool:
        return getattr(self, "_gingerbread_show_off", False)

    @property
    def gingerbread_slippery(self) -> bool:
        return getattr(self, "_gingerbread_slippery", False)

    @property
    def gingerbread_ungrateful(self) -> bool:
        return getattr(self, "_gingerbread_ungrateful", False)

    @property
    def halloween2017_all_ghosts_2018(self) -> bool:
        return getattr(self, "_halloween2017_all_ghosts_2018", False)

    @property
    def halloween2017_bewitching(self) -> bool:
        return getattr(self, "_halloween2017_bewitching", False)

    @property
    def halloween2017_not_so_scary(self) -> bool:
        return getattr(self, "_halloween2017_not_so_scary", False)

    @property
    def halloween2017_sweet_treat(self) -> bool:
        return getattr(self, "_halloween2017_sweet_treat", False)

    @property
    def murdermystery_bow_killstreak(self) -> bool:
        return getattr(self, "_murdermystery_bow_killstreak", False)

    @property
    def murdermystery_double_duty(self) -> bool:
        return getattr(self, "_murdermystery_double_duty", False)

    @property
    def murdermystery_drink_many_potions(self) -> bool:
        return getattr(self, "_murdermystery_drink_many_potions", False)

    @property
    def murdermystery_kill_in_rapid_transport(self) -> bool:
        return getattr(self, "_murdermystery_kill_in_rapid_transport", False)

    @property
    def murdermystery_kill_murderer_while_blinded(self) -> bool:
        return getattr(
            self,
            "_murdermystery_kill_murderer_while_blinded",
            False,
        )

    @property
    def murdermystery_kill_while_monorail(self) -> bool:
        return getattr(self, "_murdermystery_kill_while_monorail", False)

    @property
    def murdermystery_murderer_bow_kills(self) -> bool:
        return getattr(self, "_murdermystery_murderer_bow_kills", False)

    @property
    def murdermystery_stealth(self) -> bool:
        return getattr(self, "_murdermystery_stealth", False)

    @property
    def murdermystery_trapper_territory(self) -> bool:
        return getattr(self, "_murdermystery_trapper_territory", False)

    @property
    def murdermystery_tricked(self) -> bool:
        return getattr(self, "_murdermystery_tricked", False)

    @property
    def paintball_lights_out(self) -> bool:
        return getattr(self, "_paintball_lights_out", False)

    @property
    def paintball_sampling(self) -> bool:
        return getattr(self, "_paintball_sampling", False)

    @property
    def pit_collect_trickle_down(self) -> bool:
        return getattr(self, "_pit_collect_trickle_down", False)

    @property
    def pit_fast_quick_maths(self) -> bool:
        return getattr(self, "_pit_fast_quick_maths", False)

    @property
    def pit_get_endless_quiver_arrows(self) -> bool:
        return getattr(self, "_pit_get_endless_quiver_arrows", False)

    @property
    def pit_heal_with_vampire(self) -> bool:
        return getattr(self, "_pit_heal_with_vampire", False)

    @property
    def pit_mine_obsidian(self) -> bool:
        return getattr(self, "_pit_mine_obsidian", False)

    @property
    def quake_apple_corer(self) -> bool:
        return getattr(self, "_quake_apple_corer", False)

    @property
    def quake_lookin_good(self) -> bool:
        return getattr(self, "_quake_lookin_good", False)

    @property
    def skyblock_rough_deal(self) -> bool:
        return getattr(self, "_skyblock_rough_deal", False)

    @property
    def skyblock_the_prodigy(self) -> bool:
        return getattr(self, "_skyblock_the_prodigy", False)

    @property
    def skyblock_wasted_potential(self) -> bool:
        return getattr(self, "_skyblock_wasted_potential", False)

    @property
    def skyclash_im_a_wizard(self) -> bool:
        return getattr(self, "_skyclash_im_a_wizard", False)

    @property
    def skyclash_my_playstyle(self) -> bool:
        return getattr(self, "_skyclash_my_playstyle", False)

    @property
    def skyclash_powerspike(self) -> bool:
        return getattr(self, "_skyclash_powerspike", False)

    @property
    def skywars_mystery_mob(self) -> bool:
        return getattr(self, "_skywars_mystery_mob", False)

    @property
    def skywars_playing_it_safe(self) -> bool:
        return getattr(self, "_skywars_playing_it_safe", False)

    @property
    def skywars_solo_warrior(self) -> bool:
        return getattr(self, "_skywars_solo_warrior", False)

    @property
    def skywars_teamwork(self) -> bool:
        return getattr(self, "_skywars_teamwork", False)

    @property
    def speeduhc_diamonds(self) -> bool:
        return getattr(self, "_speeduhc_diamonds", False)

    @property
    def speeduhc_paper_cut(self) -> bool:
        return getattr(self, "_speeduhc_paper_cut", False)

    @property
    def speeduhc_skeleton_bow(self) -> bool:
        return getattr(self, "_speeduhc_skeleton_bow", False)

    @property
    def speeduhc_snipe_player(self) -> bool:
        return getattr(self, "_speeduhc_snipe_player", False)

    @property
    def speeduhc_use_enderpearl(self) -> bool:
        return getattr(self, "_speeduhc_use_enderpearl", False)

    @property
    def summer_beach_bash(self) -> bool:
        return getattr(self, "_summer_beach_bash", False)

    @property
    def summer_oasis_jake(self) -> bool:
        return getattr(self, "_summer_oasis_jake", False)

    @property
    def summer_ocean_offering(self) -> bool:
        return getattr(self, "_summer_ocean_offering", False)

    @property
    def summer_seaside_shootout(self) -> bool:
        return getattr(self, "_summer_seaside_shootout", False)

    @property
    def supersmash_bulk_challenge(self) -> bool:
        return getattr(self, "_supersmash_bulk_challenge", False)

    @property
    def supersmash_frostmage_challenge(self) -> bool:
        return getattr(self, "_supersmash_frostmage_challenge", False)

    @property
    def tntgames_leave_me_alone(self) -> bool:
        return getattr(self, "_tntgames_leave_me_alone", False)

    @property
    def tntgames_pvp_run_nodjs(self) -> bool:
        return getattr(self, "_tntgames_pvp_run_nodjs", False)

    @property
    def tntgames_pvp_run_nohit(self) -> bool:
        return getattr(self, "_tntgames_pvp_run_nohit", False)

    @property
    def tntgames_pvp_run_triple(self) -> bool:
        return getattr(self, "_tntgames_pvp_run_triple", False)

    @property
    def tntgames_wrong_game(self) -> bool:
        return getattr(self, "_tntgames_wrong_game", False)

    @property
    def truecombat_diamond_armor(self) -> bool:
        return getattr(self, "_truecombat_diamond_armor", False)

    @property
    def vampirez_chest_hunter(self) -> bool:
        return getattr(self, "_vampirez_chest_hunter", False)

    @property
    def vampirez_dont_need_it(self) -> bool:
        return getattr(self, "_vampirez_dont_need_it", False)

    @property
    def walls3_max_herobrine_skills(self) -> bool:
        return getattr(self, "_walls3_max_herobrine_skills", False)

    @property
    def walls3_max_skeleton_skills(self) -> bool:
        return getattr(self, "_walls3_max_skeleton_skills", False)

    @property
    def walls3_max_zombie_skills(self) -> bool:
        return getattr(self, "_walls3_max_zombie_skills", False)

    @property
    def walls3_veteran(self) -> bool:
        return getattr(self, "_walls3_veteran", False)

    @property
    def warlords_bearing_gifts(self) -> bool:
        return getattr(self, "_warlords_bearing_gifts", False)

    @property
    def warlords_boot_camp(self) -> bool:
        return getattr(self, "_warlords_boot_camp", False)

    @property
    def warlords_green_is_love(self) -> bool:
        return getattr(self, "_warlords_green_is_love", False)

    @property
    def warlords_i_got_you_bro(self) -> bool:
        return getattr(self, "_warlords_i_got_you_bro", False)

    @property
    def warlords_mad_skillz_yo(self) -> bool:
        return getattr(self, "_warlords_mad_skillz_yo", False)

    @property
    def warlords_slow_down_there(self) -> bool:
        return getattr(self, "_warlords_slow_down_there", False)

    @property
    def warlords_world_travel(self) -> bool:
        return getattr(self, "_warlords_world_travel", False)

    @property
    def woolgames_shopping_for_wool(self) -> bool:
        return getattr(self, "_woolgames_shopping_for_wool", False)

    @property
    def blitz_youtuber(self) -> bool:
        return getattr(self, "_blitz_youtuber", False)

    @property
    def skyblock_defeat_sun_gecko(self) -> bool:
        return getattr(self, "_skyblock_defeat_sun_gecko", False)

    @property
    def skyblock_finally_over(self) -> bool:
        return getattr(self, "_skyblock_finally_over", False)

    @property
    def skyblock_genius(self) -> bool:
        return getattr(self, "_skyblock_genius", False)

    @property
    def skyblock_hasta_la_vista(self) -> bool:
        return getattr(self, "_skyblock_hasta_la_vista", False)

    @property
    def skyblock_multidimensional_slayer(self) -> bool:
        return getattr(self, "_skyblock_multidimensional_slayer", False)

    @property
    def skyblock_not_the_exit(self) -> bool:
        return getattr(self, "_skyblock_not_the_exit", False)

    @property
    def skyblock_not_worth_it_bro(self) -> bool:
        return getattr(self, "_skyblock_not_worth_it_bro", False)

    @property
    def skyblock_return_from_breach(self) -> bool:
        return getattr(self, "_skyblock_return_from_breach", False)

    @property
    def skyblock_tragedy_reversed(self) -> bool:
        return getattr(self, "_skyblock_tragedy_reversed", False)

    @property
    def skyblock_watchful_presence(self) -> bool:
        return getattr(self, "_skyblock_watchful_presence", False)

    @property
    def skyblock_wizard_food_chain(self) -> bool:
        return getattr(self, "_skyblock_wizard_food_chain", False)

    @property
    def skyblock_zoop(self) -> bool:
        return getattr(self, "_skyblock_zoop", False)
