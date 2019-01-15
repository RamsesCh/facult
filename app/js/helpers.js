function init() {
    gapi.load('auth2', function() {});
}
function loginSuccess(){
    toastr.success('Bienvenido','')
}
function loginError(){
    toastr.error('El usuario no tiene acceso a la aplicación', '')
}
function altaAlert(){
    toastr.success('Solicitud registrada', '')
}

function aprobadoAlert(){
    toastr.success('Solicitud Aprobada','')
}

function rechazarAlert(){
    toastr.error('Solicitud Rechazada','')
}

function terminarAlert(){
    toastr.success('Solicitud Terminada','')
}

function cancelarAlert(){
    toastr.error('Solicitud Rechazada','')
}
function cancelarFolioAlert(){
    toastr.error('Folio Cancelado')
}
function altaReportSuccess(){
    toastr.success('Reporte Agregado','')
}

function deleteReport(){
    toastr.error('Reporte Eliminado','')
}

function altaUserSuccess(){
    toastr.success('El usuario ha sido registrado', '')
}

function updateUserSuccess(){
    toastr.success('Cambios guardados', '')
}

function updateFondoSuccess(){
    toastr.success('Cambios guardados', '')
}
function altaFondoSuccess(){
    toastr.success('Fondo registrado', '')
}
function catalogFondoSuccess(){
    toastr.success('Cátalogo de fondos actualizado', '')
}
function altaPolitSuccess(){
    toastr.success('Archivo Agregado','')
}
function deletePolitica(){
    toastr.error('Archivo Eliminado','')
}