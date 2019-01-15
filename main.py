import cloudstorage as gcs
from google.appengine.api import memcache
from google.appengine.api import images
from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers
import webapp2

import json
import webapp2
import conexion

class RestHandler(webapp2.RequestHandler):
    def dispatch(self):
        super(RestHandler, self).dispatch()
    def SendJson(self, r):
        self.response.headers['content-type'] = 'text/plain'
        self.response.write(json.dumps(r))
        
class QueryHandler(RestHandler):
    def get(self):
        facults = conexion.consulta()
        self.SendJson(facults)
class QueryFilesHandler(RestHandler):
    def post(self):
        r = json.loads(self.request.body)
        files = conexion.consultaFiles(r['id_facultamiento'])
        self.SendJson(files)
class QueryCatTipoFae(RestHandler):
    def get(self):
        faes = conexion.cattipoFae()
        self.SendJson(faes)
        
class QueryCatHandler(RestHandler):
    def get(self):
        cat = conexion.catconsulta()
        self.SendJson(cat)

class QueryCatLineaNegoHandler(RestHandler):
    def get(self):
        linea_nego = conexion.cat_linea_nego()
        self.SendJson(linea_nego)
    
class QueryCatTipoPagoHandler(RestHandler):
    def get(self):
        tipo_pago = conexion.cattipo_pago()
        self.SendJson(tipo_pago)
        
class QueryCatConceptosHandler(RestHandler):
    def get(self):
        concepto = conexion.cat_concepto() 
        self.SendJson(concepto)
        
class QueryCatMotivosHandler(RestHandler):
    def get(self):
        motivo = conexion.cat_motivo() 
        self.SendJson(motivo)
        
class QueryCatDetallesHandler(RestHandler):
    def get(self):
        detalle = conexion.cat_detalle() 
        self.SendJson(detalle)
class QueryCatTipoFondoHandler(RestHandler):
    def get(self):
        tipo_fondo = conexion.cat_tipoFondo()
        self.SendJson(tipo_fondo)
class QueryMonto(RestHandler):
    def get(self):
        monto = conexion.consult_monto()
        self.SendJson(monto)
class QueryGastos(RestHandler):
    def get(self):
        gastos = conexion.consult_gastos()
        self.SendJson(gastos)
class QueryGastosAutos(RestHandler):
    def get(self):
        gastosAutos = conexion.consult_gastos_autos()
        self.SendJson(gastosAutos)
class InsertHandler(RestHandler):
    def post(self):
        r = json.loads(self.request.body)
        facult = conexion.altaFAE(r['id_tipo_fae'],r['id_solicitante'], r['email_solicitante'],r['siniestro'], r['poliza'], r['reclamacion'], r['id_ramo'], r['id_linea_nego'], r['nombre_benef'],r['ap_pat_benef'],r['ap_mat_benef'], r['folio_nvo_barra'], r['id_tipo_pago'], r['id_concepto'], r['id_motivo'], r['id_detalle'], r['causa'], r['id_tipo_fondo'], r['id_funcionario'], r['monto_autorizado'], r['fondo_actual'], r['fondo_restante'], r['id_func_vb'])
        self.SendJson(facult)
        
class FileUploadHandler(RestHandler):
    def post(self):
        id_facultamiento = self.request.POST['id_facultamiento']
        file_data = self.request.POST['archivos']
        conexion.crear_archivo(id_facultamiento,file_data.filename,file_data.type,file_data.value)
        
class viewFileUploadHandler(blobstore_handlers.BlobstoreDownloadHandler):
    def get(self, blob_key):
        self.send_blob(blob_key)
        
class AprobHandler(RestHandler):
    def post(self):
        r = json.loads(self.request.body)
        facult = conexion.aprob(r['id_facultamiento'],r['id_estatus'],r['func_observ'])
        self.SendJson(r)
class TerminarHandler(RestHandler):
    def post(self):
        r = json.loads(self.request.body)
        facult = conexion.terminar(r['id_facultamiento'], r['fecha_registro'], r['solicitante'], r['email_solic'], r['monto_autorizado'], r['ramo'], r['linea_nego'], r['nom_benef'], r['appat_benef'], r['apmat_benef'], r['id_estatus'], r['facult_observ'])
        
class cancelaFolio(RestHandler):
    def post(self):
        r = json.loads(self.request.body)
        facult = conexion.cancelFolio(r['id_facult'], r['observ_cancel_folio'], r['email_solic'], r['email_func_vb'], r['folio_termino'], r['ramo'], r['linea_nego'], r['monto'], r['nom_benef'], r['appat_benef'], r['apmat_benef'])
class QueryEdocta(RestHandler):
    def get(self):
        edocta = conexion.edocta()
        self.SendJson(edocta)
class QueryEdoctaMontos(RestHandler):
    def get(self):
        edoctaMontos = conexion.edoctaMontos()
        self.SendJson(edoctaMontos)
class QueryCatUsers(RestHandler):
    def get(self):
        users = conexion.catUsers()
        self.SendJson(users)
class QueryCatPerfiles(RestHandler):
    def get(self):
        perfiles = conexion.catPerfiles()
        self.SendJson(perfiles)
