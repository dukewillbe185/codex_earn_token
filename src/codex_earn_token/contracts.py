from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class OrderProposal:
    """A fictional order proposal with no broker-side behavior."""

    symbol: str
    side: str
    notional: float
    position_quantity: float = 0.0


@dataclass(frozen=True)
class AccountSnapshot:
    """The minimum fictional account state used by the public example."""

    equity: float
    buying_power: float


@dataclass(frozen=True)
class SafetyEnvelope:
    """Illustrative constraints that are not an operating configuration."""

    paper_only: bool
    allow_short: bool
    max_order_fraction: float


@dataclass(frozen=True)
class GuardDecision:
    """A deterministic acceptance result suitable for audit logging."""

    allowed: bool
    reason: str
