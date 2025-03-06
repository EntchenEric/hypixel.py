class Rank:
    DEFAULT = ("PLAYER", "", "§7")
    VIP = ("VIP", "VIP", "§a")
    VIP_PLUS = ("VIP+", "VIP+", "§a")
    MVP = ("MVP", "MVP", "§b")
    MVP_PLUS = ("MVP+", "MVP+", "§b")
    MVP_PLUS_PLUS = ("MVP++", "MVP++", "§6")

    HELPER = ("HELPER", "HELPER", "§9")
    MODERATOR = ("MODERATOR", "MOD", "§2")
    ADMIN = ("ADMIN", "ADMIN", "§c")

    YOUTUBE = ("YOUTUBE", "YOUTUBE", "§c")

    def __init__(self, name: str, prefix: str, color: str):
        self.name = name
        self.prefix = prefix
        self.color = color

    def __str__(self):
        if self.prefix:
            return f"{self.color}[{self.prefix}] {self.name}"
        return f"{self.color}{self.name}"

    @classmethod
    def from_api(cls, rank_str: str):
        """Convert API rank string to Rank enum"""
        if not rank_str or rank_str == "NONE":
            return cls(*cls.DEFAULT)

        rank_str = str(rank_str).upper()
        try:
            rank_tuple = getattr(cls, rank_str)
            return cls(*rank_tuple)
        except AttributeError:
            return cls(*cls.DEFAULT)
