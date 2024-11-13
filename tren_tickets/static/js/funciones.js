$(document).ready(function(){
    let nboleto = $('.boleto_num').val();
    let folio = $('.folio').val();
    let sig = 1
    let bolnew= parseInt(nboleto) + parseInt(sig);
    $('#num_boleto').val(bolnew);
    let nfol = parseInt(folio) + parseInt(sig);
    $('#folio').val(nfol);
});