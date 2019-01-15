import cloudstorage as gcs
from google.appengine.api import memcache
from google.appengine.api import images
from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers
import webapp2

import os
import MySQLdb
import envio_email
import envio_smtp
import send_mail_gmail2

#VARIABLES DE ENTORNO app.yaml
cloud_user = os.getenv('CLOUDSQL_USER')
cloud_pass = os.getenv('CLOUDSQL_PASSWORD')
cloud_conexion_name = os.getenv('CLOUDSQL_CONNECTION_NAME')
cloud_db = os.getenv('CLOUDSQL_DB')
bucket = os.getenv('BUCKET')

#FUNCION QUE CONECTA A LA BASE DE DATOS 
def connect_to_cloudsql():
    if os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine/'):
        cloudsql_unix_socket = os.path.join('/cloudsql', cloud_conexion_name)
        conect_db = MySQLdb.connect(
                    unix_socket=cloudsql_unix_socket,
                    user=cloud_user,
                    passwd=cloud_pass,
                    db= cloud_db, charset='utf8',use_unicode=True)
    else:
        conect_db = MySQLdb.connect(
                    host='35.193.7.90', 
                    user=cloud_user, 
                    passwd=cloud_pass, 
                    db= cloud_db,charset='utf8',use_unicode=True)
    return conect_db

#RETORNA UNA CONSULTA MYSQL
def consulta():
    db = connect_to_cloudsql()
    cursor = db.cursor()
    cursor.execute("SELECT reg_facultamientos.id_facultamiento, CONCAT(UNIX_TIMESTAMP(reg_facultamientos.fecha_registro),112) as fecha_alta, cat_tipo_fae.tipo_fae,reg_facultamientos.id_solicitante, cat_usuarios.email, CONCAT(cat_usuarios.nombre,' ',cat_usuarios.ap_pat,' ',cat_usuarios.ap_mat) AS solicitante, reg_facultamientos.siniestro, reg_facultamientos.poliza, reg_facultamientos.reclamacion, reg_facultamientos.nombre_benef,reg_facultamientos.ap_pat_benef,reg_facultamientos.ap_mat_benef, reg_facultamientos.folio_nvo_barra_serv, cat_tipo_pago.tipo_pago, cat_concepto.concepto, reg_facultamientos.id_motivo, cat_motivo.motivo, cat_detalle.detalle, reg_facultamientos.causa, cat_tipo_fondo.tipo_fondo, reg_facultamientos.monto_autorizado, reg_facultamientos.fondo_actual, reg_facultamientos.fondo_restante, CONCAT(func2.nombre,' ', func2.ap_pat,' ', func2.ap_mat) AS funcionario_vb, estatus_facult.estatus, cat_ramo.ramo, cat_linea_nego.linea_nego, CONCAT(func.nombre,' ', func.ap_pat,' ', func.ap_mat) AS funcionario, reg_facultamientos.id_ramo, reg_facultamientos.id_funcionario, reg_facultamientos.id_func_vb, CONCAT(UNIX_TIMESTAMP(reg_facultamientos.fecha_autorizacion),112), CONCAT(UNIX_TIMESTAMP(reg_facultamientos.fecha_rechazo),112), CONCAT(UNIX_TIMESTAMP(reg_facultamientos.fecha_termino), 112), reg_facultamientos.folio_termino, reg_facultamientos.func_observ, reg_facultamientos.facult_observ, CONCAT(UNIX_TIMESTAMP(reg_facultamientos.fecha_rechazo_facult), 112), CONCAT(UNIX_TIMESTAMP(reg_facultamientos.fecha_cancel_folio), 112), observ_cancel_folio, func2.email, reg_facultamientos.id_estatus FROM reg_facultamientos INNER JOIN cat_tipo_fae ON cat_tipo_fae.id_tipo_fae = reg_facultamientos.id_tipo_fae INNER JOIN cat_usuarios ON cat_usuarios.id_usuario = reg_facultamientos.id_solicitante INNER JOIN cat_ramo ON reg_facultamientos.id_ramo = cat_ramo.id_ramo INNER JOIN cat_linea_nego ON reg_facultamientos.id_linea_nego = cat_linea_nego.id_linea_nego INNER JOIN cat_tipo_pago ON reg_facultamientos.id_tipo_pago = cat_tipo_pago.id_tipo_pago INNER JOIN cat_concepto ON reg_facultamientos.id_concepto = cat_concepto.id_concepto LEFT JOIN cat_motivo ON cat_motivo.id_motivo = reg_facultamientos.id_motivo LEFT JOIN cat_detalle ON reg_facultamientos.id_detalle = cat_detalle.id_detalle INNER JOIN cat_tipo_fondo ON reg_facultamientos.id_tipo_fondo = cat_tipo_fondo.id_tipo_fondo INNER JOIN cat_usuarios AS func ON reg_facultamientos.id_funcionario = func.id_usuario INNER JOIN estatus_facult ON reg_facultamientos.id_estatus = estatus_facult.id_estatus INNER JOIN cat_usuarios AS func2 ON func2.id_usuario = reg_facultamientos.id_func_vb")
    data = cursor.fetchall()
    payload = []
    content = {}
    for result in data:
        content = {'id_facultamiento':result[0], 'fecha_registro':result[1], 'tipo_fae':result[2],'id_solicitante':result[3], 'email_solicitante':result[4], 'solicitante':result[5], 'siniestro':result[6], 'poliza': result[7], 'reclamacion': result[8], 'nom_benef': result[9], 'appat_benef': result[10], 'apmat_benef': result[11], 'folio_nvo_barra': result[12], 'tipo_pago': result[13], 'concepto': result[14], 'id_motivo': result[15], 'motivo': result[16], 'detalle': result[17], 'causa': result[18], 'tipo_fondo': result[19], 'monto_autorizado': float(result[20]), 'fondo_actual': result[21], 'fondo_restante': result[22],'func_vb': result[23], 'estatus': result[24], 'ramo':result[25], 'linea_nego':result[26], 'funcionario': result[27], 'id_ramo': result[28], 'id_funcionario': result[29], 'id_func_vb':result[30], 'fecha_autorizacion':result[31], 'fecha_rechazo':result[32], 'fecha_termino':result[33], 'folio_termino':result[34], 'func_observ':result[35], 'facult_observ':result[36], 'fecha_rechazo_facult':result[37], 'fecha_cancel_folio':result[38], 'observ_cancel_folio':result[39], 'email_func_vb':result[40], 'id_estatus':result[41]}
        payload.append(content)
        content = {}
    return payload

