from django.db import models

class Empresa(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    contato = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Funcionario(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    cidade = models.CharField(max_length=200)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    matricula = models.PositiveIntegerField(unique=True)

    def __str__(self):
        return self.nome

    @classmethod
    def proximo_matricula_funcionario(cls, empresa):
        ultimo_matricula = cls.objects.filter(empresa=empresa).aggregate(models.Max('matricula'))['matricula__max']
        return ultimo_matricula + 1 if ultimo_matricula is not None else 1