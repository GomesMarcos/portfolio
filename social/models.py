from django.core.validators import MinLengthValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

STATE_CHOICES = [
    ('AC', 'Acre'),
    ('AL', 'Alagoas'),
    ('AP', 'Amapá'),
    ('AM', 'Amazonas'),
    ('BA', 'Bahia'),
    ('CE', 'Ceará'),
    ('DF', 'Distrito Federal'),
    ('ES', 'Espírito Santo'),
    ('GO', 'Goiás'),
    ('MA', 'Maranhão'),
    ('MT', 'Mato Grosso'),
    ('MS', 'Mato Grosso do Sul'),
    ('MG', 'Minas Gerais'),
    ('PA', 'Pará'),
    ('PB', 'Paraíba'),
    ('PR', 'Paraná'),
    ('PE', 'Pernambuco'),
    ('PI', 'Piauí'),
    ('RJ', 'Rio de Janeiro'),
    ('RN', 'Rio Grande do Norte'),
    ('RS', 'Rio Grande do Sul'),
    ('RO', 'Rondônia'),
    ('RR', 'Roraima'),
    ('SC', 'Santa Catarina'),
    ('SP', 'São Paulo'),
    ('SE', 'Sergipe'),
    ('TO', 'Tocantins'),
]


class Address(models.Model):
    street = models.CharField(max_length=100)
    number = models.CharField(blank=True, null=True, max_length=12)
    complement = models.CharField(max_length=100, blank=True, null=True)
    neighborhood = models.CharField(max_length=50)
    city = models.CharField(max_length=50, default='Salvador')
    state = models.CharField(max_length=2, choices=STATE_CHOICES, default='BA')
    country = models.CharField(max_length=3, default='BRA')
    zipcode = models.CharField(max_length=8, verbose_name='ZIP Code')

    def __str__(self):
        number = f'Nº {self.number}' if self.number is not None else ''
        complement = self.complement or ''
        return f'{self.zipcode} - {self.street}, {number}, {complement}, {self.neighborhood}, {self.city} - {self.state}/{self.country}'


class PhoneNumber(models.Model):
    prefix = models.CharField(max_length=2, default='71')
    number = models.CharField(validators=[MinLengthValidator(8)], max_length=12)

    def __str__(self):
        return f'({self.prefix}) {self.number}'


class SocialMedia(models.Model):
    name = models.CharField(max_length=50)
    url = models.URLField(max_length=300)

    @property
    def logo(self):
        # TODO: configurar o ícone via font awesome pelo name
        ...

    def __str__(self):
        return self.name


class Social(models.Model):
    name = models.CharField(max_length=50, default='GomeSystems')
    author = models.CharField(max_length=50, default='Marcos Gomes')
    about_us = models.TextField()
    address = models.ForeignKey(Address, verbose_name='address', on_delete=models.CASCADE)
    phone_number = models.ForeignKey(PhoneNumber, on_delete=models.CASCADE, blank=True, null=True)
    email = models.EmailField(max_length=254)
    social_media = models.ManyToManyField(SocialMedia, verbose_name=_('Social Media'))
    founded_in = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name
