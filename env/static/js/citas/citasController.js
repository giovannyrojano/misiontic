
/*
Controlador de Citas

*metodos:
*detalleCita(cita)

*/


var text = document.getElementById("text-cita");
//document.getElementById("");

var table = document.querySelectorAll("#table-citas tr");

text.addEventListener('keyup', function () {
    var value = this.value.toLowerCase();
    console.log(value);
    console.log(table);
    var itemsArray = Array.from(table);
    console.log(itemsArray);
    itemsArray.filter(function () {
        // no funciona
        table.classList.toggle(table.innerHTML.toLowerCase().indexOf(value) > -1);
    });

});



/*
   $("#myInput").on("keyup", function () {
       var value = $(this).val().toLowerCase();
       $("#myTable tr").filter(function () {
           $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
       });
   });*/





detalleCita = function (cita) {

    Swal.fire({

        title: 'detalle cita ' + cita,
        width: 700,
        html: `<div class="row col-md-12 border-bottom">

        <div class="col-md-6">
            <h2> <strong>Paciente:</strong> </h2>
        </div>
        <div class="col-md-6">
            <h2> CArlos Muños</h2>
        </div>
    
    </div>
    <div class="row col-md-12 border-bottom">
    
        <div class="col-md-6">
            <h2> <strong>Medico:</strong> </h2>
        </div>
        <div class="col-md-6">
            <h2>Feliciano Valencia</h2>
        </div>
    
    </div>
    
    <div class="row col-md-12 border-bottom">
    
        <div class="col-md-6">
            <h2> <strong>Fecha:</strong> </h2>
        </div>
        <div class="col-md-6">
            <h2> 13-12-2021 </h2>
        </div>
    
    </div>
    
    <div class="row col-md-12 border-bottom">
    
        <div class="col-md-6">
            <h2> <strong>Hora:</strong> </h2>
        </div>
        <div class="col-md-6">
            <h2> 10:30:00</h2>
        </div>
    
    </div>
    
    <div class="row col-md-12 border-bottom">
    
        <div class="col-md-6">
            <h2> <strong>Estado:</strong> </h2>
        </div>
        <div class="col-md-6">
            <h2 class="text-blue"> Pendiente</h2>
        </div>
    
    </div>
    
    
    <div class="row col-md-12">
        <h2 class="text-center"> <strong>Comentarios:</strong> </h2>
    
        <div class="col-md-12">
    
            <div class="card">
                <div class="card-body"> Ok estare pendiente</div>
                <div class="card-footer"> 10/12/2021 10:45:10</div>
            </div>
        </div>
    
    
    </div>
    
     `

    });
}
