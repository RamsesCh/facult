from google.appengine.api import mail
import MySQLdb
import conexion

def envioMailSolic(id_facult_last,email_solicitante,id_ramo,id_func_vb,monto_autorizado,nombre_benef,ap_pat_benef,ap_mat_benef):
    db = conexion.connect_to_cloudsql()
    cursor = db.cursor()
    cursor.execute('SELECT CONCAT(cat_usuarios.nombre," ",cat_usuarios.ap_pat, " ", cat_usuarios.ap_mat) AS funcionario, cat_usuarios.email, cat_ramo.ramo FROM cat_usuarios, cat_ramo WHERE cat_usuarios.id_usuario = %s AND cat_ramo.id_ramo = %s',(int(id_func_vb), int(id_ramo)))
    data = cursor.fetchone()
    nombre_func= data[0]
    mail_func= data[1]
    nombre_ramo = data[2]
    db.close()
    benef = nombre_benef + ' ' + ap_pat_benef + ' ' + ap_mat_benef
    mail.EmailMessage(sender='facultamientos@gnp.com.mx',
                      to=mail_func,
                      subject="Solicitud de Facultamiento",
                      reply_to='noreply@departamentales-gnp.com.mx',
                      html="""<table align='center' style='width: 100%; font-family: arial;'>
                                    <tr>
                                        <td colspan='3' style='border-bottom: solid 3px #00cec9' align='right'><img src='http://www.departamentales.gnp.com.mx/curso_virtual/img/logo-gnp.jpg'></td>
                                    </tr>
                                    <tr>
                                        <td><h4 style='color: #1f3f79; font-size: 16px;'><strong><span><img src='http://www.departamentales.gnp.com.mx/curso_virtual/img/maletin.png'></span> SOLICITUD DE FACULTAMIENTO</strong></h4></td>
                                    </tr>
                                    <tr align='center'>
                                        <td>
                                            <div style='background-color: #fff; margin: 10px; padding-right: 20px; padding-left: 20px; padding-bottom: 50px;'>
                                                <h3>Nueva solicitud por autorizar</h3>
                                                <p>Ha sido registrada una nueva solicitud de facultamiento que requiere de tu Visto Bueno.</p>
                                                <table>
                                                    <tr>
                                                        <td>Solicitante: <strong>""" + email_solicitante + """</strong></td>
                                                    </tr>
                                                    <tr>
                                                        <td>Ramo: <strong>""" + nombre_ramo + """</strong></td>
                                                    </tr>
                                                    <tr>
                                                        <td>Monto Solicitado: <strong>"""+ str(monto_autorizado) +"""</strong></td>
                                                    </tr>
                                                    <tr>
                                                        <td>Beneficiario: <strong>"""+ benef +"""</strong></td>
                                                    </tr>
                                                </table>
                                                <br>
                                                <br>
                                                <a href='https://facultamiento-dot-gnp-infra-159601.appspot.com'>Ir a la solicitud</a>
                                            </div>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td></td>
                                    </tr>
                                    <tr>
                                        <td colspan='3' style='border-bottom: solid 3px #00cec9' align='right'></td>
                                    </tr>
                                </table>
                            """
                     ).Send()

def envioMailAprob(id_facultamiento):
    db = conexion.connect_to_cloudsql()
    cursor = db.cursor()
    cursor.execute('SELECT reg_facultamientos.id_facultamiento, CONCAT(cat_usuarios.nombre," ",cat_usuarios.ap_pat," ",cat_usuarios.ap_mat) AS solicitante, cat_usuarios.email, cat_ramo.ramo, CONCAT(reg_facultamientos.nombre_benef," ",reg_facultamientos.ap_pat_benef," ",reg_facultamientos.ap_mat_benef) AS beneficiario, reg_facultamientos.monto_autorizado, estatus_facult.estatus FROM reg_facultamientos INNER JOIN cat_usuarios on cat_usuarios.id_usuario = reg_facultamientos.id_solicitante INNER JOIN cat_ramo ON reg_facultamientos.id_ramo=cat_ramo.id_ramo INNER JOIN estatus_facult ON reg_facultamientos.id_estatus=estatus_facult.id_estatus WHERE reg_facultamientos.id_facultamiento ='+id_facultamiento)
    data = cursor.fetchone()
    solic = data[1]
    email_solid = data[2]
    data_ramo = data[3]
    data_benef = data[4]
    data_monto = data[5]
    data_estatus = data[6]
