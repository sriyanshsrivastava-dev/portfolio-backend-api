import io

from PIL import Image, UnidentifiedImageError
from django.core.files.base import ContentFile


class ImageProcessor:

    @staticmethod
    def resize(file, dimensions: tuple[int, int]):
        try:
            image = Image.open(file)
            image.load()
        except (UnidentifiedImageError, OSError):
            return file

        # Preserve aspect ratio while limiting maximum dimensions.
        image.thumbnail(
            dimensions,
            Image.Resampling.LANCZOS
        )

        # WebP supports RGB/RGBA and therefore transparency.
        if image.mode not in ("RGB", "RGBA"):
            if "transparency" in image.info:
                image = image.convert("RGBA")
            else:
                image = image.convert("RGB")

        buffer = io.BytesIO()

        image.save(
            buffer,
            format="WEBP",
            quality=95,
            method=6
        )

        buffer.seek(0)

        return ContentFile(buffer.getvalue())