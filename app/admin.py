from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Cidade)
admin.site.register(Editora)
admin.site.register(Leitor)
class LivroInline(admin.TabularInline):
    model = Livro
    extra = 1

class AutorAdmin(admin.ModelAdmin):
    list_display = ('nome',)# Campos que serão exibidos na tabela
    search_fields = ('nome',)# Campos que serão pesquisados
    inlines = [LivroInline]# Adiciona a tabela de livros no admin de gêneros

admin.site.register(Autor, AutorAdmin)
admin.site.register(Livro)
admin.site.register(Genero)
admin.site.register(EmprestimoLivro)