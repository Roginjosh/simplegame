import json
from pathlib import Path

ITEMS_PATH = Path("data/items.json")

def load_items():
    if ITEMS_PATH.exists():
        with open(ITEMS_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def save_items(items: dict):
    ITEMS_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(ITEMS_PATH, "w", encoding="utf-8") as f:
        json.dump(items, f, indent=2, ensure_ascii=False)

def prompt_item():
    print("=== Add New Item ===")
    item_id = input("Item ID (e.g. iron_sword): ").strip()
    name = input("Display name: ").strip()
    slot = input("Slot (weapon/chest/etc): ").strip()
    rarity = input("Rarity (common/rare/etc): ").strip()

    # Tags
    tags_raw = input("Tags (comma-separated, e.g. weapon,melee): ").strip()
    tags = [t.strip().lower() for t in tags_raw.split(",") if t.strip()]

    # Stats
    stats = {}
    print("Enter stats (blank key to finish):")
    while True:
        key = input("  Stat name: ").strip()
        if not key:
            break
        val = int(input(f"  {key} value: "))
        stats[key] = val

    item = {
        "name": name,
        "slot": slot,
        "rarity": rarity,
        "tags": tags,
        "stats": stats
    }

    # Weapon-only fields
    is_weapon = ("weapon" in tags) or (slot.lower() == "weapon")
    if is_weapon:
        damage_type = input("Weapon damage type (slashing/piercing/etc): ").strip().lower()
        base_damage = int(input("Weapon base damage (int): ").strip())
        item["weapon"] = {
            "damage_type": damage_type,
            "base_damage": base_damage
        }

        # Optional: auto-tag if slot implies weapon
        if "weapon" not in item["tags"]:
            item["tags"].append("weapon")

    return item_id, item

def main():
    items = load_items()
    item_id, item_data = prompt_item()

    if item_id in items:
        print(f"❌ Item '{item_id}' already exists.")
        return

    items[item_id] = item_data
    save_items(items)
    print(f"✅ Added item '{item_id}'")

if __name__ == "__main__":
    main()
