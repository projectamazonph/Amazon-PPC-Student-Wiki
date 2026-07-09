---
title: "PPC Strategy Hub"
summary: "Master Amazon PPC strategies from launch through scale — campaign types, bidding approaches, and seasonal playbooks."
last_updated: 2026-07-09
owner: "Wiki Maintenance Agent"
status: "active"
tags: ["strategy", "campaign-types", "bidding", "seasonal", "advanced"]
---

# PPC Strategy Hub

This hub pulls together every strategy-related page in the wiki and adds context for 2026. If you want to know what to actually do with your campaigns — start here.

## Existing Strategy Pages

These pages in the wiki cover the foundations. Read them in this order:

| Topic | Page | What It Covers |
|-------|------|----------------|
| Campaign Types | [Sponsored Products](/sections/03-3-campaign-types/3-1-3-1-sponsored-products-sp.md) | The workhorse of Amazon PPC. Most campaigns start and end here. |
| Campaign Types | [Sponsored Brands](/sections/03-3-campaign-types/3-2-3-2-sponsored-brands-sb.md) | Brand awareness, headline search ads, when to use SB vs. SP |
| Campaign Types | [Sponsored Display](/sections/03-3-campaign-types/3-3-3-3-sponsored-display-sd.md) | Audience-based targeting, retargeting, competitor outreach |
| Campaign Types | [Amazon DSP](/sections/03-3-campaign-types/3-5-3-5-amazon-dsp.md) | Programmatic advertising, off-Amazon audiences, enterprise level |
| Targeting | [Keyword Match Types](/sections/04-4-targeting-and-match-types/4-1-4-1-keyword-match-types.md) | Broad, phrase, exact — when to use each |
| Targeting | [Product Targeting](/sections/04-4-targeting-and-match-types/4-2-4-2-product-targeting.md) | ASIN targeting, category targeting, competitor campaigns |
| Targeting | [Audience Targeting](/sections/04-4-targeting-and-match-types/4-3-4-3-audience-targeting.md) | In-market audiences, lifestyle segments, retargeting audiences |
| Bidding | [Manual Bidding Fundamentals](/sections/06-6-bidding-strategies-and-bid-management/6-1-6-1-manual-bidding-fundamentals.md) | Your starting point before using any automation |
| Bidding | [Dynamic and Rule-Based Bidding](/sections/06-6-bidding-strategies-and-bid-management/6-2-6-2-dynamic-and-rule-based-bidding.md) | When to use dynamic bids up/down, and when to write your own rules |
| Bidding | [Bid Adjustment Cadence](/sections/06-6-bidding-strategies-and-bid-management/6-3-6-3-bid-adjustment-cadence.md) | How often to check and change bids without wasting time |
| Bidding | [Placement Bid Modifiers](/sections/06-6-bidding-strategies-and-bid-management/6-4-6-4-placement-bid-modifiers.md) | Top of search, product pages, rest of results — adjust by placement |
| Structure | [Campaign Structuring Models](/sections/02-2-account-and-campaign-architecture/2-2-2-2-campaign-structuring-models.md) | Single keyword campaigns, campaign-per-match-type, hybrid approaches |

---

## Advanced Strategies

These tactics go beyond the basics. Most work best once you have 30+ days of data.

### Single Keyword Campaigns (SKC)

Instead of grouping keywords into ad groups, run each keyword in its own campaign. This gives you total control over each keyword's budget and bid. It sounds like overkill but it solves a real problem: when you group 20 keywords together and one starts spending 80% of the budget on a term that barely converts.

