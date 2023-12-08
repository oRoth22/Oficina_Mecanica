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
    telefone = models.CharField(max_length=20)

    class Meta:
        db_table = 'mecanico'

    def __str__(self):
        return self.nome

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

    class Meta:
        db_table = 'veiculo'

class Equipe(models.Model):
    nome = models.CharField(max_length=45)
    descricao = models.CharField(max_length=50)
    especialidade = models.CharField(max_length=45)
    mecanicos = models.ManyToManyField(Mecanico)

    class Meta:
        db_table = 'equipe'

    def __str__(self):
        return self.nome

    @classmethod
    def create_default_equipe(cls, equipe_id=None):
        if equipe_id:
            equipe_padrao, _ = cls.objects.get_or_create(id=equipe_id)
        else:
            equipe_padrao, _ = cls.objects.get_or_create(
                nome='Equipe Padrão',
                descricao='Descrição da Equipe Padrão',
                especialidade='Especialidade Padrão'
            )
        return equipe_padrao

class OrdemServico(models.Model):
    dataEmissao = models.DateTimeField()
    dataConclusao = models.DateTimeField(null=True)
    valor = models.FloatField()
    descricao = models.TextField()
    status = models.CharField(max_length=20, choices=[('pendente', 'Pendente'), ('concluido', 'Concluído')])
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    equipe = models.ForeignKey(Equipe, on_delete=models.CASCADE, default=Equipe.create_default_equipe, related_name='ordens_servico')

    class Meta:
        db_table = 'ordem_servico'

class PecasOrdemServico(models.Model):
    pecas = models.ForeignKey(Pecas, on_delete=models.CASCADE)
    ordem_servico = models.ForeignKey(OrdemServico, on_delete=models.CASCADE)
    quantidade = models.IntegerField(default=1)

    class Meta:
        db_table = 'pecas_ordem_servico'

    @classmethod
    def get_default_peca_id(cls):
        default_peca = Pecas.objects.get(nome='Peca Padrão')
        return default_peca.id