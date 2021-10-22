
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

        title: 'Detalle de cita ' + cita,
        width: 700,
        html: `<div class="row col-md-12 border-bottom">

        <div class="col-md-6">
            <h2> <strong>Paciente:</strong> </h2>
        </div>
        <div class="col-md-6">
            <h2> Carlos Muños</h2>
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
        <div class="col-md-6 ">
            <label for="estado">Pendiente</label>
            <input type="radio" name="estado" value="pendiente" checked>
            <label for="estado">Realizada</label>
            <input type="radio" name="estado" value="realizada">
        </div>
    
    </div>
    
    
    <div class="row col-md-12">
        <h2 class="text-center"> <strong>Comentarios:</strong> </h2>
    
        <div class="col-md-12">
            <textarea rows="6" cols="50"> sin comentarios </textarea>
        </div>
    
    
    </div>
    
     `

    });
}
