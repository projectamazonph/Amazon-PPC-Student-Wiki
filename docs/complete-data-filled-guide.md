---
title: Complete Data-Filled Guide
---

# The Amazon PPC Wiki — Complete Data-Filled Guide

This page is the consolidated source page for the new beginner-friendly data added across the wiki section pages. The same material is split into the numbered section pages under `docs/sections`.

## Section 0
## Merged beginner guide content

This wiki teaches Amazon PPC from the ground up. Start with [[1. Foundations & Fundamentals]], then move through [[2. Account & Campaign Architecture]], [[3. Campaign Types]], and [[4. Targeting & Match Types]]. If you want a quick win, go to [[9. Negative Keywords & Negation Strategy]] — cutting wasted spend is often the fastest improvement you can make.

### Role-based start paths

| Role | Best first path | Goal |
|---|---|---|
| Fresh graduate | Sections 1 to 4, then Glossary | Understand the language and ad system |
| VA | Sections 1 to 9, then Team Ops | Execute daily PPC tasks safely |
| Junior strategist | Sections 1 to 11, then lifecycle strategy | Optimize campaigns and explain performance |
| Brand owner | Foundations, metrics, reporting, launch strategy | Understand what your PPC team is doing |
| Agency owner | Team Ops, communication, reporting, tooling | Build repeatable service delivery |

### Wiki conventions

- **Bold terms** should exist in [[28. Glossary & Acronyms]].
- `MONOSPACED TERMS` refer to console buttons, menu names, fields, reports, or file columns.
- ACOS, TACOS, ROAS, CTR, CVR, CPC, SP, SB, SD, DSP, AMC, and SQP should always be capitalized.
- Every operational page should include a beginner explanation, workflow, worked example, common mistake, and definition of done.

### Maintenance rules

Use this review path for content changes: Draft -> Peer Review -> Senior Strategist Review -> Publish. If Amazon changes a feature that affects live operations, mark the page as `[Stale?]` or `[Deprecated]`, add the replacement page link, and update `last_verified_against_live_console`.

## Section 1
## Complete data-filled section notes

Amazon PPC means pay-per-click advertising on Amazon. You pay when a shopper clicks the ad, not when the ad merely appears. Imagine Amazon as a giant mall and PPC as paying for better shelf placement near where shoppers are already looking.

PPC feeds the Amazon growth loop: paid visibility can create sales; sales can improve ranking; better ranking can create more organic visibility; more reviews and stronger conversion can make future ads more efficient. This is why PPC is not only a traffic tool. It is also a learning tool and ranking accelerator.

### How the auction works

1. You choose a keyword, product target, category target, or audience.
2. You set a bid, which is the most you are willing to pay for a click.
3. A shopper searches or views a page.
4. Amazon runs an ad auction.
5. Amazon considers bid, relevance, expected conversion, and eligibility.
6. The winner gets the placement and pays based on auction mechanics, not always their full bid.

### Core beginner terms

| Term | Plain-English meaning |
|---|---|
| Impression | Your ad appeared on screen |
| Click | A shopper clicked your ad |
| CTR | Clicks divided by impressions. Measures attention. |
| CVR | Orders divided by clicks. Measures listing conversion. |
| CPC | Spend divided by clicks. Measures click cost. |
| ACOS | Ad spend divided by ad revenue. Measures ad efficiency. |
| ROAS | Ad revenue divided by ad spend. Inverse of ACOS. |
| TACOS | Ad spend divided by total revenue. Measures business-level ad pressure. |

### Campaign hierarchy

`Account -> Campaign -> Ad Group -> Ad -> Keyword or Target`

A campaign is the main container. An ad group is a focused theme inside the campaign. The ad is what the shopper sees. The keyword or target decides when the ad is eligible to show.

### Eligibility checks before running ads

- Professional selling account.
- Buy Box ownership for Sponsored Products.
- Good account health.
- In-stock inventory.
- Brand Registry for Sponsored Brands, Sponsored Display, Brand Store, and A+ Content.

### Common beginner mistake

A common early mistake is thinking ads can fix a weak product page. Ads can bring traffic, but the listing must still convert. Poor images, high price, bad reviews, or missing Buy Box will wreck performance faster than any bid strategy can save it.

## Section 2
## Complete data-filled section notes

Account architecture is the filing system for your PPC work. A strong structure lets any strategist understand purpose, budget, match type, funnel stage, and ownership without asking the person who built it.

### Naming convention standard

Use a predictable pattern such as:

