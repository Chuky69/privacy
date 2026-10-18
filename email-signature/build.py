"""Builds signature.html from the Flowline Operations Brand Book palette.
Run: python3 build.py
Gmail's editor strips images hosted elsewhere, so the signature carries numbered
placeholders. After pasting it into Gmail's signature settings, replace each one
with the matching file from upload/ (Insert image > Upload > Original size)."""
import sys, pathlib
HERE = pathlib.Path(__file__).parent
GRAPHITE, CYAN, LIME, CORAL = "#374151", "#06b6d4", "#84cc16", "#f97316"
MUTED = "#6B7280"
FONT = "Poppins,Montserrat,Arial,Helvetica,sans-serif"

# Companies Act 2014, s.151(2): company details on business letters (ODCE says emails too).
# Directors (s.151(1)) left out at the owner's request.
COMPANY = {
    "name": "Flowline Operations Limited",
    "cro": "822462",
    "office": "11 Sruth an Mhuillinn, Emyvale, Co. Monaghan, H18 RW62, Ireland",
    "vat": "IE4820511MH",
}
LEGAL = (f"{COMPANY['name']} is a private company limited by shares, registered in Ireland, "
         f"CRO no. {COMPANY['cro']}. Registered office: {COMPANY['office']}. "
         f"VAT no. {COMPANY['vat']}.")
PRIVACY = ("This email and any attachments are confidential and intended only for the named recipient. "
           "If you received it in error, please tell the sender and delete it. "
           "We process personal data in line with the GDPR. To ask about your data, email "
           f'<a href="mailto:tristan@flowlineops.com" style="color:{MUTED};text-decoration:underline;">tristan@flowlineops.com</a>.')


NUM = {"phone": 1, "email": 2, "web": 3, "location": 4}

def row(icon, content):
    badge = (f'<div style="width:18px;height:18px;line-height:18px;border:1px dashed {CYAN};border-radius:10px;'
             f'text-align:center;font-size:10px;font-weight:bold;color:{CYAN};font-family:Arial,sans-serif;">{NUM[icon]}</div>')
    return (f'<tr><td width="30" valign="middle" style="padding:4px 10px 4px 0;">{badge}</td>'
            f'<td valign="middle" style="padding:4px 0;font-size:13px;line-height:18px;color:{GRAPHITE};">{content}</td></tr>')

def link(href, text, color=GRAPHITE, bold=False):
    w = "font-weight:bold;" if bold else ""
    return f'<a href="{href}" style="color:{color};text-decoration:none;{w}">{text}</a>'

contacts = "".join([
    row("phone", link("tel:+353857825953", "+353 85 782 5953")),
    row("email", link("mailto:tristan@flowlineops.com", "tristan@flowlineops.com")),
    row("web", link("https://www.flowlineops.com/", "www.flowlineops.com", CYAN, True)),
    row("location", "Monaghan, Ireland"),
])

button = (f'<table cellpadding="0" cellspacing="0" border="0" role="presentation" style="border-collapse:separate;margin-top:12px;">'
          f'<tr><td bgcolor="{CORAL}" style="background-color:{CORAL};border-radius:6px;padding:8px 14px;">'
          f'<a href="https://calendly.com/tristan-flowlineops/30min" style="color:#ffffff;text-decoration:none;font-size:12px;font-weight:bold;font-family:{FONT};">'
          f'Book a 30-min call &rarr;</a></td></tr></table>')

SIG = f'''<table cellpadding="0" cellspacing="0" border="0" role="presentation" style="border-collapse:collapse;font-family:{FONT};">
<tr>
<td valign="middle" style="padding:0 24px 0 0;">
<div style="font-size:18px;line-height:24px;font-weight:bold;color:{GRAPHITE};">Tristan Messer</div>
<div style="font-size:13px;line-height:19px;font-weight:bold;color:{CYAN};">Managing Director</div>
<div style="font-size:13px;line-height:19px;color:{GRAPHITE};padding-bottom:12px;">Flowline Operations</div>
<div style="width:118px;height:86px;line-height:86px;border:1px dashed {CYAN};border-radius:10px;text-align:center;font-size:13px;font-weight:bold;color:{CYAN};font-family:Arial,sans-serif;">LOGO</div>
</td>
<td width="2" style="width:2px;background-color:{CYAN};font-size:0;line-height:0;">&nbsp;</td>
<td valign="middle" style="padding:0 0 0 24px;">
<table cellpadding="0" cellspacing="0" border="0" role="presentation" style="border-collapse:collapse;">{contacts}</table>
{button}
</td>
</tr>
</table>
<table cellpadding="0" cellspacing="0" border="0" role="presentation" style="border-collapse:collapse;font-family:{FONT};">
<tr><td style="padding-top:16px;">
<table cellpadding="0" cellspacing="0" border="0" role="presentation" style="border-collapse:collapse;"><tr>
<td width="40" height="3" style="width:40px;height:3px;background-color:{CYAN};font-size:0;line-height:0;">&nbsp;</td>
<td width="40" height="3" style="width:40px;height:3px;background-color:{LIME};font-size:0;line-height:0;">&nbsp;</td>
<td width="40" height="3" style="width:40px;height:3px;background-color:{CORAL};font-size:0;line-height:0;">&nbsp;</td>
</tr></table>
<div style="padding-top:6px;font-size:11px;line-height:16px;letter-spacing:1px;font-weight:bold;color:{GRAPHITE};">DESIGNED TO FLOW. BUILT TO PROFIT.</div>
</td></tr>
<tr><td style="padding-top:14px;">
<table width="480" cellpadding="0" cellspacing="0" border="0" role="presentation" style="border-collapse:collapse;width:480px;max-width:100%;"><tr>
<td style="font-size:10px;line-height:14px;color:{MUTED};">
<p style="margin:0 0 6px 0;">{LEGAL}</p>
<p style="margin:0;">{PRIVACY}</p>
</td></tr></table>
</td></tr>
</table>'''

HEADER = "<!-- Flowline Ops email signature, on-brand and safe in light AND dark mode.\n     Generated by build.py. Install steps are in README.md in this folder. -->\n"
out = HERE / "signature.html"
out.write_text(HEADER + SIG + "\n")
print(out)
