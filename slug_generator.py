
import re
import unidecode

def generate_slug(title):
    slug = re.sub(r'[^\w\s-]', '', title.lower())
    slug = re.sub(r'[\s]+', '-', slug)
    return unidecode.unidecode(slug)
