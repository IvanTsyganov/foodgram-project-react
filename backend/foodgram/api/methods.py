from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response

from recipes.models import Recipe
from .serializers import RecipeSerializer


def favorite_shopping_cart(self, request, model, **kwargs):
    recipe = get_object_or_404(Recipe, id=kwargs['pk'])

    if request.method == 'POST':
        serializer = RecipeSerializer(recipe, data=request.data,
                                      context={"request": request})
        serializer.is_valid(raise_exception=True)
        if not model.objects.filter(user=request.user,
                                    recipe=recipe).exists():
            model.objects.create(user=request.user, recipe=recipe)
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response({'errors': 'Рецепт уже добавлен.'},
                        status=status.HTTP_400_BAD_REQUEST)
    else:
        get_object_or_404(model, user=request.user,
                          recipe=recipe).delete()
        return Response({'detail': 'Рецепт успешно удален.'},
                        status=status.HTTP_204_NO_CONTENT)
