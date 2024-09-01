from django.db import models
#


class EntryManagers(models.Manager):

    def query_entrys(self,titulo, categoria):
        if titulo and categoria:
            datos = self.filter(
                title__icontains=titulo,
                category__name__icontains=categoria,
                active=True
            )
        elif titulo:
            datos = self.filter(
                title__icontains=titulo, 
                active=True
            )
        elif categoria:
            datos = self.filter(
                category__name__icontains=categoria, 
                active=True
            )
        else:
            datos = self.all()
        return datos