def consultaFiles(id_facultamiento):
    db = connect_to_cloudsql()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM rep_archivos WHERE id_facultamiento =" + str(id_facultamiento))
    data = cursor.fetchall()
    payload = []
    content = {}
    for result in data:
        content = {'id_archivo':result[0],'nombre':result[1], 'filename':result[2], 'key_name':result[3], 'id_facultamiento':result[4]}
        payload.append(content)
        content = {}
    return payload
def cattipoFae():
    db = connect_to_cloudsql()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM cat_tipo_fae WHERE cat_tipo_fae.activo = 1")
    data = cursor.fetchall()
    payload = []
    content = {}
    for result in data:
        content = {'id_tipo_fae':result[0],'tipo_fae':result[1]}
        payload.append(content)
        content = {}
    return payload
def catconsulta():
    db = connect_to_cloudsql()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM cat_ramo WHERE cat_ramo.activo = 1")
    data = cursor.fetchall()
    payload = []
    content = {}
    for result in data:
        content = {'id_ramo':result[0],'ramo':result[1],'id_tipo_fae':str(result[2])}
        payload.append(content)
        content = {}
    return payload

def cat_linea_nego():
    db = connect_to_cloudsql()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM cat_linea_nego WHERE cat_linea_nego.activo = 1")
    data = cursor.fetchall()
    payload = []
    content = {}
    for result in data:
        content = {'id_linea_nego':result[0],'linea_nego':result[1],'id_ramo':str(result[2])}
        payload.append(content)
        content = {}
    return payload

