from __future__ import annotations

from codex_earn_token.contracts import (
    AccountSnapshot,
    GuardDecision,
    OrderProposal,
    SafetyEnvelope,
)


def evaluate_order(
    proposal: OrderProposal,
    account: AccountSnapshot,
    envelope: SafetyEnvelope,
    *,
    mode: str,
) -> GuardDecision:
    """Evaluate a fictional order without performing I/O or contacting a broker."""
    if envelope.paper_only and mode != "paper":
        return GuardDecision(False, "paper_only")

    if mode not in {"paper", "live"}:
        return GuardDecision(False, "invalid_mode")

    if proposal.side not in {"buy", "sell"}:
        return GuardDecision(False, "invalid_side")

    if proposal.notional <= 0:
        return GuardDecision(False, "invalid_notional")

    if account.equity <= 0:
        return GuardDecision(False, "invalid_equity")

    if not 0 < envelope.max_order_fraction <= 1:
        return GuardDecision(False, "invalid_envelope")

    if proposal.side == "sell" and proposal.position_quantity <= 0 and not envelope.allow_short:
        return GuardDecision(False, "short_sale_disabled")

    maximum_notional = account.equity * envelope.max_order_fraction
    if proposal.notional > maximum_notional:
        return GuardDecision(False, "order_fraction_exceeded")

    if proposal.side == "buy" and proposal.notional > account.buying_power:
        return GuardDecision(False, "insufficient_buying_power")

    return GuardDecision(True, "accepted")
