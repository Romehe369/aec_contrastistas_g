import mysql.connector
import datetime

class Registro_datos():

    def __init__(self):
        try:
            self.conexion = mysql.connector.connect( host='localhost',database ='db_aeccontratistas', 
                                            user = 'root',
                                            password ='')
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
        mensaje=""
        try:
            cur = self.conexion.cursor()
            sql='''INSERT INTO tlogin_data (users, password) 
            VALUES('{}', '{}')'''.format(users, password)
            cur.execute(sql)
            self.conexion.commit() 
        except Exception as e:
            mensaje=e
        finally:
            cur.close()
            return mensaje

    def busca_users(self, users):
        cur = self.conexion.cursor()
        sql = "SELECT * FROM tlogin_data WHERE users = '{}'".format(users)
        cur.execute(sql)
        usersx = cur.fetchone()
        cur.close()     
        return usersx 

    def busca_password(self, password):
        cur = self.conexion.cursor()
        sql = "SELECT * FROM tlogin_data WHERE password = {}".format(password)
        cur.execute(sql)
        passwordx = cur.fetchall()
        cur.close()     
        return passwordx
    
    # Se cambia la contraseña del usuario
    def actualiza_password(self, users, password):
        cur = self.conexion.cursor()
        sql ='''UPDATE tlogin_data SET password = '{}'
        WHERE users = '{}' '''.format(password,users)
        cur.execute(sql)
        a = cur.rowcount
        # Se guarde y persista simpre
        self.conexion.commit()    
        cur.close()
        return a   
    ################################### date ######################
    def convert_date(self,date_str):
        # Falta modificar para no presentar errores, con la funcion datetime
        date_str= date_str.split("/")       
        date_str=datetime.date(int(date_str[2]), int(date_str[1]), int(date_str[0]))
        return date_str
    # Modifcar los datos de trabajador
    def insertar_trabajador(self,dni, nombres, apellidos, sexo, fecha_inicio,correo,nro_celular,categoria,foto):    
        fecha_inicio=self.convert_date(fecha_inicio)
        cur = self.conexion.cursor()
        sql= '''INSERT INTO ttrabajador (DNI, NOMBRES, APELLIDOS, SEXO, FECHA_INICIO,CORREO,NRO_CELULAR,CATEGORIA,FOTO) 
        VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
        # Convert data into tuple format
        insert_blob_tuple = (dni, nombres, apellidos, sexo, fecha_inicio,correo,nro_celular,categoria,foto)
        cur.execute(sql,insert_blob_tuple)
        self.conexion.commit()    
        cur.close()

    def mostrar_trabajador(self):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM ttrabajador" 
        cursor.execute(sql)
        registro = cursor.fetchall()
        cursor.close()
        return registro

    # 60 seconds or more 2 minutes
    def buscar_trabajador(self, dni):
        dnix=0
        try:
            cur = self.conexion.cursor()
            sql = "SELECT * FROM ttrabajador WHERE DNI = {}".format(dni)
            cur.execute(sql)
            # Solo obtiene un solo registro
            dnix = cur.fetchone()
            cur.close()
        # Se ejecuta cuando se comete un error     
        except Exception as e:
            dnix=-1
        return dnix # siempre se ejecuta
        

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
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM tproject" 
        cursor.execute(sql)
        registro = cursor.fetchall()
        cursor.close()
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

    # Manejar datos of region
    def get_region(self):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM tdepartments" 
        cursor.execute(sql)
        name_region = cursor.fetchall()
        cursor.close()
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