def cattipo_pago():
    db2 = connect_to_cloudsql()
    cursor2 = db2.cursor()
    cursor2.execute("SELECT cat_tipo_pago.id_tipo_pago, cat_tipo_pago.tipo_pago, cat_tipo_pago.id_ramo, cat_tipo_pago.id_tipo_fae, cat_tipo_pago.activo, cat_ramo.ramo, cat_tipo_fae.tipo_fae FROM cat_tipo_pago INNER JOIN cat_ramo ON cat_tipo_pago.id_ramo = cat_ramo.id_ramo INNER JOIN cat_tipo_fae ON cat_tipo_pago.id_tipo_fae = cat_tipo_fae.id_tipo_fae")
    data2 = cursor2.fetchall()
    payload2 = []
    content2 = {}
    for result2 in data2:
        content2 = {'id_tipo_pago':result2[0], 'tipo_pago':result2[1], 'id_ramo':str(result2[2]), 'id_tipo_fae':result2[3], 'activo':result2[4], 'ramo':result2[5], 'tipo_fae':result2[6]}
        payload2.append(content2)
        content2 = {}
    return payload2

def cat_concepto(): 
    db = connect_to_cloudsql()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM cat_concepto WHERE cat_concepto.activo = 1")
    data = cursor.fetchall()
    payload = []
    content = {}
    for result in data:
        content = {'id_concepto':result[0], 'concepto':result[1], 'id_tipo_pago':str(result[2])}
        payload.append(content)
        content = {}
    return payload
def cat_motivo(): 
    db = connect_to_cloudsql()
    cursor = db.cursor()
    cursor.execute("SELECT cat_motivo.id_motivo, cat_motivo.motivo, cat_motivo.id_aspecto, cat_usuarios.id_usuario FROM cat_usuarios INNER JOIN cat_motivo on cat_motivo.id_aspecto = cat_usuarios.id_aspecto WHERE cat_motivo.activo = 1")
    data = cursor.fetchall()
    payload = []
    content = {}
    for result in data:
        content = {'id_motivo':result[0], 'motivo':result[1], 'id_aspecto':str(result[2]), 'id_func':str(result[3])}
        payload.append(content)
        content = {}
    return payload
def cat_detalle(): 
    db = connect_to_cloudsql()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM cat_detalle WHERE cat_detalle.activo = 1")
    data = cursor.fetchall()
    payload = []
    content = {}
    for result in data:
        content = {'id_detalle':result[0], 'detalle':result[1], 'id_motivo':str(result[2])}
        payload.append(content)
        content = {}
    return payload
def cat_tipoFondo():
    db = connect_to_cloudsql()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM cat_tipo_fondo WHERE cat_tipo_fondo.activo = 1")
    data = cursor.fetchall()
    payload = []
    content = {}
    for result in data:
        content = {'id_tipo_fondo':result[0], 'tipo_fondo':result[1]}
        payload.append(content)
        content = {}
    return payload
def consult_monto():
    db = connect_to_cloudsql()
    cursor = db.cursor()
    cursor.execute("SELECT cat_fondos.id_ramo, cat_fondos.id_linea_nego, cat_fondos.id_func, cat_fondos.monto FROM cat_fondos WHERE cat_fondos.mes = MONTH(CURRENT_DATE())")
    data = cursor.fetchall()
    payload = []
    content = {}
    for result in data:
        content = {'id_ramo':str(result[0]),'id_linea_nego':str(result[1]),'id_funcionario':str(result[2]),'monto':str(result[3])}
        payload.append(content)
        content = {}
    return payload

def consult_gastos():
    db = connect_to_cloudsql()
    cursor = db.cursor()
    cursor.execute("SELECT reg_facultamientos.id_ramo, reg_facultamientos.id_linea_nego, reg_facultamientos.id_funcionario, SUM(reg_facultamientos.monto_autorizado) AS total_aut FROM reg_facultamientos WHERE (reg_facultamientos.id_estatus = 1 OR reg_facultamientos.id_estatus = 2 OR reg_facultamientos.id_estatus= 4) AND MONTH(reg_facultamientos.fecha_registro) = MONTH(CURRENT_DATE()) GROUP BY reg_facultamientos.id_ramo, reg_facultamientos.id_linea_nego, reg_facultamientos.id_funcionario")
    data = cursor.fetchall()
    payload = []
    content = {}
    for result in data:
        content = {'id_ramo':str(result[0]),'id_linea_nego':str(result[1]),'id_funcionario':str(result[2]),'total_aut':str(result[3])}
        payload.append(content)
        content = {}
    return payload
