# Voice-of-Customer AI Analyzer

A Python tool that uses the Claude API to analyze unstructured customer review data and turn it into commercial recommendations a marketing team can act on.

Built by [Maren Rosen](https://www.linkedin.com/in/marenrosen/) — marketing and commercial growth executive exploring how AI accelerates voice-of-customer work.

## Why I built this

I've spent 20+ years leading marketing, merchandising, and BD teams in apparel, jewelry, and healthcare. Voice-of-customer analysis has traditionally meant weeks of survey design, agency fees, or manual review reading. I wanted to test how much of that insight cycle AI can compress — and whether the output holds up against category expertise. I chose an apparel dataset deliberately so I could judge the AI's findings against a category I know well.

## What it does

1. Loads 23,000+ real apparel customer reviews (Kaggle: Women's E-Commerce Clothing Reviews)
2. Samples a review set and sends it to Claude with a structured analyst prompt
3. Returns, in under a minute:
   - Sentiment breakdown (positive / neutral / negative)
   - Top praise themes with representative quotes
   - Top complaint themes with representative quotes
   - Recommended marketing actions tied to the findings

## Sample findings from a 50-review run

- 56% positive / 26% mixed / 18% negative sentiment
- #1 praise driver: unique design details (embroidery, lace, construction details)
- #1 complaint driver: inconsistent sizing, appearing in roughly a third of reviews
- Recommended actions included dynamic fit guidance on product pages, close-up detail photography in creative, and proactive fabric/care communication to reduce disappointment-driven returns

## How to run it

1. Get an Anthropic API key at console.anthropic.com
2. Download the dataset from Kaggle (Women's E-Commerce Clothing Reviews)
3. Open the script in Google Colab, upload the CSV, add your API key where marked
4. Run. Results print in ~60 seconds.

## Tools used

- Python (pandas)
- Anthropic Claude API (claude-sonnet-4-6)
- Google Colab
- Kaggle public dataset

## What's next

- Segment analysis: comparing what 5-star vs 1-star customers say differently
- A campaign brief generator that turns VoC findings into ready-to-route creative briefs
- Applying the same pipeline to live brand engagements
