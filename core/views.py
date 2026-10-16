from django.shortcuts import get_object_or_404, render

from .models import Article, Catalog, Equipment, Trainer

#بخش تابع های نمایشی و خروجی گرفتن که با کلاس ها در ارتباط هستن
def home(request):
    """Render the NIVAD homepage with the latest content."""
    context = {
        "articles": Article.objects.filter(is_published=True)[:3],
        "equipment": Equipment.objects.filter(is_active=True)[:6],
        "trainers": Trainer.objects.filter(is_active=True)[:4],
    }
    return render(request, "core/home.html", context)


def article_list(request):
    """Render the list of published articles."""
    articles = Article.objects.filter(is_published=True)
    return render(request, "core/articles.html", {"articles": articles})


def article_detail(request, slug):
    """Render a single published article."""
    article = get_object_or_404(Article, slug=slug, is_published=True)
    return render(request, "core/article_detail.html", {"article": article})


def equipment_list(request):
    """Render all active equipment."""
    equipment = Equipment.objects.filter(is_active=True)
    return render(request, "core/equipment.html", {"equipment": equipment})


def equipment_detail(request, slug):
    """Render one active equipment item."""
    item = get_object_or_404(Equipment, slug=slug, is_active=True)
    return render(request, "core/equipment_detail.html", {"item": item})


def trainer_list(request):
    """Render all active trainers."""
    trainers = Trainer.objects.filter(is_active=True)
    return render(request, "core/trainers.html", {"trainers": trainers})


def trainer_detail(request, slug):
    """Render one active trainer."""
    trainer = get_object_or_404(Trainer, slug=slug, is_active=True)
    return render(request, "core/trainer_detail.html", {"trainer": trainer})


def catalog_list(request):
    """Render all downloadable catalogs."""
    catalogs = Catalog.objects.all()
    return render(request, "core/catalogs.html", {"catalogs": catalogs})
