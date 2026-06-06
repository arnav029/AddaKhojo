from django.db import models
from django.utils.text import slugify


class Place(models.Model):
    TYPE_CHOICES = [
        ('cafe', 'Café'),
        ('thela', 'Thela / Cart'),
        ('garden', 'Garden / Park'),
        ('restaurant', 'Restaurant'),
        ('shop', 'Shop'),
        ('shortcut', 'Shortcut / Spot'),
        ('other', 'Other'),
    ]
    VIBE_CHOICES = [
        ('worth_the_detour', 'Worth the detour'),
        ('only_if_nearby', 'Only if nearby'),
        ('calm_o_meter_max', 'Calm-o-meter: max'),
        ('hidden_gem', 'Hidden gem'),
        ('local_favourite', 'Local favourite'),
    ]
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
    ]

    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True, blank=True)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='other')
    is_on_google = models.BooleanField(default=False, verbose_name='Listed on Google?')
    sector = models.CharField(max_length=60, blank=True, help_text='e.g. Sector 3')
    location_text = models.CharField(max_length=300, blank=True, help_text='Human directions: "footpath near 27th Main"')
    lat = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    lng = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    timings_text = models.CharField(max_length=150, blank=True, help_text='e.g. "evenings only", "9am-11pm"')
    price_text = models.CharField(max_length=100, blank=True, help_text='e.g. "Rs 30", "Rs 500 for two", "free"')
    vibe_tag = models.CharField(max_length=30, choices=VIBE_CHOICES, blank=True)
    caption = models.TextField(help_text='Main review / write-up')
    practical_notes = models.CharField(max_length=300, blank=True, help_text='"cash only", "sells out by 9"')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.name)
            slug = base
            n = 1
            while Place.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f'{base}-{n}'
                n += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def vibe_icon(self):
        icons = {
            'worth_the_detour': '🚶',
            'only_if_nearby': '📍',
            'calm_o_meter_max': '😌',
            'hidden_gem': '💎',
            'local_favourite': '❤️',
        }
        return icons.get(self.vibe_tag, '')


class Photo(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='photos')
    image = models.ImageField(upload_to='places/%Y/%m/')
    caption = models.CharField(max_length=200, blank=True, help_text='Handwritten-style aside')
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return f'{self.place.name} — photo {self.order}'
