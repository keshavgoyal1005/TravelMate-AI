from langchain_core.tools import tool

@tool
def convert_currency(
    amount: float,
    from_currency: str,
    to_currency: str,
) -> float:
    """
    Convert an amount from one currency to another.
    """

    exchange_rates = {
        ("USD", "INR"): 85.0,
        ("EUR", "INR"): 92.0,
        ("GBP", "INR"): 108.0,
    }

    rate = exchange_rates.get(
        (from_currency.upper(), to_currency.upper())
    )

    if rate is None:
        raise ValueError(
            f"Unsupported currency conversion: "
            f"{from_currency} to {to_currency}"
        )

    return amount * rate
    