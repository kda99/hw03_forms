# import shutil
# import tempfile
#
# from ..forms import PostForm
# from ..models import Group, Post
# from django.conf import settings
# from django.core.files.uploadedfile import SimpleUploadedFile
# from django.test import Client, TestCase, override_settings
# from django.urls import reverse
#
# # Создаем временную папку для медиа-файлов;
# # на момент теста медиа папка будет переопределена
# TEMP_MEDIA_ROOT = tempfile.mkdtemp(dir=settings.BASE_DIR)
#
#
# @override_settings(MEDIA_ROOT=TEMP_MEDIA_ROOT)
# class TaskPostFormTest(TestCase):
#     @classmethod
#     def setUpClass(cls):
#         super().setUpClass()
#         # Создаем запись в базе данных для проверки сушествующего slug
#         Post.objects.create(
#             title='Тестовый заголовок',
#             text='Тестовый текст',
#             slug='first'
#         )
#         # Создаем форму, если нужна проверка атрибутов
#         cls.form = TaskCreateForm()
#
#     @classmethod
#     def tearDownClass(cls):
#         super().tearDownClass()
#         # Модуль shutil - библиотека Python с удобными инструментами
#         # для управления файлами и директориями:
#         # создание, удаление, копирование, перемещение, изменение папок и файлов
#         # Метод shutil.rmtree удаляет директорию и всё её содержимое
#         shutil.rmtree(TEMP_MEDIA_ROOT, ignore_errors=True)
#
#     def setUp(self):
#         # Создаем неавторизованный клиент
#         self.guest_client = Client()
#
#
#
