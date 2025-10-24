🧠 PolyOrch — Multi-Agent MCP Orchestration for Market Intelligence
Predict. Reason. Converge.
🏗️ Overview

PolyOrch is an MCP-orchestrated multi-agent research framework built to evaluate prediction-market bets (starting with Polymarket and Kalshi) through coordinated, autonomous research.

Given a screenshot of a market, PolyOrch routes the image through a hierarchy of MCPs (Model Control Processes) — specialized reasoning and research agents — that collectively perform context extraction, evidence gathering, and consensus formation to arrive at a weighted final decision on the bet.

🔍 How It Works
1. Screenshot Input

A user provides a screenshot of a Polymarket or Kalshi bet.

The Screenshot Analyzer MCP performs OCR and visual parsing to identify:

Event title (e.g., “Will Tyrese Maxey score more than 40 points?”)

Market options (“Yes”/“No”, probabilities, expiration date)

Context cues (time, ticker, odds, platform).

2. Contextual Factor Extraction & Routing Decision

Once the bet is parsed, the Orchestration MCP interprets the event and infers the key factors required to evaluate it.
It identifies the dimensions of uncertainty and maps them to specialized research tasks before dispatching them to the relevant MCPs.

For example:

If the bet is sports-related (“Will Tyrese Maxey score more than 40 points?”):

Extract key factors: player performance trend, injury status, opposing defense strength, game schedule, and team news.

Route to: Reddit MCP (fan/injury chatter), Twitter MCP (beat reporters), Sports Data MCP (statistical models).

If the bet is political (“Will X candidate win state Y?”):

Extract key factors: polling averages, endorsements, recent events, turnout models.

Route to: Metaculus MCP, Twitter MCP, News MCP, FiveThirtyEight MCP.

If the bet is crypto/finance-related (“Will ETH exceed $5k by December?”):

Extract key factors: on-chain inflows, macroeconomic indicators, market sentiment.

Route to: Dune MCP, CoinDesk MCP, Twitter MCP, Reddit MCP.

This step effectively turns the Orchestrator into a query planner for intelligence gathering — dynamically deciding which MCPs to activate and what they should research based on the topic and time horizon.

3. Parallel Research

Each Research MCP independently gathers and summarizes relevant data:

Twitter MCP → real-time sentiment & expert commentary

Reddit MCP → retail crowd sentiment & discussion threads

LinkedIn MCP → insider/company network activity

News MCP → verified factual updates

On-Chain MCP → transaction flows, liquidity metrics

Sports MCP (if applicable) → player stats, injury updates, matchups

4. Aggregation & Weighting

The DecisionMaker MCP receives structured summaries and confidence scores from each research stream.
It then performs:

Cross-source correlation

Weight calibration based on historical predictive accuracy

Bayesian or heuristic consensus formation

→ producing a final probabilistic judgment (e.g., “Tyrese Maxey > 40 points: 58% Yes confidence, primary risks = defensive matchup and rest day uncertainty”).

5. Output

PolyOrch outputs:

The final prediction and rationale

Breakdown of factor weights and contributing sources

Relevant links and evidence trail for auditability

🧩 Architecture
flowchart TD
  A[Screenshot Input] --> B[OCR + Market Extractor MCP]
  B --> C[Orchestration MCP]
  C --> D1[Twitter MCP]
  C --> D2[Reddit MCP]
  C --> D3[LinkedIn MCP]
  C --> D4[News MCP]
  C --> D5[On-Chain MCP]
  D1 & D2 & D3 & D4 & D5 --> E[DecisionMaker MCP]
  E --> F[Final Prediction + Explanation]


Each MCP is a modular container that can be swapped or retrained independently, allowing rapid experimentation with different reasoning or retrieval paradigms.

🧠 Core Concepts
Concept	Description
MCP (Model Control Process)	A specialized reasoning unit with its own context window, API access, and memory.
Orchestration Layer	Determines which MCPs to invoke based on the parsed bet context.
Research Streams	Independent investigative flows (social, on-chain, news, expert).
Decision Fusion	The weighting and merging of multiple research perspectives into a unified probabilistic conclusion.
Convergence Hyperparameters	Tunable weights for exploration–exploitation, trust calibration, and recency bias per MCP.
⚙️ Tech Stack

Core: Python + MCP SDK (OpenAI MCP protocol)

Orchestration: asyncio + task graph

Vision/OCR: tesseract, OpenCV, or pytesseract

APIs: Polymarket GraphQL, Kalshi API, Twitter/X API, Reddit API, Dune Analytics, LinkedIn (scraper or Sales Navigator), GDELT / NewsAPI

Database: Supabase / Postgres for caching and historical weighting

Visualization: Streamlit or lightweight web dashboard

Deployment: Dockerized micro-MCPs or Ray Serve cluster

🚀 Quickstart
# Clone the repo
git clone https://github.com/your-org/polyorch.git
cd polyorch

# Install dependencies
pip install -r requirements.txt

# Launch orchestrator
python main.py --image path/to/screenshot.png

🧭 Example Flow
Input: Screenshot of Polymarket market “Will ETH be above $5,000 by Dec 31?”
↓
OCR → Extracts market name, type, and expiration
↓
Orchestration MCP → Activates Twitter, Dune, News MCPs
↓
Research MCPs → Return sentiment, on-chain data, macro news
↓
DecisionMaker MCP → Weights Twitter (0.4), Dune (0.35), News (0.25)
↓
Output → “ETH > $5k: 62% Yes confidence, driven by liquidity inflows & positive developer activity”

🧰 Future Extensions

Reinforcement learning for automatic weight tuning (meta-optimization)

Continuous training on historical prediction accuracy

Integration with portfolio management tools

Human-in-the-loop oversight dashboards

⚖️ Disclaimer

PolyOrch is a research and analysis tool.
It provides informational insights only and does not constitute financial advice or trading recommendations. Always perform independent due diligence before placing any bets or trades.

Would you like me to extend this README with a short “Contributing” + “Config File Schema” section so collaborators can easily add new MCPs (e.g., TikTok, GitHub Trends, or YouTube MCPs)?


This is a [Next.js](https://nextjs.org) project bootstrapped with [`create-next-app`](https://nextjs.org/docs/app/api-reference/cli/create-next-app).

## Getting Started

First, run the development server:

```bash
npm run dev
# or
yarn dev
# or
pnpm dev
# or
bun dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

You can start editing the page by modifying `app/page.tsx`. The page auto-updates as you edit the file.

This project uses [`next/font`](https://nextjs.org/docs/app/building-your-application/optimizing/fonts) to automatically optimize and load [Geist](https://vercel.com/font), a new font family for Vercel.

## Learn More

To learn more about Next.js, take a look at the following resources:

- [Next.js Documentation](https://nextjs.org/docs) - learn about Next.js features and API.
- [Learn Next.js](https://nextjs.org/learn) - an interactive Next.js tutorial.

You can check out [the Next.js GitHub repository](https://github.com/vercel/next.js) - your feedback and contributions are welcome!

## Deploy on Vercel

The easiest way to deploy your Next.js app is to use the [Vercel Platform](https://vercel.com/new?utm_medium=default-template&filter=next.js&utm_source=create-next-app&utm_campaign=create-next-app-readme) from the creators of Next.js.

Check out our [Next.js deployment documentation](https://nextjs.org/docs/app/building-your-application/deploying) for more details.
