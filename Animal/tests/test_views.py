from django.urls import reverse
from django.test import TestCase, Client
from Animal.models import animal


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.obj = animal.objects.create(id=1,
                                         name='Rex',
                                         submitter='Afik',
                                         species='dog',
                                         breed='Boxer',
                                         description='very good dog',
                                         sex='M',
                                         Adoption='No',
                                         image='default.png')

    def test_all_animals_GET(self):
        response = self.client.get(reverse('Animal:all_animals'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'adopter/Base.html')
        self.assertTemplateUsed(response, 'Animal/all_animals.html')

    def test_Animal_detail_GET(self):
        response = self.client.get(reverse('Animal:animal_detail', args=[self.obj.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'adopter/Base.html')
        self.assertTemplateUsed(response, 'Animal/animal_detail.html')

    def test_add_Animal_GET(self):
        response = self.client.get(reverse('Animal:add_Animal'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'adopter/Base.html')
        self.assertTemplateUsed(response, 'Animal/add_Animal.html')

    def test_add_Animal_POST_Valid(self):
        animal_count = animal.objects.count()
        response = self.client.post(reverse('Animal:add_Animal'))
        animal.objects.create(id=2,
                              name='Rex',
                              submitter='Afik',
                              species='dog',
                              breed='Boxer',
                              description='very good dog',
                              sex='M',
                              Adoption='No',
                              image='default.png')

        self.assertEqual(response.status_code, 302)  # means redirection works
        self.assertEqual(animal.objects.count(), animal_count + 1)  # object created so expected true

    def test_add_Animal_POST_Not_Valid(self):
        response = self.client.post(reverse('Animal:add_Animal'),
                                    {'name': '',
                                     'submitter': '',
                                     'species': '',
                                     'breed': '',
                                     'description': '',
                                     'sex': '',
                                     'Adoption': '',
                                     'image': ''})
        self.assertEqual(response.status_code, 302)  # means redirection works in case of a bad form

    def test_edit_Animal_GET(self):
        response = self.client.get(reverse('Animal:editAnimal', args=[self.obj.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'adopter/Base.html')
        self.assertTemplateUsed(response, 'Animal/add_Animal.html')

    def test_edit_Animal_POST(self):
        animal_count = animal.objects.count()
        response = self.client.post(reverse('Animal:editAnimal', args=[self.obj.pk]), {'name': 'Rex',
                                                                                       'submitter': 'Afik',
                                                                                       'species': 'dog',
                                                                                       'breed': 'Boxer',
                                                                                       'description': 'very good dog',
                                                                                       'sex': 'M',
                                                                                       'Adoption': 'No',
                                                                                       'image': 'default.png'})

        self.assertEqual(response.status_code, 200)  # means redirection works
        self.assertEqual(animal.objects.count(), animal_count)  # all fields are in place updated

    def test_delete_Animal_GET(self):
        response = self.client.get(reverse('Animal:deleteAnimal', args=[self.obj.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'adopter/Base.html')
        self.assertTemplateUsed(response, 'Animal/DeleteAnimal.html')

    def test_delete_Animal_POST(self):
        animal_count = animal.objects.count()
        response = self.client.get(reverse('Animal:deleteAnimal', args=[self.obj.pk]))
        testAnimal = self.obj
        pk = testAnimal.pk
        get_testAnimal = animal.objects.get(id=testAnimal.pk)
        get_testAnimal.delete()
        self.assertFalse(animal.objects.filter(pk=pk).exists())
        self.assertEqual(response.status_code, 200)  # means redirection works
        self.assertEqual(animal.objects.count(), animal_count - 1)  # -1 the number that been before
