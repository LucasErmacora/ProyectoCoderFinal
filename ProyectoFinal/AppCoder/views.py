from django.shortcuts import render

# Create your views here.

def inicio_view(request):
    return render(request,"AppCoder/inicio.html")

def cursos_view(request):
    if request.method == "GET":
     print("+" * 90) #  Imprimimos esto para ver por consola
     print("+" * 90) #  Imprimimos esto para ver por consola
     return render(
         request,
         "AppCoder/curso_formulario_basico.html",
     )
    else:
        print("*" * 90)     #  Imprimimos esto para ver por consola
        print(request.POST) #  Imprimimos esto para ver por consola
        print("*" * 90)     #  Imprimimos esto para ver por consola
        return render(
            request,
            "AppCoder/curso_formulario_basico.html",
        )    







#    return render(
#        request,
#        "AppCoder/cursos.html",
#        {
#            "nombre": "Curso de Python",
#            "camadas": [1000, 1001, 1002, 1003, 1004, 1005]
#        }
#    )