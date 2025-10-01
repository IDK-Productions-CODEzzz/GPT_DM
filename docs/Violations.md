# Violations Report

## JSON Files/master.json
- Converted every object key to lowercase `snake_case` so nested structures now comply with the repository's naming convention (for example, `Lorebook` → `lorebook`, `Planets` → `planets`, and `Virella` → `virella`).
- Normalized abbreviations while preserving meaning, correcting keys such as `Standard_DC` → `standard_dc`, `DM_Difficulty_Scaling` → `dm_difficulty_scaling`, and `At_0_HP` → `at_0_hp`.
- Replaced numbered turn-phase keys with readable snake_case identifiers (`"1"`, `"2"`, `"3"` → `step_1`, `step_2`, `step_3`) to eliminate bare numeric keys inside objects.
- Cleaned string content by swapping curly punctuation and special symbols (e.g., `\u2019`, `\u2014`, `→`, `×`) for ASCII-friendly characters so values no longer contain typographic glyphs.
- Updated keys containing punctuation to snake_case-friendly forms (`Zai'kir Cell` → `zai_kir_cell`, `Space_Stations_and_Trade` → `space_stations_and_trade`, etc.) and ensured all apostrophes in keys now use underscores instead of disallowed characters.
