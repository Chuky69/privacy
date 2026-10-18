# Flowline Ops Gmail signature (light + dark mode)

## Why the old signature broke in dark mode
- **Logo has a transparent background.** Its navy "FLOWLINE OPERATIONS" text sits on whatever the reader's background is. On dark mode that is near-black, so the text disappears.
- **Icons were HubSpot images** with a blue background faked by CSS. Gmail strips that CSS, so the icons sit in black boxes.
- **Font fell back to Times New Roman** because the HubSpot table set it.
- **Links were forced to pure black** and the old block carried empty HubSpot rows and an extra divider line.

## What the new signature does
Built from the Flowline Operations Brand Book.
- **Colours:** Graphite `#374151` for text, Cyan Blue `#06b6d4` for title, icons, divider and website, Cyan, Lime Green `#84cc16` and Warm Coral `#f97316` in the accent bar, and Warm Coral for the call-to-action button.
- **Font:** Poppins, then Montserrat, then Arial. Most email apps don't load web fonts, so many readers will see Arial.
- **Tagline:** "Designed to Flow. Built to Profit."
- **Booking button** links to your Calendly. Delete it in the signature editor if you don't want it.
- Icons are cyan circles with white text symbols: an outline phone (no emoji version exists), @ in Arial, a house and a pin.
- Graphite text is dark enough that dark-mode apps, including the Gmail app, flip it to light automatically.
- **Legal footer:** company name, CRO no. 822462, registered office, and VAT no. Irish Companies Act 2014, section 151, requires company details on business letters, and the corporate enforcement regulator advises including them on emails. Directors were left out at the owner's request.
- **Confidentiality and GDPR note:** asks misdirected recipients to delete the email and gives an email address for data requests. Add a link to a privacy page once one is live on flowlineops.com.
- To change anything, edit `build.py` and run `python3 build.py`.

## Install (on a computer)
1. Copy the signature from the Gmail draft (or open `signature.html` in Chrome), from your name to the end of the grey text.
2. In Gmail, go to Settings, See all settings, General, Signature. Delete the old signature and paste.
3. Click the **LOGO** box, delete it, click the image icon, choose **Upload**, pick `upload/flowline-logo.png`, then click the logo and choose **Original size**.
4. Click **Save Changes** at the bottom of the page.

Icons are text symbols in cyan circles, so they paste straight in. The logo has to be uploaded because Gmail strips images hosted elsewhere.

## Test it
Send yourself an email and open it in the Gmail app with dark mode on, and in Gmail on desktop.
