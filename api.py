from models import Category

categories = []


def create_category(cat: str) -> Category:
    new_category = Category(id=len(categories), name=cat)
    categories.append(new_category)
    return new_category
