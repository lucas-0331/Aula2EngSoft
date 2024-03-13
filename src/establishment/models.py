from django.db import models


class Establishment(models.Model):
    establishment_id = models.AutoField(
        primary_key=True,
        unique=True,
        editable=False,
    )
    establishment_name = models.CharField(
        max_length=45,
        verbose_name="Nome Fantasia",
        help_text="Nome que aparecerá na interface do usuário.",
    )
    establishment_legal_name = models.CharField(
        max_length=45,
        verbose_name="Razão Social",
        help_text="Nome registrado oficialmente nos documentos legais e registros comerciais.",
    )
    establishment_cnpj = models.CharField(
        max_length=14,
        verbose_name="CNPJ",
        unique=True,
    )
    establishment_address = models.CharField(
        max_length=45,
        verbose_name="Endereço",
    )
    establishment_description = models.CharField(
        max_length=255,
        verbose_name="Descrição",
        help_text="Uma breve descrição do comércio.",
    )
    establishment_email = models.EmailField(
        verbose_name="E-mail",
    )
    establishment_ddd_phone = models.CharField(
        max_length=3,
        verbose_name="DDD",
    )
    establishment_phone = models.CharField(
        max_length=9,
        verbose_name="Telefone",
    )

    class Meta:
        verbose_name = "Estabelecimento"
        verbose_name_plural = "Estabelecimentos"

    def __str__(self):
        return f"{self.establishment_name}"