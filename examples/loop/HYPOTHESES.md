# Hypotheses — Loop

## H1: PMs spend significant time manually reconciling feedback with implementation
- **Risk:** If this is less than 1-2 hrs/week, the pain isn't acute enough to pay for a tool
- **Test:** 🗣️ conversation
- **How:** Ask "how many hours/week do you spend translating between call notes and tickets/PRDs/code?" across 10+ interviews. Look for >2 hrs/week as the threshold.
- **Status:** ✅ confirmed — Marcus: 4-5 hrs/week, Priya: estimated "more than I want to admit", 8/12 interviewees cited this as a top-3 pain

## H2: The biggest drift point is user calls → PRD, not PRD → code
- **Risk:** If drift happens mainly at the ticket-to-code handoff, the right product is a PR review tool, not a feedback analyzer
- **Test:** 🗣️ conversation
- **How:** Ask "where does the signal get lost most — writing the spec, writing the ticket, or building it?" Look for which handoff is cited most.
- **Status:** ✅ confirmed — both Marcus and Priya independently identified call→PRD as the primary failure point. "Three layers of telephone" (Marcus). PRD→code is a secondary pain.

## H3: LLM can extract structured requirements from call notes with high recall
- **Risk:** If extraction misses important feedback items or invents ones that weren't there, the whole pipeline is unreliable
- **Test:** 🛠️ prototype
- **How:** Run extraction on 10 real call note files. Have a PM independently list requirements. Measure recall (% of real requirements captured) and precision (% of extracted items that are real).
- **Status:** untested

## H4: LLM can evaluate PRD-to-feedback alignment and surface gaps a PM agrees are real
- **Risk:** If the evaluator produces false positives (gaps that aren't real) or misses obvious gaps, PMs won't trust it
- **Test:** 🛠️ prototype — **building this first**
- **How:** Run the evaluator on 5 PRD+call-note pairs. Show the gap report to the PM who wrote the PRD. Measure: % of flagged gaps they agree are real, % of real gaps the evaluator caught.
- **Status:** untested — this sprint builds the prototype

## H5: LLM can detect ticket-to-code drift from a PR diff
- **Risk:** Code diffs are noisy — lots of implementation detail that's irrelevant to requirements. LLM may produce too many false positives to be useful.
- **Test:** 🛠️ prototype
- **How:** Feed 10 real (ticket, PR diff) pairs to the evaluator. Have the engineer and PM independently judge whether the PR addressed the ticket. Measure agreement with LLM verdict.
- **Status:** untested

## H6: Multi-source synthesis (call notes + usage data + support tickets) produces better PRDs than call notes alone
- **Risk:** Adding more data sources increases complexity significantly. May not be worth it if call notes alone are sufficient.
- **Test:** 🛠️ prototype
- **How:** Generate PRDs from call notes only vs. call notes + Mixpanel data + support ticket themes. Have PMs rate both blind. Measure preference and specific improvements cited.
- **Status:** untested

## H7: An evaluator-optimizer loop can iteratively improve PRD alignment score
- **Risk:** The optimizer may overfit to the evaluator — improving the score without making the PRD actually better. Human validation required.
- **Test:** 🛠️ prototype
- **How:** Run 3 iterations of evaluate→rewrite on 5 PRDs. Measure score improvement. Then have PMs rate v1 vs v3 blind — do they agree v3 is better?
- **Status:** untested
