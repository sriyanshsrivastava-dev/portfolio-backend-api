from django.utils.text import slugify


def generate_unique_slug(instance, field_name):
    base_value = getattr(instance, field_name)
    base_slug = slugify(base_value)

    slug = base_slug
    counter = 2

    model = type(instance)

    while model.objects.filter(slug=slug).exclude(pk=instance.pk).exists():
        slug = f"{base_slug}-{counter}"
        counter += 1

    return slug

