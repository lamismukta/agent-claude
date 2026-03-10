# Dropbox — Example Test Case

The actual YC application Drew Houston submitted in 2007. Useful for testing the `/onboard` and `/sprint` flow without needing your own application handy.

## How to use

1. Run `/onboard`
2. When prompted for your YC application, paste the contents of `yc-application.md` or share the file path
3. Run `/sprint`

## What makes this a good test

The Dropbox application is famously sparse — one founder, no traction numbers, no co-founder, not yet incorporated. It forces the flow to work from thin context and ask the right follow-up questions rather than just summarising what's there.

The interesting tensions to surface:
- Solo founder (YC usually wants two) — does `/sprint` flag this?
- "6–8 weeks to commercial version" — optimistic; what's the riskiest assumption?
- Competitors are dismissed quickly — is that confidence or blind spot?
- The core hypothesis ("people will trust a background process with all their files") is never stated explicitly in the application

The prototype that would make sense: a script that syncs a local folder to S3 and back. Simple enough to build in a session, directly tests the core technical risk.
