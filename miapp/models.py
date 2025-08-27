from django.db import models

# Create your models here.
class Cliente(models.Model):
    #si no se especifica ID, Django creará una internamente
    id_cliente= models.CharField(primary_key=True, max_length=5)
    cli_nombre= models.CharField(max_length=40, null= True, blank=True)
    cli_direccion= models.CharField(max_length=60, null= True, blank=True)
    cli_telefono= models.CharField(max_length=24, null= True, blank=True)

    #opcionalmente agregar el nombre de la tabla
    class Meta: 
        db_table = 'CLIENTE'

    def __str__(self):
        return self.cli_nombre or f"Cliente {self.id_cliente} "



#entidad Orden
class Orden(models.Model):
    #primary key
    id_orden= models.AutoField(primary_key=True)

    #foreign key
    id_cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE, to_field='id_cliente')
    ord_fecha = models.DateField(null=True, blank= True)

    class Meta:
        db_table = 'ORDEN'

    def __str__(self):
        return f"Orden {self.id_orden}"
    