def consult_gastos_autos():
    db = connect_to_cloudsql()
    cursor = db.cursor()
    cursor.execute("SELECT reg_facultamientos.id_ramo, reg_facultamientos.id_funcionario, SUM(reg_facultamientos.monto_autorizado) AS total_aut FROM reg_facultamientos WHERE reg_facultamientos.id_ramo = 2 AND (reg_facultamientos.id_estatus = 1 OR reg_facultamientos.id_estatus = 2 OR reg_facultamientos.id_estatus= 4) AND MONTH(reg_facultamientos.fecha_registro) = MONTH(CURRENT_DATE()) GROUP BY reg_facultamientos.id_ramo, reg_facultamientos.id_funcionario")
    data = cursor.fetchall()
    payload = []
    content = {}
    for result in data:
        content = {'id_ramo':str(result[0]),'id_funcionario':str(result[1]),'total_aut':str(result[2])}
        payload.append(content)
        content = {}
    return payload
    
    
def altaFAE(id_tipo_fae,id_solicitante, email_solicitante,siniestro,poliza,reclamacion, id_ramo, id_linea_nego, nombre_benef, ap_pat_benef, ap_mat_benef,folio_nvo_barra, id_tipo_pago, id_concepto, id_motivo, detalle, causa, id_tipo_fondo, id_funcionario, monto_autorizado, fondo_actual, fondo_restante,id_func_vb):
    db = connect_to_cloudsql()
    cursor = db.cursor()
    cursor.execute("INSERT INTO reg_facultamientos(`fecha_registro`,`id_tipo_fae`,`id_solicitante`,`siniestro`, `poliza`, `reclamacion`, `id_ramo`, `id_linea_nego`, `nombre_benef`, `ap_pat_benef`, `ap_mat_benef`, `folio_nvo_barra_serv`,`id_tipo_pago`, `id_concepto`, `id_motivo`, `id_detalle`, `causa`, `id_tipo_fondo`, `id_funcionario`, `monto_autorizado`, `fondo_actual`, `fondo_restante`,`id_func_vb`, `id_estatus` ) VALUES (NOW(),%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,1)", (id_tipo_fae,int(id_solicitante),siniestro,poliza,reclamacion, int(id_ramo), int(id_linea_nego), nombre_benef, ap_pat_benef, ap_mat_benef,folio_nvo_barra, int(id_tipo_pago), int(id_concepto), int(id_motivo), int(detalle), causa, int(id_tipo_fondo), int(id_funcionario), monto_autorizado, fondo_actual, fondo_restante, int(id_func_vb)))
    db.commit()
    db.close()
    last_facult = cursor.lastrowid
    #envio_email.envioMailSolic(last_facult,email_solicitante,id_ramo,id_func_vb,monto_autorizado,nombre_benef,ap_pat_benef,ap_mat_benef)
    #envio_smtp.envio_mail2(last_facult,email_solicitante,id_ramo,id_func_vb,monto_autorizado,nombre_benef,ap_pat_benef,ap_mat_benef)
    #send_mail_gmail2.main()
    return last_facult
    
def crear_archivo(id_facultamiento,nombre,file_type,value):
    nomASCII = nombre.encode('ascii', errors='ignore')
    filename= bucket + '/' + nomASCII
    write_retry_params = gcs.RetryParams(backoff_factor=1.1)
    gcs_file = gcs.open(filename, 'w',
                        content_type=file_type,
                        options={
                            'x-goog-meta-foo': 'foo',
                            'x-goog-meta-bar': 'bar'},
                        retry_params=write_retry_params)
    gcs_file.write(value)
    gcs_file.close()
    blob_key = blobstore.create_gs_key('/gs' + filename)
    #img_url = images.get_serving_url(blob_key=blob_key)
    db = connect_to_cloudsql()
    cursor = db.cursor()
    cursor.execute("INSERT INTO rep_archivos(`nombre`,`filename`,`key_name`,`id_facultamiento`) VALUES(%s,%s,%s,%s)",(nomASCII,filename,blob_key,id_facultamiento))
    db.commit()
    db.close()
    
        
