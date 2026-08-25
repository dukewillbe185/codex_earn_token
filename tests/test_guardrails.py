import pytest

from codex_earn_token import evaluate_order
from tests.fakes import fake_account, fake_envelope, fake_order


def test_accepts_a_small_fictional_paper_buy() -> None:
    decision = evaluate_order(
        fake_order(),
        fake_account(),
        fake_envelope(),
        mode="paper",
    )

    assert decision.allowed is True
    assert decision.reason == "accepted"


def test_rejects_live_mode_for_a_paper_only_example() -> None:
    decision = evaluate_order(
        fake_order(),
        fake_account(),
        fake_envelope(),
        mode="live",
    )

    assert decision.allowed is False
    assert decision.reason == "paper_only"


def test_rejects_a_short_sale() -> None:
    decision = evaluate_order(
        fake_order(side="sell", position_quantity=0.0),
        fake_account(),
        fake_envelope(),
        mode="paper",
    )

    assert decision.allowed is False
    assert decision.reason == "short_sale_disabled"


@pytest.mark.parametrize("notional", [0.0, -1.0])
def test_rejects_non_positive_notional(notional: float) -> None:
    decision = evaluate_order(
        fake_order(notional=notional),
        fake_account(),
        fake_envelope(),
        mode="paper",
    )

    assert decision.allowed is False
    assert decision.reason == "invalid_notional"


def test_rejects_an_order_above_the_fictional_fraction_limit() -> None:
    decision = evaluate_order(
        fake_order(notional=11.0),
        fake_account(equity=100.0),
        fake_envelope(),
        mode="paper",
    )

    assert decision.allowed is False
    assert decision.reason == "order_fraction_exceeded"


def test_rejects_a_buy_above_buying_power() -> None:
    decision = evaluate_order(
        fake_order(notional=8.0),
        fake_account(equity=100.0, buying_power=5.0),
        fake_envelope(),
        mode="paper",
    )

    assert decision.allowed is False
    assert decision.reason == "insufficient_buying_power"
