import json
from pathlib import Path

all_achievements = set()
player_jsons_dir = Path("playerJsons")

player_jsons_dir.mkdir(exist_ok=True)

for json_file in player_jsons_dir.glob("*.json"):
    with open(json_file, "r") as f:
        player_data = json.load(f)
        if "vanityMeta" in player_data:
            all_achievements.update(player_data["vanityMeta"]["packages"])

achievements_file = Path("classes/vanity_meta.py").read_text()

existing_achievements = set()
for line in achievements_file.splitlines():
    if line.startswith("    def ") and "self" in line:
        achievement = line.split("def ")[1].split("(")[0]
        existing_achievements.add(achievement)

missing_achievements = set()
for achievement in all_achievements:
    property_name = achievement.replace("-", "_")
    if property_name not in existing_achievements:
        missing_achievements.add(achievement)

missing_achievements = sorted(missing_achievements)

property_template = """    @property
    def {property_name}(self) -> bool:
        return getattr(self, "_{safe_name}", False)
"""

print("# Add these properties to the Achievements class:")
print()
for achievement in missing_achievements:
    property_name = achievement.replace("-", "_")
    safe_name = achievement.replace("-", "_")
    print(
        property_template.format(
            property_name=property_name,
            safe_name=safe_name,
        )
    )
