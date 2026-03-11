# Hypotheses — Bridge

## H1: People lose useful knowledge across tabs, chats, and docs when researching a topic
- **Risk:** If people are actually fine with their current workflow (bookmarks + ChatGPT), there's no activation energy to switch
- **Test:** 🗣️ conversation
- **How:** Ask 5 people who actively research topics: "Show me how you saved things from your last deep dive. Can you find them now?" If 3+ can't find what they saved, pain is real.
- **Status:** untested

## H2: AI-generated suggestions surface content users wouldn't have found on their own
- **Risk:** If suggestions are obvious ("you like startups? here's an article about startups"), the feature is worthless
- **Test:** 🛠️ prototype
- **How:** Build the suggestion engine. Give users a list of 3-5 topics, generate suggestions, ask "how many of these are new to you?" Target: 30%+ novel.
- **Status:** untested

## H3: Users prefer a growing document over disposable chat responses
- **Risk:** People might actually prefer the fresh-start-every-time model of ChatGPT — regeneration feels cleaner than accumulation
- **Test:** 🛠️ prototype
- **How:** Build the "create project" flow. Give users a structured document that grows. After a week, ask: did you come back to it? Did the structure help or feel rigid?
- **Status:** untested

## H4: A browser extension is the right capture surface (vs. a standalone app or CLI)
- **Risk:** If users don't have the extension open when they find interesting content, capture doesn't happen. The habit never forms.
- **Test:** 🗣️ conversation
- **How:** Ask users: "When you find something interesting while browsing, what do you do right now?" If the answer involves the browser (bookmarks, tabs, copy-paste), extension fits. If it's "I send it to myself on Slack," different surface needed.
- **Status:** untested

## H5: Two clicks to capture is fast enough to not break flow
- **Risk:** Even two clicks might be too much friction. Users might want a keyboard shortcut or auto-detect.
- **Test:** 🛠️ prototype
- **How:** Build the extension capture flow. Time it. If users consistently take >5 seconds or abandon mid-capture, simplify.
- **Status:** untested
