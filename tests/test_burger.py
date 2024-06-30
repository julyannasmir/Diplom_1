from unittest.mock import Mock
from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient


class TestsBurger:

    def test_set_buns(self):
        burger = Burger()
        bun = Bun('Флюоресцентная булка R2-D3', 988)
        burger.set_buns(bun)
        assert burger.bun.get_name() == 'Флюоресцентная булка R2-D3'

    def test_add_ingredients(self):
        burger = Burger()
        ingredient = Ingredient('SAUCE', 'Соус Spicy-X', 90)
        burger.add_ingredient(ingredient)
        assert burger.ingredients[0] == ingredient

    def test_remove_ingredient(self):
        burger = Burger()
        ingredient = Ingredient('SAUCE', 'Соус Spicy-X', 90)
        burger.add_ingredient(ingredient)
        burger.remove_ingredient(0)
        assert burger.ingredients == []

    def test_move_ingredient(self):
        burger = Burger()
        ingredient = Ingredient('SAUCE', 'Соус Spicy-X', 90)
        ingredient2 = Ingredient('FILLING', 'Мясо бессмертных моллюсков Protostomia', 90)
        burger.add_ingredient(ingredient)
        burger.add_ingredient(ingredient2)
        burger.move_ingredient(1, 0)
        assert burger.ingredients == [ingredient2, ingredient]

    def test_get_price(self):
        bun_mock = Mock(spec=Bun)
        ingredient_mock = Mock(spec=Ingredient)
        bun_mock.get_price.return_value = 100
        ingredient_mock.get_price.return_value = 200
        burger = Burger()
        burger.bun = bun_mock
        burger.ingredients = [ingredient_mock]

        assert burger.get_price() == 400

    def test_get_receipt(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_name.return_value = 'Краторная булка N-200i'
        mock_ingredient1 = Mock()
        mock_ingredient1.get_type.return_value = 'SAUCE'
        mock_ingredient1.get_name.return_value = 'Соус Spicy-X'
        mock_ingredient2 = Mock()
        mock_ingredient2.get_type.return_value = 'FILLING'
        mock_ingredient2.get_name.return_value = 'Говяжий метеорит (отбивная)'
        burger.bun = mock_bun
        burger.ingredients = [mock_ingredient1, mock_ingredient2]
        burger.get_price = Mock(return_value=400)

        expected_receipt = "(==== Краторная булка N-200i ====)\n= sauce Соус Spicy-X =\n= filling Говяжий метеорит (отбивная) =\n(==== Краторная булка N-200i ====)\n\nPrice: 400"
        assert burger.get_receipt() == expected_receipt