#EMAIL PARA FACULTAMIENTO
    mail.EmailMessage(sender='facultamientos@gnp.com.mx',
                      to='facultamiento@gnp.com.mx',
                      subject='Solicitud de Facultamiento',
                      reply_to='noreply@departamentales-gnp.com.mx',
                      html="""<table align='center' style='width: 100%; font-family: arial;'>
                                    <tr>
                                        <td colspan='3' style='border-bottom: solid 3px #00cec9' align='right'><img src='http://www.departamentales.gnp.com.mx/curso_virtual/img/logo-gnp.jpg'></td>
                                    </tr>
                                    <tr>
                                        <td><h4 style='color: #1f3f79; font-size: 16px;'><strong><span><img src='http://www.departamentales.gnp.com.mx/curso_virtual/img/maletin.png'></span> SOLICITUD DE FACULTAMIENTO</strong></h4></td>
                                    </tr>
                                    <tr align='center'>
                                        <td>
                                            <div style='background-color: #fff; margin: 10px; padding-right: 20px; padding-left: 20px; padding-bottom: 50px;'>
                                                <h3>Nueva solicitud.</h3>
                                                <p>Hay una nueva solicitud de FAE que requiere ser revisada..</p>
                                                <table>
                                                    <tr>
                                                        <td>Solicitante: <strong>"""+ solic +"""</strong></td>
                                                    </tr>
                                                    <tr>
                                                        <td>Ramo: <strong>"""+ data_ramo +"""</strong></td>
                                                    </tr>
                                                    <tr>
                                                        <td>Monto Solicitado: <strong>"""+ str(data_monto) +"""</strong></td>
                                                    </tr>
                                                    <tr>
                                                        <td>Beneficiario: <strong>"""+ data_benef +"""</strong></td>
                                                    </tr>
                                                </table>
                                                <br>
                                                <br>
                                                <a href='https://facultamiento-dot-gnp-infra-159601.appspot.com'>Ir a la solicitud</a>
                                            </div>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td></td>
                                    </tr>
                                    <tr>
                                        <td colspan='3' style='border-bottom: solid 3px #00cec9' align='right'></td>
                                    </tr>
                                </table>
                            """
                     ).Send()
