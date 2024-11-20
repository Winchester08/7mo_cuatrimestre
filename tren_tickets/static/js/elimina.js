$(document).ready(function(){
    $('.eliminar').click(function(){
    $.blockUI({ message:'<h2> Eliminando Registro  </h2>',
                css: { border:'none',
                       padding: '15px',
                        
                       backgroundColor: '#000',
                       opacity: '.5',
                       color:'#fff'
               }});    
      setTimeout($.unblockUI, 3000);
            
    });
});