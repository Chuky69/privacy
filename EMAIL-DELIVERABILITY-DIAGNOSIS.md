# workflowalchemy.com — Email Deliverability Diagnosis & Fix Runbook

_Date: 2026-06-12_

## TL;DR

**workflowalchemy.com is NOT blacklisted by any provider.** The domain and its
email authentication are healthy. The real cause of "no email going through" is
**damaged sending reputation from high bounce rates on cold-outreach campaigns
sent via lemlist using unverified lead lists** — which causes receiving
providers (Gmail/Microsoft) to send mail to spam and throttle/soft-block it.

This is a reputation/list-hygiene problem, not a blacklist problem. Delisting
requests will not help.

---

## Evidence

### 1. Domain & authentication are healthy
| Check | Result |
|---|---|
| MX | Google Workspace (`aspmx.l.google.com`) ✅ |
| SPF | `v=spf1 include:_spf.google.com ~all` ✅ (see gap below) |
| DKIM (`google` selector) | Valid 2048-bit key published ✅ |
| DMARC | `v=DMARC1; p=quarantine; rua=mailto:dmarc@workflowalchemy.com; ruf=...; fo=1` ✅ |

### 2. Blacklist checks — all clean
Live DNSBL/DBL lookups against Spamhaus ZEN, SpamCop, Barracuda, SORBS,
UCEPROTECT, Mailspike, SURBL, and URIBL all returned **not listed**.

The one apparent Spamhaus ZRD "hit" (`127.255.255.252`) is a **false positive**:
that is an error code returned when Spamhaus is queried through a public resolver
(e.g. 8.8.8.8). Proof: the identical code is returned for a random non-existent
domain, and Spamhaus's always-listed test points (`dbltest.com`,
`2.0.0.127.zen`) came back "clean" via the same path — meaning Spamhaus simply
refused the queries.

### 3. Native Gmail mail delivers fine
Mail from `@workflowalchemy.com` users lands in recipient inboxes (verified in a
connected Google Workspace mailbox). A deliverability test message ("This is a
test to see if it will land in spam") was confirmed: **"Landed fine."** No
workflowalchemy mail found in spam.

### 4. Root cause — lemlist high bounce rate
A lemlist notification (17 Mar 2026) to the team flagged:

> Campaign **"Asana Ambassadors - 1 (ASP)"** has a bounce rate of **12%**.
> "A high bounce rate ... means a lot of your leads have invalid email
> addresses. High bounce rates affect your sending reputation, and will cause
> your messages to go to spam."

A healthy cold-outreach bounce rate is **< 2–3%**. 12% is severe and is the
mechanism degrading deliverability. (Also observed: outbound to non-existent
internal addresses returning `550 5.1.1 ... account does not exist`, and a
domain typo `workflowalcheny.com` — both inflate bounce metrics.)

---

## Fix plan (priority order)

### A. Stop the bleeding (today)
1. **Pause** the high-bounce lemlist campaigns (start with "Asana Ambassadors -
   1 (ASP)").
2. **Verify every list** before sending. Use lemlist waterfall enrichment or a
   verifier (NeverBounce, ZeroBounce, MillionVerifier, Bouncer). Remove
   invalid/catch-all/role addresses. Target bounce rate **< 2%**.
3. **Fix obvious data errors** — typos like `workflowalcheny.com`, addresses
   that don't exist.

### B. Confirm "which provider, why" with real data
- **Google Postmaster Tools** (postmaster.google.com): add the domain → view
  domain reputation + spam rate as Gmail recipients see it.
- **DMARC aggregate reports**: already collected at
  `dmarc@workflowalchemy.com`. Load into a reader (dmarcian / Postmark / EasyDMARC)
  to see every sending source and per-receiver SPF/DKIM/DMARC pass-fail. This
  identifies any unauthenticated sending source and which providers reject it.
- **Microsoft SNDS + JMRP** (sendersupport.olc.protection.outlook.com): if
  prospects are on Outlook/Office 365 (the most common blocker of new-domain
  cold outreach), register to see Microsoft's view and request mitigation.

### C. Authentication hardening
- SPF currently authorizes **only Google**. Confirm lemlist sends *through the
  connected Google Workspace mailboxes* (OAuth/SMTP) — if so, SPF/DKIM already
  pass. If lemlist (or any tool) sends from its own infrastructure, add its
  **SPF `include:`** and **DKIM** records, or mail will fail DMARC `p=quarantine`
  and be junked.
- Consider a **dedicated sending subdomain** for cold outreach (e.g.
  `go.workflowalchemy.com`) so campaign reputation is isolated from the primary
  corporate domain.

### D. Rebuild reputation (ongoing)
- **Warm up** the domain/mailboxes (lemwarm or similar); ramp volume gradually.
- Keep daily volume modest per mailbox; use multiple mailboxes if needed.
- Maintain low bounce + low spam-complaint rates; include unsubscribe; write
  non-spammy copy.
- Keep DMARC at `p=quarantine` once all legitimate sources are authenticated.
  Only drop to `p=none` as a short-term bridge if legitimate tool mail is being
  quarantined purely by misalignment.

---

## What is NOT the problem
- ❌ Domain blacklisting (verified clean)
- ❌ Broken MX / SPF / DKIM / DMARC records
- ❌ Google Workspace account suspension (native mail flows fine)