**When SKC makes sense:**
- Head terms with high volume and high competition (where small bid changes have big spend implications)
- Brand protection keywords (you want to know exactly what you're spending)
- Long-tail keywords you want to test without cannibalizing other campaigns

**When to skip it:**
- You have 500+ products — managing 500+ campaigns becomes its own problem
- Early-stage campaigns where you're still discovering which keywords matter

### Dynamic Bidding Deep Dive

Amazon's dynamic bidding has three modes:
- **Dynamic bids — down only**: Amazon lowers your bid when a conversion seems unlikely. Safe, conservative.
- **Dynamic bids — up and down**: Amazon raises your bid when a conversion seems very likely. More aggressive, can spend more than expected.
- **Fixed bids**: You set it and Amazon doesn't touch it.

In 2026, the algorithm also factors in shopper engagement signals (time on page, bounce rate from your product page, add-to-cart rate) alongside conversion probability. This means a keyword that used to bid up aggressively might not anymore if Amazon sees weak engagement signals on your listing.

**Practical advice:** Start with dynamic bids down only for new campaigns. Once you have data showing which keywords convert, switch to dynamic up and down for the winners. Keep everything else on fixed or down-only.

### Competitor ASIN Targeting

Targeting competitor products directly can be one of the fastest ways to generate sales when you're new. The trick is not to just target every competitor blindly — be selective.

**Target competitors who:**
- Have 4+ stars (buyers there are happy and ready to consider alternatives)
- Have fewer than 20 reviews (your review count advantage is meaningful)
- Are priced higher than you (give buyers a deal comparison)

**Don't target competitors who:**
- Are the market leader with 10,000+ reviews (you're fighting an uphill battle)
- Have a fundamentally different product (you're just burning spend on uninterested shoppers)

---

## Seasonal Playbooks

### Q4 Peak Season (November — December)

Q4 is the highest-spending period on Amazon. The playbook:

**Timing:** Start ramping budgets 4-6 weeks before Black Friday. If you start in late October with cold campaigns, you're too late.

**Budget:** Many sellers 3x-5x their normal PPC budget in Q4. The math works because conversion rates spike even as CPCs rise. Your breakeven ACOS is higher than normal and that's fine.

**Bidding:** Use aggressive placement modifiers. Top of search during Q4 is expensive but it converts. Many sellers set +50% to +100% modifiers for the top 3 weeks of December.

**Match types:** Shift toward broader match during Q4. More people are searching who don't know exactly what they want — they're buying gifts. Broader reach captures these browsers.

**Pitfall:** Don't get into Q4 with campaigns that haven't been optimized. If your normal campaigns have a 35% ACOS in October, they won't magically fix themselves in November.

### Prime Day (July)

Prime Day is compressed — usually 48 hours of peak traffic. The playbook:

**Before Prime Day (4 weeks out):**
- Increase budgets modestly (not Q4-level, but noticeable)
- Pause or reduce bids on keywords with poor conversion history
- Ensure your campaigns can run through the day without hitting limits

**During Prime Day:**
- Monitor campaigns hourly if possible
- Raise placement modifiers for top of search
- Accept higher ACOS — the goal is to capture sales momentum and ranking
- Many sellers run at ACOS targets 5-10 percentage points above normal

**After Prime Day:**
- Drop budgets back down the day it ends (or the day after) — spending while conversion is still elevated but traffic is dropping will hurt your ACOS
- Analyze which campaigns drove the most incremental sales

### Back to School (August — September)

Less dramatic than Q4 but significant for relevant categories. Strategy:
- Create a separate campaign or ad group with school-related keywords ("back to school", "school supplies", "college dorm")
- Budget is typically 1.5x-2x normal for the category
- This is a bridge between slow summer and Q4 ramp — use it to gather data

---

## Real Campaign Examples

### Example 1: Long-Tail Focus Strategy
- Product: specialized phone case, $22 price
- Approach: 100% exact match, long-tail keywords only ("iphone 15 pro max waterproof case", "shockproof phone case with card holder")
- Starting ACOS: 28% at $50/day
- After 60 days: ACOS 19% — the long-tail terms cost more per click but convert at a higher rate
- Key learning: head terms look efficient by CTR but often have lower CVR once you factor in wasted impressions

### Example 2: Auto-to-Manual Pipeline
- Product: yoga mat, $35 price
- Approach: 8-week auto campaign to harvest search terms, then moved winners to manual exact campaigns
- Auto campaign ACOS: 38% (acceptable for discovery)
- Manual exact campaign ACOS: 22% (same terms, much better efficiency)
- Key learning: auto campaigns are expensive but valuable as a research layer. Run them long enough to find your winners, then graduate those terms to manual campaigns where you have full control.

### Example 3: Competitive Category Breakthrough
- Product: protein powder, $30 price, 3rd-party brand in a crowded category
- Approach: Sponsored Products + Sponsored Display competitor targeting
- First 90 days: ACOS 45% — expected given the category
- Year 2: ACOS stabilized at 27% after building up organic rank and review momentum
- Key learning: in competitive categories, the first year of PPC is often unprofitable on its own. The payoff comes from the organic sales that PPC ranking generates.
