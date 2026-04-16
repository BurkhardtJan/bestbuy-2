import pytest
import products


def test_create_product():
    """Tests the creation of a normal product."""
    test_product = products.Product("Test 1", price=250, quantity=500)
    # assert test_product.name == "Test 1"
    # assert test_product.price == 250
    # assert test_product.quantity == 500
    assert hasattr(test_product, "name")
    assert getattr(test_product, "name") == "Test 1"
    assert hasattr(test_product, "price")
    assert getattr(test_product, "price") == 250
    assert hasattr(test_product, "quantity")
    assert getattr(test_product, "quantity") == 500


def test_create_product_empty_name():
    """Tests the creation of a product with empty name.
    Should raise an exception."""
    with pytest.raises(Exception) as e:
        test_product = products.Product("", price=250, quantity=500)


def test_create_product_negative_price():
    """Tests the creation of a product with negative price.
    Should raise an exception."""
    with pytest.raises(ValueError) as e:
        test_product = products.Product("Test", price=-250, quantity=500)


def test_product_becomes_inactive():
    """Test if product becomes inactive after reaching 0 units"""
    test_product = products.Product("Test", price=250, quantity=500)
    test_product.buy(500)
    assert test_product.is_active() == False


def test_buy_modifies_quantity():
    """Tests if the buy modifies quantity."""
    test_product = products.Product("Test", price=250, quantity=500)
    test_product.buy(300)
    assert test_product.quantity == 200


def test_buy_too_many_quantity():
    """Tests if raises error when buy too many quantity."""
    with pytest.raises(Exception) as e:
        test_product = products.Product("Test", price=250, quantity=500)
        test_product.buy(600)
