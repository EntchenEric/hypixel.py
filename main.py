from hypixel import Hypixel
import asyncio

Hypixel = Hypixel("035b8caf-5f2f-4f9e-ae9f-c09212005ff0")


async def main():
    player = await Hypixel.get_player("d33671f7baf14e95a027377ae6ed5efb")
    player = await Hypixel.get_player("e23eb596934c456ab8c740c2a951b3fc")
    player = await Hypixel.get_player("fe15273ac6604a6f95daee3f9458eeba")
    player = await Hypixel.get_player("383a081f6dc04ac0bb951f8d50c3e532")
    player = await Hypixel.get_player("23f55db9a6154d83a63a152e1b1315f5")
    player = await Hypixel.get_player("8a7ce3df6a4b4befad4e42028efe19cc")
    print(player.display_name)
    print(player.rank)
    print(player.stats.bedwars)
    print(player.stats.bedwars.kills)
    print(player.achievement_progress.arcade_arcade_banker)
    print(player.achievements.skyblock_end_race)
    print(player.pet_consumables.carrot_item)

if __name__ == "__main__":
    asyncio.run(main())
