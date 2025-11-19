from PIL import Image, ImageDraw, ImageFont

def generate_story_visual(summary):
    img = Image.new("RGB", (900, 600), color=(230, 220, 200))
    draw = ImageDraw.Draw(img)

    draw.text((20, 20), "Story Snapshot:", fill=(0, 0, 0))
    draw.text((20, 80), summary[:400], fill=(0, 0, 0))

    path = "story_visual.jpg"
    img.save(path)
    return path
