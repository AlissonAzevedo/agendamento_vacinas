import uuid
from django.db import models


# Create your models here.
# Create your models here.
class Paciente(models.Model):
  COMORBIDADE_CHOICE = (
    ("N", "Nenhum"),
    ("DM","Diabetes mellitus"),
    ("PCG","Pneumopatias cronicas graves"),
    ("HAR","Hipertensao Arterial Resistente (HAR)"),
    ("DNC","Doença neurologicas cronicas"),
    ("DRC","Doença renal cronica"),
  )

  nome = models.CharField(max_length=70)
  sobrenome = models.CharField(max_length=50)
  idade = models.IntegerField()
  comorbidade = models.CharField(max_length=3, choices=COMORBIDADE_CHOICE, default="N")
  
  def __str__(self):
    return self.nome + " " + self.sobrenome

  
class Enfermeiro(models.Model):
  nomeEnfermeiro = models.CharField(max_length=70)

  def __str__(self):
    return self.nome

class Estado(models.Model):
  nome = models.CharField(max_length=70)
  
  def __str__(self):
    return self.nome

class Cidade(models.Model):
  nomeCidade = models.CharField(max_length=70)
  estado = models.ManyToManyField(Estado)

  def __str__(self):
    return self.nomeCidade

class Local(models.Model):
  nomeLocal = models.CharField(max_length=90)
  endereco = models.CharField(max_length=70)
  cidade = models.OneToOneField(Cidade,
  on_delete=models.CASCADE,
  primary_key=True,
  default=""
  )

  def __str__(self):
    return self.nomeLocal


class Vacina(models.Model):
  nome = models.CharField(max_length=70)

  def __str__(self):
    return self.nome


class Vacinacao(models.Model):
  
  paciente = models.OneToOneField(Paciente, on_delete=models.CASCADE)
 # comorbidade = 
  vacina = models.ForeignKey(Vacina, on_delete=models.CASCADE, default=uuid.uuid4)
  local = models.ForeignKey(Local, on_delete=models.CASCADE)
  
  def __str__(self):
    if self.paciente is None:
      return
    return 'Paciente: {} '.format(self.paciente)
  