class PetConsumables:
    """Class representing a player"s pet consumables"""

    def __init__(self, pet_consumables: dict):
        for name, progress in pet_consumables.items():
            safe_name = name.replace("-", "_")
            setattr(self, f"_{safe_name.lower()}", progress)

    @property
    def carrot_item(self) -> int:
        return getattr(self, "_carrot_item", 0)

    @property
    def cookie(self) -> int:
        return getattr(self, "_cookie", 0)

    @property
    def feather(self) -> int:
        return getattr(self, "_feather", 0)

    @property
    def slime_ball(self) -> int:
        return getattr(self, "_slime_ball", 0)

    @property
    def red_rose(self) -> int:
        return getattr(self, "_red_rose", 0)

    @property
    def water_bucket(self) -> int:
        return getattr(self, "_water_bucket", 0)

    @property
    def wood_sword(self) -> int:
        return getattr(self, "_wood_sword", 0)

    @property
    def milk_bucket(self) -> int:
        return getattr(self, "_milk_bucket", 0)

    @property
    def pork(self) -> int:
        return getattr(self, "_pork", 0)

    @property
    def pumpkin_pie(self) -> int:
        return getattr(self, "_pumpkin_pie", 0)

    @property
    def LEASH(self) -> int:
        return getattr(self, "_leash", 0)

    @property
    def lava_bucket(self) -> int:
        return getattr(self, "_lava_bucket", 0)

    @property
    def magma_cream(self) -> int:
        return getattr(self, "_magma_cream", 0)

    @property
    def apple(self) -> int:
        return getattr(self, "_apple", 0)

    @property
    def wheat(self) -> int:
        return getattr(self, "_wheat", 0)

    @property
    def melon(self) -> int:
        return getattr(self, "_melon", 0)

    @property
    def stick(self) -> int:
        return getattr(self, "_stick", 0)

    @property
    def gold_record(self) -> int:
        return getattr(self, "_gold_record", 0)

    @property
    def bone(self) -> int:
        return getattr(self, "_bone", 0)

    @property
    def baked_potato(self) -> int:
        return getattr(self, "_baked_potato", 0)

    @property
    def bread(self) -> int:
        return getattr(self, "_bread", 0)