#EMAIL PARA EL SOLICITANTE
def envioMailRechaz(id_facultamiento):
    db = conexion.connect_to_cloudsql()
    cursor = db.cursor()
    cursor.execute('SELECT reg_facultamientos.id_facultamiento, CONCAT(cat_usuarios.nombre," ",cat_usuarios.ap_pat," ",cat_usuarios.ap_mat) AS solicitante, cat_usuarios.email, cat_ramo.ramo, CONCAT(reg_facultamientos.nombre_benef," ",reg_facultamientos.ap_pat_benef," ",reg_facultamientos.ap_mat_benef) AS beneficiario, reg_facultamientos.monto_autorizado, estatus_facult.estatus FROM reg_facultamientos INNER JOIN cat_usuarios on cat_usuarios.id_usuario = reg_facultamientos.id_solicitante INNER JOIN cat_ramo ON reg_facultamientos.id_ramo=cat_ramo.id_ramo INNER JOIN estatus_facult ON reg_facultamientos.id_estatus=estatus_facult.id_estatus WHERE reg_facultamientos.id_facultamiento ='+id_facultamiento)
    data = cursor.fetchone()
    solic = data[1]
    email_solic = data[2]
    data_ramo = data[3]
    data_benef = data[4]
    data_monto = data[5]
    data_estatus = data[6]
    mail.EmailMessage(sender='facultamientos@gnp.com.mx',
                      to=email_solic,
                      subject='Solicitud de Facultamiento',
                      reply_to='noreply@departamentales-gnp.com.mx',
                      html="""<table align='center' style='width: 100%; font-family: arial;'>
                                    <tr>
                                        <td colspan='3' style='border-bottom: solid 3px #00cec9' align='right'><img src='http://www.departamentales.gnp.com.mx/curso_virtual/img/logo-gnp.jpg'></td>
                                    </tr>
                                    <tr>
                                        <td><h4 style='color: #1f3f79; font-size: 16px;'><strong><span><img src='http://www.departamentales.gnp.com.mx/curso_virtual/img/maletin.png'></span> SOLICITUD DE FACULTAMIENTO</strong></h4></td>
                                    </tr>
                                    <tr align='center'>
                                        <td>
                                            <div style='background-color: #fff; margin: 10px; padding-right: 20px; padding-left: 20px; padding-bottom: 50px;'>
                                                <h3>Solicitud Rechazada</h3>
                                                <div>
                                                    <img src='http://www.departamentales.gnp.com.mx/curso_virtual/img/cara_triste.png'>
                                                </div>
                                                <p>Tu solicitud ha sido rechazada por el funcionario.</p>
                                                <table>
                                                    <tr>
                                                        <td>Solicitante: <strong>""" + solic + """</strong></td>
                                                    </tr>
                                                    <tr>
                                                        <td>Ramo: <strong>"""+ data_ramo +"""</strong></td>
                                                    </tr>
                                                    <tr>
                                                        <td>Monto Solicitado: <strong>"""+ str(data_monto) +"""</strong></td>
                                                    </tr>
                                                    <tr>
                                                        <td>Beneficiario: <strong>"""+ data_benef +"""</strong></td>
                                                    </tr>
                                                </table>
                                                <br>
                                                <br>
                                                <a href='https://facultamiento-dot-gnp-infra-159601.appspot.com'>Ir a la solicitud</a>
                                            </div>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td></td>
                                    </tr>
                                    <tr>
                                        <td colspan='3' style='border-bottom: solid 3px #00cec9' align='right'></td>
                                    </tr>
                                </table>
                            """
                     ).Send()
#EMAIL FUNCIONARIO
def envioMailTermino(folio, ramo, linea_nego, solicitante, email_solic, monto_autorizado, benef):
    mail.EmailMessage(sender='facultamientos@gnp.com.mx',
                      to=email_solic,
                      subject='Solicitud de Facultamiento',
                      reply_to='noreply@departamentales-gnp.com.mx',
                      html="""<table align='center' style='width: 100%; font-family: arial;'>
                                    <tr>
                                        <td colspan='3' style='border-bottom: solid 3px #00cec9' align='right'><img src='http://www.departamentales.gnp.com.mx/curso_virtual/img/logo-gnp.jpg'></td>
                                    </tr>
                                    <tr>
                                        <td><h4 style='color: #1f3f79; font-size: 16px;'><strong><span><img src='http://www.departamentales.gnp.com.mx/curso_virtual/img/maletin.png'></span> SOLICITUD DE FACULTAMIENTO</strong></h4></td>
                                    </tr>
                                    <tr align='center'>
                                        <td>
                                            <div style='background-color: #fff; margin: 10px; padding-right: 20px; padding-left: 20px; padding-bottom: 50px;'>
                                                <h3>Solicitud Terminada</h3>
                                                <div>
                                                    <img src='http://www.departamentales.gnp.com.mx/curso_virtual/img/terminado.png'>
                                                </div>
                                                <h3>Folio de T&eacute;rmino:</h3>
                                                <h1>""" + folio + """</h1>
                                                <table>
                                                    <tr>
                                                        <td>Solicitante: <strong>"""+ solicitante +"""</strong></td>
                                                    </tr>
                                                    <tr>
                                                        <td>Ramo: <strong>""" + ramo + linea_nego +"""</strong></td>
                                                    </tr>
                                                    <tr>
                                                        <td>Monto Solicitado: <strong>"""+ str(monto_autorizado) +"""</strong></td>
                                                    </tr>
                                                    <tr>
                                                        <td>Beneficiario: <strong>"""+ benef +"""</strong></td>
                                                    </tr>
                                                </table>
                                                <br>
                                                <br>
                                                <a href='https://facultamiento-dot-gnp-infra-159601.appspot.com'>Ir a la solicitud</a>
                                            </div>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td></td>
                                    </tr>
                                    <tr>
                                        <td colspan='3' style='border-bottom: solid 3px #00cec9' align='right'></td>
                                    </tr>
                                </table>
                            """
                     ).Send()