`Brand | Parent ASIN or Product Line | Country | Ad Type | Strategy | Target Type | Match Type | Bid Strategy | Portfolio`

Simpler beginner version:

`Product - Match Type - Purpose - Date or Version`

Examples:

- `RunningShoes-Men-Exact-Scaling-2026`
- `CoffeeMugs-Winter-Broad-Launch-2026`
- `BrandDefense-Branded-Exact-Protect-2026`

### Structuring models

| Model | How it works | Best use |
|---|---|---|
| SKU-level | Separate campaigns per product or parent ASIN | Clean product-level control |
| Category-level | Campaigns cover a product family | Smaller accounts or shared budget |
| Match-type segmented | Separate Broad, Phrase, Exact | Cleaner reporting and control |
| Funnel-stage | Awareness, consideration, conversion | Strategy-led scaling |
| Defense/offense | Protect own brand, attack competitor traffic | Mature accounts |
| Launch/mature/harvest | Structure changes by lifecycle stage | Product lifecycle planning |

### Ad group rule

Use one theme per ad group. Do not mix unrelated products or intents. A messy ad group gives messy data, and messy data makes optimization feel like reading tea leaves in a thunderstorm.

### Portfolios

Portfolios act like folders with optional budget control. Use them to group by product line, season, campaign objective, or P&L owner. Portfolio budgets work best when grouped campaigns have similar priorities.

### Definition of done

A campaign architecture is ready when a new team member can answer these questions from the name and folder alone: What product is this for? What ad type is it? What targeting method is it using? Is it for discovery, scaling, defense, or harvesting? Who owns the budget?

## Section 3
## Complete data-filled section notes

Amazon has several ad types. Each one solves a different job. New sellers should usually master Sponsored Products first before expanding into Sponsored Brands, Sponsored Display, Sponsored TV, or DSP.

### Sponsored Products

Sponsored Products look like normal listings with a `Sponsored` label. They can appear in search results and product detail pages. They are the main direct-sales ad type and are usually the first campaign type you will learn.

Auto campaigns let Amazon choose targets using four buckets: Close Match, Loose Match, Substitutes, and Complements. Manual campaigns let you choose keyword, ASIN, or category targets.

Bidding settings include Dynamic Bids Down Only, Dynamic Up and Down, and Fixed Bids. Placement modifiers can increase bids for Top of Search, Rest of Search, or Product Pages.

### Sponsored Brands

Sponsored Brands feature your brand logo, headline, and multiple products or video. They require Brand Registry. Use them for brand awareness, store traffic, branded defense, and high-intent category visibility.

Formats include Product Collection, Store Spotlight, and Video. Good headlines explain value, not just the brand name.

### Sponsored Display

Sponsored Display can target shoppers by product context or audience behavior. Use it for remarketing, competitor page visibility, cross-selling, and upper-funnel reach. Views remarketing targets people who viewed but did not buy. Purchase remarketing targets existing customers for cross-sell or repeat purchase.

### Sponsored TV and DSP

Sponsored TV and DSP are advanced. They fit brands with larger budgets and stronger creative assets. DSP can run display, video, audio, and connected TV ads across Amazon and external inventory. It is best used once Sponsored Ads already have enough data.

### Budget allocation example

| Brand stage | SP | SB | SD | DSP/STV |
|---|---:|---:|---:|---:|
| New brand | 90%+ | 0-10% | 0-5% | 0% |
| Growing brand | 65-80% | 10-20% | 5-15% | 0-5% |
| Mature brand | 60-70% | 15-20% | 10-15% | 5-10% |

## Section 4
## Complete data-filled section notes

Targeting decides when your ad is allowed to show. Match types decide how closely a shopper search must match your keyword.

### Keyword match types

| Match type | Volume | Precision | Best use | Main risk |
|---|---:|---:|---|---|
| Broad | High | Low | Discovery | Irrelevant spend |
| Phrase | Medium | Medium | Refinement | Still catches some waste |
| Exact | Low | High | Proven winners | Misses discovery volume |

Broad match catches many variations. Phrase match keeps the phrase in order. Exact match focuses on the exact term or close variations. A healthy account usually uses all three, but for different jobs.

### Migration pipeline

`Broad -> Phrase -> Exact -> Scale and optimize`

Start broad enough to discover real customer language. Move converting terms into Phrase or Exact. Then add negatives in the source campaign so the same term does not keep competing in the discovery bucket.

### Product targeting

Use ASIN targeting to target your own products for defense or competitor products for conquesting. Use category targeting when you want scale, then refine by price, brand, rating, or Prime eligibility.

