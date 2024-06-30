from praktikum.ingredient import Ingredient


class TestsIngredient:
    def test_get_price(self):
        ingredient = Ingredient(ingredient_type='SAUCE', name='Соус Spicy-X', price=1337)
        assert ingredient.get_price() == 1337

    def test_get_name(self):
        ingredient = Ingredient(ingredient_type='SAUCE', name='Соус Spicy-X', price=1337)
        assert ingredient.get_name() == 'Соус Spicy-X'

    def test_get_type(self):
        ingredient = Ingredient(ingredient_type='SAUCE', name='Соус Spicy-X', price=1337)
        assert ingredient.get_type() == 'SAUCE'