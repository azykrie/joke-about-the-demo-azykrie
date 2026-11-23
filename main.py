from pathlib import Path

JOKE = "Placeholder joke, revised below."

out = Path("/output/entry.txt")
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(JOKE + "\n", encoding="utf-8")
