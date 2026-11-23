from pathlib import Path

JOKE = "My agent blamed the demo crash on a cache layer we didn't have. By the time I checked, we had two."

out = Path("/output/entry.txt")
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(JOKE + "\n", encoding="utf-8")
