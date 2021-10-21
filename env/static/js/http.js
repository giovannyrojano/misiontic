
function http(URL, METHOD) {
    var objXMLHTTP = new XMLHttpRequest();

    objXMLHTTP.open(METHOD, URL);

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
        console.log(data);
        return data;
    }
}

//this.http('http://localhost:5000/api/test/', 'GET');