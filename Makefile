.PHONY: check lint test smoke

check: lint test smoke

lint:
	uv run ruff check .

test:
	uv run pytest -q

smoke:
	PYTHONPATH=src uv run python -c 'from codex_earn_token import AccountSnapshot, OrderProposal, SafetyEnvelope, evaluate_order; decision = evaluate_order(OrderProposal("DEMO", "buy", 5.0), AccountSnapshot(100.0, 80.0), SafetyEnvelope(True, False, 0.10), mode="paper"); assert decision.allowed'
