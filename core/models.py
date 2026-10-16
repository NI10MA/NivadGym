from django.db import models
from django.urls import reverse


class Article(models.Model):#کلاس مقالات
    """Educational blog article shown on the NIVAD website."""

    title = models.CharField(max_length=200, verbose_name="عنوان")
    slug = models.SlugField(unique=True, allow_unicode=True)
    excerpt = models.TextField(verbose_name="خلاصه")
    body = models.TextField(verbose_name="متن")
    image = models.ImageField(upload_to="articles/", blank=True, null=True, verbose_name="تصویر")
    published_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True, verbose_name="منتشر شده")

    class Meta:
        ordering = ["-published_at"]
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("article_detail", args=[self.slug])


class Equipment(models.Model):#کلاس دستگا ها 
    """Gym equipment displayed in the equipment catalog."""

    name = models.CharField(max_length=150, verbose_name="نام دستگاه")
    slug = models.SlugField(unique=True, allow_unicode=True)
    category = models.CharField(max_length=100, verbose_name="دسته‌بندی")
    description = models.TextField(verbose_name="توضیحات")
    features = models.TextField(blank=True, verbose_name="ویژگی‌ها")
    image = models.ImageField(upload_to="equipment/", blank=True, null=True, verbose_name="تصویر دستگاه")
    catalog_file = models.FileField(upload_to="catalogs/equipment/", blank=True, null=True, verbose_name="کاتالوگ")
    is_active = models.BooleanField(default=True, verbose_name="فعال")

    class Meta:
        ordering = ["name"]
        verbose_name = "دستگاه"
        verbose_name_plural = "دستگاه‌ها"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("equipment_detail", args=[self.slug])


class Trainer(models.Model):#کلاس مربیان
    """Trainer profile shown on the NIVAD website."""

    name = models.CharField(max_length=120, verbose_name="نام مربی")
    slug = models.SlugField(unique=True, allow_unicode=True)
    specialty = models.CharField(max_length=150, verbose_name="تخصص")
    bio = models.TextField(verbose_name="معرفی")
    experience = models.PositiveIntegerField(default=1, verbose_name="سابقه (سال)")
    image = models.ImageField(upload_to="trainers/", blank=True, null=True, verbose_name="تصویر مربی")
    catalog_file = models.FileField(upload_to="catalogs/trainers/", blank=True, null=True, verbose_name="کاتالوگ مربی")
    is_active = models.BooleanField(default=True, verbose_name="فعال")

    class Meta:
        ordering = ["name"]
        verbose_name = "مربی"
        verbose_name_plural = "مربی‌ها"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("trainer_detail", args=[self.slug])


class Catalog(models.Model):
    """Downloadable catalog or document."""

    title = models.CharField(max_length=200, verbose_name="عنوان کاتالوگ")
    description = models.TextField(blank=True, verbose_name="توضیحات")
    file = models.FileField(upload_to="catalogs/general/", verbose_name="فایل")
    category = models.CharField(max_length=80, default="عمومی", verbose_name="دسته")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "کاتالوگ"
        verbose_name_plural = "کاتالوگ‌ها"

    def __str__(self):
        return self.title
