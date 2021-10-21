

function getTipoDocumentos() {
    var objXMLHTTP = new XMLHttpRequest();

    objXMLHTTP.open('GET', API_URL + 'TipoDocumento/');

    objXMLHTTP.addEventListener('load', completado);
    objXMLHTTP.addEventListener('error', manejarError);
    objXMLHTTP.addEventListener('progress', progreso);
    objXMLHTTP.addEventListener('abort', abortado);

    objXMLHTTP.send();

    function manejarError(evt) {
        console.log('ocurrio un error.');
    }

    function progreso(evt) {
        var procentaje = evt.loaded / evt.total * 100;
        console.log(procentaje);
    }


    function abortado(evt) {
        console.log('cancelado');
    }

    async function completado(evt) {
        var data = JSON.parse(this.response);
        html = "";
        data.forEach(element => {
            html += `<label for="rCedula">${element.abreviatura}</label>
            <input id="${element.nombre}" type="radio" value="${element.id}" name="documento_id"> `
        });

        document.getElementById('list-tipo-documento').innerHTML = html;
    }
}

this.getTipoDocumentos();



function registrarUsuario(event) {
    event.preventDefault();
    console.log("OK");
    form = document.querySelector('#registro');
    // data = new FormData(form.target);
    console.log(Object.fromEntries(new FormData(form).entries()));
    usuario = Object.fromEntries(new FormData(form).entries());


    var objXMLHTTP = new XMLHttpRequest();

    objXMLHTTP.open('POST', API_URL + 'usuario/');

    objXMLHTTP.addEventListener('load', completado);
    objXMLHTTP.addEventListener('error', manejarError);
    objXMLHTTP.addEventListener('progress', progreso);
    objXMLHTTP.addEventListener('abort', abortado);
    objXMLHTTP.setRequestHeader("Content-Type", "application/json");
    objXMLHTTP.send(JSON.stringify(usuario));



    function manejarError(evt) {
        console.log('ocurrio un error.');
    }

    function progreso(evt) {
        var procentaje = evt.loaded / evt.total * 100;
        console.log(procentaje);
    }


    function abortado(evt) {
        console.log('cancelado');
    }

    async function completado(evt) {
        var data = JSON.parse(this.response);
        console.log(data);
    }
}

