from .types import MarketContext


def build_system_prompt(context: MarketContext, server_keys: list[str]) -> str:
	sources = ", ".join(server_keys) if server_keys else ""
	return (
		"You are an orchestration agent for market intelligence. Use ONLY the available tools from these sources: "
		f"{sources}.\n"
		"Goals:\n"
		"1) Extract the key factors of uncertainty relevant to the market.\n"
		"2) Produce a research plan: map factors to source-specific tasks and search terms.\n"
		"3) Execute calls via provided tools and summarize evidence per source.\n"
		"4) Return a JSON with fields: {factors[], tasks[], findings[], overall_probability, confidence}.\n"
		"Constraints:\n"
		"- Use ONLY the provided tools.\n"
		"- Probabilities/confidences in [0,1].\n"
		"- Keep summaries concise and cite links.\n"
		"- Return ONLY JSON, no prose.\n"
		"JSON schema guidance (not strict):\n"
		"{\n"
		"  \"factors\": [{\"name\": str, \"description\": str}],\n"
		"  \"tasks\": [{\"source\": str, \"objectives\": [str], \"search_terms\": [str]}],\n"
		"  \"findings\": [{\"source\": str, \"summary\": str, \"probability\": float, \"confidence\": float, \"citations\": [str], \"factor\": str}],\n"
		"  \"overall_probability\": float,\n"
		"  \"confidence\": float\n"
		"}\n"
		"Context:\n"
		f"- Title: {context.title}\n"
		f"- Category: {context.category}\n"
		f"- Expiry: {context.expiry or 'unknown'}\n"
	)
