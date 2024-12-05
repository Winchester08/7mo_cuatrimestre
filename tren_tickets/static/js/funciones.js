$(document).ready(function(){
    $(".error-form").hide();
    let nboleto = $('.boleto_num').val();
    let folio = $('.folio').val();
    let sig = 1
    let bolnew= parseInt(nboleto) + parseInt(sig);
    $('#num_boleto').val(bolnew);
    let nfol = parseInt(folio) + parseInt(sig);
    $('#folio').val(nfol);

    $(".genera_boleto").click(function(){
        if ($(".num_personas").val()=="" || $(".origen").val()=="" || $(".destino").val()=="" || 
        $(".hsalida").val()=="" || $(".hllegada").val()=="" || $(".fsalida").val()=="" || $(".fllegada").val()==""
        || $(".nombre").val()=="" || $(".telefono").val()=="" || $(".tren").val()=="0" || $(".vagon").val()=="0"
        || $(".asiento").val()=="0" || $(".estatus").val()=="" || $(".precio").val()=="" || $(".observaciones").val()==""
        || $(".boleto_num").val()=="" || $(".folio").val()=="" || $(".nota").val()==""){
            $(".error-form").show();
            
            
        }
        else {  
                
            $.blockUI({ message:'<h1> Generando su Ticket </h1>',
                        css: { border:'none',
                               padding: '15px',
                                
                               backgroundColor: '#000',
                               opacity: '.5',
                               color:'#fff'
                       }});    
                       setTimeout($.unblockUI, 2000);
                       $(".form").submit();
              //setTimeout($.unblockUI, 2000);
              
            
        }
    });
});