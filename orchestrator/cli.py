import json
import argparse
from pathlib import Path
from typing import Optional

from .types import MarketContext
from .run_orchestration import orchestrate


def _load_context(path: Path) -> MarketContext:
	data = json.loads(path.read_text(encoding="utf-8"))
	return MarketContext(**data)


def main() -> None:
	parser = argparse.ArgumentParser(description="Run PolyOrch Orchestration")
	parser.add_argument("--context", type=str, help="Path to JSON context file")
	parser.add_argument("--title", type=str, help="Market title", default=None)
	parser.add_argument("--category", type=str, help="Market category", default=None)
	parser.add_argument("--expiry", type=str, help="Expiry ISO date", default=None)
	parser.add_argument("--stream", action="store_true", help="Enable streaming")
	args = parser.parse_args()

	if args.context:
		ctx = _load_context(Path(args.context))
	else:
		if not args.title or not args.category:
			raise SystemExit("Either --context path OR --title and --category must be provided")
		ctx = MarketContext(title=args.title, category=args.category, expiry=args.expiry)

	# Run orchestration
	import asyncio
	result = asyncio.run(orchestrate(ctx, stream=args.stream))

	print(json.dumps(result.model_dump(), ensure_ascii=False, indent=2))


if __name__ == "__main__":
	main()
