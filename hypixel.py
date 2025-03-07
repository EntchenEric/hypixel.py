from config import BASE_URL
from classes.player import Player
import aiohttp
import json


class Hypixel:
    def __init__(self, api_key: str):
        self.api_key = api_key

    async def get_player(self, uuid: str) -> Player:
        url = f"{BASE_URL}/player?key={self.api_key}&uuid={uuid}"
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                data = await response.json()
                if data["success"]:
                    player = data["player"]
                    # Save raw player data to JSON file
                    with open(f"playerJsons/player_{uuid}.json", "w") as f:
                        json.dump(player, f, indent=4)

                    return Player(
                        _id=player["_id"],
                        uuid=player["uuid"],
                        display_name=player["displayname"],
                        rank=player["rank"] if "rank" in player else "player",
                        package_rank=(
                            player["packageRank"] if "packageRank" in player
                            else None
                        ),
                        new_package_rank=(
                            player["newPackageRank"]
                            if "newPackageRank" in player
                            else None
                        ),
                        monthly_package_rank=(
                            player["monthlyPackageRank"]
                            if "monthlyPackageRank" in player
                            else None
                        ),
                        first_login=player.get("firstLogin", 0),
                        last_login=player.get(
                            "lastLogin", 0
                        ),
                        last_logout=player.get(
                            "lastLogout", 0
                        ),
                        stats=player["stats"],
                        achievements=player.get("achievementsOneTime", {}),
                        achievement_progress=player.get(
                            "achievements", {}
                        ),
                        networkExp=player.get("networkExp", 0),
                        spec_auto_teleport=player.get(
                            "spec_auto_teleport", False
                        ),
                        spec_always_flying=player.get(
                            "spec_always_flying", False
                        ),
                        karma=player.get("karma", 0),
                        pet_consumables=player.get("petConsumables", {}),
                        network_update_book=player.get(
                            "networkUpdateBook", ""
                        ),
                        last_adsense_generate_time=player.get(
                            "lastAdsenseGenerateTime", 0
                        ),
                        achievement_points=player.get(
                            "achievementPoints", 0
                        ),
                        user_language=player.get("userLanguage", "ENGLISH"),
                        last_claimed_reward=player.get(
                            "lastClaimedReward", 0
                        ),
                        reward_high_score=player.get("rewardHighScore", 0),
                        reward_score=player.get("rewardScore", 0),
                        reward_streak=player.get("rewardStreak", 0),
                        total_daily_rewards=player.get(
                            "totalDailyRewards", 0
                        ),
                        total_rewards=player.get("totalRewards", 0),
                        level_up_vip=player.get("levelUpVIP", 0),
                        claimed_potato_talisman=player.get(
                            "claimed_potato_talisman", 0
                        ),
                        adsense_tokens=player.get("adsense_tokens", 0),
                        skyblock_free_cookie=player.get(
                            "skyblock_free_cookie", 0
                        ),
                        scorpius_bribe_96=player.get("scorpius_bribe_96", 0),
                        claimed_century_cake=player.get(
                            "claimed_century_cake", 0
                        ),
                        level_up_vip_plus=player.get(
                            "levelUp_VIP_PLUS", 0
                        ),
                        vanity_favorites=player.get("vanityFavorites", {}),
                        level_up_mvp_plus=player.get(
                            "levelUp_MVP_PLUS", 0
                        ),
                        rank_plus_color=player.get("rankPlusColor", ""),
                        current_pet=player.get("currentPet", ""),
                        claimed_year143_cake=player.get(
                            "claimed_year143_cake", 0
                        ),
                        channel=player.get("channel", ""),
                        claimed_century_cake2000=player.get(
                            "claimed_century_cake2000", 0
                        ),
                        most_recent_game_type=player.get(
                            "mostRecentGameType", ""
                        ),
                        fortune_buff=player.get("fortuneBuff", 0),
                    )
                else:
                    raise Exception("Failed to get player")