### Audience targeting

Sponsored Display and DSP can target remarketing, in-market, lifestyle, purchase, and custom audiences. Use remarketing once you have traffic. Use lifestyle and in-market audiences when you have enough budget to learn.

### Auto targeting buckets

Close Match is the safest. Loose Match is broader. Substitutes targets similar products. Complements targets related products that go with yours. Auto campaigns are useful discovery engines when paired with regular search term mining.

## Section 5
## Complete data-filled section notes

Keyword research is how you learn the language customers use. Don't guess forever. Start with common-sense terms, then replace guesses with real search term data.

### Research methods

1. Brainstorm product names, features, use cases, problems solved, and customer types.
2. Review competitor titles, bullets, and product positioning.
3. Use Amazon autocomplete to see real search phrasing.
4. Use Search Term Reports after campaigns run.
5. Use reverse ASIN tools like Helium 10 Cerebro or Jungle Scout Keyword Scout.
6. Use Brand Analytics Search Query Performance when Brand Registry is available.

### Search term vs keyword

A keyword is what you bid on. A search term is what the customer actually typed. The Search Term Report is gold because it shows reality, not theory.

### Harvesting workflow

1. Launch Auto and Broad discovery campaigns.
2. Wait for enough clicks and orders.
3. Download the Search Term Report.
4. Sort by orders, CVR, ACOS, spend, and CTR.
5. Promote winners to Exact.
6. Add harvested terms as Negative Exact in the source campaign.
7. Scale bids and budgets for proven terms.

### Starter harvesting thresholds

| Metric | Starter threshold |
|---|---:|
| Clicks | 50+ |
| Orders | 5+ |
| ACOS | At or below target |
| CTR | 0.5%+ as a rough starter |

### Head vs long-tail terms

Head terms are short and high-volume, like `running shoes`. Long-tail terms are specific, like `men's running shoes size 10 wide`. Head terms create reach. Long-tail terms usually create efficiency.

## Section 6
## Complete data-filled section notes

A bid is the most you are willing to pay for a click. Bid management is where PPC becomes math plus judgment. The goal is not to always lower bids. The goal is to buy the right clicks at a cost the business can afford.

### Practical bid formula

`Target Bid = Price x CVR x Target ACOS`

Example: A $50 product with 10% CVR and 25% target ACOS has a target bid of `$50 x 0.10 x 0.25 = $1.25`.

A more conservative profit-aware formula can subtract margin pressure, but beginners should start with the basic target ACOS formula.

### Dynamic bidding settings

| Setting | What Amazon can do | Best for |
|---|---|---|
| Down Only | Lower your bid when conversion looks weak | Conservative control |
| Up and Down | Raise or lower bids based on conversion likelihood | Aggressive scaling or proven campaigns |
| Fixed Bids | Use the bid as set | Clean tests and strict control |

### Bid cadence

Daily checks are for fires: budget issues, sudden ACOS spikes, campaigns that stopped spending. Weekly checks are for real optimization. Monthly checks are for deeper structure changes.

### Do not overreact

A keyword with 3 clicks and 0 orders is not a problem yet. A keyword with 80 clicks, $60 spend, and 0 orders is a problem. Beginner PPC sins usually come from touching bids before the data says anything.

### Placement modifiers

Placement modifiers let you bid more aggressively for Top of Search, Rest of Search, or Product Pages. Increase modifiers only where placement-level ACOS and CVR justify the cost.

## Section 7
## Complete data-filled section notes

Budget management answers this question: where should limited money go today? Pacing answers this question: will the budget last long enough to collect good data?

### Budget frameworks

Top-down budgeting starts with total company ad budget and allocates by channel, product, or objective. Bottom-up budgeting starts with each SKU or campaign need, then totals the required spend.

### Portfolio vs campaign budget

| Level | Best use |
|---|---|
| Portfolio budget | Similar campaigns that can share spend flexibly |
| Campaign budget | Strict control, testing, or client-specific budget rules |

### Budget-starved high performers

A high-performing campaign that runs out of budget early is leaving money on the table. First confirm ACOS, CVR, inventory, and margin. Then increase budget, move to a stronger portfolio, or shift budget from weaker campaigns.

### Seasonal planning

Prime Day, Black Friday, Cyber Monday, Q4, and category events need pre-event warmup, event-day scaling, and post-event tapering. Do not cut budget immediately after an event because delayed conversions and late shoppers still matter.

### Beginner rule

Never increase budget only because a campaign spent all its money. Increase budget because performance justifies more spend.

