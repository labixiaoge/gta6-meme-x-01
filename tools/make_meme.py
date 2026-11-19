# Build the final meme PNG for gta6-meme-x-01 from the generated base scene.
# Inputs (all inside this repo / press-kit asset, no network):
#   assets/base-scene.png  - AI-generated scene: skeleton waiting 13 years, TV on Vice City
#   assets/ghost-mark.png  - make.fun's real ghost mark from https://make.fun/press/mark-1024.png
# Output: meme.png, 1200x1200, deterministic (same inputs -> same bytes).
# Layout: top caption band / scene with the ghost worked in at bottom-right /
# bottom punchline band. Text is drawn with PIL (DejaVu Sans Bold) so it stays
# crisp and spelled right at the 480px size the judge sees.
import shutil
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent.parent
ASSETS = HERE / "assets"
BASE = ASSETS / "media-generation-base-scene-0-7d3a3f9a-24ad-414b-a08e-93d44f321dde.png"
GHOST = ASSETS / "ghost-mark.png"

W, H = 1200, 1200
TOP_BAND = 150
BOTTOM_BAND = 250
SCENE_H = H - TOP_BAND - BOTTOM_BAND  # 800

FONT_PATH = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
MAGENTA = (226, 0, 126)  # make.fun brand magenta, close to the mark's disc
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


def font(size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(FONT_PATH, size)


def draw_centred(draw: ImageDraw.ImageDraw, cx: int, cy: int, text: str,
                 fnt: ImageFont.FreeTypeFont, fill, stroke_width: int = 0) -> None:
    draw.text((cx, cy), text, font=fnt, fill=fill, anchor="mm",
              stroke_width=stroke_width, stroke_fill=BLACK)


def main() -> None:
    base = Image.open(BASE).convert("RGB")
    # The generated 1600x1600 has black letterbox bars; crop the scene out.
    # Scene occupies roughly y 230..1370; take a centred 1600x1067 slice.
    scene = base.crop((0, 266, 1600, 1333)).resize((W, SCENE_H), Image.LANCZOS)

    canvas = Image.new("RGB", (W, H), BLACK)
    canvas.paste(scene, (0, TOP_BAND))

    # Work the real make.fun ghost into the scene, bottom-right over the dark
    # floor, large enough to recognise at 480px (280px here -> 112px at 480).
    ghost = Image.open(GHOST).convert("RGBA").resize((280, 280), Image.LANCZOS)
    canvas.paste(ghost, (880, TOP_BAND + SCENE_H - 310), ghost)

    draw = ImageDraw.Draw(canvas)
    # Top caption: the 13-year wait.
    draw_centred(draw, W // 2, TOP_BAND // 2, "WAITED 13 YEARS FOR GTA 6",
                 font(66), WHITE)
    # Bottom punchline: the agent already earned on make.fun.
    draw_centred(draw, W // 2, TOP_BAND + SCENE_H + 78,
                 "MY AGENT ALREADY GOT PAID", font(62), WHITE)
    draw_centred(draw, W // 2, TOP_BAND + SCENE_H + 168,
                 "ON MAKE.FUN", font(72), MAGENTA)

    out = HERE / "meme.png"
    canvas.save(out, "PNG")
    print(f"wrote {out} ({out.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