def aprob(id_facultamiento,id_estatus,func_observ):
    db = connect_to_cloudsql()
    cursor = db.cursor()
    if id_estatus == "2":
        cursor.execute('UPDATE reg_facultamientos SET id_estatus = %s, fecha_autorizacion = NOW(), func_observ = %s WHERE id_facultamiento = %s', (id_estatus, func_observ, id_facultamiento))
        db.commit()
        db.close()
    else:
        cursor.execute('UPDATE reg_facultamientos SET id_estatus = %s, fecha_rechazo = NOW(), func_observ = %s WHERE id_facultamiento = %s', (id_estatus, func_observ, id_facultamiento))
        db.commit()
        db.close()
    if id_estatus == "2":
        envio_email.envioMailAprob(id_facultamiento)
    else:
        envio_email.envioMailRechaz(id_facultamiento)
    
def terminar(id_facultamiento, fecha_registro, solicitante, email_solic, monto_autorizado, ramo, linea_nego, nom_benef, appat_benef, apmat_benef, id_estatus,facult_observ):
    folio = 'FAE' + '-' + ramo[:3] + linea_nego + '-' + id_facultamiento
    benef = nom_benef + ' ' + appat_benef + ' ' + apmat_benef
    db = connect_to_cloudsql()
    cursor = db.cursor()
    if id_estatus == "4":
        cursor.execute('UPDATE reg_facultamientos SET id_estatus = %s, fecha_termino = NOW(), facult_observ = %s, folio_termino = %s WHERE id_facultamiento = %s',(id_estatus, facult_observ, folio, id_facultamiento))
        db.commit()
        db.close()
    else:
        cursor.execute('UPDATE reg_facultamientos SET id_estatus = %s, fecha_rechazo_facult = NOW(), facult_observ = %s WHERE id_facultamiento = %s',(id_estatus, facult_observ, id_facultamiento))
        db.commit()
        db.close()
        
    if id_estatus == "4":
        envio_email.envioMailTermino(folio, ramo, linea_nego, solicitante, email_solic, monto_autorizado, benef)
    else:
        envio_email.envioMailCancel(ramo, linea_nego, solicitante, email_solic, monto_autorizado, benef)
    
def cancelFolio(id_facult,observ_cancel_folio,email_solic,email_func_vb,folio_termino, ramo, linea_nego, monto, nom_benef, appat_benef, apmat_benef):
    db = connect_to_cloudsql()
    benef = nom_benef + ' ' + appat_benef + ' ' + apmat_benef
    cursor = db.cursor()
    cursor.execute('UPDATE reg_facultamientos SET id_estatus = 6, fecha_cancel_folio = NOW(), observ_cancel_folio = %s WHERE id_facultamiento = %s',(observ_cancel_folio,str(id_facult)))
    db.commit()
    db.close()
    envio_email.envioMailCancelFAE(email_solic,email_func_vb,folio_termino, ramo, linea_nego, monto,benef)
    
