from django.test import TestCase, Client

from film.models import Movie


class TestMovieViewSet(TestCase):
    def setUp(self) -> None:

        self.movie1 = Movie.objects.create(title='Janob hec kim', year=2009, imdb=1, genre='Romace')
        self.movie1.actors.create(first_name='Alisher', last_name='Uzoqov',
                                           birthdate='1984-08-25', gender='Male')
        self.movie1.actors.create(first_name='Asal', last_name='Shodiyeva',
                                           birthdate='1992-04-06', gender='Female')

        self.movie2 = Movie.objects.create(title='Tundan-tonggacha', year=2010, imdb=3, genre='Comedy')
        self.movie2.actors.create(first_name='Shaxzoda', last_name='Muxamedova',
                                           birthdate='1991-04-15', gender='Female')

        self.movie3 = Movie.objects.create(title='Snayper', year=2019, imdb=2, genre='Adventure')
        self.movie3.actors.create(first_name='Ulug`bek', last_name='Qodirov',
                                           birthdate='1983-08-03', gender='Male')

        self.client = Client()

    def test_get_all_movies(self):
        response = self.client.get('/movies/')
        data = response.data

        self.assertEquals(response.status_code, 200)
        self.assertEquals(len(data), 3)
        self.assertEquals(data[0]['title'], "Janob hec kim")
        self.assertEquals(data[0]['actors'][0]['first_name'], "Alisher")
        self.assertEquals(data[0]['actors'][1]['first_name'], "Asal")

    def test_search(self):
        response = self.client.get('/movies/?search=Janob')
        data = response.data

        self.assertEquals(response.status_code, 200)
        self.assertEquals(data[0]['title'], "Janob hec kim")

    def test_ordering(self):
        response = self.client.get('/movies/?ordering=-imdb')
        data = response.data

        self.assertEquals(response.status_code, 200)
        self.assertEquals(len(data), 3)
        self.assertEquals(data[0]['title'], "Tundan-tonggacha")
        self.assertTrue(data[0]['imdb'] == 3)
        self.assertFalse(data[0]['actors'][0]['first_name'] == 'Ulug`bek')
