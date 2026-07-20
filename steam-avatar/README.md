# Geralt Steam Avatar

Original stylized fan art of Geralt of Rivia (The Witcher) — a front-facing portrait
looking straight at the viewer, ember-lit like the quiet ending scene: white hair and
beard, amber cat eyes, the scar over his left brow, and the wolf-school medallion.

Hand-built as a single SVG (no AI image generation, no copied artwork) and rendered
to PNG with headless Chromium.

## Files

| File | Purpose |
|------|---------|
| `geralt-steam-avatar.png` | 1024×1024 portrait version (full stylized face) |
| `geralt-steam-avatar-dark.png` | 1024×1024 dark version — ember-rimmed silhouette, glowing cat eyes |
| `geralt-steam-avatar-184.png` | 184×184 preview (Steam's profile display size) |
| `source/geralt.svg` | Editable vector source (portrait) |
| `source/geralt-dark.svg` | Editable vector source (dark variant) |
| `source/PHILOSOPHY.md` | The "Ember Vigil" design philosophy behind the pieces |

## How to set it as your Steam avatar

1. Download `geralt-steam-avatar.png` from this folder.
2. Open Steam (app or [steamcommunity.com](https://steamcommunity.com)) and log in.
3. Click your username (top right) → **View my profile** → **Edit Profile**.
4. Choose **Avatar** in the left sidebar.
5. Click **Upload your avatar**, pick the PNG, and hit **Save**.

Steam scales it down automatically; the image is already square so no cropping is needed.

## Tweaking

Edit `source/geralt.svg` and re-render:

```bash
chromium --headless=new --hide-scrollbars --window-size=1024,1024 \
  --screenshot=geralt-steam-avatar.png "file://$PWD/source/geralt.svg"
```