def edocta():
    db = connect_to_cloudsql()
    cursor = db.cursor()
    cursor.execute("SELECT reg_facultamientos.folio_termino,reg_facultamientos.id_funcionario, CONCAT(cat_usuarios.nombre,' ', cat_usuarios.ap_pat, ' ', cat_usuarios.ap_mat) as funcionario, IF(reg_facultamientos.id_ramo = 1 AND reg_facultamientos.id_linea_nego = 1, reg_facultamientos.monto_autorizado, 0) AS GMMLP, IF(reg_facultamientos.id_ramo = 1 AND reg_facultamientos.id_linea_nego = 2, reg_facultamientos.monto_autorizado, 0) AS GMMLC, IF(reg_facultamientos.id_ramo = 2, reg_facultamientos.monto_autorizado, 0) AS AUTOS, DATE_FORMAT(reg_facultamientos.fecha_registro, '%d %b %Y') AS fecha_alta, DATE_FORMAT(reg_facultamientos.fecha_registro, '%m') AS mes, reg_facultamientos.id_facultamiento FROM reg_facultamientos INNER JOIN cat_usuarios ON cat_usuarios.id_usuario = reg_facultamientos.id_funcionario WHERE reg_facultamientos.id_estatus = 4")
    data = cursor.fetchall()
    payload = []
    content = {}
    for result in data:
        content = {'folio_termino':result[0],'id_func':result[1], 'funcionario':result[2], 'gmmlp':result[3], 'gmmlc':result[4], 'autos':result[5], 'fecha_alta':result[6], 'mes':result[7], 'id_facult':result[8]}
        payload.append(content)
        content = {}
    return payload
def edoctaMontos():
    db = connect_to_cloudsql()
    cursor = db.cursor()
    cursor.execute("SELECT cat_fondos.id_func, CONCAT(cat_usuarios.nombre,' ',cat_usuarios.ap_pat,' ',cat_usuarios.ap_mat) AS FUNCIONARIO, cat_usuarios.activo, SUM(IF (cat_fondos.id_ramo = 1 AND cat_fondos.id_linea_nego=1, cat_fondos.monto, 0)) as GMMLP, sum(IF (cat_fondos.id_ramo = 1 AND cat_fondos.id_linea_nego=2, cat_fondos.monto, 0)) as GMMLC, sum(IF (cat_fondos.id_ramo = 2, cat_fondos.monto, 0)) as AUTOS, cat_fondos.mes FROM `cat_fondos` INNER JOIN cat_usuarios ON cat_usuarios.id_usuario = cat_fondos.id_func GROUP BY cat_fondos.id_func, cat_fondos.mes")
    data = cursor.fetchall()
    payload = []
    content = {}
    for result in data:
        content = {'id_func':result[0],'func':result[1], 'activo':result[2], 'gmmlp':int(result[3]), 'gmmlc':int(result[4]), 'autos':int(result[5]), 'mes':result[6]}
        payload.append(content)
        content = {}
    return payload
def catUsers():
    db = connect_to_cloudsql()
    cursor = db.cursor()
    cursor.execute("SELECT cat_usuarios.id_usuario, DATE_FORMAT(cat_usuarios.fecha_alta, '%d %b %Y') AS fecha, cat_usuarios.email, cat_usuarios.nombre, cat_usuarios.ap_pat, cat_usuarios.ap_mat, cat_direcciones.direccion, cat_puestos.puesto, cat_aspectos.aspecto, cat_perfiles.perfil, IF(cat_usuarios.activo = 1, 'ACTIVO','BAJA') AS estatus, cat_usuarios.id_direccion, cat_usuarios.id_puesto, cat_usuarios.id_aspecto, cat_usuarios.id_perfil, cat_usuarios.activo FROM `cat_usuarios` LEFT JOIN cat_direcciones ON cat_direcciones.id_direcion = cat_usuarios.id_direccion LEFT JOIN cat_puestos ON cat_puestos.id_puesto = cat_usuarios.id_puesto LEFT JOIN cat_aspectos ON cat_aspectos.id_aspecto = cat_usuarios.id_aspecto LEFT JOIN cat_perfiles ON cat_perfiles.id_perfil = cat_usuarios.id_perfil")
    data = cursor.fetchall()
    payload = []
    content = {}
    for result in data:
        content = {'id_usuario':result[0], 'fecha_alta':result[1], 'email':result[2], 'nombre':result[3], 'ap_pat':result[4], 'ap_mat':result[5], 'direccion':result[6], 'puesto':result[7], 'aspecto':result[8], 'perfil':result[9],  'estatus':result[10], 'id_direccion':result[11], 'id_puesto':result[12], 'id_aspecto':result[13], 'id_perfil':result[14], 'activo':result[15]}
        payload.append(content)
        content = {}
    return payload
