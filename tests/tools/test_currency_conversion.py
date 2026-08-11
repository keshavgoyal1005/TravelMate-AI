from app.tools.currency_conversion import convert_currency
import pytest


def test_convert_usd_to_inr():
    result = convert_currency.invoke({
        "amount": 100,
        "from_currency": "USD",
        "to_currency": "INR"
    })

    assert result == 8500.0


def test_convert_eur_to_inr():
    result = convert_currency.invoke({
        "amount": 100,
        "from_currency": "EUR",
        "to_currency": "INR"
    })

    assert result == 9200.0


def test_unsupported_currency():
    with pytest.raises(ValueError):
        convert_currency.invoke({
            "amount": 100,
            "from_currency": "XYZ",
            "to_currency": "INR"
        })