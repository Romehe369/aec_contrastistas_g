import mysql.connector
import datetime
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
#from controllers.change_password import Dialogo

class Registro_datos():

    def __init__(self):
        try:
            self.conexion = mysql.connector.connect( host='localhost',database ='db_aeccontratistas', 
                                            user = 'root',
                                            password ='')
            self.mensaje=Dialogo()
        except Exception as e:
            return None
        
    ################### login data ########################
    def elimina_admin(self,users):
        # Indica que se genero un error o no existe dicho ussers
        eliminado=True
        try:
            cur = self.conexion.cursor()
            sql = "DELETE FROM tlogin_data WHERE users = %s"
            cur.execute(sql,(users,))
            cur.rowcount
            self.conexion.commit()    
        except Exception as e:
            eliminado=False
        finally:
            cur.close() 
            return eliminado

    def add_admin(self,users, password):
        agregado=True
        try:
            cur = self.conexion.cursor()
            sql='''INSERT INTO tlogin_data (id,users, password) 
            VALUES(DEFAULT,'{}', '{}')'''.format(users, password)
            cur.execute(sql)
            self.conexion.commit() 
        except Exception as e:
            agregado=False
        finally:
            cur.close()
            return agregado

    def busca_users(self, users):
        try:
            cur = self.conexion.cursor()
            sql = "SELECT * FROM tlogin_data WHERE users = '{}'".format(users)
            cur.execute(sql)
            encontrado = cur.fetchone()
            cur.close()    
        except Exception as e:
            encontrado=[]
        finally:
            return encontrado 
    
    # Se cambia la contraseña del usuario
    def actualiza_password(self, users, password):
        update=True
        try:
            cur = self.conexion.cursor()
            sql ='''UPDATE tlogin_data SET id=DEFAULT password = '{}'
            WHERE users = '{}' '''.format(password,users)
            cur.execute(sql)
            a = cur.rowcount
            # Se guarde y persista simpre
            self.conexion.commit()    
            cur.close()
        except Exception as e:
            update=False
        finally:
            return update
    ################################### date ######################
    def convert_date(self,date_str):
        # Falta modificar para no presentar errores, con la funcion datetime
        date_str= date_str.split("/")       
        date_str=datetime.date(int(date_str[2]), int(date_str[1]), int(date_str[0]))
        return date_str
    # Modifcar los datos de trabajador
    def insertar_trabajador(self,dni, nombres, apellidos, sexo, fecha_inicio,correo,nro_celular,categoria,sueldo_diario,foto):    
        fecha_inicio=self.convert_date(fecha_inicio)
        cur = self.conexion.cursor()
        sql= '''INSERT INTO ttrabajador (DNI, NOMBRES, APELLIDOS, SEXO, FECHA_INICIO,CORREO,NRO_CELULAR,CATEGORIA,SUELDO_DIARIO,FOTO) 
        VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
        # Convert data into tuple format
        insert_blob_tuple = (dni, nombres, apellidos, sexo, fecha_inicio,correo,nro_celular,categoria,sueldo_diario,foto)
        cur.execute(sql,insert_blob_tuple)
        self.conexion.commit()    
        cur.close()
    def phrases_similares(self,sql,param):
        try:
            cur = self.conexion.cursor()
            cur.execute(sql,("%" + param + "%",))
            results = cur.fetchall()
            cur.close()
        except Exception as e:
            results=None
        finally:
            return results
        

    def mostrar_trabajador(self):
        cur = self.conexion.cursor()
        sql = "SELECT * FROM ttrabajador" 
        cur.execute(sql)
        registro = cur.fetchall()
        cur.close()
        return registro

    # 60 seconds or more 2 minutes
    def buscar_trabajador(self, dni):
        try:
            cur = self.conexion.cursor()
            sql = "SELECT * FROM ttrabajador WHERE DNI = {}".format(dni)
            cur.execute(sql)
            # Solo obtiene un solo registro
            trabajador = cur.fetchone()
            cur.close()
        # Se ejecuta cuando se comete un error o no existe dicho valor     
        except Exception as e:
            trabajador=None
        finally:
            return trabajador # siempre se ejecuta

    def elimina_trabajador(self,dni):
        cur = self.conexion.cursor()
        sql='''DELETE FROM ttrabajador WHERE DNI = {}'''.format(dni)
        cur.execute(sql)
        a = cur.rowcount
        self.conexion.commit()    
        cur.close()
        return a   

    def actualiza_trabajador(self, dni, nombre, apellidos, sexo, fecha_inicio,correo,nro_celular,categoria,foto):
        cur = self.conexion.cursor()
        sql ='''UPDATE ttrabajador SET  NOMBRE ='{}', APELLIDOS ='{}', SEXO ='{}', FECHA_INICIO ='{}',CORREO ='{}',NRO_CELULAR ='{}',CATEGORIA ='{}',FOTO ='{}'
        WHERE DNI = '{}' '''.format(nombre, apellidos, sexo, fecha_inicio,correo,nro_celular,categoria,foto,dni)
        cur.execute(sql)
        a = cur.rowcount
        self.conexion.commit()    
        cur.close()
        return a  

    ########################## insert project ###################
    def insertar_project(self,code_project, name, dni_responsable, region, province,district,start_project,end_project,reference):
        start_project=self.convert_date(start_project)
        end_project=self.convert_date(end_project)
        cur = self.conexion.cursor()
        sql= '''INSERT INTO tproject (code_project, name, dni_responsable, region, province,district,start_project,end_project,reference) 
        VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
        # Convert data into tuple format
        insert_blob_tuple = (code_project, name, dni_responsable, region, province,district,start_project,end_project,reference)
        cur.execute(sql,insert_blob_tuple)
        self.conexion.commit()    
        cur.close()

    def show_tproject(self):
        cur = self.conexion.cursor()
        sql = "SELECT * FROM tproject" 
        cur.execute(sql)
        registro = cur.fetchall()
        cur.close()
        return registro

    def delete_project_bcode(self,code_project):
        # inidca si se ha elimiando empieza en verdadero
        eliminado=True
        try:
            cur = self.conexion.cursor()
            sql = "DELETE FROM tproject WHERE code_project = %s"
            cur.execute(sql,(code_project,))
            cur.rowcount
            self.conexion.commit()    
        except Exception as e:
            # Si no se logro elimianar
            eliminado=False
        finally:
            cur.close() 
            return eliminado
    ###################################### DISTRIBUCION ##########################
    def add_distribution_presence(self, id_distribucion,code_project,dni,estado):
        agregado=False
        try:
            cur = self.conexion.cursor()
            sql='''INSERT INTO ttrabajador_distribucion (id_distribucion,code_project,dni,estado) 
            VALUES('{}', '{}','{}', '{}')'''.format(id_distribucion,code_project,dni,estado)
            cur.execute(sql)
            agregado=True
            self.conexion.commit() 
            cur.close()
        except Exception as e:
            agregado=False
        finally:
            return agregado
    ###################################### ASISTENCIA ################################
    def list_tasistencia(self, code_project):
        try:
            cur = self.conexion.cursor()
            sql = "SELECT * FROM ttrabajador_distribucion WHERE code_project = '{}'".format(code_project)
            cur.execute(sql)
            # Se obtiene todos los relacionados
            registro = cur.fetchall()
            cur.close() 
        # Se ejecuta cuando se comete un error     
        except Exception as e:
            registro=[]
        finally:
            return registro
    def add_presence(self,date_month,id_distribucion,code_project, dni, asistencia, observacion, justificacion):
        date_month=self.convert_date(date_month)
        agregado=False
        try:
            cur = self.conexion.cursor()
            sql='''INSERT INTO tasistencia (id,date_month, id_distribucion,code_project, dni, asistencia, observacion, justificacion) 
            VALUES(DEFAULT,'{}', '{}','{}', '{}','{}', '{}','{}')'''.format(date_month, id_distribucion,code_project, dni, asistencia, observacion, justificacion)
            cur.execute(sql)
            agregado=True
            self.conexion.commit() 
            cur.close()
        except Exception as e:
            print(e)
            agregado=False
        finally:
            return agregado
        
    ###################################### UBICACION #################################
    # Manejar datos of region
    def get_region(self):
        cur = self.conexion.cursor()
        sql = "SELECT * FROM tdepartments" 
        cur.execute(sql)
        name_region = cur.fetchall()
        cur.close()
        return name_region
    
    def get_provinces(self,department_id):
        cur = self.conexion.cursor()
        sql = "SELECT * FROM tprovinces WHERE department_id = {}".format(department_id)
        cur.execute(sql)
        name_provinces = cur.fetchall()
        cur.close()     
        return name_provinces
    
    def get_districts(self,province_id):
        cur = self.conexion.cursor()
        sql = "SELECT * FROM tdistricts WHERE province_id = {}".format(province_id)
        cur.execute(sql)
        name_districts = cur.fetchall()
        cur.close()     
        return name_districts

#variable=Registro_datos()
#variable.phrases_similares()