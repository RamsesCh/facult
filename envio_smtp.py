import smtplib
import email.message
import MySQLdb
import conexion

#CREDENCIALES DE ACCESO
server = smtplib.SMTP('smtp.gmail.com','587')
user = 'jose.chavarria@gnp.com.mx'
password = "Oct.2018"



def envio_mail2(id_facult_last,email_solicitante,id_ramo,id_func_vb,monto_autorizado,nombre_benef,ap_pat_benef,ap_mat_benef):
    db = conexion.connect_to_cloudsql()
    cursor = db.cursor()
    cursor.execute('SELECT CONCAT(cat_usuarios.nombre," ",cat_usuarios.ap_pat, " ", cat_usuarios.ap_mat) AS funcionario, cat_usuarios.email, cat_ramo.ramo FROM cat_usuarios, cat_ramo WHERE cat_usuarios.id_usuario = %s AND cat_ramo.id_ramo = %s',(int(id_func_vb), int(id_ramo)))
    data = cursor.fetchone()
    nombre_func= data[0]
    mail_func= data[1]
    nombre_ramo = data[2]
    db.close()
    benef = nombre_benef + ' ' + ap_pat_benef + ' ' + ap_mat_benef
    
    email_content = """
    <table align='center' style='width: 100%; font-family: arial;'>
        <tr>
            <td colspan='3' style='border-bottom: solid 3px #00cec9' align='right'><img src='http://www.departamentales.gnp.com.mx/curso_virtual/img/logo-gnp.jpg'></td>
        </tr>
        <tr>
            <td><h4 style='color: #1f3f79; font-size: 16px;'><strong><span><img src='http://www.departamentales.gnp.com.mx/curso_virtual/img/maletin.png'></span> SOLICITUD DE FACULTAMIENTO</strong></h4></td>
        </tr>
        <tr align='center'>
            <td>
                <div style='background-color: #fff; margin: 10px; padding-right: 20px; padding-left: 20px; padding-bottom: 50px;'>
                    <h3>Solicitud Registrada</h3>
                    <p>Tu solicitud ha sido registrada con &eacute;xito. Enviamos un correo electr&oacute;nico al funcionario <span style='font-weight: bold; text-transform: capitalize;'>"""+ nombre_func +"""</span> para solicitar su Visto Bueno.</p>
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

    #INICIALIZAR EL OBJETO MAIL
    msg = email.message.Message()
    #PARAMETROS DEL MAIL
    msg['Subject'] = 'Solicitud de Facultamiento'
    msg['From'] = 'facultamientos@gnp.com.mx'
    msg['To'] = email_solicitante
    #TEXTO DEL MAIL A HTML
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(email_content)
    #INICIALIZAR EL SERVER
    server.starttls()
    server.ehlo

    # LOGIN CON LAS CREDENCIALES
    server.login(user, password)

    # SEND MAIL
    server.sendmail(msg['From'], [msg['To']], msg.as_string())
    server.quit()