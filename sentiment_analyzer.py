import pandas as pd
import anthropic

# ---- SETTINGS ----
API_KEY = "PUT-KEY-HERE"
CSV_FILE = "/content/Womens Clothing E-Commerce Reviews.csv"

# ---- LOAD THE REVIEWS ----
df = pd.read_csv(CSV_FILE)
reviews = df["Review Text"].dropna().sample(50, random_state=1).tolist()
review_block = "\n".join(f"{i+1}. {r}" for i, r in enumerate(reviews))

# ---- ASK CLAUDE TO ANALYZE ----
client = anthropic.Anthropic(api_key=API_KEY)

prompt = f"""You are a voice-of-customer analyst for an apparel brand.
Analyze the 50 customer reviews below and return:
1. Sentiment breakdown (count of positive / neutral / negative)
2. Top 3 praise themes, each with one short example quote
3. Top 3 complaint themes, each with one short example quote
4. Three recommended actions for the marketing team

Reviews:
{review_block}"""

response = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1500,
    messages=[{"role": "user", "content": prompt}],
)

# ---- PRINT THE RESULTS ----
print(response.content[0].text)
