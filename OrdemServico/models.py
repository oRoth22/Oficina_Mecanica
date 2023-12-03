from django.db import models

class Admin(models.Model):
    email = models.CharField(max_length=50, unique=True)
    senha = models.CharField(max_length=255)
    cpf = models.CharField(max_length=50)
    codigoAdmin = models.CharField(max_length=255)
    class Meta:
        db_table = 'admin'

class Cliente(models.Model):
    nome = models.CharField(max_length=45)
    email = models.CharField(max_length=50)
    telefone = models.IntegerField()
    cpf = models.CharField(max_length=45)
    endereco = models.CharField(max_length=100)
    class Meta:
        db_table = 'cliente'

class Mecanico(models.Model):
    nome = models.CharField(max_length=45)
    cpf = models.CharField(max_length=45)
    especialidade = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    telefone = models.IntegerField()
    class Meta:
        db_table = 'mecanico'

class Pecas(models.Model):
    nome = models.CharField(max_length=45)
    marca = models.CharField(max_length=50)
    preco = models.FloatField()
    quantidade = models.IntegerField()
    class Meta:
        db_table = 'pecas'

class Veiculo(models.Model):
    nome = models.CharField(max_length=45)
    marca = models.CharField(max_length=45)
    cor = models.CharField(max_length=45)
    placa = models.CharField(max_length=45)
    modelo = models.CharField(max_length=45)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    class Meta:
        db_table = 'veiculo'

class OrdemServico(models.Model):
    dataEmissao = models.DateTimeField()
    dataConclusao = models.DateTimeField()
    valor = models.FloatField()
    descricao = models.TextField()
    status = models.CharField(max_length=20, choices=[('pendente', 'Pendente'), ('concluido', 'Concluído')])
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    class Meta:
        db_table = 'ordem_servico'


class Equipe(models.Model):
    nome = models.CharField(max_length=45)
    descricao = models.CharField(max_length=50)
    especialidade = models.CharField(max_length=45)
    mecanico = models.ForeignKey(Mecanico, on_delete=models.CASCADE)
    ordem_servico = models.ForeignKey(OrdemServico, on_delete=models.CASCADE)
    class Meta:
        db_table = 'equipe'

class PecasOrdemServico(models.Model):
    pecas = models.ForeignKey(Pecas, on_delete=models.CASCADE)
    ordem_servico = models.ForeignKey(OrdemServico, on_delete=models.CASCADE)
    class Meta:
        db_table = 'pecas_ordem_servico'
