from django.shortcuts import render, get_object_or_404
from .models import DatosPersonales

def detalle_cv(request, idperfil):
    perfil = get_object_or_404(DatosPersonales, idperfil=idperfil)

    context = {
        'perfil': perfil,
        'experiencias': perfil.experiencias.filter(activarparaqueseveaenfront=True),
        'cursos': perfil.cursos.filter(activarparaqueseveaenfront=True),
        'reconocimientos': perfil.reconocimientos.filter(activarparaqueseveaenfront=True),
        'productosacademicos': perfil.productos_academicos.filter(activarparaqueseveaenfront=True),
        'productoslaborales': perfil.productos_laborales.filter(activarparaqueseveaenfront=True),
        'ventagarage': perfil.ventas_garage.filter(activarparaqueseveaenfront=True),
    }

    return render(request, 'cv/detalle_cv.html', context)


from django.shortcuts import render

def bienvenida(request):
    return render(request, 'cv/bienvenida.html')
def lista_cv(request):
    perfiles = DatosPersonales.objects.filter(perfilactivo=1)
    return render(request, 'cv/lista_cv.html', {
        'perfiles': perfiles
    })



from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from .models import DatosPersonales


def cv_pdf(request, id):
    perfil = DatosPersonales.objects.get(pk=id)
    template = get_template('cv/cv_pdf.html')
    html = template.render({'perfil': perfil})

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="CV_{perfil.nombres}.pdf"'

    pisa_status = pisa.CreatePDF(
        html, dest=response
    )

    if pisa_status.err:
        return HttpResponse('Error al generar el PDF')

    return response
