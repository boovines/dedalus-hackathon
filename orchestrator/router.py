from typing import Dict, List
from .types import MarketContext


def _normalize_category(category: str) -> str:
    value = (category or "").strip().lower()
    synonyms = {
        "politics": "political",
        "election": "political",
        "governance": "political",
        "crypto": "crypto",
        "cryptocurrency": "crypto",
        "tech": "tech",
        "technology": "tech",
    }
    return synonyms.get(value, value or "default")


def select_server_keys(context: MarketContext, config: Dict) -> List[str]:
    routing = (config or {}).get("routing", {})
    normalized = _normalize_category(context.category)
    if normalized in routing:
        return list(routing.get(normalized, []))
    return list(routing.get("default", []))


def resolve_mcp_servers(keys: List[str], config: Dict) -> Dict[str, str]:
    servers = (config or {}).get("marketplace_servers", {})
    resolved: Dict[str, str] = {}
    for key in keys:
        slug = servers.get(key)
        if slug:
            resolved[key] = slug
    return resolved
