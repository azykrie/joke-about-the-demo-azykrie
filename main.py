"""Write the one-line demo-crash joke to /output/entry.txt."""

from pathlib import Path

JOKE = "My agent blamed the demo crash on a cache layer we didn't have. By the time I checked, we had two."

OUTPUT_PATH = Path("/output/entry.txt")
OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
OUTPUT_PATH.write_text(JOKE + "\n", encoding="utf-8")
