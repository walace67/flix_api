from django.db import models


NATIONALITY_CHOISES = (
    ('USA', 'Estados Unidos'),
    ('BRAZIL', 'Brasil'),
)


class Actor(models.Model):
    name = models.CharField(max_length=200)
    birthday = models.DateField(null=True, blank=True)
    nationality = models.CharField(
        max_length=100,
        choices=NATIONALITY_CHOISES,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name
