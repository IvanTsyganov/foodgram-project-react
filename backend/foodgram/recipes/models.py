from django.db import models
from django.core.validators import RegexValidator

from users.models import UserFoodgram


class Tag(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Тег',
        help_text='Тег'
    )
    slug = models.SlugField(
        max_length=50,
        verbose_name='Тег',
        help_text='Укажите тег',
        unique=True,
        null=True
    )
    color = models.CharField(
        max_length=7,
        null=True,
        validators=[
            RegexValidator(
                '^#([a-fA-F0-9]{6})',
                message='Поле должно содержать HEX-код выбранного цвета.'
            )
        ]

    )

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Название ингридиента',
        help_text='Название ингридиента',
        blank=False
    )
    count = models.PositiveSmallIntegerField(
        verbose_name='Количество ингридиента',
        help_text='Количество ингридиента',
        blank=False
    )
    measurement_unit = models.TextField(
        verbose_name='Единица измерения',
        help_text='Единица измерения',
        max_length=200,
        blank=True
    )

    class Meta:
        verbose_name = 'Ингридиент'
        verbose_name_plural = 'Ингридиенты'
        ordering = ('name',)

    def __str__(self):
        return f'{self.name}, {self.measurement_unit}'


class Recipe(models.Model):
    author = models.ForeignKey(
        UserFoodgram,
        on_delete=models.CASCADE,
        verbose_name='Рецепт',
        help_text='Автор рецепта',
        blank=False
    )
    title = models.CharField(
        max_length=100,
        verbose_name='Название',
        help_text='Название рецепта',
    )
    image = models.ImageField(
        upload_to='recipes/images',
        blank=False,
        null=False,
        verbose_name='Картинка',
        help_text='Картинка'
    )
    text = models.TextField(
        verbose_name='Инструкция',
    )
    ingredient = models.ManyToManyField(
        Ingredient,
        verbose_name='Ингридиенты',
        help_text='Ингридиенты',
        blank=False
    )
    tag = models.ManyToManyField(
        Tag,
        verbose_name='Теги',
        help_text='Теги',
    )
    time = models.PositiveSmallIntegerField(
        verbose_name='Время приготовления, мин.',
        help_text='Время приготовления, мин.',
    )
    pub_date = models.DateTimeField(
        verbose_name='Дата публикации',
        auto_now_add=True
    )

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'
        ordering = ('-pub_date',)

    def __str__(self):
        return self.title


class Favorite(models.Model):
    user = models.ForeignKey(
        UserFoodgram,
        on_delete=models.CASCADE,
        related_name='favorite_user',
        verbose_name='Избранное',
        help_text='Избранное',
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='favorite_recipe',
        verbose_name='Избранный рецепт',
        help_text='Избранный рецепт',
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'recipe'],
                name='unique_favorite'
            )
        ]
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранное'

    def __str__(self):
        return f'{self.user.username} - {self.recipe.title}'


class ShoppingCart(models.Model):
    user = models.ForeignKey(
        UserFoodgram,
        on_delete=models.CASCADE,
        related_name='shopping_user',
        verbose_name='Добавил в корзину'
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='shopping_recipe',
        verbose_name='Рецепт в корзине'
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'recipe'],
                name='unique_shoppingcart'
            )
        ]
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзина'

    def __str__(self):
        return f'{self.user.username} - {self.recipe.title}'


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='recipes',
        verbose_name='Рецепт'
    )
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        related_name='ingredients',
        verbose_name='Ингредиент'
    )
    amount = models.PositiveSmallIntegerField(
        verbose_name='Количество ингридиента',
        help_text='Количество ингридиента',
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['recipe', 'ingredient'],
                name='unique_recipe_in_ingredient'
            )
        ]
        verbose_name = 'Ингредиенты в рецепте'
        verbose_name_plural = 'Ингредиенты в рецептах'

    def __str__(self):
        return (f'{self.recipe.title}: '
                f'{self.ingredient.name} - '
                f'{self.amount} '
                f'{self.ingredient.measurement_unit}')
