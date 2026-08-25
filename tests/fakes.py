from codex_earn_token import AccountSnapshot, OrderProposal, SafetyEnvelope


def fake_account(*, equity: float = 100.0, buying_power: float = 80.0) -> AccountSnapshot:
    """Return fictional account data used only by public tests."""
    return AccountSnapshot(equity=equity, buying_power=buying_power)


def fake_order(
    *,
    side: str = "buy",
    notional: float = 5.0,
    position_quantity: float = 0.0,
) -> OrderProposal:
    """Return a fictional order that has no broker integration."""
    return OrderProposal(
        symbol="DEMO",
        side=side,
        notional=notional,
        position_quantity=position_quantity,
    )


def fake_envelope() -> SafetyEnvelope:
    """Return illustrative limits that are unrelated to any operating system."""
    return SafetyEnvelope(paper_only=True, allow_short=False, max_order_fraction=0.10)
