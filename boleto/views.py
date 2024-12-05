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
        return render(request,'boleto/valida.html',{
            'fecha':fec, 'origen':ori, 'destino':dest, 'hsal':hs, 'hlle':hl,
            'fechas':fs, 'usuario':nom, 'tren':tren, 'sit':sit, 'fol':fol,
            'bn':nb
        })
    
    return render(request, 'boleto/captura.html',{
        'msj':ventana,
        'nfecha':fecha,
        'boleto_no':boletos,
        'num_fol':folio
    })

def imprimir_documento(request):
    titulo = 'Sistema Tickets IH'
    fe = request.POST.get('fecha')
    origen = request.POST.get('origen')
    destino = request.POST.get('destino')
    salida = request.POST.get('hsalida')
    llegada = request.POST.get('hllegada')
    fs = request.POST.get('fsalida')
    cliente = request.POST.get('nombre')
    tren = request.POST.get('tren')
    asiento = request.POST.get('asiento')
    boleto = request.POST.get('num_boleto')
    folio = request.POST.get('folio')

    archivo = get_template('plantillas/pdf.html')
    
    html = archivo.render({'titulo':titulo,'fecha':fe, 'or':origen, 'des':destino,
                        'salida':salida, 'llegada':llegada, 'fechas':fs, 
                        'nombre':cliente, 'tren':tren,'sit':asiento,'boleto':boleto,
                        'fol':folio})
    
    pdf = HTML(string=html).write_pdf()
    res = HttpResponse(pdf,  content_type='application/pdf')
    res['Content-Disposition']='inline; filename="ticket_rw.pdf"'
    return res
    


def listado_salidas(request):
    salidas = boleto.objects.all()
    ven = "Últimos Boletos"
    return render(request, 'boleto/listado_datos.html',{
        'boletos':salidas,
        'ven':ven
    })

def borrado_boletos(request, id):
    borra = boleto.objects.get(id=id)
    borra.delete()
    return redirect('salidas')

def actualizacion_boleto(request, id):
    titulo = 'Actualizar Datos'
    datos = boleto.objects.get(id=id)
    numb = datos.num_boleto
    fecha = datos.fecha
    fechas = datos.fecha_salida
    fechal = datos.fecha_llegada
    usuario = datos.nombre
    tel = datos.telefono
    ori = datos.origen
    des = datos.destino
    horas =datos.hsalida
    horal =datos.hllegada
    horal =datos.hllegada
    tren = datos.tren
    vagon= datos.vagon
    asiento = datos.asiento
    fol = datos.folio
    es = datos.estatus
    nota = datos.nota
    ob = datos.observaciones
    pre = datos.precio
    personas = datos.num_personas
    identifica = datos.id
    return render (request, 'boleto/actualiza_salida.html',{
        'ventana':titulo, 'num_boleto':numb,'fecha':fecha, 'nombre':usuario, 'telefono':tel,
        'origen':ori, 'destino':des, 'fecha_salida':fechas, 'fecha_llegada':fechal, 'hsalida':horal,
        'asiento':asiento, 'estatus':es, 'folio':fol, 'nota':nota, 'observaciones':ob, 'precio':pre,
        'tren':tren, 'vagon':vagon, 'num_personas':personas, 'hllegada':horal, 'id':identifica

    })

def cambia_boleto(request, id):
    cambia = boleto.objects.get(id=id)
    
    #recupéramos los datos del formulario

    fe = request.POST.get('fecha')
    personas = request.POST.get('num_personas')
    origen = request.POST.get('origen')
    des = request.POST.get('destino')
    hs = request.POST.get('hsalida')
    hl = request.POST.get('hllegada')
    fs = request.POST.get('fecha_salida')
    fl = request.POST.get('fecha_llegada')
    user = request.POST.get('nombre')
    tel = request.POST.get('telefono')
    tre = request.POST.get('tren')
    vag = request.POST.get('vagon')
    asiento = request.POST.get('asiento')
    es = request.POST.get('estatus')
    pre = request.POST.get('precio')
    ob = request.POST.get('observaciones')
    bn = request.POST.get('num_boleto')
    nota = request.POST.get('nota')
    fol = request.POST.get('folio')
    actualiza = boleto.objects.get(id=id)
     # reasignamos  a las variables del formulario
    actualiza.fecha = fe
    actualiza.nombre = user
    actualiza.telefono =tel
    actualiza.num_boleto = bn
    actualiza.origen = origen
    actualiza.destino = des
    actualiza.fecha_salida = fs
    actualiza.fecha_llegada = fl
    actualiza.hsalida = hs
    actualiza.hllegada = hl
    actualiza.asiento = asiento
    actualiza.estatus = es
    actualiza.folio = fol
    actualiza.nota = nota
    actualiza.observaciones = ob
    actualiza.precio = pre
    actualiza.tren = tre
    actualiza.vagon = vag
    actualiza.num_personas = personas
    actualiza.save()
    return redirect('salidas')


def pdf_file(request):
    titulo = "Archivo PDF Linux"
    file = get_template('plantillas/pdf.html')
    html = file.render({'titulo':titulo})
    pdf = HTML(string=html).write_pdf()
    res = HttpResponse(pdf, content_type='application/pdf')
    res['Content-Disposition']='inline; filename="ticket_rw.pdf"'
    return res

def new_impresion(request, id):
    f = date.today()
    ffecha='{}-{}-{}'.format(f.year,f.month,f.day)
    
    fecha = ffecha
    datos = boleto.objects.get(id=id)
    numb = datos.num_boleto
    fecha = datos.fecha
    fechas = datos.fecha_salida
    fechal = datos.fecha_llegada
    usuario = datos.nombre
    tel = datos.telefono
    ori = datos.origen
    des = datos.destino
    horas =datos.hsalida
    horal =datos.hllegada
    horal =datos.hllegada
    tren = datos.tren
    vagon= datos.vagon
    asiento = datos.asiento
    fol = datos.folio
    es = datos.estatus
    nota = datos.nota
    ob = datos.observaciones
    pre = datos.precio
    personas = datos.num_personas
    identifica = datos.id
    return render (request, 'boleto/nueva_impresion.html',{
        'num_boleto':numb,'fecha':fecha, 'nombre':usuario, 'telefono':tel,
        'origen':ori, 'destino':des, 'fecha_salida':fechas, 'fecha_llegada':fechal, 'hsalida':horal,
        'asiento':asiento, 'estatus':es, 'folio':fol, 'nota':nota, 'observaciones':ob, 'precio':pre,
        'tren':tren, 'vagon':vagon, 'num_personas':personas, 'hllegada':horal, 'id':identifica

    })