## Section 8
## Complete data-filled section notes

Placement optimization controls where your ads appear. The three main Sponsored Products placements are Top of Search, Rest of Search, and Product Detail Pages.

| Placement | Typical behavior | Operator note |
|---|---|---|
| Top of Search | High visibility, high CPC, often high CVR | Worth bidding up only when efficient |
| Rest of Search | Middle ground | Often stable and scalable |
| Product Detail Pages | Lower intent, cheaper clicks | Useful for conquesting and cross-sell |

### Diagnosis workflow

1. Pull the Placement Report.
2. Compare ACOS, CTR, CVR, CPC, and sales by placement.
3. Increase modifier where ACOS is below target and volume is limited.
4. Reduce modifier where CPC is high and CVR is weak.
5. Recheck after enough data, not the next morning.

### Worked example

If Top of Search ACOS is 25%, Rest of Search is 35%, and Product Pages is 45%, increase Top of Search modestly, leave Rest alone, and reduce Product Pages or keep it conservative.

## Section 9
## Complete data-filled section notes

Negative keywords are terms you tell Amazon not to target. This is one of the fastest ways beginners can save money because it removes obviously irrelevant traffic.

### Negative match types

| Type | What it blocks | Example |
|---|---|---|
| Negative Exact | The exact search term or close variation | `[used running shoes]` |
| Negative Phrase | Any search containing that phrase in order | `"free shipping"` |
| Negative Product Targeting | Specific ASINs or product targets | Exclude poor-fit products |

### Cross-campaign negation

When a search term graduates from Broad or Auto into Exact, add it as Negative Exact in the source campaign. This helps the Exact campaign own the term and keeps discovery campaigns focused on finding new terms.

### Wasted spend workflow

1. Download the Search Term Report.
2. Filter for high spend or high clicks with zero orders.
3. Check relevance before negating.
4. Use Negative Exact for one bad term.
5. Use Negative Phrase for a bad concept that should never match.
6. Log the change.

### Common mistakes

Over-negating kills discovery. Negative conflicts can block your own good keyword. Using Negative Exact when you need Negative Phrase can let similar waste keep slipping through.

## Section 10
## Complete data-filled section notes

Metrics are the language of PPC. Beginners should learn what each metric answers, not just memorize formulas.

| Metric | Formula | What it answers |
|---|---|---|
| CTR | Clicks / Impressions | Is the ad attractive and relevant? |
| CVR | Orders / Clicks | Does the listing convert traffic? |
| CPC | Spend / Clicks | How expensive is traffic? |
| ACOS | Spend / Ad Sales | How efficient is ad spend? |
| ROAS | Ad Sales / Spend | How much revenue per ad dollar? |
| TACOS | Spend / Total Sales | How much the business relies on ads? |

### ACOS vs TACOS

ACOS measures ad-attributed sales only. TACOS includes organic sales. A campaign can have higher ACOS while TACOS improves if PPC helps organic rank and total revenue grows. That is why serious PPC managers look at both.

### Health scorecard starter

| Metric | Good | Warning | Danger |
|---|---|---|---|
| ACOS | At or below target | Target + 10% | Target + 20% |
| CTR | At category norm | 75% of norm | 50% of norm |
| CVR | At category norm | 75% of norm | 50% of norm |
| Budget use | 80-100% | 60-80% | Below 60% if campaign should scale |

### Break-even ACOS

`Break-even ACOS = Gross Profit / Price`

If a product sells for $50 and profit before ads is $15, break-even ACOS is 30%. Above that, ads are likely unprofitable unless there is a launch or ranking reason.

## Section 11
## Complete data-filled section notes

Reporting turns PPC activity into decisions. A report should answer: what happened, why it happened, and what we will do next.

### Native reports

| Report | Main use |
|---|---|
| Search Term Report | Find winners, waste, and customer language |
| Placement Report | Optimize Top of Search, Rest of Search, Product Pages |
| Targeting Report | Review keyword and ASIN target performance |
| Bulk Operations | Make and audit large-scale changes |

### Brand Analytics

Brand Analytics can provide Search Query Performance, Market Basket Analysis, Item Comparison, and Repeat Purchase Behavior. Use these to understand market demand, competitor overlap, and cross-sell opportunities.

### Client dashboard layers

Executive dashboards need total spend, sales, ROAS, ACOS, TACOS, and trend. Operator dashboards need campaign, keyword, placement, budget, and search-term detail.

### Data storytelling formula

1. What happened.
2. Why it happened.
3. What we are doing next.

