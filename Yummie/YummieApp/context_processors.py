from .models import FoodCategory
def menu_links(request):
    links=FoodCategory.objects.all()
    return dict(links=links)