def catPerfiles():
    db = connect_to_cloudsql()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM cat_perfiles WHERE cat_perfiles.activo = 1")
    data = cursor.fetchall()
    payload = []
    content = {}
    for result in data:
        content = {'id_perfil':result[0],'perfil':result[1]}
        payload.append(content)
        content = {}
    return payload
def altaUser(email,nombre,ap_pat,ap_mat,id_perfil,aspecto,puesto,direccion):
    db = connect_to_cloudsql()
    cursor = db.cursor()
    cursor.execute("INSERT INTO cat_usuarios (`email`,`nombre`,`ap_pat`,`ap_mat`,`id_perfil`,`id_aspecto`,`id_puesto`,`id_direccion`,`fecha_alta`) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,NOW())",(email,nombre,ap_pat,ap_mat,id_perfil,aspecto,puesto,direccion))    
    db.commit()
    db.close()
    content = {'id_user':cursor.lastrowid}
    return content
def upUser(id_usuario, email, nombre, ap_pat, ap_mat, direccion, puesto, aspecto, perfil, estatus, id_direccion, id_puesto, id_aspecto, id_perfil, activo):
    db = connect_to_cloudsql()
    cursor = db.cursor()
    cursor.execute('UPDATE cat_usuarios SET email = %s, nombre = %s, ap_pat = %s, ap_mat = %s, id_perfil = %s, id_aspecto = %s, id_puesto = %s, id_direccion = %s, activo = %s WHERE id_usuario = %s',(email,nombre, ap_pat, ap_mat, int(id_perfil), int(id_aspecto), int(id_puesto), int(id_direccion), int(activo), int(id_usuario)))
    db.commit()
    db.close()
def catFondos():
    db = connect_to_cloudsql()
    cursor = db.cursor()
    cursor.execute("SELECT cat_fondos.id_fondo, cat_fondos.id_func, CONCAT(cat_usuarios.nombre,' ',cat_usuarios.ap_pat,' ',cat_usuarios.ap_mat) AS FUNCIONARIO, cat_usuarios.activo, cat_fondos.id_ramo, cat_ramo.ramo, cat_fondos.id_linea_nego, cat_linea_nego.linea_nego, cat_fondos.monto, cat_fondos.mes, year FROM `cat_fondos` LEFT JOIN cat_usuarios ON cat_usuarios.id_usuario = cat_fondos.id_func LEFT JOIN cat_ramo on cat_ramo.id_ramo = cat_fondos.id_ramo LEFT JOIN cat_linea_nego on cat_linea_nego.id_linea_nego = cat_fondos.id_linea_nego WHERE cat_fondos.mes >= MONTH(NOW())")
    data = cursor.fetchall()
    payload = []
    content = {}
    for result in data:
        content = {'id_fondo':result[0], 'id_func':result[1],'funcionario':result[2], 'activo':result[3],'id_ramo':result[4],'ramo':result[5], 'id_linea_nego':result[6], 'linea_nego':result[7], 'monto':int(result[8]), 'mes':result[9], 'year':result[10]}
        payload.append(content)
        content = {}
    return payload

def updFondo(id_fondo,funcionario,ramo,id_ramo,id_linea_nego,linea_nego,monto,mes):
    db = connect_to_cloudsql()
    cursor = db.cursor()
    cursor.execute('UPDATE cat_fondos SET monto = %s WHERE id_fondo = %s',(monto,id_fondo))
    db.commit()
    db.close()
def altaFondo(user,ramo,linea_nego,mes,year,monto):
    db = connect_to_cloudsql()
    cursor = db.cursor()
    cursor.execute("INSERT INTO cat_fondos(`id_ramo`,`id_linea_nego`, `id_func`, `monto`,`mes`,`year`) VALUES(%s,%s,%s,%s,%s,%s)",(ramo,linea_nego,user,monto,mes,year))    
    db.commit()
    db.close()
    content = {'id_fondo':cursor.lastrowid}
    return content
def catDirecciones():
    db = connect_to_cloudsql()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM cat_direcciones WHERE cat_direcciones.activo = 1")
    data = cursor.fetchall()
    payload = []
    content = {}
    for result in data:
        content = {'id_direccion':result[0], 'direccion':result[1]}
        payload.append(content)
        content = {}
    return payload    
