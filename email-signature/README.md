# Flowline Ops Gmail signature (light + dark mode)

## Why the old signature broke in dark mode
- **Logo has a transparent background.** Its navy "FLOWLINE OPERATIONS" text sits on whatever the reader's background is. On dark mode that is near-black, so the text disappears.
- **Icons were HubSpot images** with a blue background faked by CSS. Gmail strips that CSS, so the icons sit in black boxes.
- **Font fell back to Times New Roman** because the HubSpot table set it.
- **Links were forced to pure black** and the old block carried empty HubSpot rows and an extra divider line.

## What the new signature does
- No icon images. Small blue letters (M, E, W, A) label each line, so nothing can vanish.
- Text uses a soft near-black, never pure black. Dark-mode apps, including the Gmail app, flip it to white automatically.
- Accent colour is a mid-blue that reads on both white and black backgrounds.
- Arial throughout, no underlines, phone written in a readable format.

## Install (5 minutes, on a computer)
1. Open `signature.html` in Chrome.
2. Press Ctrl+A (Cmd+A on Mac), then Ctrl+C.
3. In Gmail, go to Settings, See all settings, General, Signature.
4. Delete the old signature completely, then paste.
5. **Add the logo.** In the signature box, highlight the word LOGO. Click Insert image, choose My Drive, and pick `Flowline Operations Logo.png`. Set its size to Small. That file has a solid background, so it shows as a clean tile in dark mode.
6. Save changes at the bottom of the page.

## Test it
Send yourself an email and open it in the Gmail app with dark mode on, and in Gmail on desktop.
