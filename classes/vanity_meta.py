class VanityMeta:
    """Class representing a player"s vanity meta"""

    def __init__(self, vanity_meta: dict):
        for name in vanity_meta["packages"]:
            safe_name = name.replace("-", "_")
            setattr(self, f"_{safe_name.lower()}", True)

    @property
    def clickeffects_blizzard(self) -> bool:
        return getattr(self, "_clickeffects_blizzard", False)

    @property
    def clickeffects_easter_egg(self) -> bool:
        return getattr(self, "_clickeffects_easter_egg", False)

    @property
    def clickeffects_holiday_firework(self) -> bool:
        return getattr(self, "_clickeffects_holiday_firework", False)

    @property
    def clickeffects_hypixel(self) -> bool:
        return getattr(self, "_clickeffects_hypixel", False)

    @property
    def clickeffects_skull(self) -> bool:
        return getattr(self, "_clickeffects_skull", False)

    @property
    def clickeffects_snow(self) -> bool:
        return getattr(self, "_clickeffects_snow", False)

    @property
    def clickeffects_spout(self) -> bool:
        return getattr(self, "_clickeffects_spout", False)

    @property
    def cloak_achievement_points(self) -> bool:
        return getattr(self, "_cloak_achievement_points", False)

    @property
    def cloak_acid_rain(self) -> bool:
        return getattr(self, "_cloak_acid_rain", False)

    @property
    def cloak_archangel(self) -> bool:
        return getattr(self, "_cloak_archangel", False)

    @property
    def cloak_blaze(self) -> bool:
        return getattr(self, "_cloak_blaze", False)

    @property
    def cloak_blizzard(self) -> bool:
        return getattr(self, "_cloak_blizzard", False)

    @property
    def cloak_bone_wings(self) -> bool:
        return getattr(self, "_cloak_bone_wings", False)

    @property
    def cloak_candy_cane(self) -> bool:
        return getattr(self, "_cloak_candy_cane", False)

    @property
    def cloak_candy_spiral(self) -> bool:
        return getattr(self, "_cloak_candy_spiral", False)

    @property
    def cloak_clover(self) -> bool:
        return getattr(self, "_cloak_clover", False)

    @property
    def cloak_colorbox(self) -> bool:
        return getattr(self, "_cloak_colorbox", False)

    @property
    def cloak_comets(self) -> bool:
        return getattr(self, "_cloak_comets", False)

    @property
    def cloak_dark_angel(self) -> bool:
        return getattr(self, "_cloak_dark_angel", False)

    @property
    def cloak_dark_energy(self) -> bool:
        return getattr(self, "_cloak_dark_energy", False)

    @property
    def cloak_downpour(self) -> bool:
        return getattr(self, "_cloak_downpour", False)

    @property
    def cloak_easter_egg(self) -> bool:
        return getattr(self, "_cloak_easter_egg", False)

    @property
    def cloak_egg_scanner(self) -> bool:
        return getattr(self, "_cloak_egg_scanner", False)

    @property
    def cloak_feathered(self) -> bool:
        return getattr(self, "_cloak_feathered", False)

    @property
    def cloak_firewings(self) -> bool:
        return getattr(self, "_cloak_firewings", False)

    @property
    def cloak_frosty_cloak(self) -> bool:
        return getattr(self, "_cloak_frosty_cloak", False)

    @property
    def cloak_frozen_dragon_wings(self) -> bool:
        return getattr(self, "_cloak_frozen_dragon_wings", False)

    @property
    def cloak_icy_wings(self) -> bool:
        return getattr(self, "_cloak_icy_wings", False)

    @property
    def cloak_menorah(self) -> bool:
        return getattr(self, "_cloak_menorah", False)

    @property
    def cloak_monarch_wings(self) -> bool:
        return getattr(self, "_cloak_monarch_wings", False)

    @property
    def cloak_mystical(self) -> bool:
        return getattr(self, "_cloak_mystical", False)

    @property
    def cloak_rainy_day(self) -> bool:
        return getattr(self, "_cloak_rainy_day", False)

    @property
    def cloak_ranks_gifted(self) -> bool:
        return getattr(self, "_cloak_ranks_gifted", False)

    @property
    def cloak_rose(self) -> bool:
        return getattr(self, "_cloak_rose", False)

    @property
    def cloak_scanner(self) -> bool:
        return getattr(self, "_cloak_scanner", False)

    @property
    def cloak_school(self) -> bool:
        return getattr(self, "_cloak_school", False)

    @property
    def cloak_shaman(self) -> bool:
        return getattr(self, "_cloak_shaman", False)

    @property
    def cloak_shimmering_wings(self) -> bool:
        return getattr(self, "_cloak_shimmering_wings", False)

    @property
    def cloak_snowball(self) -> bool:
        return getattr(self, "_cloak_snowball", False)

    @property
    def cloak_spooky_wings(self) -> bool:
        return getattr(self, "_cloak_spooky_wings", False)

    @property
    def cloak_superhero(self) -> bool:
        return getattr(self, "_cloak_superhero", False)

    @property
    def cloak_sweetwings(self) -> bool:
        return getattr(self, "_cloak_sweetwings", False)

    @property
    def cloak_twisted(self) -> bool:
        return getattr(self, "_cloak_twisted", False)

    @property
    def cloak_vampire_wings(self) -> bool:
        return getattr(self, "_cloak_vampire_wings", False)

    @property
    def emote_angry(self) -> bool:
        return getattr(self, "_emote_angry", False)

    @property
    def emote_cheeky(self) -> bool:
        return getattr(self, "_emote_cheeky", False)

    @property
    def emote_cool(self) -> bool:
        return getattr(self, "_emote_cool", False)

    @property
    def emote_cry(self) -> bool:
        return getattr(self, "_emote_cry", False)

    @property
    def emote_deal_with_it(self) -> bool:
        return getattr(self, "_emote_deal_with_it", False)

    @property
    def emote_dizzy(self) -> bool:
        return getattr(self, "_emote_dizzy", False)

    @property
    def emote_face_melter(self) -> bool:
        return getattr(self, "_emote_face_melter", False)

    @property
    def emote_grin(self) -> bool:
        return getattr(self, "_emote_grin", False)

    @property
    def emote_heart(self) -> bool:
        return getattr(self, "_emote_heart", False)

    @property
    def emote_present_unwrap(self) -> bool:
        return getattr(self, "_emote_present_unwrap", False)

    @property
    def emote_relax(self) -> bool:
        return getattr(self, "_emote_relax", False)

    @property
    def emote_rip(self) -> bool:
        return getattr(self, "_emote_rip", False)

    @property
    def emote_sad(self) -> bool:
        return getattr(self, "_emote_sad", False)

    @property
    def emote_sleepy(self) -> bool:
        return getattr(self, "_emote_sleepy", False)

    @property
    def emote_smile(self) -> bool:
        return getattr(self, "_emote_smile", False)

    @property
    def emote_spicy(self) -> bool:
        return getattr(self, "_emote_spicy", False)

    @property
    def emote_sun_tan(self) -> bool:
        return getattr(self, "_emote_sun_tan", False)

    @property
    def emote_surprised(self) -> bool:
        return getattr(self, "_emote_surprised", False)

    @property
    def emote_wink(self) -> bool:
        return getattr(self, "_emote_wink", False)

    @property
    def gadget_advent_proof(self) -> bool:
        return getattr(self, "_gadget_advent_proof", False)

    @property
    def gadget_anniversary_knight(self) -> bool:
        return getattr(self, "_gadget_anniversary_knight", False)

    @property
    def gadget_anniversary_trampoline(self) -> bool:
        return getattr(self, "_gadget_anniversary_trampoline", False)

    @property
    def gadget_bat_launcher(self) -> bool:
        return getattr(self, "_gadget_bat_launcher", False)

    @property
    def gadget_bbq_grill(self) -> bool:
        return getattr(self, "_gadget_bbq_grill", False)

    @property
    def gadget_bunny_party(self) -> bool:
        return getattr(self, "_gadget_bunny_party", False)

    @property
    def gadget_chicken_cannon(self) -> bool:
        return getattr(self, "_gadget_chicken_cannon", False)

    @property
    def gadget_christmas_cracker(self) -> bool:
        return getattr(self, "_gadget_christmas_cracker", False)

    @property
    def gadget_cornucopia(self) -> bool:
        return getattr(self, "_gadget_cornucopia", False)

    @property
    def gadget_corrupted(self) -> bool:
        return getattr(self, "_gadget_corrupted", False)

    @property
    def gadget_creeper_astronaut(self) -> bool:
        return getattr(self, "_gadget_creeper_astronaut", False)

    @property
    def gadget_dice(self) -> bool:
        return getattr(self, "_gadget_dice", False)

    @property
    def gadget_disco_ball(self) -> bool:
        return getattr(self, "_gadget_disco_ball", False)

    @property
    def gadget_diving_board(self) -> bool:
        return getattr(self, "_gadget_diving_board", False)

    @property
    def gadget_dj_booth(self) -> bool:
        return getattr(self, "_gadget_dj_booth", False)

    @property
    def gadget_dreidel(self) -> bool:
        return getattr(self, "_gadget_dreidel", False)

    @property
    def gadget_duels_banner(self) -> bool:
        return getattr(self, "_gadget_duels_banner", False)

    @property
    def gadget_exploding_sheep(self) -> bool:
        return getattr(self, "_gadget_exploding_sheep", False)

    @property
    def gadget_explosive_bow(self) -> bool:
        return getattr(self, "_gadget_explosive_bow", False)

    @property
    def gadget_fire_trail(self) -> bool:
        return getattr(self, "_gadget_fire_trail", False)

    @property
    def gadget_firework_launcher(self) -> bool:
        return getattr(self, "_gadget_firework_launcher", False)

    @property
    def gadget_flaming_egg_launcher(self) -> bool:
        return getattr(self, "_gadget_flaming_egg_launcher", False)

    @property
    def gadget_flammable_grappling_hook(self) -> bool:
        return getattr(self, "_gadget_flammable_grappling_hook", False)

    @property
    def gadget_flower_giver(self) -> bool:
        return getattr(self, "_gadget_flower_giver", False)

    @property
    def gadget_fortune_cookie(self) -> bool:
        return getattr(self, "_gadget_fortune_cookie", False)

    @property
    def gadget_frisbee(self) -> bool:
        return getattr(self, "_gadget_frisbee", False)

    @property
    def gadget_ghosts(self) -> bool:
        return getattr(self, "_gadget_ghosts", False)

    @property
    def gadget_giant_skeleton(self) -> bool:
        return getattr(self, "_gadget_giant_skeleton", False)

    @property
    def gadget_grappling_hook(self) -> bool:
        return getattr(self, "_gadget_grappling_hook", False)

    @property
    def gadget_graveyard(self) -> bool:
        return getattr(self, "_gadget_graveyard", False)

    @property
    def gadget_holiday_choir(self) -> bool:
        return getattr(self, "_gadget_holiday_choir", False)

    @property
    def gadget_holiday_tree(self) -> bool:
        return getattr(self, "_gadget_holiday_tree", False)

    @property
    def gadget_horror_movie(self) -> bool:
        return getattr(self, "_gadget_horror_movie", False)

    @property
    def gadget_hot_potato(self) -> bool:
        return getattr(self, "_gadget_hot_potato", False)

    @property
    def gadget_hype_train(self) -> bool:
        return getattr(self, "_gadget_hype_train", False)

    @property
    def gadget_ice_cream_stand(self) -> bool:
        return getattr(self, "_gadget_ice_cream_stand", False)

    @property
    def gadget_ice_skating(self) -> bool:
        return getattr(self, "_gadget_ice_skating", False)

    @property
    def gadget_jetpack(self) -> bool:
        return getattr(self, "_gadget_jetpack", False)

    @property
    def gadget_latte(self) -> bool:
        return getattr(self, "_gadget_latte", False)

    @property
    def gadget_let_snow(self) -> bool:
        return getattr(self, "_gadget_let_snow", False)

    @property
    def gadget_levitation_gun(self) -> bool:
        return getattr(self, "_gadget_levitation_gun", False)

    @property
    def gadget_magic_carpet(self) -> bool:
        return getattr(self, "_gadget_magic_carpet", False)

    @property
    def gadget_meteorite(self) -> bool:
        return getattr(self, "_gadget_meteorite", False)

    @property
    def gadget_new_year(self) -> bool:
        return getattr(self, "_gadget_new_year", False)

    @property
    def gadget_new_year_countdown(self) -> bool:
        return getattr(self, "_gadget_new_year_countdown", False)

    @property
    def gadget_paint_trail(self) -> bool:
        return getattr(self, "_gadget_paint_trail", False)

    @property
    def gadget_paintball_gun(self) -> bool:
        return getattr(self, "_gadget_paintball_gun", False)

    @property
    def gadget_parachute(self) -> bool:
        return getattr(self, "_gadget_parachute", False)

    @property
    def gadget_party_popper(self) -> bool:
        return getattr(self, "_gadget_party_popper", False)

    @property
    def gadget_pinata(self) -> bool:
        return getattr(self, "_gadget_pinata", False)

    @property
    def gadget_pocket_beach(self) -> bool:
        return getattr(self, "_gadget_pocket_beach", False)

    @property
    def gadget_pong(self) -> bool:
        return getattr(self, "_gadget_pong", False)

    @property
    def gadget_poop_bomb(self) -> bool:
        return getattr(self, "_gadget_poop_bomb", False)

    @property
    def gadget_portable_pond(self) -> bool:
        return getattr(self, "_gadget_portable_pond", False)

    @property
    def gadget_pumpkin_cannon(self) -> bool:
        return getattr(self, "_gadget_pumpkin_cannon", False)

    @property
    def gadget_pumpkin_rain(self) -> bool:
        return getattr(self, "_gadget_pumpkin_rain", False)

    @property
    def gadget_radio(self) -> bool:
        return getattr(self, "_gadget_radio", False)

    @property
    def gadget_rainbow(self) -> bool:
        return getattr(self, "_gadget_rainbow", False)

    @property
    def gadget_rock_paper_shears(self) -> bool:
        return getattr(self, "_gadget_rock_paper_shears", False)

    @property
    def gadget_rocket(self) -> bool:
        return getattr(self, "_gadget_rocket", False)

    @property
    def gadget_rush_pearl(self) -> bool:
        return getattr(self, "_gadget_rush_pearl", False)

    @property
    def gadget_sand_castle(self) -> bool:
        return getattr(self, "_gadget_sand_castle", False)

    @property
    def gadget_scare_crow(self) -> bool:
        return getattr(self, "_gadget_scare_crow", False)

    @property
    def gadget_secret_service(self) -> bool:
        return getattr(self, "_gadget_secret_service", False)

    @property
    def gadget_skywars_banner(self) -> bool:
        return getattr(self, "_gadget_skywars_banner", False)

    @property
    def gadget_sled(self) -> bool:
        return getattr(self, "_gadget_sled", False)

    @property
    def gadget_snow_globe(self) -> bool:
        return getattr(self, "_gadget_snow_globe", False)

    @property
    def gadget_snowman(self) -> bool:
        return getattr(self, "_gadget_snowman", False)

    @property
    def gadget_spooky_fish(self) -> bool:
        return getattr(self, "_gadget_spooky_fish", False)

    @property
    def gadget_swarm(self) -> bool:
        return getattr(self, "_gadget_swarm", False)

    @property
    def gadget_swing(self) -> bool:
        return getattr(self, "_gadget_swing", False)

    @property
    def gadget_teleporter(self) -> bool:
        return getattr(self, "_gadget_teleporter", False)

    @property
    def gadget_tennis_ball(self) -> bool:
        return getattr(self, "_gadget_tennis_ball", False)

    @property
    def gadget_tetherball(self) -> bool:
        return getattr(self, "_gadget_tetherball", False)

    @property
    def gadget_tic_tac_toe(self) -> bool:
        return getattr(self, "_gadget_tic_tac_toe", False)

    @property
    def gadget_tidal_wave(self) -> bool:
        return getattr(self, "_gadget_tidal_wave", False)

    @property
    def gadget_tnt_fountain(self) -> bool:
        return getattr(self, "_gadget_tnt_fountain", False)

    @property
    def gadget_tournament_banner(self) -> bool:
        return getattr(self, "_gadget_tournament_banner", False)

    @property
    def gadget_tournament_banner_bedwars4s_0(self) -> bool:
        return getattr(self, "_gadget_tournament_banner_bedwars4s_0", False)

    @property
    def gadget_tournament_banner_bedwars4s_1(self) -> bool:
        return getattr(self, "_gadget_tournament_banner_bedwars4s_1", False)

    @property
    def gadget_tournament_banner_bedwars_two_four_0(self) -> bool:
        return getattr(
            self,
            "_gadget_tournament_banner_bedwars_two_four_0",
            False,
        )

    @property
    def gadget_tournament_banner_mcgo_defusal_0(self) -> bool:
        return getattr(
            self,
            "_gadget_tournament_banner_mcgo_defusal_0",
            False,
        )

    @property
    def gadget_tournament_banner_quake_solo2_0(self) -> bool:
        return getattr(self, "_gadget_tournament_banner_quake_solo2_0", False)

    @property
    def gadget_tournament_banner_quake_solo_0(self) -> bool:
        return getattr(self, "_gadget_tournament_banner_quake_solo_0", False)

    @property
    def gadget_tournament_banner_sw_crazy_solo_0(self) -> bool:
        return getattr(
            self,
            "_gadget_tournament_banner_sw_crazy_solo_0",
            False,
        )

    @property
    def gadget_tournament_banner_sw_insane_doubles_0(self) -> bool:
        return getattr(
            self,
            "_gadget_tournament_banner_sw_insane_doubles_0",
            False,
        )

    @property
    def gadget_trampoline(self) -> bool:
        return getattr(self, "_gadget_trampoline", False)

    @property
    def gadget_treat_fountain(self) -> bool:
        return getattr(self, "_gadget_treat_fountain", False)

    @property
    def gadget_tree_planter(self) -> bool:
        return getattr(self, "_gadget_tree_planter", False)

    @property
    def gadget_trick_or_treat(self) -> bool:
        return getattr(self, "_gadget_trick_or_treat", False)

    @property
    def gadget_volleyball(self) -> bool:
        return getattr(self, "_gadget_volleyball", False)

    @property
    def gadget_water_balloon(self) -> bool:
        return getattr(self, "_gadget_water_balloon", False)

    @property
    def gadget_witch_cauldron(self) -> bool:
        return getattr(self, "_gadget_witch_cauldron", False)

    @property
    def gadget_wizardwand(self) -> bool:
        return getattr(self, "_gadget_wizardwand", False)

    @property
    def hat_alien_slug(self) -> bool:
        return getattr(self, "_hat_alien_slug", False)

    @property
    def hat_aqua_orb(self) -> bool:
        return getattr(self, "_hat_aqua_orb", False)

    @property
    def hat_assassin(self) -> bool:
        return getattr(self, "_hat_assassin", False)

    @property
    def hat_astronaut(self) -> bool:
        return getattr(self, "_hat_astronaut", False)

    @property
    def hat_basketball(self) -> bool:
        return getattr(self, "_hat_basketball", False)

    @property
    def hat_bauble(self) -> bool:
        return getattr(self, "_hat_bauble", False)

    @property
    def hat_beach_ball(self) -> bool:
        return getattr(self, "_hat_beach_ball", False)

    @property
    def hat_bee(self) -> bool:
        return getattr(self, "_hat_bee", False)

    @property
    def hat_bell(self) -> bool:
        return getattr(self, "_hat_bell", False)

    @property
    def hat_bird(self) -> bool:
        return getattr(self, "_hat_bird", False)

    @property
    def hat_broken_tv(self) -> bool:
        return getattr(self, "_hat_broken_tv", False)

    @property
    def hat_burger(self) -> bool:
        return getattr(self, "_hat_burger", False)

    @property
    def hat_cactus(self) -> bool:
        return getattr(self, "_hat_cactus", False)

    @property
    def hat_candy_cane(self) -> bool:
        return getattr(self, "_hat_candy_cane", False)

    @property
    def hat_cauldron(self) -> bool:
        return getattr(self, "_hat_cauldron", False)

    @property
    def hat_cheese(self) -> bool:
        return getattr(self, "_hat_cheese", False)

    @property
    def hat_chick(self) -> bool:
        return getattr(self, "_hat_chick", False)

    @property
    def hat_chocolate_egg(self) -> bool:
        return getattr(self, "_hat_chocolate_egg", False)

    @property
    def hat_clown(self) -> bool:
        return getattr(self, "_hat_clown", False)

    @property
    def hat_clown2(self) -> bool:
        return getattr(self, "_hat_clown2", False)

    @property
    def hat_clownfish(self) -> bool:
        return getattr(self, "_hat_clownfish", False)

    @property
    def hat_comet_reindeer(self) -> bool:
        return getattr(self, "_hat_comet_reindeer", False)

    @property
    def hat_crown(self) -> bool:
        return getattr(self, "_hat_crown", False)

    @property
    def hat_dead_pirate(self) -> bool:
        return getattr(self, "_hat_dead_pirate", False)

    @property
    def hat_deal_with_it_bunny(self) -> bool:
        return getattr(self, "_hat_deal_with_it_bunny", False)

    @property
    def hat_decoration_ball(self) -> bool:
        return getattr(self, "_hat_decoration_ball", False)

    @property
    def hat_demon_knight(self) -> bool:
        return getattr(self, "_hat_demon_knight", False)

    @property
    def hat_derpy_snowman(self) -> bool:
        return getattr(self, "_hat_derpy_snowman", False)

    @property
    def hat_devourer(self) -> bool:
        return getattr(self, "_hat_devourer", False)

    @property
    def hat_diamond_steve(self) -> bool:
        return getattr(self, "_hat_diamond_steve", False)

    @property
    def hat_dinosaur(self) -> bool:
        return getattr(self, "_hat_dinosaur", False)

    @property
    def hat_doge(self) -> bool:
        return getattr(self, "_hat_doge", False)

    @property
    def hat_duck(self) -> bool:
        return getattr(self, "_hat_duck", False)

    @property
    def hat_duckling(self) -> bool:
        return getattr(self, "_hat_duckling", False)

    @property
    def hat_earth(self) -> bool:
        return getattr(self, "_hat_earth", False)

    @property
    def hat_easter_basket(self) -> bool:
        return getattr(self, "_hat_easter_basket", False)

    @property
    def hat_easter_egg(self) -> bool:
        return getattr(self, "_hat_easter_egg", False)

    @property
    def hat_eater(self) -> bool:
        return getattr(self, "_hat_eater", False)

    @property
    def hat_egg_head(self) -> bool:
        return getattr(self, "_hat_egg_head", False)

    @property
    def hat_egyptian_queen(self) -> bool:
        return getattr(self, "_hat_egyptian_queen", False)

    @property
    def hat_elephant(self) -> bool:
        return getattr(self, "_hat_elephant", False)

    @property
    def hat_elf_princess(self) -> bool:
        return getattr(self, "_hat_elf_princess", False)

    @property
    def hat_elfboy(self) -> bool:
        return getattr(self, "_hat_elfboy", False)

    @property
    def hat_elfgirl(self) -> bool:
        return getattr(self, "_hat_elfgirl", False)

    @property
    def hat_ender_dragon(self) -> bool:
        return getattr(self, "_hat_ender_dragon", False)

    @property
    def hat_evil_eye(self) -> bool:
        return getattr(self, "_hat_evil_eye", False)

    @property
    def hat_ferret(self) -> bool:
        return getattr(self, "_hat_ferret", False)

    @property
    def hat_festive_herobrine(self) -> bool:
        return getattr(self, "_hat_festive_herobrine", False)

    @property
    def hat_festive_skeleton(self) -> bool:
        return getattr(self, "_hat_festive_skeleton", False)

    @property
    def hat_festive_squid(self) -> bool:
        return getattr(self, "_hat_festive_squid", False)

    @property
    def hat_festive_villager(self) -> bool:
        return getattr(self, "_hat_festive_villager", False)

    @property
    def hat_festive_zombie(self) -> bool:
        return getattr(self, "_hat_festive_zombie", False)

    @property
    def hat_fire_demon(self) -> bool:
        return getattr(self, "_hat_fire_demon", False)

    @property
    def hat_football_star(self) -> bool:
        return getattr(self, "_hat_football_star", False)

    @property
    def hat_forester(self) -> bool:
        return getattr(self, "_hat_forester", False)

    @property
    def hat_fox(self) -> bool:
        return getattr(self, "_hat_fox", False)

    @property
    def hat_frog(self) -> bool:
        return getattr(self, "_hat_frog", False)

    @property
    def hat_ghost(self) -> bool:
        return getattr(self, "_hat_ghost", False)

    @property
    def hat_gift(self) -> bool:
        return getattr(self, "_hat_gift", False)

    @property
    def hat_ginger_bread(self) -> bool:
        return getattr(self, "_hat_ginger_bread", False)

    @property
    def hat_gingerbread(self) -> bool:
        return getattr(self, "_hat_gingerbread", False)

    @property
    def hat_gingerbread_man(self) -> bool:
        return getattr(self, "_hat_gingerbread_man", False)

    @property
    def hat_gold_steve(self) -> bool:
        return getattr(self, "_hat_gold_steve", False)

    @property
    def hat_golden_knight(self) -> bool:
        return getattr(self, "_hat_golden_knight", False)

    @property
    def hat_golden_pufferfish(self) -> bool:
        return getattr(self, "_hat_golden_pufferfish", False)

    @property
    def hat_golem(self) -> bool:
        return getattr(self, "_hat_golem", False)

    @property
    def hat_gorilla(self) -> bool:
        return getattr(self, "_hat_gorilla", False)

    @property
    def hat_grinch(self) -> bool:
        return getattr(self, "_hat_grinch", False)

    @property
    def hat_groopo(self) -> bool:
        return getattr(self, "_hat_groopo", False)

    @property
    def hat_halloween_evil_pumpkin(self) -> bool:
        return getattr(self, "_hat_halloween_evil_pumpkin", False)

    @property
    def hat_halloween_ghast(self) -> bool:
        return getattr(self, "_hat_halloween_ghast", False)

    @property
    def hat_halloween_marionette(self) -> bool:
        return getattr(self, "_hat_halloween_marionette", False)

    @property
    def hat_halloween_pig_zombie(self) -> bool:
        return getattr(self, "_hat_halloween_pig_zombie", False)

    @property
    def hat_halloween_skull(self) -> bool:
        return getattr(self, "_hat_halloween_skull", False)

    @property
    def hat_holiday_tree_banner(self) -> bool:
        return getattr(self, "_hat_holiday_tree_banner", False)

    @property
    def hat_holiday_wreath_banner(self) -> bool:
        return getattr(self, "_hat_holiday_wreath_banner", False)

    @property
    def hat_horse(self) -> bool:
        return getattr(self, "_hat_horse", False)

    @property
    def hat_hp8(self) -> bool:
        return getattr(self, "_hat_hp8", False)

    @property
    def hat_hypixel_h(self) -> bool:
        return getattr(self, "_hat_hypixel_h", False)

    @property
    def hat_ice_mage(self) -> bool:
        return getattr(self, "_hat_ice_mage", False)

    @property
    def hat_iron_steve(self) -> bool:
        return getattr(self, "_hat_iron_steve", False)

    @property
    def hat_jason(self) -> bool:
        return getattr(self, "_hat_jason", False)

    @property
    def hat_joe_penguin(self) -> bool:
        return getattr(self, "_hat_joe_penguin", False)

    @property
    def hat_koala(self) -> bool:
        return getattr(self, "_hat_koala", False)

    @property
    def hat_lady_bug(self) -> bool:
        return getattr(self, "_hat_lady_bug", False)

    @property
    def hat_letter_a(self) -> bool:
        return getattr(self, "_hat_letter_a", False)

    @property
    def hat_letter_b(self) -> bool:
        return getattr(self, "_hat_letter_b", False)

    @property
    def hat_letter_c(self) -> bool:
        return getattr(self, "_hat_letter_c", False)

    @property
    def hat_letter_d(self) -> bool:
        return getattr(self, "_hat_letter_d", False)

    @property
    def hat_letter_e(self) -> bool:
        return getattr(self, "_hat_letter_e", False)

    @property
    def hat_letter_exclaimation(self) -> bool:
        return getattr(self, "_hat_letter_exclaimation", False)

    @property
    def hat_letter_f(self) -> bool:
        return getattr(self, "_hat_letter_f", False)

    @property
    def hat_letter_g(self) -> bool:
        return getattr(self, "_hat_letter_g", False)

    @property
    def hat_letter_h(self) -> bool:
        return getattr(self, "_hat_letter_h", False)

    @property
    def hat_letter_hashtag(self) -> bool:
        return getattr(self, "_hat_letter_hashtag", False)

    @property
    def hat_letter_i(self) -> bool:
        return getattr(self, "_hat_letter_i", False)

    @property
    def hat_letter_j(self) -> bool:
        return getattr(self, "_hat_letter_j", False)

    @property
    def hat_letter_k(self) -> bool:
        return getattr(self, "_hat_letter_k", False)

    @property
    def hat_letter_l(self) -> bool:
        return getattr(self, "_hat_letter_l", False)

    @property
    def hat_letter_m(self) -> bool:
        return getattr(self, "_hat_letter_m", False)

    @property
    def hat_letter_n(self) -> bool:
        return getattr(self, "_hat_letter_n", False)

    @property
    def hat_letter_o(self) -> bool:
        return getattr(self, "_hat_letter_o", False)

    @property
    def hat_letter_p(self) -> bool:
        return getattr(self, "_hat_letter_p", False)

    @property
    def hat_letter_plus(self) -> bool:
        return getattr(self, "_hat_letter_plus", False)

    @property
    def hat_letter_q(self) -> bool:
        return getattr(self, "_hat_letter_q", False)

    @property
    def hat_letter_question(self) -> bool:
        return getattr(self, "_hat_letter_question", False)

    @property
    def hat_letter_r(self) -> bool:
        return getattr(self, "_hat_letter_r", False)

    @property
    def hat_letter_s(self) -> bool:
        return getattr(self, "_hat_letter_s", False)

    @property
    def hat_letter_t(self) -> bool:
        return getattr(self, "_hat_letter_t", False)

    @property
    def hat_letter_u(self) -> bool:
        return getattr(self, "_hat_letter_u", False)

    @property
    def hat_letter_v(self) -> bool:
        return getattr(self, "_hat_letter_v", False)

    @property
    def hat_letter_w(self) -> bool:
        return getattr(self, "_hat_letter_w", False)

    @property
    def hat_letter_x(self) -> bool:
        return getattr(self, "_hat_letter_x", False)

    @property
    def hat_letter_y(self) -> bool:
        return getattr(self, "_hat_letter_y", False)

    @property
    def hat_letter_z(self) -> bool:
        return getattr(self, "_hat_letter_z", False)

    @property
    def hat_lucky_dragon(self) -> bool:
        return getattr(self, "_hat_lucky_dragon", False)

    @property
    def hat_mage(self) -> bool:
        return getattr(self, "_hat_mage", False)

    @property
    def hat_magic_dog(self) -> bool:
        return getattr(self, "_hat_magic_dog", False)

    @property
    def hat_mars(self) -> bool:
        return getattr(self, "_hat_mars", False)

    @property
    def hat_miner(self) -> bool:
        return getattr(self, "_hat_miner", False)

    @property
    def hat_minotaur(self) -> bool:
        return getattr(self, "_hat_minotaur", False)

    @property
    def hat_monitor(self) -> bool:
        return getattr(self, "_hat_monitor", False)

    @property
    def hat_monk(self) -> bool:
        return getattr(self, "_hat_monk", False)

    @property
    def hat_monkey(self) -> bool:
        return getattr(self, "_hat_monkey", False)

    @property
    def hat_mummy(self) -> bool:
        return getattr(self, "_hat_mummy", False)

    @property
    def hat_number_0(self) -> bool:
        return getattr(self, "_hat_number_0", False)

    @property
    def hat_number_1(self) -> bool:
        return getattr(self, "_hat_number_1", False)

    @property
    def hat_number_2(self) -> bool:
        return getattr(self, "_hat_number_2", False)

    @property
    def hat_number_3(self) -> bool:
        return getattr(self, "_hat_number_3", False)

    @property
    def hat_number_4(self) -> bool:
        return getattr(self, "_hat_number_4", False)

    @property
    def hat_number_5(self) -> bool:
        return getattr(self, "_hat_number_5", False)

    @property
    def hat_number_6(self) -> bool:
        return getattr(self, "_hat_number_6", False)

    @property
    def hat_number_7(self) -> bool:
        return getattr(self, "_hat_number_7", False)

    @property
    def hat_number_8(self) -> bool:
        return getattr(self, "_hat_number_8", False)

    @property
    def hat_number_9(self) -> bool:
        return getattr(self, "_hat_number_9", False)

    @property
    def hat_odin(self) -> bool:
        return getattr(self, "_hat_odin", False)

    @property
    def hat_orc(self) -> bool:
        return getattr(self, "_hat_orc", False)

    @property
    def hat_otter(self) -> bool:
        return getattr(self, "_hat_otter", False)

    @property
    def hat_owl(self) -> bool:
        return getattr(self, "_hat_owl", False)

    @property
    def hat_panda(self) -> bool:
        return getattr(self, "_hat_panda", False)

    @property
    def hat_parrot(self) -> bool:
        return getattr(self, "_hat_parrot", False)

    @property
    def hat_penguin(self) -> bool:
        return getattr(self, "_hat_penguin", False)

    @property
    def hat_polar_bear(self) -> bool:
        return getattr(self, "_hat_polar_bear", False)

    @property
    def hat_portal(self) -> bool:
        return getattr(self, "_hat_portal", False)

    @property
    def hat_present_hat(self) -> bool:
        return getattr(self, "_hat_present_hat", False)

    @property
    def hat_pug_black(self) -> bool:
        return getattr(self, "_hat_pug_black", False)

    @property
    def hat_pug_white(self) -> bool:
        return getattr(self, "_hat_pug_white", False)

    @property
    def hat_pumpkin(self) -> bool:
        return getattr(self, "_hat_pumpkin", False)

    @property
    def hat_rabbit(self) -> bool:
        return getattr(self, "_hat_rabbit", False)

    @property
    def hat_rainbow_glitch(self) -> bool:
        return getattr(self, "_hat_rainbow_glitch", False)

    @property
    def hat_rainbow_present(self) -> bool:
        return getattr(self, "_hat_rainbow_present", False)

    @property
    def hat_reindeer(self) -> bool:
        return getattr(self, "_hat_reindeer", False)

    @property
    def hat_reindeer_banner(self) -> bool:
        return getattr(self, "_hat_reindeer_banner", False)

    @property
    def hat_robo_bird(self) -> bool:
        return getattr(self, "_hat_robo_bird", False)

    @property
    def hat_sandwich(self) -> bool:
        return getattr(self, "_hat_sandwich", False)

    @property
    def hat_santa(self) -> bool:
        return getattr(self, "_hat_santa", False)

    @property
    def hat_santa_banner(self) -> bool:
        return getattr(self, "_hat_santa_banner", False)

    @property
    def hat_scarecrow(self) -> bool:
        return getattr(self, "_hat_scarecrow", False)

    @property
    def hat_scarecrow2(self) -> bool:
        return getattr(self, "_hat_scarecrow2", False)

    @property
    def hat_scavenger(self) -> bool:
        return getattr(self, "_hat_scavenger", False)

    @property
    def hat_seasoned_fisher_banner(self) -> bool:
        return getattr(self, "_hat_seasoned_fisher_banner", False)

    @property
    def hat_shibe(self) -> bool:
        return getattr(self, "_hat_shibe", False)

    @property
    def hat_siren(self) -> bool:
        return getattr(self, "_hat_siren", False)

    @property
    def hat_skull_king_banner(self) -> bool:
        return getattr(self, "_hat_skull_king_banner", False)

    @property
    def hat_sloth(self) -> bool:
        return getattr(self, "_hat_sloth", False)

    @property
    def hat_snow_bunny_banner(self) -> bool:
        return getattr(self, "_hat_snow_bunny_banner", False)

    @property
    def hat_snow_globe(self) -> bool:
        return getattr(self, "_hat_snow_globe", False)

    @property
    def hat_snowball(self) -> bool:
        return getattr(self, "_hat_snowball", False)

    @property
    def hat_snowglobe(self) -> bool:
        return getattr(self, "_hat_snowglobe", False)

    @property
    def hat_snowman(self) -> bool:
        return getattr(self, "_hat_snowman", False)

    @property
    def hat_space(self) -> bool:
        return getattr(self, "_hat_space", False)

    @property
    def hat_spooked_pufferfish(self) -> bool:
        return getattr(self, "_hat_spooked_pufferfish", False)

    @property
    def hat_spooky_fisher_banner(self) -> bool:
        return getattr(self, "_hat_spooky_fisher_banner", False)

    @property
    def hat_squid(self) -> bool:
        return getattr(self, "_hat_squid", False)

    @property
    def hat_stocking(self) -> bool:
        return getattr(self, "_hat_stocking", False)

    @property
    def hat_stone_steve(self) -> bool:
        return getattr(self, "_hat_stone_steve", False)

    @property
    def hat_toaster(self) -> bool:
        return getattr(self, "_hat_toaster", False)

    @property
    def hat_traffic_light(self) -> bool:
        return getattr(self, "_hat_traffic_light", False)

    @property
    def hat_turtle(self) -> bool:
        return getattr(self, "_hat_turtle", False)

    @property
    def hat_unlock_machine(self) -> bool:
        return getattr(self, "_hat_unlock_machine", False)

    @property
    def hat_vintage(self) -> bool:
        return getattr(self, "_hat_vintage", False)

    @property
    def hat_wall_crusher(self) -> bool:
        return getattr(self, "_hat_wall_crusher", False)

    @property
    def hat_walrus(self) -> bool:
        return getattr(self, "_hat_walrus", False)

    @property
    def hat_werewolf(self) -> bool:
        return getattr(self, "_hat_werewolf", False)

    @property
    def hat_white_wizard(self) -> bool:
        return getattr(self, "_hat_white_wizard", False)

    @property
    def hat_wood_elf(self) -> bool:
        return getattr(self, "_hat_wood_elf", False)

    @property
    def hat_wood_steve(self) -> bool:
        return getattr(self, "_hat_wood_steve", False)

    @property
    def morph_blaze(self) -> bool:
        return getattr(self, "_morph_blaze", False)

    @property
    def morph_cave_spider(self) -> bool:
        return getattr(self, "_morph_cave_spider", False)

    @property
    def morph_chicken(self) -> bool:
        return getattr(self, "_morph_chicken", False)

    @property
    def morph_cow(self) -> bool:
        return getattr(self, "_morph_cow", False)

    @property
    def morph_creeper(self) -> bool:
        return getattr(self, "_morph_creeper", False)

    @property
    def morph_enderman(self) -> bool:
        return getattr(self, "_morph_enderman", False)

    @property
    def morph_grinch(self) -> bool:
        return getattr(self, "_morph_grinch", False)

    @property
    def morph_guardian(self) -> bool:
        return getattr(self, "_morph_guardian", False)

    @property
    def morph_iron_golem(self) -> bool:
        return getattr(self, "_morph_iron_golem", False)

    @property
    def morph_pig(self) -> bool:
        return getattr(self, "_morph_pig", False)

    @property
    def morph_rabbit(self) -> bool:
        return getattr(self, "_morph_rabbit", False)

    @property
    def morph_sheep(self) -> bool:
        return getattr(self, "_morph_sheep", False)

    @property
    def morph_skeleton(self) -> bool:
        return getattr(self, "_morph_skeleton", False)

    @property
    def morph_snow_morph(self) -> bool:
        return getattr(self, "_morph_snow_morph", False)

    @property
    def morph_spider(self) -> bool:
        return getattr(self, "_morph_spider", False)

    @property
    def morph_squid(self) -> bool:
        return getattr(self, "_morph_squid", False)

    @property
    def morph_witch(self) -> bool:
        return getattr(self, "_morph_witch", False)

    @property
    def morph_wither_skeleton(self) -> bool:
        return getattr(self, "_morph_wither_skeleton", False)

    @property
    def morph_zombie(self) -> bool:
        return getattr(self, "_morph_zombie", False)

    @property
    def particlepack_cloud(self) -> bool:
        return getattr(self, "_particlepack_cloud", False)

    @property
    def particlepack_frozen(self) -> bool:
        return getattr(self, "_particlepack_frozen", False)

    @property
    def particlepack_heat_wave(self) -> bool:
        return getattr(self, "_particlepack_heat_wave", False)

    @property
    def particlepack_huge_explosion(self) -> bool:
        return getattr(self, "_particlepack_huge_explosion", False)

    @property
    def particlepack_red_dust(self) -> bool:
        return getattr(self, "_particlepack_red_dust", False)

    @property
    def particlepack_snow_trail(self) -> bool:
        return getattr(self, "_particlepack_snow_trail", False)

    @property
    def particlepack_splash(self) -> bool:
        return getattr(self, "_particlepack_splash", False)

    @property
    def particlepack_spooky(self) -> bool:
        return getattr(self, "_particlepack_spooky", False)

    @property
    def particlepack_spring(self) -> bool:
        return getattr(self, "_particlepack_spring", False)

    @property
    def particlepack_tinsel(self) -> bool:
        return getattr(self, "_particlepack_tinsel", False)

    @property
    def pet_bat(self) -> bool:
        return getattr(self, "_pet_bat", False)

    @property
    def pet_bee(self) -> bool:
        return getattr(self, "_pet_bee", False)

    @property
    def pet_black_pug(self) -> bool:
        return getattr(self, "_pet_black_pug", False)

    @property
    def pet_black_rabbit(self) -> bool:
        return getattr(self, "_pet_black_rabbit", False)

    @property
    def pet_black_white_rabbit(self) -> bool:
        return getattr(self, "_pet_black_white_rabbit", False)

    @property
    def pet_bouncy_spider(self) -> bool:
        return getattr(self, "_pet_bouncy_spider", False)

    @property
    def pet_brown_horse_baby(self) -> bool:
        return getattr(self, "_pet_brown_horse_baby", False)

    @property
    def pet_brown_rabbit(self) -> bool:
        return getattr(self, "_pet_brown_rabbit", False)

    @property
    def pet_burning_zombie(self) -> bool:
        return getattr(self, "_pet_burning_zombie", False)

    @property
    def pet_cat_black(self) -> bool:
        return getattr(self, "_pet_cat_black", False)

    @property
    def pet_cat_black_baby(self) -> bool:
        return getattr(self, "_pet_cat_black_baby", False)

    @property
    def pet_cat_red(self) -> bool:
        return getattr(self, "_pet_cat_red", False)

    @property
    def pet_cat_red_baby(self) -> bool:
        return getattr(self, "_pet_cat_red_baby", False)

    @property
    def pet_cat_siamese(self) -> bool:
        return getattr(self, "_pet_cat_siamese", False)

    @property
    def pet_cat_siamese_baby(self) -> bool:
        return getattr(self, "_pet_cat_siamese_baby", False)

    @property
    def pet_cave_spider(self) -> bool:
        return getattr(self, "_pet_cave_spider", False)

    @property
    def pet_chicken(self) -> bool:
        return getattr(self, "_pet_chicken", False)

    @property
    def pet_chicken_baby(self) -> bool:
        return getattr(self, "_pet_chicken_baby", False)

    @property
    def pet_chicken_jockey(self) -> bool:
        return getattr(self, "_pet_chicken_jockey", False)

    @property
    def pet_clone(self) -> bool:
        return getattr(self, "_pet_clone", False)

    @property
    def pet_clownfish(self) -> bool:
        return getattr(self, "_pet_clownfish", False)

    @property
    def pet_colorbox(self) -> bool:
        return getattr(self, "_pet_colorbox", False)

    @property
    def pet_cow(self) -> bool:
        return getattr(self, "_pet_cow", False)

    @property
    def pet_cow_baby(self) -> bool:
        return getattr(self, "_pet_cow_baby", False)

    @property
    def pet_creeper(self) -> bool:
        return getattr(self, "_pet_creeper", False)

    @property
    def pet_creeper_powered(self) -> bool:
        return getattr(self, "_pet_creeper_powered", False)

    @property
    def pet_donkey(self) -> bool:
        return getattr(self, "_pet_donkey", False)

    @property
    def pet_duck(self) -> bool:
        return getattr(self, "_pet_duck", False)

    @property
    def pet_enderman(self) -> bool:
        return getattr(self, "_pet_enderman", False)

    @property
    def pet_enderman_pumpkin(self) -> bool:
        return getattr(self, "_pet_enderman_pumpkin", False)

    @property
    def pet_enderman_snow_block(self) -> bool:
        return getattr(self, "_pet_enderman_snow_block", False)

    @property
    def pet_endermite(self) -> bool:
        return getattr(self, "_pet_endermite", False)

    @property
    def pet_fish(self) -> bool:
        return getattr(self, "_pet_fish", False)

    @property
    def pet_flying_guardian(self) -> bool:
        return getattr(self, "_pet_flying_guardian", False)

    @property
    def pet_frog(self) -> bool:
        return getattr(self, "_pet_frog", False)

    @property
    def pet_frozen_skeleton(self) -> bool:
        return getattr(self, "_pet_frozen_skeleton", False)

    @property
    def pet_frozen_zombie(self) -> bool:
        return getattr(self, "_pet_frozen_zombie", False)

    @property
    def pet_gold_rabbit(self) -> bool:
        return getattr(self, "_pet_gold_rabbit", False)

    @property
    def pet_gorrila(self) -> bool:
        return getattr(self, "_pet_gorrila", False)

    @property
    def pet_green_helper(self) -> bool:
        return getattr(self, "_pet_green_helper", False)

    @property
    def pet_grinch(self) -> bool:
        return getattr(self, "_pet_grinch", False)

    @property
    def pet_growing_zombie(self) -> bool:
        return getattr(self, "_pet_growing_zombie", False)

    @property
    def pet_hay_bale(self) -> bool:
        return getattr(self, "_pet_hay_bale", False)

    @property
    def pet_herobrine(self) -> bool:
        return getattr(self, "_pet_herobrine", False)

    @property
    def pet_horse_black(self) -> bool:
        return getattr(self, "_pet_horse_black", False)

    @property
    def pet_horse_brown(self) -> bool:
        return getattr(self, "_pet_horse_brown", False)

    @property
    def pet_horse_chestnut(self) -> bool:
        return getattr(self, "_pet_horse_chestnut", False)

    @property
    def pet_horse_chestnut_baby(self) -> bool:
        return getattr(self, "_pet_horse_chestnut_baby", False)

    @property
    def pet_horse_creamy(self) -> bool:
        return getattr(self, "_pet_horse_creamy", False)

    @property
    def pet_horse_creamy_baby(self) -> bool:
        return getattr(self, "_pet_horse_creamy_baby", False)

    @property
    def pet_horse_dark_brown(self) -> bool:
        return getattr(self, "_pet_horse_dark_brown", False)

    @property
    def pet_horse_dark_brown_baby(self) -> bool:
        return getattr(self, "_pet_horse_dark_brown_baby", False)

    @property
    def pet_horse_gray_baby(self) -> bool:
        return getattr(self, "_pet_horse_gray_baby", False)

    @property
    def pet_horse_grey(self) -> bool:
        return getattr(self, "_pet_horse_grey", False)

    @property
    def pet_horse_skeleton(self) -> bool:
        return getattr(self, "_pet_horse_skeleton", False)

    @property
    def pet_horse_skeleton_baby(self) -> bool:
        return getattr(self, "_pet_horse_skeleton_baby", False)

    @property
    def pet_horse_undead(self) -> bool:
        return getattr(self, "_pet_horse_undead", False)

    @property
    def pet_horse_white(self) -> bool:
        return getattr(self, "_pet_horse_white", False)

    @property
    def pet_hp8(self) -> bool:
        return getattr(self, "_pet_hp8", False)

    @property
    def pet_hp8_2(self) -> bool:
        return getattr(self, "_pet_hp8_2", False)

    @property
    def pet_iron_golem(self) -> bool:
        return getattr(self, "_pet_iron_golem", False)

    @property
    def pet_jack_dog(self) -> bool:
        return getattr(self, "_pet_jack_dog", False)

    @property
    def pet_killer_rabbit(self) -> bool:
        return getattr(self, "_pet_killer_rabbit", False)

    @property
    def pet_magma_cube_big(self) -> bool:
        return getattr(self, "_pet_magma_cube_big", False)

    @property
    def pet_magma_cube_small(self) -> bool:
        return getattr(self, "_pet_magma_cube_small", False)

    @property
    def pet_magma_cube_tiny(self) -> bool:
        return getattr(self, "_pet_magma_cube_tiny", False)

    @property
    def pet_merry_sheep(self) -> bool:
        return getattr(self, "_pet_merry_sheep", False)

    @property
    def pet_mini_wither(self) -> bool:
        return getattr(self, "_pet_mini_wither", False)

    @property
    def pet_mooshroom(self) -> bool:
        return getattr(self, "_pet_mooshroom", False)

    @property
    def pet_mooshroom_baby(self) -> bool:
        return getattr(self, "_pet_mooshroom_baby", False)

    @property
    def pet_mule(self) -> bool:
        return getattr(self, "_pet_mule", False)

    @property
    def pet_packed_ice(self) -> bool:
        return getattr(self, "_pet_packed_ice", False)

    @property
    def pet_panda(self) -> bool:
        return getattr(self, "_pet_panda", False)

    @property
    def pet_pastel_sheep(self) -> bool:
        return getattr(self, "_pet_pastel_sheep", False)

    @property
    def pet_pig(self) -> bool:
        return getattr(self, "_pet_pig", False)

    @property
    def pet_pig_baby(self) -> bool:
        return getattr(self, "_pet_pig_baby", False)

    @property
    def pet_pig_zombie(self) -> bool:
        return getattr(self, "_pet_pig_zombie", False)

    @property
    def pet_pig_zombie_baby(self) -> bool:
        return getattr(self, "_pet_pig_zombie_baby", False)

    @property
    def pet_pufferfish(self) -> bool:
        return getattr(self, "_pet_pufferfish", False)

    @property
    def pet_rabbit_jockey(self) -> bool:
        return getattr(self, "_pet_rabbit_jockey", False)

    @property
    def pet_rabbit_white_baby(self) -> bool:
        return getattr(self, "_pet_rabbit_white_baby", False)

    @property
    def pet_red_helper(self) -> bool:
        return getattr(self, "_pet_red_helper", False)

    @property
    def pet_salmon(self) -> bool:
        return getattr(self, "_pet_salmon", False)

    @property
    def pet_salt_pepper_rabbit(self) -> bool:
        return getattr(self, "_pet_salt_pepper_rabbit", False)

    @property
    def pet_sheep_black(self) -> bool:
        return getattr(self, "_pet_sheep_black", False)

    @property
    def pet_sheep_black_baby(self) -> bool:
        return getattr(self, "_pet_sheep_black_baby", False)

    @property
    def pet_sheep_blue(self) -> bool:
        return getattr(self, "_pet_sheep_blue", False)

    @property
    def pet_sheep_blue_baby(self) -> bool:
        return getattr(self, "_pet_sheep_blue_baby", False)

    @property
    def pet_sheep_brown(self) -> bool:
        return getattr(self, "_pet_sheep_brown", False)

    @property
    def pet_sheep_brown_baby(self) -> bool:
        return getattr(self, "_pet_sheep_brown_baby", False)

    @property
    def pet_sheep_cyan(self) -> bool:
        return getattr(self, "_pet_sheep_cyan", False)

    @property
    def pet_sheep_cyan_baby(self) -> bool:
        return getattr(self, "_pet_sheep_cyan_baby", False)

    @property
    def pet_sheep_gray(self) -> bool:
        return getattr(self, "_pet_sheep_gray", False)

    @property
    def pet_sheep_gray_baby(self) -> bool:
        return getattr(self, "_pet_sheep_gray_baby", False)

    @property
    def pet_sheep_green(self) -> bool:
        return getattr(self, "_pet_sheep_green", False)

    @property
    def pet_sheep_green_baby(self) -> bool:
        return getattr(self, "_pet_sheep_green_baby", False)

    @property
    def pet_sheep_light_blue(self) -> bool:
        return getattr(self, "_pet_sheep_light_blue", False)

    @property
    def pet_sheep_light_blue_baby(self) -> bool:
        return getattr(self, "_pet_sheep_light_blue_baby", False)

    @property
    def pet_sheep_lime(self) -> bool:
        return getattr(self, "_pet_sheep_lime", False)

    @property
    def pet_sheep_lime_baby(self) -> bool:
        return getattr(self, "_pet_sheep_lime_baby", False)

    @property
    def pet_sheep_magenta(self) -> bool:
        return getattr(self, "_pet_sheep_magenta", False)

    @property
    def pet_sheep_magenta_baby(self) -> bool:
        return getattr(self, "_pet_sheep_magenta_baby", False)

    @property
    def pet_sheep_orange(self) -> bool:
        return getattr(self, "_pet_sheep_orange", False)

    @property
    def pet_sheep_orange_baby(self) -> bool:
        return getattr(self, "_pet_sheep_orange_baby", False)

    @property
    def pet_sheep_pink(self) -> bool:
        return getattr(self, "_pet_sheep_pink", False)

    @property
    def pet_sheep_pink_baby(self) -> bool:
        return getattr(self, "_pet_sheep_pink_baby", False)

    @property
    def pet_sheep_purple(self) -> bool:
        return getattr(self, "_pet_sheep_purple", False)

    @property
    def pet_sheep_purple_baby(self) -> bool:
        return getattr(self, "_pet_sheep_purple_baby", False)

    @property
    def pet_sheep_rainbow(self) -> bool:
        return getattr(self, "_pet_sheep_rainbow", False)

    @property
    def pet_sheep_red(self) -> bool:
        return getattr(self, "_pet_sheep_red", False)

    @property
    def pet_sheep_red_baby(self) -> bool:
        return getattr(self, "_pet_sheep_red_baby", False)

    @property
    def pet_sheep_silver(self) -> bool:
        return getattr(self, "_pet_sheep_silver", False)

    @property
    def pet_sheep_silver_baby(self) -> bool:
        return getattr(self, "_pet_sheep_silver_baby", False)

    @property
    def pet_sheep_white(self) -> bool:
        return getattr(self, "_pet_sheep_white", False)

    @property
    def pet_sheep_white_baby(self) -> bool:
        return getattr(self, "_pet_sheep_white_baby", False)

    @property
    def pet_sheep_yellow(self) -> bool:
        return getattr(self, "_pet_sheep_yellow", False)

    @property
    def pet_sheep_yellow_baby(self) -> bool:
        return getattr(self, "_pet_sheep_yellow_baby", False)

    @property
    def pet_shibe(self) -> bool:
        return getattr(self, "_pet_shibe", False)

    @property
    def pet_silverfish(self) -> bool:
        return getattr(self, "_pet_silverfish", False)

    @property
    def pet_skeleton(self) -> bool:
        return getattr(self, "_pet_skeleton", False)

    @property
    def pet_slime_big(self) -> bool:
        return getattr(self, "_pet_slime_big", False)

    @property
    def pet_slime_small(self) -> bool:
        return getattr(self, "_pet_slime_small", False)

    @property
    def pet_slime_tiny(self) -> bool:
        return getattr(self, "_pet_slime_tiny", False)

    @property
    def pet_smoldering_skeleton(self) -> bool:
        return getattr(self, "_pet_smoldering_skeleton", False)

    @property
    def pet_snowman(self) -> bool:
        return getattr(self, "_pet_snowman", False)

    @property
    def pet_snowman_jockey(self) -> bool:
        return getattr(self, "_pet_snowman_jockey", False)

    @property
    def pet_specter(self) -> bool:
        return getattr(self, "_pet_specter", False)

    @property
    def pet_spider(self) -> bool:
        return getattr(self, "_pet_spider", False)

    @property
    def pet_spider_jockey(self) -> bool:
        return getattr(self, "_pet_spider_jockey", False)

    @property
    def pet_totem(self) -> bool:
        return getattr(self, "_pet_totem", False)

    @property
    def pet_villager_blacksmith(self) -> bool:
        return getattr(self, "_pet_villager_blacksmith", False)

    @property
    def pet_villager_blacksmith_baby(self) -> bool:
        return getattr(self, "_pet_villager_blacksmith_baby", False)

    @property
    def pet_villager_butcher(self) -> bool:
        return getattr(self, "_pet_villager_butcher", False)

    @property
    def pet_villager_butcher_baby(self) -> bool:
        return getattr(self, "_pet_villager_butcher_baby", False)

    @property
    def pet_villager_farmer(self) -> bool:
        return getattr(self, "_pet_villager_farmer", False)

    @property
    def pet_villager_farmer_baby(self) -> bool:
        return getattr(self, "_pet_villager_farmer_baby", False)

    @property
    def pet_villager_librarian(self) -> bool:
        return getattr(self, "_pet_villager_librarian", False)

    @property
    def pet_villager_librarian_baby(self) -> bool:
        return getattr(self, "_pet_villager_librarian_baby", False)

    @property
    def pet_villager_priest(self) -> bool:
        return getattr(self, "_pet_villager_priest", False)

    @property
    def pet_villager_priest_baby(self) -> bool:
        return getattr(self, "_pet_villager_priest_baby", False)

    @property
    def pet_white_pug(self) -> bool:
        return getattr(self, "_pet_white_pug", False)

    @property
    def pet_white_rabbit(self) -> bool:
        return getattr(self, "_pet_white_rabbit", False)

    @property
    def pet_witch(self) -> bool:
        return getattr(self, "_pet_witch", False)

    @property
    def pet_wolf(self) -> bool:
        return getattr(self, "_pet_wolf", False)

    @property
    def pet_wolf_baby(self) -> bool:
        return getattr(self, "_pet_wolf_baby", False)

    @property
    def pet_zombie(self) -> bool:
        return getattr(self, "_pet_zombie", False)

    @property
    def pet_zombie_baby(self) -> bool:
        return getattr(self, "_pet_zombie_baby", False)

    @property
    def pet_zombie_villager(self) -> bool:
        return getattr(self, "_pet_zombie_villager", False)

    @property
    def pet_zombie_villager_baby(self) -> bool:
        return getattr(self, "_pet_zombie_villager_baby", False)

    @property
    def punchmessage_snowball(self) -> bool:
        return getattr(self, "_punchmessage_snowball", False)

    @property
    def rankcolor_black(self) -> bool:
        return getattr(self, "_rankcolor_black", False)

    @property
    def rankcolor_blue(self) -> bool:
        return getattr(self, "_rankcolor_blue", False)

    @property
    def rankcolor_dark_aqua(self) -> bool:
        return getattr(self, "_rankcolor_dark_aqua", False)

    @property
    def rankcolor_dark_gray(self) -> bool:
        return getattr(self, "_rankcolor_dark_gray", False)

    @property
    def rankcolor_dark_green(self) -> bool:
        return getattr(self, "_rankcolor_dark_green", False)

    @property
    def rankcolor_dark_purple(self) -> bool:
        return getattr(self, "_rankcolor_dark_purple", False)

    @property
    def rankcolor_dark_red(self) -> bool:
        return getattr(self, "_rankcolor_dark_red", False)

    @property
    def rankcolor_gold(self) -> bool:
        return getattr(self, "_rankcolor_gold", False)

    @property
    def rankcolor_green(self) -> bool:
        return getattr(self, "_rankcolor_green", False)

    @property
    def rankcolor_light_purple(self) -> bool:
        return getattr(self, "_rankcolor_light_purple", False)

    @property
    def rankcolor_white(self) -> bool:
        return getattr(self, "_rankcolor_white", False)

    @property
    def rankcolor_yellow(self) -> bool:
        return getattr(self, "_rankcolor_yellow", False)

    @property
    def suit_arctic_boots(self) -> bool:
        return getattr(self, "_suit_arctic_boots", False)

    @property
    def suit_arctic_chestplate(self) -> bool:
        return getattr(self, "_suit_arctic_chestplate", False)

    @property
    def suit_arctic_helmet(self) -> bool:
        return getattr(self, "_suit_arctic_helmet", False)

    @property
    def suit_arctic_leggings(self) -> bool:
        return getattr(self, "_suit_arctic_leggings", False)

    @property
    def suit_baker_boots(self) -> bool:
        return getattr(self, "_suit_baker_boots", False)

    @property
    def suit_baker_chestplate(self) -> bool:
        return getattr(self, "_suit_baker_chestplate", False)

    @property
    def suit_baker_helmet(self) -> bool:
        return getattr(self, "_suit_baker_helmet", False)

    @property
    def suit_baker_leggings(self) -> bool:
        return getattr(self, "_suit_baker_leggings", False)

    @property
    def suit_bumblebee_boots(self) -> bool:
        return getattr(self, "_suit_bumblebee_boots", False)

    @property
    def suit_bumblebee_chestplate(self) -> bool:
        return getattr(self, "_suit_bumblebee_chestplate", False)

    @property
    def suit_bumblebee_helmet(self) -> bool:
        return getattr(self, "_suit_bumblebee_helmet", False)

    @property
    def suit_bumblebee_leggings(self) -> bool:
        return getattr(self, "_suit_bumblebee_leggings", False)

    @property
    def suit_chicken_boots(self) -> bool:
        return getattr(self, "_suit_chicken_boots", False)

    @property
    def suit_chicken_chestplate(self) -> bool:
        return getattr(self, "_suit_chicken_chestplate", False)

    @property
    def suit_chicken_helmet(self) -> bool:
        return getattr(self, "_suit_chicken_helmet", False)

    @property
    def suit_chicken_leggings(self) -> bool:
        return getattr(self, "_suit_chicken_leggings", False)

    @property
    def suit_costume_boots(self) -> bool:
        return getattr(self, "_suit_costume_boots", False)

    @property
    def suit_costume_chestplate(self) -> bool:
        return getattr(self, "_suit_costume_chestplate", False)

    @property
    def suit_costume_helmet(self) -> bool:
        return getattr(self, "_suit_costume_helmet", False)

    @property
    def suit_costume_leggings(self) -> bool:
        return getattr(self, "_suit_costume_leggings", False)

    @property
    def suit_death_angel_boots(self) -> bool:
        return getattr(self, "_suit_death_angel_boots", False)

    @property
    def suit_death_angel_chestplate(self) -> bool:
        return getattr(self, "_suit_death_angel_chestplate", False)

    @property
    def suit_death_angel_helmet(self) -> bool:
        return getattr(self, "_suit_death_angel_helmet", False)

    @property
    def suit_death_angel_leggings(self) -> bool:
        return getattr(self, "_suit_death_angel_leggings", False)

    @property
    def suit_disco_boots(self) -> bool:
        return getattr(self, "_suit_disco_boots", False)

    @property
    def suit_disco_chestplate(self) -> bool:
        return getattr(self, "_suit_disco_chestplate", False)

    @property
    def suit_disco_helmet(self) -> bool:
        return getattr(self, "_suit_disco_helmet", False)

    @property
    def suit_disco_leggings(self) -> bool:
        return getattr(self, "_suit_disco_leggings", False)

    @property
    def suit_dragon_breath_boots(self) -> bool:
        return getattr(self, "_suit_dragon_breath_boots", False)

    @property
    def suit_dragon_breath_chestplate(self) -> bool:
        return getattr(self, "_suit_dragon_breath_chestplate", False)

    @property
    def suit_dragon_breath_helmet(self) -> bool:
        return getattr(self, "_suit_dragon_breath_helmet", False)

    @property
    def suit_dragon_breath_leggings(self) -> bool:
        return getattr(self, "_suit_dragon_breath_leggings", False)

    @property
    def suit_easter_egg_boots(self) -> bool:
        return getattr(self, "_suit_easter_egg_boots", False)

    @property
    def suit_easter_egg_chestplate(self) -> bool:
        return getattr(self, "_suit_easter_egg_chestplate", False)

    @property
    def suit_easter_egg_helmet(self) -> bool:
        return getattr(self, "_suit_easter_egg_helmet", False)

    @property
    def suit_easter_egg_leggings(self) -> bool:
        return getattr(self, "_suit_easter_egg_leggings", False)

    @property
    def suit_elf_boots(self) -> bool:
        return getattr(self, "_suit_elf_boots", False)

    @property
    def suit_elf_chestplate(self) -> bool:
        return getattr(self, "_suit_elf_chestplate", False)

    @property
    def suit_elf_helmet(self) -> bool:
        return getattr(self, "_suit_elf_helmet", False)

    @property
    def suit_elf_leggings(self) -> bool:
        return getattr(self, "_suit_elf_leggings", False)

    @property
    def suit_fireman_boots(self) -> bool:
        return getattr(self, "_suit_fireman_boots", False)

    @property
    def suit_fireman_chestplate(self) -> bool:
        return getattr(self, "_suit_fireman_chestplate", False)

    @property
    def suit_fireman_helmet(self) -> bool:
        return getattr(self, "_suit_fireman_helmet", False)

    @property
    def suit_fireman_leggings(self) -> bool:
        return getattr(self, "_suit_fireman_leggings", False)

    @property
    def suit_fish_monger_boots(self) -> bool:
        return getattr(self, "_suit_fish_monger_boots", False)

    @property
    def suit_fish_monger_chestplate(self) -> bool:
        return getattr(self, "_suit_fish_monger_chestplate", False)

    @property
    def suit_fish_monger_helmet(self) -> bool:
        return getattr(self, "_suit_fish_monger_helmet", False)

    @property
    def suit_fish_monger_leggings(self) -> bool:
        return getattr(self, "_suit_fish_monger_leggings", False)

    @property
    def suit_flash_boots(self) -> bool:
        return getattr(self, "_suit_flash_boots", False)

    @property
    def suit_flash_chestplate(self) -> bool:
        return getattr(self, "_suit_flash_chestplate", False)

    @property
    def suit_flash_helmet(self) -> bool:
        return getattr(self, "_suit_flash_helmet", False)

    @property
    def suit_flash_leggings(self) -> bool:
        return getattr(self, "_suit_flash_leggings", False)

    @property
    def suit_frog_boots(self) -> bool:
        return getattr(self, "_suit_frog_boots", False)

    @property
    def suit_frog_chestplate(self) -> bool:
        return getattr(self, "_suit_frog_chestplate", False)

    @property
    def suit_frog_helmet(self) -> bool:
        return getattr(self, "_suit_frog_helmet", False)

    @property
    def suit_frog_leggings(self) -> bool:
        return getattr(self, "_suit_frog_leggings", False)

    @property
    def suit_ghost_boots(self) -> bool:
        return getattr(self, "_suit_ghost_boots", False)

    @property
    def suit_ghost_chestplate(self) -> bool:
        return getattr(self, "_suit_ghost_chestplate", False)

    @property
    def suit_ghost_helmet(self) -> bool:
        return getattr(self, "_suit_ghost_helmet", False)

    @property
    def suit_ghost_leggings(self) -> bool:
        return getattr(self, "_suit_ghost_leggings", False)

    @property
    def suit_grinch_boots(self) -> bool:
        return getattr(self, "_suit_grinch_boots", False)

    @property
    def suit_grinch_chestplate(self) -> bool:
        return getattr(self, "_suit_grinch_chestplate", False)

    @property
    def suit_grinch_helmet(self) -> bool:
        return getattr(self, "_suit_grinch_helmet", False)

    @property
    def suit_grinch_leggings(self) -> bool:
        return getattr(self, "_suit_grinch_leggings", False)

    @property
    def suit_headless_horseman_boots(self) -> bool:
        return getattr(self, "_suit_headless_horseman_boots", False)

    @property
    def suit_headless_horseman_chestplate(self) -> bool:
        return getattr(self, "_suit_headless_horseman_chestplate", False)

    @property
    def suit_headless_horseman_helmet(self) -> bool:
        return getattr(self, "_suit_headless_horseman_helmet", False)

    @property
    def suit_headless_horseman_leggings(self) -> bool:
        return getattr(self, "_suit_headless_horseman_leggings", False)

    @property
    def suit_magma_boss_boots(self) -> bool:
        return getattr(self, "_suit_magma_boss_boots", False)

    @property
    def suit_magma_boss_chestplate(self) -> bool:
        return getattr(self, "_suit_magma_boss_chestplate", False)

    @property
    def suit_magma_boss_helmet(self) -> bool:
        return getattr(self, "_suit_magma_boss_helmet", False)

    @property
    def suit_magma_boss_leggings(self) -> bool:
        return getattr(self, "_suit_magma_boss_leggings", False)

    @property
    def suit_mermaid_boots(self) -> bool:
        return getattr(self, "_suit_mermaid_boots", False)

    @property
    def suit_mermaid_chestplate(self) -> bool:
        return getattr(self, "_suit_mermaid_chestplate", False)

    @property
    def suit_mermaid_helmet(self) -> bool:
        return getattr(self, "_suit_mermaid_helmet", False)

    @property
    def suit_mermaid_leggings(self) -> bool:
        return getattr(self, "_suit_mermaid_leggings", False)

    @property
    def suit_necromancer_boots(self) -> bool:
        return getattr(self, "_suit_necromancer_boots", False)

    @property
    def suit_necromancer_chestplate(self) -> bool:
        return getattr(self, "_suit_necromancer_chestplate", False)

    @property
    def suit_necromancer_helmet(self) -> bool:
        return getattr(self, "_suit_necromancer_helmet", False)

    @property
    def suit_necromancer_leggings(self) -> bool:
        return getattr(self, "_suit_necromancer_leggings", False)

    @property
    def suit_new_years_boots(self) -> bool:
        return getattr(self, "_suit_new_years_boots", False)

    @property
    def suit_new_years_chestplate(self) -> bool:
        return getattr(self, "_suit_new_years_chestplate", False)

    @property
    def suit_new_years_helmet(self) -> bool:
        return getattr(self, "_suit_new_years_helmet", False)

    @property
    def suit_new_years_leggings(self) -> bool:
        return getattr(self, "_suit_new_years_leggings", False)

    @property
    def suit_ninja_boots(self) -> bool:
        return getattr(self, "_suit_ninja_boots", False)

    @property
    def suit_ninja_chestplate(self) -> bool:
        return getattr(self, "_suit_ninja_chestplate", False)

    @property
    def suit_ninja_helmet(self) -> bool:
        return getattr(self, "_suit_ninja_helmet", False)

    @property
    def suit_ninja_leggings(self) -> bool:
        return getattr(self, "_suit_ninja_leggings", False)

    @property
    def suit_piglin_suit_boots(self) -> bool:
        return getattr(self, "_suit_piglin_suit_boots", False)

    @property
    def suit_piglin_suit_chestplate(self) -> bool:
        return getattr(self, "_suit_piglin_suit_chestplate", False)

    @property
    def suit_piglin_suit_helmet(self) -> bool:
        return getattr(self, "_suit_piglin_suit_helmet", False)

    @property
    def suit_piglin_suit_leggings(self) -> bool:
        return getattr(self, "_suit_piglin_suit_leggings", False)

    @property
    def suit_pirate_boots(self) -> bool:
        return getattr(self, "_suit_pirate_boots", False)

    @property
    def suit_pirate_chestplate(self) -> bool:
        return getattr(self, "_suit_pirate_chestplate", False)

    @property
    def suit_pirate_helmet(self) -> bool:
        return getattr(self, "_suit_pirate_helmet", False)

    @property
    def suit_pirate_leggings(self) -> bool:
        return getattr(self, "_suit_pirate_leggings", False)

    @property
    def suit_plumber_boots(self) -> bool:
        return getattr(self, "_suit_plumber_boots", False)

    @property
    def suit_plumber_chestplate(self) -> bool:
        return getattr(self, "_suit_plumber_chestplate", False)

    @property
    def suit_plumber_helmet(self) -> bool:
        return getattr(self, "_suit_plumber_helmet", False)

    @property
    def suit_plumber_leggings(self) -> bool:
        return getattr(self, "_suit_plumber_leggings", False)

    @property
    def suit_pumpkin_boots(self) -> bool:
        return getattr(self, "_suit_pumpkin_boots", False)

    @property
    def suit_pumpkin_chestplate(self) -> bool:
        return getattr(self, "_suit_pumpkin_chestplate", False)

    @property
    def suit_pumpkin_helmet(self) -> bool:
        return getattr(self, "_suit_pumpkin_helmet", False)

    @property
    def suit_pumpkin_leggings(self) -> bool:
        return getattr(self, "_suit_pumpkin_leggings", False)

    @property
    def suit_santa_boots(self) -> bool:
        return getattr(self, "_suit_santa_boots", False)

    @property
    def suit_santa_chestplate(self) -> bool:
        return getattr(self, "_suit_santa_chestplate", False)

    @property
    def suit_santa_helmet(self) -> bool:
        return getattr(self, "_suit_santa_helmet", False)

    @property
    def suit_santa_leggings(self) -> bool:
        return getattr(self, "_suit_santa_leggings", False)

    @property
    def suit_skeleton_samurai_boots(self) -> bool:
        return getattr(self, "_suit_skeleton_samurai_boots", False)

    @property
    def suit_skeleton_samurai_chestplate(self) -> bool:
        return getattr(self, "_suit_skeleton_samurai_chestplate", False)

    @property
    def suit_skeleton_samurai_helmet(self) -> bool:
        return getattr(self, "_suit_skeleton_samurai_helmet", False)

    @property
    def suit_skeleton_samurai_leggings(self) -> bool:
        return getattr(self, "_suit_skeleton_samurai_leggings", False)

    @property
    def suit_soccer_boots(self) -> bool:
        return getattr(self, "_suit_soccer_boots", False)

    @property
    def suit_soccer_chestplate(self) -> bool:
        return getattr(self, "_suit_soccer_chestplate", False)

    @property
    def suit_soccer_helmet(self) -> bool:
        return getattr(self, "_suit_soccer_helmet", False)

    @property
    def suit_soccer_leggings(self) -> bool:
        return getattr(self, "_suit_soccer_leggings", False)

    @property
    def suit_solar_boots(self) -> bool:
        return getattr(self, "_suit_solar_boots", False)

    @property
    def suit_solar_chestplate(self) -> bool:
        return getattr(self, "_suit_solar_chestplate", False)

    @property
    def suit_solar_helmet(self) -> bool:
        return getattr(self, "_suit_solar_helmet", False)

    @property
    def suit_solar_leggings(self) -> bool:
        return getattr(self, "_suit_solar_leggings", False)

    @property
    def suit_spiderman_boots(self) -> bool:
        return getattr(self, "_suit_spiderman_boots", False)

    @property
    def suit_spiderman_chestplate(self) -> bool:
        return getattr(self, "_suit_spiderman_chestplate", False)

    @property
    def suit_spiderman_helmet(self) -> bool:
        return getattr(self, "_suit_spiderman_helmet", False)

    @property
    def suit_spiderman_leggings(self) -> bool:
        return getattr(self, "_suit_spiderman_leggings", False)

    @property
    def suit_thor_boots(self) -> bool:
        return getattr(self, "_suit_thor_boots", False)

    @property
    def suit_thor_chestplate(self) -> bool:
        return getattr(self, "_suit_thor_chestplate", False)

    @property
    def suit_thor_helmet(self) -> bool:
        return getattr(self, "_suit_thor_helmet", False)

    @property
    def suit_thor_leggings(self) -> bool:
        return getattr(self, "_suit_thor_leggings", False)

    @property
    def suit_tnt_boots(self) -> bool:
        return getattr(self, "_suit_tnt_boots", False)

    @property
    def suit_tnt_chestplate(self) -> bool:
        return getattr(self, "_suit_tnt_chestplate", False)

    @property
    def suit_tnt_helmet(self) -> bool:
        return getattr(self, "_suit_tnt_helmet", False)

    @property
    def suit_tnt_leggings(self) -> bool:
        return getattr(self, "_suit_tnt_leggings", False)

    @property
    def suit_toy_boots(self) -> bool:
        return getattr(self, "_suit_toy_boots", False)

    @property
    def suit_toy_chestplate(self) -> bool:
        return getattr(self, "_suit_toy_chestplate", False)

    @property
    def suit_toy_helmet(self) -> bool:
        return getattr(self, "_suit_toy_helmet", False)

    @property
    def suit_toy_leggings(self) -> bool:
        return getattr(self, "_suit_toy_leggings", False)

    @property
    def suit_treasure_boots(self) -> bool:
        return getattr(self, "_suit_treasure_boots", False)

    @property
    def suit_treasure_helmet(self) -> bool:
        return getattr(self, "_suit_treasure_helmet", False)

    @property
    def suit_treasure_leggings(self) -> bool:
        return getattr(self, "_suit_treasure_leggings", False)

    @property
    def suit_vampire_boots(self) -> bool:
        return getattr(self, "_suit_vampire_boots", False)

    @property
    def suit_vampire_chestplate(self) -> bool:
        return getattr(self, "_suit_vampire_chestplate", False)

    @property
    def suit_vampire_helmet(self) -> bool:
        return getattr(self, "_suit_vampire_helmet", False)

    @property
    def suit_vampire_leggings(self) -> bool:
        return getattr(self, "_suit_vampire_leggings", False)

    @property
    def suit_warrior_boots(self) -> bool:
        return getattr(self, "_suit_warrior_boots", False)

    @property
    def suit_warrior_chestplate(self) -> bool:
        return getattr(self, "_suit_warrior_chestplate", False)

    @property
    def suit_warrior_helmet(self) -> bool:
        return getattr(self, "_suit_warrior_helmet", False)

    @property
    def suit_warrior_leggings(self) -> bool:
        return getattr(self, "_suit_warrior_leggings", False)

    @property
    def suit_wolf_boots(self) -> bool:
        return getattr(self, "_suit_wolf_boots", False)

    @property
    def suit_wolf_chestplate(self) -> bool:
        return getattr(self, "_suit_wolf_chestplate", False)

    @property
    def suit_wolf_helmet(self) -> bool:
        return getattr(self, "_suit_wolf_helmet", False)

    @property
    def suit_wolf_leggings(self) -> bool:
        return getattr(self, "_suit_wolf_leggings", False)

    @property
    def suit_yeti_boots(self) -> bool:
        return getattr(self, "_suit_yeti_boots", False)

    @property
    def suit_yeti_chestplate(self) -> bool:
        return getattr(self, "_suit_yeti_chestplate", False)

    @property
    def suit_yeti_helmet(self) -> bool:
        return getattr(self, "_suit_yeti_helmet", False)

    @property
    def suit_yeti_leggings(self) -> bool:
        return getattr(self, "_suit_yeti_leggings", False)

    @property
    def taunt_ballet(self) -> bool:
        return getattr(self, "_taunt_ballet", False)

    @property
    def taunt_can(self) -> bool:
        return getattr(self, "_taunt_can", False)

    @property
    def taunt_clapping(self) -> bool:
        return getattr(self, "_taunt_clapping", False)

    @property
    def taunt_cool_dance(self) -> bool:
        return getattr(self, "_taunt_cool_dance", False)

    @property
    def taunt_crab_dance(self) -> bool:
        return getattr(self, "_taunt_crab_dance", False)

    @property
    def taunt_goodbye(self) -> bool:
        return getattr(self, "_taunt_goodbye", False)

    @property
    def taunt_graduation(self) -> bool:
        return getattr(self, "_taunt_graduation", False)

    @property
    def taunt_hi_5(self) -> bool:
        return getattr(self, "_taunt_hi_5", False)

    @property
    def taunt_hula(self) -> bool:
        return getattr(self, "_taunt_hula", False)

    @property
    def taunt_hype_dance(self) -> bool:
        return getattr(self, "_taunt_hype_dance", False)

    @property
    def taunt_jump(self) -> bool:
        return getattr(self, "_taunt_jump", False)

    @property
    def taunt_karaoke(self) -> bool:
        return getattr(self, "_taunt_karaoke", False)

    @property
    def taunt_mind(self) -> bool:
        return getattr(self, "_taunt_mind", False)

    @property
    def taunt_possessed(self) -> bool:
        return getattr(self, "_taunt_possessed", False)

    @property
    def taunt_snowball_toss(self) -> bool:
        return getattr(self, "_taunt_snowball_toss", False)

    @property
    def taunt_sun(self) -> bool:
        return getattr(self, "_taunt_sun", False)

    @property
    def taunt_treasure(self) -> bool:
        return getattr(self, "_taunt_treasure", False)

    @property
    def taunt_victory(self) -> bool:
        return getattr(self, "_taunt_victory", False)

    @property
    def taunt_wave_dance(self) -> bool:
        return getattr(self, "_taunt_wave_dance", False)

    @property
    def taunt_zombie_dance(self) -> bool:
        return getattr(self, "_taunt_zombie_dance", False)
