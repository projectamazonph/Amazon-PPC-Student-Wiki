---
title: "Interview Questions Hub"
summary: "How to answer the most common Amazon PPC interview questions — frameworks, strong answers, and red flags to avoid."
last_updated: 2026-07-09
owner: "Wiki Maintenance Agent"
status: "active"
tags: ["interview", "questions", "hiring", "preparation", "acronym"]
---

# Interview Questions Hub

This page covers how to answer the interview questions you're most likely to get when applying for Amazon PPC roles — from junior coordinator to senior manager. For each question, you'll find: why interviewers ask it, what a strong answer sounds like, and the red flags that get candidates rejected.

## Core Strategy Questions

### "Walk me through how you'd structure a new campaign from scratch."

**Why they ask it:** They want to see your systematic thinking and whether you understand the building blocks of a campaign. This is a foundational question — a poor answer here disqualifies candidates regardless of how well they answer everything else.

**What a strong answer looks like:**
"Before I touch anything, I'd look at the product — price, category, review count, competitive landscape. Then I'd do keyword research using at least two tools to build a list of 50-100 terms. From there, I'd structure the campaign with one auto campaign for discovery and one exact match campaign for my primary keywords. I'd set initial bids at Amazon's suggested bid plus 20-30%, and a daily budget that's 10x my target CPC so I get data quickly. In the first two weeks, I monitor search terms closely and build my negative keyword list. By week 3, I start graduating winning terms from auto to manual exact campaigns where I have full control."

Notice what's in there: research before action, structure before keywords, monitoring and iteration built in, clear sequencing.

**Red flags:**
- Starting with "I'd set up some campaigns and see how they do" — no framework, just hope
- Mentioning all match types from day one
- Forgetting about negative keywords entirely
- No mention of bid strategy or budget planning

---

### "How do you decide when to use automatic vs. manual bidding?"

**Why they ask it:** This question tests whether you understand the tradeoffs between control and scale. Manual bidding is safer but slower; automatic bidding is faster but requires trust in the algorithm.

**What a strong answer looks like:**
"Manual bidding is where I start with every new account or new campaign. I need data before I hand control to the algorithm. Once I have 30+ days of data showing which keywords convert and at what rate, I can switch to dynamic bidding with confidence. The exception is campaigns where I'm deliberately testing — I'll use dynamic up-and-down on proven winners to let them spend more when conversion likelihood is high, while keeping everything else on dynamic down-only as a safety floor."

**What interviewers actually want to hear:**
That you don't default to automation. That you earn the right to automate through data. That you know the difference between dynamic up/down and down-only and when to use each.

**Red flags:**
- Saying you always use auto bidding because "Amazon knows better than I do"
- Saying you always use manual because "you can't trust the algorithm"
- Not knowing what dynamic up/down means
- No mention of data thresholds before switching strategies

---

### "Tell me about a campaign you managed. What happened, what did you do, what was the result?"

**Why they ask it:** The most important interview question. They're assessing your real experience, your analytical thinking, and whether you can connect actions to outcomes.

**What a strong answer looks like:**
Use this structure: **Situation → Action → Result → Learning**

"For a protein supplement client, we launched at 42% ACOS in the first month. I broke down the search term report and found 60% of spend was going to three auto campaign categories that had nothing to do with their actual product — they were being matched to general fitness searches. I added those as negatives, which dropped spend by 35% without reducing revenue. Then I moved the five best-performing exact match terms from auto into their own manual campaign with tighter bids. By month 3, ACOS was at 27% and revenue was up 15% because the budget was going to actual buyers instead of browsers. The lesson I took: auto campaigns need active negative management from day one, not as a cleanup exercise after months of waste."

Notice: specific numbers, causal reasoning, not just "I checked the report and made changes," genuine reflection.

**Red flags:**
- Vague answers with no numbers ("it did well")
- Taking credit for results that were driven by the product or category, not the campaign
- No mention of what went wrong or what they would do differently

---

## Tactical Questions

### "How do you reduce ACOS?"

**Why they ask it:** ACOS is the metric non-technical stakeholders care about most. They want to know you can think through ACOS systematically rather than just "lower bids."

**What a strong answer looks like:**
"ACOS is spend divided by revenue, so I can improve it in two directions. On the spend side: I tighten negative keywords to eliminate waste, reduce bids on keywords with high spend but below-target ACOS, and check placement modifiers to make sure I'm not overbidding on low-CVR placements. On the revenue side: I look for keywords where bids are too low to get visibility — raising those bids generates more impressions from buyers who convert, which reduces ACOS even if spend increases. The biggest mistake I see is lowering bids on everything when ACOS is high, which just cuts revenue. You need to distinguish between keywords that waste money and keywords that are underperforming because they're underbid."

This answer shows you understand the math, can think in both directions, and know the common mistake.

---

### "Walk me through your keyword research process."

**Why they ask it:** Keyword research is the foundation of PPC. If you do this poorly, everything downstream suffers.

**What a strong answer looks like:**
"I start with the product — what problem does it solve, who buys it, what words would they use to search for it? Then I use multiple sources: Helium 10 Cerebro to reverse-engineer competitor ASINs, Amazon Brand Analytics for search frequency data if I have access, Google Keyword Planner for volume context, and the Amazon search bar autocomplete for real buyer language. I compile a list of 50-100 terms, then score each one on volume, competition level, and relevance — I only want terms where a buyer searching for that term would actually consider my product. From there I build match type strategy: exact for my primary confirmed terms, phrase for broader discovery, auto for ongoing harvesting."

