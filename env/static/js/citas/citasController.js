


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

