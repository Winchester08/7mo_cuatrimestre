from django.shortcuts import render, HttpResponse, redirect
from . models import boleto
from . forms import Captura_Form
from datetime import date
from weasyprint import HTML
from django.template.loader import get_template



def captura(request):
    ventana = "Ventana de Captura de Tickets"
    f = date.today()
    ffecha='{}-{}-{}'.format(f.year,f.month,f.day)
    fecha = ffecha
    campos = boleto.objects.latest("num_boleto", "folio")
    boletos = campos.num_boleto
    folio = campos.folio
    
    if request.method == 'POST':
        fec = request.POST.get('fecha')
        np = request.POST.get('num_personas')
        ori = request.POST.get('origen')
        dest = request.POST.get('destino')
        hs = request.POST.get('hsalida')
        hl = request.POST.get('hllegada')
        fs = request.POST.get('fsalida')
        fl = request.POST.get('fllegada')
        nom = request.POST.get('nombre')
        tel = request.POST.get('telefono')
        sit = request.POST.get('asiento')
        es = request.POST.get('estatus')
        p = request.POST.get('precio')
        ob = request.POST.get('observaciones')
        nota = request.POST.get('nota')
        tren = request.POST.get('tren')
        vag = request.POST.get('vagon')
        nb = request.POST.get('num_boleto')
        fol = request.POST.get('folio')

        guarda = boleto(fecha=fec,nombre=nom, telefono=tel, num_boleto=nb, origen=ori, 
                        destino=dest,fecha_salida=fs,fecha_llegada=fl, hsalida=hs, 
                        hllegada=hl, asiento=sit, estatus=es, folio=fol, nota=nota,
                        observaciones=ob, precio=p, tren=tren, vagon=vag, num_personas=np)
        guarda.save()
        return redirect('listado_boletos')
    
    return render(request, 'boleto/captura.html',{
        'msj':ventana,
        'nfecha':fecha,
        'boleto_no':boletos,
        'num_fol':folio
    })

def listado_salidas(request):
    salidas = boleto.objects.all()
    ven = "Ultimos Boletos"
    return render(request, 'boleto/listado_datos.html',{
        'boletos':salidas,
        'ven':ven
    })

def borrado_boletos(request, id):
    borra = boleto.objects.get(id=id)
    borra.delete()
    return redirect('salidas')


def pdf_file(request):
    titulo = "Archivo PDF Linux"
    file = get_template('plantillas/pdf.html')
    html = file.render({'titulo':titulo})
    pdf = HTML(string=html).write_pdf()
    res = HttpResponse(pdf, content_type='application/pdf')
    res['Content-Disposition']='inline; filename="ticket_rw.pdf"'
    return res

