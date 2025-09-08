import json
from pathlib import Path

# Original data (restructured into a Python dict)
universe_lore = {
    "Category_1_Planets": {
        "Virella": {
            "Role": "Home of the Dawnbound Creed",
            "Inhabitants": "All major species",
            "Political Alignment": "Independent religious theocracy",
            "Notes": "Strict spiritual order, highly militarized channeler training"
        },
        "Sersai": {
            "Role": "Home of the Arcanum of the Veil",
            "Inhabitants": "All major species",
            "Political Alignment": "Independent religious theocracy",
            "Notes": "Espouses individual enlightenment through the Entity, in constant ideological conflict with Virella"
        },
        "Nuvia": {
            "Role": "Trade-focused capitalist republic",
            "Inhabitants": "All species",
            "Political Alignment": "Coalition Member",
            "Notes": "Acts as neutral economic power, major trading hub"
        },
        "Dravon": {
            "Role": "Divided war-world",
            "Inhabitants": "Giantfolk (surface), Delverkin (underground)",
            "Political Alignment": "Coalition Member",
            "Notes": "Internal civil war, holds 4 council seats (2 each side)"
        },
        "Takkir": {
            "Role": "Recently revealed Zai'kir hive world",
            "Inhabitants": "Zai’kir only (insectoid)",
            "Political Alignment": "New Coalition Member",
            "Notes": "Strange culture, a splinter hive has formed a religious faction tied to the Entity"
        }
    },
    "Category_2_Religions_and_Factions": {
        "Dawnbound Creed": {
            "Belief": "The Entity is divine structure, best used in unity and discipline",
            "Traits": "Radiance, order, martial virtue",
            "Planet": "Virella"
        },
        "Arcanum of the Veil": {
            "Belief": "The Entity is personal, mysterious, and best explored individually",
            "Traits": "Dreams, psionics, mystery",
            "Planet": "Sersai"
        },
        "Coalition of Three": {
            "Members": ["Nuvia", "Dravon", "Takkir"],
            "Purpose": "Mutual defense, economic unity, limiting religious war escalation"
        },
        "Zai'kir Cell": {
            "Status": "Unclaimed by either major order",
            "Belief": "The Entity is a unifying psychic song",
            "Planet": "Takkir"
        }
    },
    "Category_3_Historical_Conflicts": {
        "Age of Awakening": {
            "Event": "First channelers appear; religious divisions form",
            "Notable": "Sixth planet destroyed by Arcanum mystic in final battle",
            "Result": "Both Orders scarred; limits of Entity-channelling realized"
        }
    },
    "Category_4_Technology_and_Channeling": {
        "Technology Level": {
            "General": "Slightly above modern Earth",
            "Key Features": ["Jetpacks", "Powered armor", "Energy weapons", "Basic space travel"]
        },
        "Entity Use": {
            "Population": "Approx. 1 million users among trillions",
            "Abilities": ["Flight", "Teleportation", "Mass manipulation", "Psionic control", "Radiant weapons"],
            "Rarity": "Extremely rare, highly trained or chosen"
        },
        "Training Systems": {
            "Dawnbound": "Martial discipline, radiant focus",
            "Arcanum": "Dreamwalking, emotion and memory control",
            "Other Worlds": "Some local traditions exist, mostly martial or espionage-based"
        }
    },
    "Category_5_Species_and_Sapient_Life": {
        "Humans": "Most populous species; adaptable and politically diverse",
        "Giantfolk": "Towering humanoids, live on surface of Dravon",
        "Delverkin": "Subterranean humanoids with echo-based senses and culture",
        "Zai'kir": "Insectoid species, hive-based with psionic queens",
        "Ratfolk": "Scavenger-like, specialize in tech repair and salvage"
    },
    "Category_6_Everyday_Life": {
        "Virella": "Structured, militarized, spiritual pilgrimage sites common",
        "Sersai": "Dream temples, decentralized communes, shadow markets",
        "Nuvia": "Corporate megacities, cyber fashion, constant trade",
        "Dravon": {
            "Giantfolk": "Tribal fortresses, honor-based societies",
            "Delverkin": "Underground cities, secrecy and stealth norms"
        },
        "Takkir": "Hive cities, pheromonal communication zones, psychic relay towers"
    },
    "Category_7_Space_Stations_and_Trade": {
        "Spacestations": [
            "Relay Spires – Military & cargo stops between planets",
            "Ghost Arcs – Abandoned or pirate-claimed trade hubs",
            "Solar Netway – Dawnbound’s communication and energy web",
            "The Spindle – Coalition HQ and diplomacy nexus"
        ]
    },
    "Category_8_Mythic_and_Living_Legends": {
        "Mythic Heroes": {
            "Dawnbound": "Eidon the Blazing, Entity-wielder who died ending the Age of Awakening",
            "Arcanum": "Kelyx the Silent, whose dreamwalker spirit is said to still influence minds",
            "Zai'kir": "Zithyr Queen Eternal, mythical Zai’kir that whispered the first command",
            "Dravon": "Torrok & Sevrak, sibling warriors that split the planet in half",
            "Nuvia": "The Gilded Trickster, founder of the first interplanetary black market"
        },
        "Living Legends": {
            "Virella": "Lady Calyra the Silver Flame",
            "Sersai": "Syra the Dreamweaver",
            "Nuvia": "Selira Ghostblade",
            "Dravon": ["King Gorrath", "Sevrin of the Thousand Echoes"],
            "Takkir": "Queen Ithara of the Broken Chorus"
        }
    },
    "Category_9_Warfare_and_Conflict": {
        "Common Conflicts": ["Resource raiding", "Orbital skirmishes", "Religious proxy wars", "Political sabotage"],
        "Major Flashpoints": [
            "Dravon civil war",
            "Zai’kir independence",
            "Religious cold war between Dawnbound and Arcanum"
        ],
        "Notable Groups": {
            "Ashen Circle": "Psychopathic rogue Channelers controlled by a manipulator known as The Shepherd",
            "Veilbreakers": "Mysterious, unaffiliated Channeler-hunters feared across all planets",
            "Fangspire Company": "Mercenary army led by Lucien Vale, unaffiliated but deeply influential"
        }
    }
}

# Save each category into a separate file

output_dir = Path(__file__).parent
output_dir.mkdir(parents=True, exist_ok=True)
file_paths = []

for category, content in universe_lore.items():
    file_name = f"{category}.json"
    path = output_dir / file_name
    with open(path, "w") as f:
        json.dump({category: content}, f, indent=2)
    file_paths.append(path)

file_paths
