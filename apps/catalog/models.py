from django.db import models


class Product(models.Model):
    """Products"""
    name = models.CharField("Name", max_length=50)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name


class Filial(models.Model):
    """Filials"""
    name = models.CharField("Name", max_length=50)
    region = models.IntegerField("Region")

    class Meta:
        verbose_name = 'Filial'
        verbose_name_plural = 'Filials'

    def __str__(self):
        return self.name


class Characteristics(models.Model):
    """Characteristics"""
    self = models.AutoField("self", primary_key=True)
    name = models.CharField("Name", max_length=50)
    product = models.ManyToManyField(Product)

    class Meta:
        verbose_name = 'Characteristic'
        verbose_name_plural = 'Characteristics'

    def __str__(self):
        return self.name


class FilialPrice(models.Model):
    """FilialPrices"""
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    filial = models.ForeignKey(Filial, on_delete=models.CASCADE)
    price = models.DecimalField("Price", max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'FilialPrice'
        verbose_name_plural = 'FilialPrices'

    def __str__(self):
        return f"{self.filial}/{self.product}: {self.price}"
