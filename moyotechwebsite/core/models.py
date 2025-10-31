from django.db import models


class TeamMember(models.Model):
    """One person – either Leadership or Instructor."""
    ROLE_CHOICES = [
        ('leadership', 'Leadership Team'),
        ('instructor', 'Our Team'),          # matches the two sections in the HTML
    ]

    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)          # e.g. CEO/Founder, Senior Engineer
    role_group = models.CharField(max_length=20, choices=ROLE_CHOICES)
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to='team/', blank=True, null=True)

    # optional ordering inside each group
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['role_group', 'order', 'name']

    def __str__(self):
        return f"{self.name} – {self.get_role_group_display()}"
    
# your_app/models.py
from django.db import models
from django.utils.html import mark_safe

class Product(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.CharField(max_length=100, help_text="e.g. EdTech Platform, Agri-Tech App")
    short_description = models.TextField(max_length=300)
    price = models.CharField(max_length=50, help_text="e.g. From MWK 1M, Free Tier Available")
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    # Popup details
    popup_title = models.CharField(max_length=120, blank=True)
    features = models.TextField(
        help_text="One feature per line. Will be converted to bullet list."
    )
    stats = models.CharField(max_length=150, help_text="e.g. Powering 5K+ students across Malawi.", blank=True)

    class Meta:
        ordering = ['order', 'name']
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name

    def feature_list(self):
        """Return HTML bullet list of features."""
        if not self.features:
            return ""
        items = self.features.strip().split('\n')
        html = '<ul class="space-y-2 text-sm text-gray-700 mb-4">'
        for item in items:
            item = item.strip()
            if item:
                html += f'<li><i class="fas fa-check text-orange-600 mr-2"></i>{item}</li>'
        html += '</ul>'
        return mark_safe(html)
    feature_list.short_description = "Features"
    
    
# your_app/models.py
from django.db import models
from django.utils.html import mark_safe


# ---------- SOFTWARE PRODUCTS ----------
class SoftwareProduct(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.CharField(max_length=100, help_text="e.g. Learning Management")
    short_description = models.TextField(max_length=300)
    price = models.CharField(max_length=50, default="Contact for Pricing")
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'name']
        verbose_name = "Software Product"

    def __str__(self):
        return self.name


# ---------- COURSES ----------
class Course(models.Model):
    title = models.CharField(max_length=120)
    subtitle = models.CharField(max_length=100, help_text="e.g. React + Django")
    short_description = models.TextField(max_length=300)
    duration = models.CharField(max_length=50, default="6 Months")
    image = models.ImageField(upload_to='courses/', blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    # Popup details
    popup_title = models.CharField(max_length=150, blank=True)
    features = models.TextField(
        help_text="One bullet per line. Will become <li> list."
    )

    class Meta:
        ordering = ['order', 'title']
        verbose_name = "Course"

    def __str__(self):
        return self.title

    def feature_list(self):
        if not self.features:
            return ""
        items = [i.strip() for i in self.features.split('\n') if i.strip()]
        html = '<ul class="space-y-2 text-sm text-gray-700 mb-4">'
        for item in items:
            html += f'<li><i class="fas fa-check text-orange-600 mr-2"></i>{item}</li>'
        html += '</ul>'
        return mark_safe(html)
    feature_list.short_description = "Features"


# ---------- HOSTING PACKAGES ----------
class HostingPackage(models.Model):
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=50, help_text="e.g. MWK 15 K/mo or Custom")
    description = models.TextField(max_length=500)
    is_popular = models.BooleanField(default=False, help_text="Highlight with scale")
    features = models.TextField(
        help_text="One feature per line."
    )
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'name']
        verbose_name = "Hosting Package"

    def __str__(self):
        return f"{self.name} – {self.price}"

    def feature_list(self):
        if not self.features:
            return ""
        items = [i.strip() for i in self.features.split('\n') if i.strip()]
        html = '<ul class="text-left space-y-2 mb-6 text-sm">'
        for item in items:
            html += f'<li><i class="fas fa-check text-orange-600 mr-2"></i>{item}</li>'
        html += '</ul>'
        return mark_safe(html)
    feature_list.short_description = "Features"