class altaUserHandler(RestHandler):
    def post(self):
        r = json.loads(self.request.body)
        user = conexion.altaUser(r['email'],r['nombre'],r['ap_pat'],r['ap_mat'],r['id_perfil'],r['aspecto'],r['puesto'],r['direccion'])
        self.SendJson(r)
class updateUser(RestHandler):
    def post(self):
        r = json.loads(self.request.body)
        updUser = conexion.upUser(r['id_usuario'], r['email'], r['nombre'], r['ap_pat'], r['ap_mat'], r['direccion'], r['puesto'], r['aspecto'], r['perfil'], r['estatus'], r['id_direccion'], r['id_puesto'], r['id_aspecto'], r['id_perfil'], r['activo'])
        self.SendJson(r)
class QueryCatFondos(RestHandler):
    def get(self):
        fondos = conexion.catFondos()
        self.SendJson(fondos)
class updateFondo(RestHandler):
    def post(self):
        r = json.loads(self.request.body)
        updFondo = conexion.updFondo(r['id_fondo'], r['funcionario'], r['id_ramo'], r['ramo'], r['id_linea_nego'], r['linea_nego'], r['monto'], r['mes'])
        self.SendJson(r)
        
class altaFondo(RestHandler):
    def post(self):
        r = json.loads(self.request.body)
        user = conexion.altaFondo(r['user'],r['ramo'],r['linea_nego'],r['mes'],r['year'],r['monto'])
        self.SendJson(user) 
class catDirecciones(RestHandler):
    def get(self):
        direcciones = conexion.catDirecciones()
        self.SendJson(direcciones)
class catPuestos(RestHandler):
    def get(self):
        puestos = conexion.catPuestos()
        self.SendJson(puestos)
class catAspectos(RestHandler):
    def get(self):
        aspectos = conexion.catAspectos()
        self.SendJson(aspectos)
class listReports(RestHandler):
    def get(self):
        reports = conexion.listReports()
        self.SendJson(reports)
        
class altaReport(RestHandler):
    def post(self):
        r = json.loads(self.request.body)
        report = conexion.altaReport(r['titulo'],r['url'],r['descripcion'])
        self.SendJson(report)
class deleteReport(RestHandler):
    def post(self):
        r = json.loads(self.request.body)
        report = conexion.deleteReport(r['id_report'])
        self.SendJson(report)
        
class listPoliticas(RestHandler):
    def get(self):
        politicas = conexion.listPoliticas()
        self.SendJson(politicas)
class altaPolit(RestHandler):
    def post(self):
        file_data = self.request.POST['file']
        conexion.crear_archivo_polit(file_data.filename,file_data.type,file_data.value)
class deletePolitica(RestHandler):
    def post(self):
        r = json.loads(self.request.body)
        polit = conexion.deletePolit(r['id_file'])
        self.SendJson(polit)
        
APP = webapp2.WSGIApplication([
    ('/rest/query', QueryHandler),
    ('/rest/insert', InsertHandler),
    ('/rest/files', QueryFilesHandler),
    ('/rest/aprobar', AprobHandler),
    ('/rest/terminar', TerminarHandler),
    ('/rest/cancelaFolio', cancelaFolio),
    ('/rest/cat_tipo_fae', QueryCatTipoFae),
    ('/rest/cat', QueryCatHandler),
    ('/rest/cat_tipo_pago', QueryCatTipoPagoHandler),
    ('/rest/cat_linea_nego', QueryCatLineaNegoHandler),
    ('/rest/cat_concepto', QueryCatConceptosHandler),
    ('/rest/cat_motivo', QueryCatMotivosHandler),
    ('/rest/cat_detalle', QueryCatDetallesHandler),
    ('/rest/cat_tipoFondo', QueryCatTipoFondoHandler),
    ('/rest/consult_monto', QueryMonto),
    ('/rest/consult_gastos', QueryGastos),
    ('/rest/consult_gastos_autos', QueryGastosAutos),
    ('/rest/edocta', QueryEdocta),
    ('/rest/edoctaMontos', QueryEdoctaMontos),
    ('/rest/admin_users',QueryCatUsers),
    ('/rest/cat_perfiles',QueryCatPerfiles),
    ('/rest/alta_user',altaUserHandler),
    ('/rest/update_user',updateUser),
    ('/rest/admin_fondos',QueryCatFondos),
    ('/rest/update_fondo',updateFondo),
    ('/rest/alta_fondo',altaFondo),
    ('/rest/cat_direcciones',catDirecciones),
    ('/rest/cat_puestos', catPuestos),
    ('/rest/cat_aspectos', catAspectos),
    ('/rest/reports', listReports),
    ('/rest/alta_report', altaReport),
    ('/rest/delete_report', deleteReport),
    ('/rest/politicas', listPoliticas),
    ('/rest/alta_polit', altaPolit),
    ('/rest/delete_polit', deletePolitica),
    ('/rest/upload_files', FileUploadHandler),
    ('/rest/viewFile/([^/]+)?', viewFileUploadHandler),
], debug=True)