def envioMailCancel(ramo, linea_nego, solicitante, email_solic, monto_autorizado, benef):
    mail.EmailMessage(sender='facultamientos@gnp.com.mx',
                      to=email_solic,
                      subject='Solicitud de Facultamiento',
                      reply_to='noreply@departamentales-gnp.com.mx',
                      html="""<table align='center' style='width: 100%; font-family: arial;'>
                                    <tr>
                                        <td colspan='3' style='border-bottom: solid 3px #00cec9' align='right'><img src='http://www.departamentales.gnp.com.mx/curso_virtual/img/logo-gnp.jpg'></td>
                                    </tr>
                                    <tr>
                                        <td><h4 style='color: #1f3f79; font-size: 16px;'><strong><span><img src='http://www.departamentales.gnp.com.mx/curso_virtual/img/maletin.png'></span> SOLICITUD DE FACULTAMIENTO</strong></h4></td>
                                    </tr>
                                    <tr align='center'>
                                        <td>
                                            <div style='background-color: #fff; margin: 10px; padding-right: 20px; padding-left: 20px; padding-bottom: 50px;'>
                                                <h3>Solicitud Rechazada</h3>
                                                <div>
                                                    <img src='http://www.departamentales.gnp.com.mx/curso_virtual/img/cancel.png'>
                                                </div>
                                                <h3>Su solicitud ha sido rechazada por el area de FACULTAMIENTO</h3>
                                                <table>
                                                    <tr>
                                                        <td>Solicitante: <strong>"""+ solicitante +"""</strong></td>
                                                    </tr>
                                                    <tr>
                                                        <td>Ramo: <strong>"""+ ramo + linea_nego +"""</strong></td>
                                                    </tr>
                                                    <tr>
                                                        <td>Monto Solicitado: <strong>"""+ str(monto_autorizado) +"""</strong></td>
                                                    </tr>
                                                    <tr>
                                                        <td>Beneficiario: <strong>"""+ benef +"""</strong></td>
                                                    </tr>
                                                </table>
                                                <br>
                                                <br>
                                                <a href='https://facultamiento-dot-gnp-infra-159601.appspot.com'>Ir a la solicitud</a>
                                            </div>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td></td>
                                    </tr>
                                    <tr>
                                        <td colspan='3' style='border-bottom: solid 3px #00cec9' align='right'></td>
                                    </tr>
                                </table>
                            """
                     ).Send()
