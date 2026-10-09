import os


def test_payment_key_present():
    assert os.environ.get("PAYMENT_API_KEY"), "PAYMENT_API_KEY secret is required"
