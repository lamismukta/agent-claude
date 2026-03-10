# Dropbox — YC S07 Application

> The actual YC application Drew Houston submitted in 2007.
> Use this to test the `/onboard` and `/sprint` flow.
> Paste it in when prompted for your YC application.

---

## Company

**Company name:** Dropbox

**URL:** http://www.getdropbox.com/

**What are you making?**
Dropbox synchronises files across computers automatically. It has Windows integration, a web interface, and secure Amazon S3 backup. It's like combining the best parts of subversion, rsync, and a USB drive — but one that works for normal people.

Demo screencast: http://www.getdropbox.com/screencast/

---

## Founders

**Drew Houston** — age 24, MIT 2006, Computer Science.
Previously project lead at Bit9. Started programming at 5, built a profitable SAT prep company in college, reverse-engineered poker software and built a bot that played for real money. Planning to leave Bit9 in May.

Solo founder. Jeff Mancuso is working on the Mac port. Tom Hoover is helping but can't commit due to employment restrictions.

---

## Progress

Three months of part-time work. ~5K lines of client code (Python, C++), ~2K server-side. Prototype finished February. Beta users already using it. Commercial version in 6–8 weeks.

Not yet incorporated. Drew owns 100% with ~2% reserved for Jeff and Tom.

---

## The Idea

**What problem are you solving?**
People need their files to be accessible, backed up, and in sync across computers. Every solution today is either too technical, too manual, or doesn't work offline.

The core insight: "online disk drive" doesn't work because you need your files when you're not online. But web-based file managers require you to manually upload and download. Neither is right.

Dropbox works at the user layer. You just save your file. It syncs automatically in the background, handles binary diffs for large files efficiently, and everything is available offline.

**Who are your competitors?**
Carbonite, Mozy (backup only, not sync). Sharpcast's Hummingbird, Microsoft Groove (too complex). Various other attempts that are all "pretty buggy and not ready for non-technical users."

**Why will you win?**
We work exactly like a normal folder. No configuration. No thinking about it. You hit Save and it's done.

---

## Business model

Free 1GB accounts. Paid tiers: ~$5/month for 10GB individual, ~$20/month for team plans. Business accounts with version history, branded extranets, and enterprise options.

Also: web services API (already talking to Assembla.com). Self-hosted enterprise versions.

---

## Other ideas we considered

- One-click screen sharing
- Collaborative version-controlled drawing tool for teams
- Web analytics for beginners
