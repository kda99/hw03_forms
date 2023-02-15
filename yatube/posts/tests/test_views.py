from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse

from ..models import Group, Post

User = get_user_model()

class TaskPagesTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.author = User.objects.create_user(username='author')
        cls.group = Group.objects.create(
            title='Тестовая группа',
            slug='test-slug',
            description='Тестовое описание',
        )
        cls.post = Post.objects.create(
            text='Тестовый пост',
            author=cls.author,
            group=cls.group,
            id=1,
        )

    def setUp(self):
        self.authorized_client_author = Client()
        self.authorized_client_author.force_login(self.author)

    def test_pages_uses_correct_template(self):
        """URL-адрес использует соответствующий шаблон."""
        # Собираем в словарь пары "имя_html_шаблона: reverse(name)"
        templates_pages_names = {
            reverse('posts:index'): 'posts/index.html',
            reverse('posts:group_list', kwargs={'slug': 'test-slug'}): 'posts/group_list.html',
            reverse('posts:profile', kwargs={'username': 'author'}): 'posts/profile.html',
            reverse('posts:post_detail', kwargs={'post_id': '1'}): 'posts/post_detail.html',
            reverse('posts:post_edit', kwargs={'post_id': '1'}): 'posts/create_post.html',
            reverse('posts:post_create'): 'posts/create_post.html',
        }
        # Проверяем, что при обращении к name вызывается соответствующий HTML-шаблон
        for reverse_name, template in templates_pages_names.items():
            with self.subTest(reverse_name=reverse_name):
                response = self.authorized_client_author.get(reverse_name)
                self.assertTemplateUsed(response, template)