Bad: `ACOS increased due to CPC inflation.`
Good: `Ad efficiency decreased because competitors drove up click costs. We are lowering weak bids and shifting budget to the keywords still converting profitably.`

## Section 12
## Complete data-filled section notes

Amazon Marketing Cloud is an advanced analytics clean room. A clean room means advertisers can analyze privacy-safe Amazon data without taking raw customer data out of Amazon.

AMC is useful for enterprise brands, agencies, and advanced advertisers that need cross-channel attribution, overlap analysis, custom audience creation, and deeper funnel measurement.

### Common use cases

- See whether DSP exposure helped Sponsored Products conversion.
- Measure audience overlap between campaigns.
- Build audiences like `people who bought Product A but not Product B`.
- Compare exposed and unexposed audiences.

### SQL primer

AMC requires SQL-style querying. Beginners do not need to write complex queries immediately, but they should understand that AMC is not a normal dashboard. It is closer to a privacy-safe analytics database.

## Section 13
## Complete data-filled section notes

Amazon DSP is Amazon's advanced programmatic ad platform. It can buy display, video, audio, and connected TV ads across Amazon-owned and third-party inventory.

### Sponsored Ads vs DSP

| Sponsored Ads | DSP |
|---|---|
| Search and retail-intent focused | Programmatic audience buying |
| Easier for beginners | Advanced setup and measurement |
| Direct response heavy | Full-funnel awareness and retargeting |
| Lower entry point | Higher budget and expertise needed |

### Campaign types

DSP campaigns can include display, video, audio, OTT/connected TV, prospecting, and retargeting. Prospecting reaches new audiences. Retargeting brings back shoppers who already interacted with your brand or category.

### Synergy model

`DSP Awareness -> Sponsored Brands Consideration -> Sponsored Products Conversion -> DSP/SD Retargeting`

Use AMC when possible to understand overlap and incremental impact.

## Section 14
## Complete data-filled section notes

Brand presence affects PPC because shoppers rarely buy from an ad alone. They click into a listing or Brand Store and decide whether the brand looks trustworthy.

### Brand Registry unlocks

- Sponsored Brands.
- Sponsored Display features.
- Brand Store.
- A+ Content.
- Stronger brand protection.

### Brand Store

A Brand Store is a mini website inside Amazon. It helps Sponsored Brands campaigns send traffic somewhere richer than a single product page. Structure stores by product category, use clear navigation, and track Store Insights.

### A+ Content

A+ Content improves the product detail page with richer images and modules. Better content can improve CVR, and better CVR can lower ACOS because each click becomes more likely to produce revenue.

## Section 15
## Complete data-filled section notes

Listing quality gates PPC performance. Ads bring traffic. The listing turns traffic into sales. A weak listing makes every click more expensive because fewer clicks convert.

### Listing readiness checklist

Critical before ads:

- Main image meets Amazon requirements.
- Title is complete and keyword-aware.
- Bullets explain benefits and features.
- Price is competitive.
- Product is in stock.
- Buy Box is active.

Important before scaling:

- Strong review base.
- A+ Content if Brand Registered.
- Multiple high-quality images.
- Video if available.
- Clear variation structure.

### Keyword placement hierarchy

Title is usually most important, followed by bullets, description/A+ content, and backend search terms. Backend terms should include relevant synonyms and misspellings without repeating words unnecessarily.

### Pricing and promotions

Coupons, deals, Prime Exclusive Discounts, and event promotions can lift CVR. When CVR rises, bids may become more affordable. Time bid and budget increases around deal periods, then taper after the event.

## Section 16
## Complete data-filled section notes

Automation helps scale PPC work, but it should not replace judgment. Good automation handles repetitive rules. Humans handle context, margins, inventory, and strategy.

### Native automation

Amazon automated rules can adjust bids or budgets based on conditions. Example rules: increase bid when ACOS is below target and orders are strong; decrease bid when ACOS is too high; raise budget during events.

### Bulk Operations

Bulk files are spreadsheets for large-scale changes. Use them to add keywords, change bids, pause targets, update budgets, and add negatives. Always review upload errors and keep a backup before mass changes.

### API and scripts

The Amazon Ads API can request reports, update campaigns, adjust bids, and manage targets. Build automation for alerts, recurring reports, search-term classification, and controlled bid changes.

### AI-assisted workflows

LLMs can classify search terms, draft reports, suggest negatives, summarize anomalies, and generate QA checklists. Keep human review on every change that touches bids, budgets, negatives, or campaign status.

