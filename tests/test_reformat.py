import pytest

from src.consumer import _reformat_message


@pytest.fixture()
def message() -> dict[str, str]:
    return {
        "company": "Taylor Group",
        "first_name": "Maria",
        "last_name": "Smith",
        "phone_number": "415.891.5222",
        "address": "8618 Lisa Via Apt. 573\nFisherfort, TX 14385",
        "credit_card": "Maestro\nKimberly Jones\n584192994856 09/30\nCVV: 267\n",
        "date": "2023-06-04T07:17:48+00:00",
        "amount": 2826.8691548518036,
    }


def test_reformat_message(message: dict[str, str]) -> None:
    reformatted_message = _reformat_message(message)
    print(reformatted_message)
    for key, value in reformatted_message.items():
        if isinstance(value, str):
            assert "\n" not in value
        else:
            assert len(str(value).split(".")[-1]) <= 3
