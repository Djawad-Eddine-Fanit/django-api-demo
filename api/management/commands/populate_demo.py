from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from api.models import Category, BlogPost
from django.utils.text import slugify

User = get_user_model()

class Command(BaseCommand):
    help = "Populate demo categories and blog posts"

    def handle(self, *args, **kwargs):
        # Create a demo user
        user, created = User.objects.get_or_create(username="demo_user")
        if created:
            user.set_password("password123")
            user.save()
            self.stdout.write(self.style.SUCCESS("Created demo user 'demo_user' with password 'password123'"))
        else:
            self.stdout.write(self.style.WARNING("Demo user already exists"))

        # Create demo categories
        category_names = ["Technology", "Science", "Art"]
        categories = []
        for name in category_names:
            category, created = Category.objects.get_or_create(name=name, defaults={"slug": slugify(name)})
            categories.append(category)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Created category: {name}"))
            else:
                self.stdout.write(self.style.WARNING(f"Category '{name}' already exists"))

        # Create demo blog posts
        demo_posts = [
            ("Welcome to the Blog", "This is the first demo post.", "Technology"),
            ("Science Update", "Latest discoveries in science.", "Science"),
            ("Art Showcase", "Exploring modern art trends.", "Art"),
        ]

        for title, content, category_name in demo_posts:
            category = next((c for c in categories if c.name == category_name), None)
            if category:
                slug = slugify(title)
                post, created = BlogPost.objects.get_or_create(
                    title=title,
                    defaults={
                        "slug": slug,
                        "content": content,
                        "author": user,
                        "category": category
                    }
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f"Created post: {title}"))
                else:
                    self.stdout.write(self.style.WARNING(f"Post '{title}' already exists"))

        self.stdout.write(self.style.SUCCESS("Demo data population complete!"))