## Section 17
## Complete data-filled section notes

Tools help with research, automation, reporting, and scale. The right tool depends on account size, team skill, budget, and workflow complexity.

### Tool categories

| Category | Examples | Best use |
|---|---|---|
| All-in-one suites | Helium 10, Jungle Scout, SellerApp | Seller workflows and research |
| PPC automation | Perpetua, Pacvue, Teikametrics | Bid and budget automation |
| Reporting | Looker Studio, Power BI, Tableau | Dashboards and stakeholder reporting |
| Enterprise retail media | Pacvue, Skai, CommerceIQ | Multi-marketplace scale |

### Build vs buy

Buy if your needs are standard and speed matters. Build if your workflow is unique, you manage many accounts, or the tool must feed a simulator, LMS, reporting engine, or internal operating system.

### Evaluation checklist

Assess features, ease of use, integrations, support, pricing, scalability, API access, export options, audit logs, and whether a junior team member can use it safely.

## Section 18
## Complete data-filled section notes

PPC strategy changes as the product matures. A launch campaign should learn fast. A mature campaign should protect profit. A sunset campaign should spend only where it still makes sense.

### New product launch

Weeks 1-2: launch Auto and Broad discovery campaigns. Expect higher ACOS because the account is buying data.

Weeks 3-6: expand into Manual Broad and Phrase using discovered terms. Begin adding negatives and moving clear winners.

Weeks 7-12: scale Exact campaigns and proven ASIN targets. Increase budgets where ACOS and inventory allow.

### Growth stage

Identify top keywords by orders, increase bids carefully, add similar terms, test Sponsored Brands, and expand into Sponsored Display if traffic and budget justify it.

### Mature stage

Shift more budget to Exact, Brand Defense, and proven ASIN targets. Keep discovery alive but controlled. Audit negatives, placements, and budget waste weekly.

### Decline or sunset

Reduce bids, pause weak campaigns, keep only profitable exact terms, and align spend with remaining inventory. Liquidation campaigns can accept higher ACOS only if the goal is stock clearance.

## Section 19
## Complete data-filled section notes

Different categories need different PPC expectations. A $250 product behaves differently from a $12 impulse item.

### High-consideration products

Higher price products usually have longer research cycles and lower CVR. Use brand-building, remarketing, better content, and longer analysis windows.

### Low-price impulse products

Low-price products need volume and efficient CPC. Margins are often thin, so bids must be controlled tightly. Broad match can work, but waste must be watched closely.

### Seasonal and gift products

Seasonal products need pre-season testing, peak-season budget scaling, and post-season tapering. Build keyword data before the buying rush, not during the last frantic week.

### Regulated categories

Supplements, health, beauty, grocery, and other restricted categories require conservative claims, approval awareness, and strong documentation. Compliance mistakes can stop ads cold.

## Section 20
## Complete data-filled section notes

Seasonal PPC is planned in phases: before the event, during the event, and after the event.

### Prime Day playbook

Pre-event: increase budget moderately, test keywords, confirm inventory, and prepare campaigns.

During event: raise budgets and bids only on campaigns that can convert and have inventory. Watch spend several times per day.

Post-event: taper budget instead of cutting instantly. Late shoppers, carts, and delayed attribution still matter.

### Q4 and BFCM

Black Friday, Cyber Monday, and Q4 require inventory-aware bidding. If stock is low, throttle bids to avoid selling out too early. If inventory is high, push proven campaigns harder.

### Other peaks

Back to School, Spring Cleaning, Mother's Day, Father's Day, Valentine's Day, and category-specific events should have their own prep calendars.

## Section 21
## Complete data-filled section notes

International PPC is not copy-paste PPC. Currency, language, culture, competition, and search behavior change by marketplace.

### Marketplace considerations

US is usually the largest and most competitive. UK uses different spelling and market behavior. EU requires language localization. Canada may require English and French. Australia is smaller but growing.

### Centralized vs localized management

Centralized strategy keeps standards consistent. Localized execution improves keyword relevance and cultural fit. Best practice is often central strategy with local language validation.

### Localization workflow

Translate meaning, not just words. Use native speakers where possible. Test small. Review search term reports by marketplace. Keep separate negatives and keyword banks per language.

## Section 22
## Complete data-filled section notes

Team operations turn PPC knowledge into repeatable execution. Without clear roles, change logs, and QA, even good strategy becomes chaos wearing a spreadsheet hat.

### Role ladder