def envioMailCancelFAE(email_solic,email_func_vb,folio_termino, ramo, linea_nego, monto,benef):
    mail.EmailMessage(sender='facultamientos@gnp.com.mx',
                      to=email_solic,
                      subject='Solicitud de Facultamiento',
                      reply_to='noreply@departamentales-gnp.com.mx',
                      html="""<table align='center' style='width: 100%; font-family: arial;'>
                                    <tr>
                                        <td colspan='3' style='border-bottom: solid 3px #00cec9' align='right'><img src='http://www.departamentales.gnp.com.mx/curso_virtual/img/logo-gnp.jpg'></td>
                                    </tr>
                                    <tr>
                                        <td><h4 style='color: #1f3f79; font-size: 16px;'><strong><span><img src='http://www.departamentales.gnp.com.mx/curso_virtual/img/maletin.png'></span> SOLICITUD DE FACULTAMIENTO</strong></h4></td>
                                    </tr>
                                    <tr align='center'>
                                        <td>
                                            <div style='background-color: #fff; margin: 10px; padding-right: 20px; padding-left: 20px; padding-bottom: 50px;'>
                                                <h3>Folio Cancelado</h3>
                                                <div>
                                                    <img src='http://www.departamentales.gnp.com.mx/curso_virtual/img/cancel.png'>
                                                </div>
                                                <h3>Se ha cancelado la solicitud de FAE con el folio de autorizaci&oacute;n:</h3>
                                                <h1>""" + folio_termino + """</h1>
                                                <table>
                                                    <tr>
                                                        <td>Solicitante: <strong>"""+ email_solic +"""</strong></td>
                                                    </tr>
                                                    <tr>
                                                        <td>Ramo: <strong>""" + ramo + """ """ + linea_nego +"""</strong></td>
                                                    </tr>
                                                    <tr>
                                                        <td>Monto Solicitado: <strong>"""+ str(monto) +"""</strong></td>
                                                    </tr>
                                                    <tr>
                                                        <td>Beneficiario: <strong>"""+ benef +"""</strong></td>
                                                    </tr>
                                                </table>
                                                <br>
                                                <br>
                                                <a href='https://facultamiento-dot-gnp-infra-159601.appspot.com'>Ir a la solicitud</a>
                                            </div>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td></td>
                                    </tr>
                                    <tr>
                                        <td colspan='3' style='border-bottom: solid 3px #00cec9' align='right'></td>
                                    </tr>
                                </table>
                            """
                     ).Send()
    mail.EmailMessage(sender='facultamientos@gnp.com.mx',
                      to= email_func_vb,
                      subject='Solicitud de Facultamiento',
                      reply_to='noreply@departamentales-gnp.com.mx',
                      html="""<table align='center' style='width: 100%; font-family: arial;'>
                                    <tr>
                                        <td colspan='3' style='border-bottom: solid 3px #00cec9' align='right'><img src='http://www.departamentales.gnp.com.mx/curso_virtual/img/logo-gnp.jpg'></td>
                                    </tr>
                                    <tr>
                                        <td><h4 style='color: #1f3f79; font-size: 16px;'><strong><span><img src='http://www.departamentales.gnp.com.mx/curso_virtual/img/maletin.png'></span> SOLICITUD DE FACULTAMIENTO</strong></h4></td>
                                    </tr>
                                    <tr align='center'>
                                        <td>
                                            <div style='background-color: #fff; margin: 10px; padding-right: 20px; padding-left: 20px; padding-bottom: 50px;'>
                                                <h3>Folio Cancelado</h3>
                                                <div>
                                                    <img src='http://www.departamentales.gnp.com.mx/curso_virtual/img/cancel.png'>
                                                </div>
                                                <h3>Se ha cancelado la solicitud de FAE con el folio de autorizaci&oacute;n:</h3>
                                                <h1>""" + folio_termino + """</h1>
                                                <table>
                                                    <tr>
                                                        <td>Solicitante: <strong>"""+ email_solic +"""</strong></td>
                                                    </tr>
                                                    <tr>
                                                        <td>Ramo: <strong>""" + ramo + linea_nego +"""</strong></td>
                                                    </tr>
                                                    <tr>
                                                        <td>Monto Solicitado: <strong>"""+ str(monto) +"""</strong></td>
                                                    </tr>
                                                    <tr>
                                                        <td>Beneficiario: <strong>"""+ benef +"""</strong></td>
                                                    </tr>
                                                </table>
                                                <br>
                                                <br>
                                                <a href='https://facultamiento-dot-gnp-infra-159601.appspot.com'>Ir a la solicitud</a>
                                            </div>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td></td>
                                    </tr>
                                    <tr>
                                        <td colspan='3' style='border-bottom: solid 3px #00cec9' align='right'></td>
                                    </tr>
                                </table>
                            """
                     ).Send()