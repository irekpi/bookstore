from django.db import models
from django.utils.translation import gettext as _


class Book(models.Model):
    title = models.CharField(max_length=250, verbose_name=_('Tytuł'), null=True)
    publisher = models.ForeignKey('Publisher', on_delete=models.SET_NULL, verbose_name=_('Wydawca'), null=True)
    pages_num = models.PositiveBigIntegerField(null=True, verbose_name=_('Liczba stron'), blank=True)
    cover_image = models.ImageField(upload_to='imgs/', default='imgs/none.jpg', verbose_name=_('Okładka'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Data utworzenia'))
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Data modyfikacji'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Książka')
        verbose_name_plural = _('Książki')


class Publisher(models.Model):
    name = models.CharField(max_length=250, verbose_name=_('Nazwa'), null=True)

    class Meta:
        verbose_name = _('Wydawca')
        verbose_name_plural = _('Wydawcy')

    def __str__(self):
        return self.name


class BookAuthor(models.Model):
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, related_name='authors', verbose_name=_('Ksiązki'),
                             null=True)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, related_name='books', verbose_name=_('Autorzy'),
                               null=True)

    class Meta:
        verbose_name = _('Autor')
        verbose_name_plural = _('Autorzy')

    def __str__(self):
        return self.author.firstname + self.author.lastname


class Author(models.Model):
    firstname = models.CharField(max_length=250, verbose_name=_('Imię'), null=True)
    lastname = models.CharField(max_length=250, verbose_name=_('Nazwisko'), null=True)
    nickname = models.CharField(max_length=250, verbose_name=_('Pseudonim'), null=True)
    birthdate = models.DateField(verbose_name=_('Data urodzenia'), null=True)

    class Meta:
        verbose_name = _('Pisarz')
        verbose_name_plural = _('Pisarze')

    def __str__(self):
        return self.firstname + self.lastname