| Role | Main job |
|---|---|
| VA | Daily checks, reports, basic changes |
| Junior strategist | Optimization, keyword work, weekly analysis |
| Senior strategist | Strategy, QA, client leadership |
| Agency owner | Business direction, hiring, escalation |

### Weekly rhythm

Monday: review prior week and budget utilization. Tuesday: implement keyword and bid changes. Wednesday: reporting and alerts. Thursday: underperformer deep dive. Friday: inventory, planning, and documentation.

### QA rules

Material bid, budget, structure, and negative changes should be reviewed. Every change log needs date, owner, campaign, old value, new value, reason, and later result.

### VA competency checklist

A trained VA should create campaigns, run reports, identify wasted spend, add negatives, adjust bids within rules, format reports, update logs, and escalate issues.

## Section 23
## Complete data-filled section notes

Client communication translates PPC work into trust. Stakeholders rarely need every keyword detail. They need to know what happened, why, what it means, and what you are doing.

### Reporting cadence

Weekly reports should focus on spend, sales, ACOS, ROAS, budget utilization, top/bottom campaigns, keyword insights, and next actions.

Monthly reports should include trends, month-over-month changes, 30/60/90-day plan, budget forecast, and strategic recommendations.

Quarterly reports should cover year-to-date performance, goal progress, major learnings, strategic shifts, and planning.

### Difficult conversation framework

1. Acknowledge the issue clearly.
2. Explain the specific cause without hiding behind jargon.
3. Present the action plan and review window.

Example: `Performance is below target this month. Competitor promotions increased CPC by 20%. We are reducing weak bids, protecting proven exact terms, and reviewing results in 14 days.`

## Section 24
## Complete data-filled section notes

Compliance protects the account. A great PPC strategy is useless if ads are rejected or the seller account is restricted.

### Policy basics

Avoid prohibited products, misleading claims, unsupported health claims, fake urgency, counterfeit products, and unsafe content. Do not use competitor trademarks in ad copy unless policy allows it for that exact context.

### Account health

Suspensions, policy strikes, Buy Box loss, listing suppression, inventory issues, and category restrictions can stop ad delivery. Check account health before troubleshooting bids.

### Competitor boundaries

Allowed: target competitor ASINs or bid on competitor-related search terms where permitted. Not allowed: pretend to be the competitor, use misleading copy, or make unsupported comparisons.

## Section 25
## Complete data-filled section notes

Retail media is expanding beyond Amazon. Walmart Connect, Target Roundel, Instacart, and other retail media networks are part of the same trend: advertisers want to reach shoppers near the point of purchase.

### Amazon's advantage

Amazon has high purchase intent and strong first-party shopping data. This becomes more valuable as privacy changes reduce third-party tracking.

### AI trends

Expect more AI-generated creative, predictive bidding, automated recommendations, and machine-learning budget allocation. The operator's job shifts from manual clicking to strategy, QA, prompt design, and guardrail setting.

### Privacy and signal loss

As third-party signals weaken, first-party data becomes more important. Build customer lists, use Brand Analytics, and design reporting around privacy-safe measurement.

## Section 26
## Complete data-filled section notes

Amazon PPC can become a full career path. Fresh graduates can start with operations, then grow into strategy, analytics, team leadership, and agency ownership.

### Certifications

Start with Amazon Ads learning resources and Sponsored Ads certifications. Then build practical skill through real console practice, report analysis, and scenario-based exercises.

### Career path

| Level | Skill focus |
|---|---|
| Junior | Basic campaign management and reporting |
| Senior | Optimization, diagnosis, and QA |
| Strategist | Full account strategy and client direction |
| Agency owner | Systems, hiring, sales, and service delivery |

### Continuing education

Follow Amazon Ads updates, marketplace communities, ecommerce newsletters, tool academies, and conferences. The platform changes often, so learning cadence is part of the job.

## Section 27
## Complete data-filled section notes

Case studies and templates turn lessons into reusable assets.

### Case study format

1. Situation: product, account, problem, baseline metrics.
2. Strategy: structure, targeting, budget, and success metric.
3. Execution: exact actions and timeline.
4. Results: before/after metrics.
5. Lessons: what worked, what failed, what to repeat.

### Template library

Include campaign structure spreadsheets, weekly optimization checklists, client report templates, naming convention cheat sheets, bulk upload QA sheets, and search term mining logs.

### Example result story

A running shoe account had 35% ACOS. The team restructured campaigns, added negatives, optimized placements, and shifted budget to proven exact terms. After three months, ACOS dropped to 22%, ROAS improved, and sales increased.

## Section 28
## Complete data-filled section notes

