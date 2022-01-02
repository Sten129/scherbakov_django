import pytest

from backend.models import Type, Genre, Technic, Document, Article, Letter, Location, Persone, Picture, Owner, Exhibition

class TestGenreAPI:
    @pytest.mark.django_db(transaction=True)
    def test_genre_not_found(self, client):
        response = client.get()
        assert response.status_code != 404, ('')
        pass

    @pytest.mark.django_db(transaction=True)
    def test_genre_get(self, client):
        response = client.get()
        assert response.status_code == 200, ('')
        pass

class TestTypeAPI:
    @pytest.mark.django_db(transaction=True)
    def test_type_not_found(self, client):
        response = client.get()
        assert response.status_code != 404, ('')
        pass

    @pytest.mark.django_db(transaction=True)
    def test_type_get(self, client):
        response = client.get()
        assert response.status_code == 200, ('')
        pass

class TestTechnicAPI:
    @pytest.mark.django_db(transaction=True)
    def test_technic_not_found(self, client):
        response = client.get()
        assert response.status_code != 404, ('')
        pass

    @pytest.mark.django_db(transaction=True)
    def test_technic_get(self, client):
        response = client.get()
        assert response.status_code == 200, ('')
        pass

class TestLocationAPI:
    @pytest.mark.django_db(transaction=True)
    def test_location_not_found(self, client):
        response = client.get()
        assert response.status_code != 404, ('')
        pass

    @pytest.mark.django_db(transaction=True)
    def test_location_get(self, client):
        response = client.get()
        assert response.status_code == 200, ('')
        pass

class TestBookAPI:
    @pytest.mark.django_db(transaction=True)
    def test_book_not_found(self, client):
        response = client.get()
        assert response.status_code != 404, ('')
        pass

    @pytest.mark.django_db(transaction=True)
    def test_book_get(self, client):
        response = client.get()
        assert response.status_code == 200, ('')
        pass

class TestPersoneAPI:
    @pytest.mark.django_db(transaction=True)
    def test_persone_not_found(self, client):
        response = client.get()
        assert response.status_code != 404, ('')
        pass

    @pytest.mark.django_db(transaction=True)
    def test_persone_get(self, client):
        response = client.get()
        assert response.status_code == 200, ('')
        pass

class TestOwnerAPI:
    @pytest.mark.django_db(transaction=True)
    def test_owner_not_found(self, client):
        response = client.get()
        assert response.status_code != 404, ('')
        pass

    @pytest.mark.django_db(transaction=True)
    def test_owner_get(self, client):
        response = client.get()
        assert response.status_code == 200, ('')
        pass

class TestLetterAPI:
    @pytest.mark.django_db(transaction=True)
    def test_letter_not_found(self, client):
        response = client.get()
        assert response.status_code != 404, ('')
        pass

    @pytest.mark.django_db(transaction=True)
    def test_letter_get(self, client):
        response = client.get()
        assert response.status_code == 200, ('')
        pass

class TestDocumentAPI:
    @pytest.mark.django_db(transaction=True)
    def test_document_not_found(self, client):
        response = client.get()
        assert response.status_code != 404, ('')
        pass

    @pytest.mark.django_db(transaction=True)
    def test_document_get(self, client):
        response = client.get()
        assert response.status_code == 200, ('')

        pass

class TestExhibitionAPI:
    @pytest.mark.django_db(transaction=True)
    def test_exhibition_not_found(self, client):
        response = client.get()
        assert response.status_code != 404, ('')
        pass

    @pytest.mark.django_db(transaction=True)
    def test_exhibition_get(self, client):
        response = client.get()
        assert response.status_code == 200, ('')
        pass

class TestPictureAPI:
    @pytest.mark.django_db(transaction=True)
    def test_picture_not_found(self, client):
        response = client.get()
        assert response.status_code != 404, ('')
        pass

    @pytest.mark.django_db(transaction=True)
    def test_picture_get(self, client):
        response = client.get()
        assert response.status_code == 200, ('')
        pass

class TestArticleAPI:
    @pytest.mark.django_db(transaction=True)
    def test_article_not_found(self, client):
        response = client.get()
        assert response.status_code != 404, ('')
        pass

    @pytest.mark.django_db(transaction=True)
    def test_article_get(self, client):
        response = client.get()
        assert response.status_code == 200, ('')
        pass