def catPuestos():
    db = connect_to_cloudsql()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM cat_puestos WHERE cat_puestos.activo = 1")
    data = cursor.fetchall()
    payload = []
    content = {}
    for result in data:
        content = {'id_puesto':result[0], 'puesto':result[1]}
        payload.append(content)
        content = {}
    return payload 
def catAspectos():
    db = connect_to_cloudsql()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM cat_aspectos WHERE cat_aspectos.activo = 1")
    data = cursor.fetchall()
    payload = []
    content = {}
    for result in data:
        content = {'id_aspecto':result[0], 'aspecto':result[1]}
        payload.append(content)
        content = {}
    return payload

def listReports():
    db = connect_to_cloudsql()
    cursor = db.cursor()
    cursor.execute("SELECT reg_reports.id_report, reg_reports.titulo, reg_reports.url, reg_reports.descripcion, DATE_FORMAT(reg_reports.fecha_alta, '%d %b %Y') AS fecha FROM reg_reports WHERE reg_reports.activo = 1")
    data = cursor.fetchall()
    payload = []
    content = {}
    for result in data:
        content = {'id_report':result[0], 'titulo':result[1], 'url':result[2], 'descripcion':result[3], 'fecha':result[4]}
        payload.append(content)
        content = {}
    return payload  
def altaReport(titulo, url, descripcion):
    db = connect_to_cloudsql()
    cursor = db.cursor()
    cursor.execute("INSERT INTO reg_reports (`titulo`,`url`,`descripcion`,`fecha_alta`) VALUES(%s,%s,%s,NOW())",(titulo,url,descripcion))    
    db.commit()
    db.close()
    content = {'id_report':cursor.lastrowid, 'titulo':titulo, 'url':url, 'descripcion':descripcion}
    return content

def deleteReport(id_report):
    db = connect_to_cloudsql()
    cursor = db.cursor()
    cursor.execute("UPDATE reg_reports SET activo = 0 WHERE id_report =" + str(id_report))    
    db.commit()
    db.close()
    content = id_report
    return content
def listPoliticas():
    db = connect_to_cloudsql()
    cursor = db.cursor()
    cursor.execute("SELECT rep_politicas.id_file, rep_politicas.nombre, rep_politicas.filename, rep_politicas.key_name, DATE_FORMAT(rep_politicas.fecha_alta, '%d %b %Y') AS fecha FROM rep_politicas WHERE rep_politicas.activo = 1")
    data = cursor.fetchall()
    payload = []
    content = {}
    for result in data:
        content = {'id_file':result[0], 'nombre':result[1], 'filename':result[2], 'keyname':result[3], 'fecha_alta':result[4]}
        payload.append(content)
        content = {}
    return payload
def crear_archivo_polit(nombre,file_type,value):
    nomASCII = nombre.encode('ascii', errors='ignore')
    filename= bucket + '/' + nomASCII
    write_retry_params = gcs.RetryParams(backoff_factor=1.1)
    gcs_file = gcs.open(filename, 'w',
                        content_type=file_type,
                        options={
                            'x-goog-meta-foo': 'foo',
                            'x-goog-meta-bar': 'bar'},
                        retry_params=write_retry_params)
    gcs_file.write(value)
    gcs_file.close()
    blob_key = blobstore.create_gs_key('/gs' + filename)
    #img_url = images.get_serving_url(blob_key=blob_key)
    db = connect_to_cloudsql()
    cursor = db.cursor()
    cursor.execute("INSERT INTO rep_politicas(`nombre`,`filename`,`key_name`,`fecha_alta`) VALUES(%s,%s,%s,NOW())",(nomASCII,filename,blob_key))
    db.commit()
    db.close()
    last_file = cursor.lastrowid
    return last_file
def deletePolit(id_file):
    db = connect_to_cloudsql()
    cursor = db.cursor()
    cursor.execute("UPDATE rep_politicas SET activo = 0 WHERE id_file =" + str(id_file))    
    db.commit()
    db.close()
    content = id_file
    return content
    
        



    
    
    