Shows: multiple sources (not just one tool), scoring framework, match type reasoning.

---

### "How do you handle a product with no reviews?"

**Why they ask it:** New products with no social proof are a real challenge. Interviewers want to know you understand how reviews affect PPC performance.

**What a strong answer looks like:**
"Low reviews kill conversion rate, which makes PPC expensive. My approach: first, run Sponsored Products at very conservative bids — I'm not going to spend aggressively until the listing can convert. Second, I'd lean heavily on Sponsored Display retargeting to reach people who viewed similar products — they may buy despite low reviews if the price and content are compelling. Third, I'd use negative keyword hygiene aggressively so I'm not spending on searches that won't convert for a low-review product. Finally, I'd make sure the PPC strategy is paired with a review generation strategy — using Amazon's Request a Review button, following up with buyers, maybe a small email campaign. PPC on a zero-review product is a bridge strategy, not a long-term plan."

Shows you understand that PPC works within the constraints of the listing, not independently.

---

### "What's your approach to negative keywords?"

**Why they ask it:** Negative keywords separate professionals from amateurs. The candidate who mentions them early and with specificity is a professional.

**What a strong answer looks like:**
"I add negatives in three layers. First, I add obvious negatives from the start — my own brand name if I'm not selling it, competitor brand names unless I'm deliberately targeting them, product variants I don't carry. Second, during the first 30 days I review every search term that generated clicks and add anything irrelevant as negative exact. Third, on a recurring schedule (every 2 weeks) I run a systematic audit looking for terms with high spend and zero conversions. The key discipline: I add negatives as negative exact first, not negative phrase — negative phrase is broader and sometimes catches legitimate searches by accident. I only use negative phrase when I'm sure a whole category of searches is wasting money."

---

## Tool and Process Questions

### "What tools do you use and why?"

**Why they ask it:** They're assessing your toolkit and whether you understand the tradeoffs between different solutions.

**What a strong answer looks like:**
"For most accounts, I start with the native Amazon reports — the data is the same, and it forces you to actually understand what you're looking at instead of relying on a tool's interpretation. For keyword research, I use Helium 10 Cerebro for reverse ASIN analysis and JungleScout for product research. For ongoing management on larger accounts, I use Helium 10 Adtomic or Sellics depending on whether the seller wants more automation or more control. I don't use tools as a crutch — if I can't explain a recommendation based on the raw data, the tool is leading me, not informing me."

This answer is honest about tool selection, shows judgment, and doesn't sound like a vendor pitch.

---

### "How often do you check campaigns and make changes?"

**Why they ask it:** Candidates who check campaigns too frequently make reactive, data-noise-driven decisions. Candidates who check too infrequently miss real problems.

**What a strong answer looks like:**
"Daily: I check that campaigns are running and no budget caps are cutting off traffic early. Weekly: I do a full review of search terms, check ACOS movement, and make bid adjustments on clear winners and losers. Monthly: I do a deeper campaign-level audit and look at structural changes — adding new campaigns, restructuring existing ones, budget reallocation. The discipline is not making changes based on less than 7 days of data unless something is clearly broken."

---

## Curveball Questions

### "What's your honest opinion of AI bidding tools?"

**Why they ask it:** AI bidding tools are controversial. Interviewers want to know if you've used them, understand their limits, and have developed an honest opinion rather than just repeating marketing claims.

**What a strong answer looks like:**
"They work when your account has enough data and consistent margins for the algorithm to learn from. They fail when your account is volatile, your margins change frequently, or you're in a category where the algorithm doesn't have enough similar accounts to learn from. I've seen AI bidding reduce ACOS significantly on established accounts with stable products. I've also seen it burn through budgets on accounts with seasonal products because the algorithm kept bidding based on last year's patterns. My approach: use AI bidding on campaigns where it's clearly winning, manage manually where it's not."

---

### "If your ACOS is 50% but your TACOS is 15%, what does that tell you?"

**Why they ask it:** This is a math question disguised as a strategy question. They want to know if you understand the difference between ACOS and TACOS and what it means in context.

**What a strong answer looks like:**
"ACOS at 50% looks bad in isolation, but TACOS at 15% tells a different story — my PPC is generating organic sales that bring my total advertising cost down to a reasonable level. The PPC isn't profitable on its own, but it's working as a ranking tool. I'd want to know whether organic rank is improving, and if so, whether I can eventually reduce PPC spend while maintaining organic sales. The risk is if organic rank plateaus — then I'm stuck paying 50% ACOS indefinitely."

---

## What Gets Candidates Rejected

These are the patterns that end interviews quickly:

1. **Can't explain ACOS formula** — if you say ACOS and TACOS are the same thing, the interview is over
2. **No mention of negative keywords** when asked about campaign optimization — shows inexperience
3. **Blames external factors for poor results** without any self-reflection or learning identified
4. **Can't walk through a search term report** or explain what columns matter
5. **Says "I let Amazon manage it"** for every bidding question — shows passivity, not strategy
6. **Vague numbers** — "we improved things a lot" instead of "ACOS went from 38% to 27% in 90 days"
7. **No curiosity** — not asking clarifying questions, not engaging with the scenario being described