The glossary is the beginner's decoder ring. Every acronym should have a short definition, long definition, related terms, and first appearance.

### Core acronyms

| Term | Meaning |
|---|---|
| ACOS | Advertising Cost of Sales: Spend / Ad Sales |
| TACOS | Total Advertising Cost of Sales: Spend / Total Sales |
| ROAS | Return on Ad Spend: Ad Sales / Spend |
| CTR | Click-Through Rate: Clicks / Impressions |
| CVR | Conversion Rate: Orders / Clicks |
| CPC | Cost Per Click: Spend / Clicks |
| SP | Sponsored Products |
| SB | Sponsored Brands |
| SD | Sponsored Display |
| STV | Sponsored TV |
| DSP | Demand Side Platform |
| AMC | Amazon Marketing Cloud |
| SQP | Search Query Performance |

### Beginner rule

Define every acronym the first time it appears on a page. Nobody should have to guess what the abbreviations mean.

## Section 29
## Complete data-filled section notes

Formulas turn PPC into controllable math. Every calculator should show inputs, formula, example, and interpretation.

### Key formulas

`ACOS = Ad Spend / Ad Sales`

`ROAS = Ad Sales / Ad Spend`

`TACOS = Ad Spend / Total Sales`

`Break-even ACOS = Gross Profit / Price`

`Target Bid = Price x Conversion Rate x Target ACOS`

### Harvesting rule starter

Harvest a search term when it has enough clicks, enough orders, and ACOS at or below target. A starter rule is 50+ clicks, 5+ orders, and ACOS under target, but the threshold should change by price, category, and conversion rate.

## Section 30
## Complete data-filled section notes

The changelog protects trust. Amazon changes features, policies, reports, and console layouts often. Track changes so learners know what is current.

### Version history example

| Version | Date | Change |
|---|---|---|
| 2.5 | 2026-07-05 | Merged complete data-filled guide into section pages |
| 2.4 | 2026-07-05 | Added complete sections, examples, and schemas |
| 2.0 | 2026-01-01 | Major rewrite and training layer added |
| 1.0 | 2025-07-01 | Initial version |

### Update policy

Every page that describes a live console workflow should include a verification date. If unsure, tag it `[Stale?]` and assign review.

## Section 31
## Complete data-filled section notes

The training layer turns each wiki page into a teachable unit. Every important topic should eventually include a learning aid, quiz, teaching guide, handout, tags, and certification link.

### Learning aid pattern

Include a one-page visual summary, key terms, common mistakes, and a worked example. For match types, show Broad -> Phrase -> Exact as a flow.

### Quiz pattern

Use 5 to 10 questions with mixed formats: multiple choice, scenario judgment, and calculations. Include answer explanations, not just answers.

### Teaching guide pattern

Include delivery time, talking points, live-demo checklist, discussion prompts, and linked handout.

### Tagging system

Tags should include topic, learner level, delivery format, and estimated time. Example learner levels: L1 Foundation, L2 Applied, L3 Strategic, L4 Advanced.

### Certification tie-in

Use capstone quizzes by level. L1 can cover Sections 1-4. L2 can cover Sections 1-9. L3 can cover core strategy and reporting. L4 can cover advanced tools, DSP, AMC, international, and leadership.

## Section 32
## Complete data-filled section notes

The wiki should be a data source, not only a document. Every quiz, glossary term, formula, scenario, and learner progress object should exist in structured JSON or YAML so apps can reuse it.

### Core schemas

Quiz question:

``​`json
{"id":"quiz-4-1-1","topic_tag":["match-types"],"difficulty":"L1","question":"Which match type gives the most impressions?","options":["Exact","Phrase","Broad"],"correct_answer":"Broad","explanation":"Broad triggers on the widest range of search terms."}
``​`

Glossary term:

``​`json
{"term":"ACOS","short_def":"Ad spend divided by ad revenue","related_terms":["ROAS","TACOS"],"first_appears_in_section":"1.3"}
``​`

Scenario:

``​`json
{"scenario_id":"scenario-broad-waste","campaign_type":"Broad Match","problem":"Irrelevant search terms are spending budget","correct_actions":["Add negatives","Reduce weak bids","Harvest winners"]}
``​`

### Sync contract

The wiki is the source of truth. Apps pull from exported JSON. Each object should have a version field so simulators and quizzes know when cached content is stale.

### Progression graph

Model topics as prerequisites, not just page numbers. Example: Bidding depends on Match Types and Core Metrics. Reporting depends on Metrics and Native Reports.
