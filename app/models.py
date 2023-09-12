from django.db import models

# Create your models here.
class Cidade(models.Model):
    nome = models.CharField(max_length = 35)
    uf = models.CharField(max_length = 2)

    def __str__(self):
        return f'{self.nome} {self.uf}'

class Autor(models.Model):
    nome = models.CharField(max_length = 50)
    site = models.CharField(max_length = 100)
    cidade = models.ForeignKey(Cidade,
                               on_delete = models.CASCADE)

    def __str__(self):
        return f'{self.nome} {self.site} {self.cidade}'
    
class Editora(models.Model):
    nome = models.CharField(max_length = 50)
    site = models.CharField(max_length = 100)
    cidade = models.ForeignKey(Cidade,
                              on_delete = models.CASCADE)

    def __str__(self):
        return f'{self.nome} {self.site} {self.cidade}'
    
class Categoria(models.Model):
    nome = models.CharField(max_length = 50)

    def __str__(self):
        return self.nome
    
class Livro(models.Model):
    nome = models.CharField(max_length = 50)
    autor = models.ForeignKey(Autor,
                             on_delete = models.CASCADE)
    editora = models.ForeignKey(Editora,
                               on_delete = models.CASCADE)
    categoria = models.ForeignKey(Categoria,
                                  on_delete = models.CASCADE)
    preco = models.DecimalField(max_digits = 6, decimal_places = 2)
    dataPublicacao = models.DateTimeField()

    def __str__(self):
        return f'{self.categoria} {self.autor} {self.nome}'
    
class Leitor(models.Model):
    nome = models.CharField(max_length = 50)
    email = models.CharField(max_length = 100)
    cpf = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.nome} {self.email} {self.cpf}'
    
class Emprestimo(models.Model):
    dataEmprestimo = models.DateTimeField()
    livro = models.ForeignKey(Livro,
                              on_delete = models.CASCADE)
    leitor = models.ForeignKey(Leitor,
                               on_delete = models.CASCADE)
    dataDevolucao = models.DateTimeField()

    def __str__(self):
        return f'{self.livro} {self.leitor} {self.dataDevolucao}'