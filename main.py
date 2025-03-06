from hypixel import Hypixel
import asyncio

Hypixel = Hypixel("035b8caf-5f2f-4f9e-ae9f-c09212005ff0")


async def main():
    player = await Hypixel.get_player("992daae1237b4459bb82b26332c9fbd9")
    print(player.display_name)
    print(player.rank)
    print(player.stats.bedwars)
    print(player.stats.bedwars.kills)
    print(player.achievement_progress.arcade_arcade_banker)
    print(player.achievements.skyblock_end_race)
    print(player.pet_consumables.carrot_item)

if __name__ == "__main__":
    asyncio.run(main())
