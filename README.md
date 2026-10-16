# NIVAD GYM

وب‌سایت باشگاه **نیواد (NIVAD GYM)** با Django، MySQL و رابط کاربری مشکی/قرمز.

## مشکلات اصلی که در این نسخه اصلاح شده‌اند

- اتصال پروژه به MySQL از حالت رمز عبور هاردکد خارج شده و با `.env` مدیریت می‌شود.
- نسخه Django روی `5.2.7` قرار گرفته تا با MySQL `8.0.x` سازگار باشد.
- نام پکیج پروژه از `newted_gym` به `nivad_gym` اصلاح شده است.
- `STATIC_URL` و `MEDIA_URL` به مسیر مطلق تبدیل شده‌اند؛ بنابراین CSS و تصاویر در صفحات داخلی هم درست لود می‌شوند.
- URL دستگاه‌ها/مربیان/مقالات با `<str:slug>` اصلاح شده تا slug فارسی مثل `زیربغل-لت` بدون خطای `NoReverseMatch` کار کند.
- تصاویر دستگاه‌ها و مربیان در صفحه اصلی، لیست و صفحه جزئیات نمایش داده می‌شوند.
- تصاویر مقالات نیز در صورت وجود نمایش داده می‌شوند.
- فایل‌های HTML از کدهای اضافه و Markdown fence پاک و مرتب شده‌اند.
- CSS به تم مشکی/قرمز کامل بازنویسی شده و برای موبایل Responsive است.
- کدهای Python، HTML، CSS و JavaScript مرتب و کامنت‌گذاری شده‌اند.
- `venv`، `.git` و `__pycache__` داخل نسخه تمیز پروژه قرار نگرفته‌اند.

## راه‌اندازی

### 1. ساخت محیط مجازی

```powershell
python -m venv venv
.env\Scripts\Activate.ps1
```

اگر PowerShell اجازه فعال‌سازی نداد:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.env\Scripts\Activate.ps1
```

### 2. نصب کتابخانه‌ها

```powershell
pip install -r requirements.txt
```

### 3. ساخت دیتابیس MySQL

در MySQL اجرا کنید:

```sql
CREATE DATABASE nivad_gym
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
```

اگر دیتابیس از قبل وجود دارد، این مرحله لازم نیست.

### 4. تنظیم رمز MySQL

فایل `.env.example` را به `.env` تغییر نام دهید و مقدار `DB_PASSWORD` را با رمز MySQL خودتان پر کنید.

نمونه:

```env
DB_NAME=nivad_gym
DB_USER=root
DB_PASSWORD=رمز_مای_اسکیو_ال
DB_HOST=127.0.0.1
DB_PORT=3306
```

### 5. اجرای Migration

```powershell
python manage.py migrate
```

### 6. ساخت کاربر مدیر

```powershell
python manage.py createsuperuser
```

### 7. اجرای پروژه

```powershell
python manage.py runserver
```

سپس:

- سایت: `http://127.0.0.1:8000/`
- پنل مدیریت: `http://127.0.0.1:8000/admin/`

## نکته مهم درباره تصاویر

تصاویر داخل پوشه `media/` هستند و Django در حالت توسعه آن‌ها را از مسیر `/media/` سرو می‌کند.

برای مثال:

```django
{% if item.image %}
    <img src="{{ item.image.url }}" alt="{{ item.name }}">
{% endif %}
```

در تنظیمات نیز باید حتماً این دو مقدار با `/` شروع شوند:

```python
STATIC_URL = "/static/"
MEDIA_URL = "/media/"
```

این موضوع مخصوصاً در صفحات داخلی مثل `/equipment/.../` مهم است.
