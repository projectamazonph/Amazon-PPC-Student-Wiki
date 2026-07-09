---
title: "VA Resources Hub"
summary: "Onboarding guide, SOPs, checklists, and communication templates for VAs managing Amazon PPC campaigns."
last_updated: 2026-07-09
owner: "Wiki Maintenance Agent"
status: "active"
tags: ["va", "virtual-assistant", "sop", "onboarding", "checklist", "templates"]
---

# VA Resources Hub

This hub is for two audiences: VAs who are new to Amazon PPC, and the people who hire and manage them. Everything VAs need to get up to speed and run campaigns correctly — and everything managers need to set expectations and review work quality.

## Onboarding Guide

### For VAs New to Amazon PPC

If you're starting with no Amazon PPC experience, work through this sequence before touching any live campaigns:

**Week 1 — Learn the language:**
1. Read the [What is Amazon PPC](/sections/01-1-foundations-and-fundamentals/1-1-1-1-what-is-amazon-ppc.md) page
2. Read the [Core Terminology Primer](/sections/01-1-foundations-and-fundamentals/1-3-1-3-core-terminology-primer.md)
3. Spend 30 minutes in the Amazon Seller Central Ads dashboard — click through every tab and report until nothing looks unfamiliar
4. Take notes: for each metric you see (ACOS, TACOS, CTR, CVR, impressions, spend, revenue), write down the formula and what a "good" value looks like for that metric

**Week 2 — Understand the data:**
1. Export a sample search term report (your manager should provide one) and go through every column
2. Practice calculating ACOS manually: `(spend / revenue) * 100`
3. Practice calculating TACOS: `(PPC spend / total revenue) * 100`
4. Identify what the difference between ACOS and TACOS tells you about the account

**Week 3 — Shadow before doing:**
1. Watch your manager run through a campaign review — ask questions about every decision
2. Practice making recommendations on historical data before making them on live campaigns
3. Draft your first bid change recommendation in writing, including your reasoning, and get feedback before executing

**Week 4 — First supervised live work:**
1. Make small changes with explicit approval required before execution
2. Document every change you make and why
3. End of week: write a summary of what you did, what changed, and what you'd recommend next

---

## Standard Operating Procedures

### Weekly PPC Review SOP

Do this every Monday morning. Consistency is what separates competent PPC management from chaotic reactive management.

1. **Check yesterday's performance** — open Campaign Manager and scan ACOS, spend, and revenue for all active campaigns. Flag anything more than 20% outside its normal range.

2. **Run a search term report for the last 7 days** — download it and review the top 50 terms by spend. Look for:
   - Terms with high spend and zero conversions (negatives to add)
   - Terms with high spend and high ACOS (bids to reduce)
   - Terms performing well that aren't in your manual campaigns (candidates to move from auto)

3. **Check placement data** — look at the placement tab for campaigns running placement modifiers. Confirm the modifiers are still appropriate.

4. **Check budget pacing** — see if any campaigns ran out of budget before end of day. If so, raise the budget or narrow the campaign scope.

5. **Review bid recommendations** — if using a tool or following a rules framework, check what it's recommending and either approve or override each recommendation.

6. **Write a brief summary** — one paragraph for your manager: "This week we [actions taken]. Results: ACOS moved from X to Y. [Outstanding issues or decisions needed]."

### Monthly PPC Audit SOP

Once a month, go deeper than the weekly review.

1. **Campaign-level performance review** — compare each campaign's ACOS, TACOS, and revenue against the previous month. Which campaigns improved? Which deteriorated?

2. **Keyword-level analysis** — pull a 30-day keyword report. Identify your top 20 and bottom 20 performing keywords by ACOS. For each, ask: is this performance expected? Is there a fix worth trying?

3. **Match type analysis** — compare ACOS by match type across campaigns. Are exact match terms performing better than phrase and broad? If so, consider tightening match type usage in the future.

4. **Budget reallocation** — review total spend and revenue. If you had more to spend, where would it go? Use that analysis to guide next month's budget decisions.

5. **Campaign structure review** — are campaigns organized in a way that makes sense? If you've been adding keywords without a consistent structure, now is the time to clean it up.

### New Product Launch SOP

When launching a new product, follow this sequence:

1. **Pre-launch (2-4 weeks before going live):**
   - Research keywords using Helium 10, JungleScout, or Amazon Brand Analytics
   - Build your keyword list: 50-100 terms across head terms and long-tail
   - Set up campaign structure: auto campaign + exact match campaign ready to launch

2. **Launch week:**
   - Set initial bids at Amazon's suggested bid + 20-30%
   - Set daily budget to 10x your target CPC (ensures you get data quickly)
   - Start auto campaign first, wait 48 hours for data to accumulate
   - Add exact match campaign once auto has data

3. **Post-launch weeks 1-4:**
   - Review search term report every 3-4 days
   - Add negatives to auto campaign to cut irrelevant spend
   - Graduate winning terms from auto to exact match
   - Adjust bids weekly based on early data

---

## Task Checklists

### Daily PPC Tasks (10 minutes)
- [ ] Check that all active campaigns are running (no paused campaigns that should be active)
- [ ] Confirm no campaign hit a spend cap before 6pm local marketplace time
- [ ] Note any unusual spikes or drops in spend

### Weekly PPC Tasks (30-60 minutes)
- [ ] Download and review 7-day search term report
- [ ] Add negative keywords for irrelevant searches
- [ ] Review top-performing keywords — are bids still appropriate?
- [ ] Check placement performance
- [ ] Confirm budget pacing
- [ ] Write weekly summary for manager

### Monthly PPC Tasks (2-3 hours)
- [ ] Full campaign audit with month-over-month comparison
- [ ] Keyword-level performance review
- [ ] Budget reallocation decisions
- [ ] Campaign structure review and cleanup
- [ ] Identify one optimization to test next month

---

## Communication Templates

Use these when briefing a VA or reporting to a manager.

### VA Status Update Template
```
**Campaign Area:** [Campaign name or "All campaigns"]
**Period:** [Week/Month]
**Overall ACOS:** [X%] vs [Y%] last [week/month]
**Overall Spend:** $[amount]
**Overall Revenue:** $[amount]

**What I did:**
- [Action 1 — why]
- [Action 2 — why]

**What changed:**
- [Metric movement and interpretation]

**Recommended for next period:**
- [Specific action with expected outcome]
- [Decision needed from manager]
```

### Manager Brief to VA Template
```
**Account:** [Account name/number]
**Priority:** [Urgent / Normal / Low]
**Deadline:** [Date]

**Context:** [What's happening with the account — new product launch, seasonal event, problem to fix]

**What I need:**
1. [Specific task with expected deliverable]
2. [Specific task with expected deliverable]

**What to flag immediately:**
- [Conditions that should trigger an urgent check-in]

**How to reach me:** [Slack/email/phone]
```

---

## Quality Assurance Checklist

When reviewing VA work, check for these:

- [ ] Are search term reports being reviewed consistently (not just when something looks wrong)?
- [ ] Were negative keywords added proactively, not just reactively?
- [ ] Are bid changes documented with reasoning, not just "reduced bid"?
- [ ] Did the VA explain recommendations before making them?
- [ ] Are campaign naming conventions consistent?
- [ ] Is the VA catching budget cap issues before end of day?
- [ ] Are ACOS targets realistic given the product price and category?
- [ ] Is the VA thinking about TACOS, not just ACOS?
- [ ] Are the weekly summaries substantive or just "nothing unusual"?
- [ ] Is the VA escalating issues proactively or waiting to be asked?
