import mysql.connector
import datetime

class Registro_datos():

    def __init__(self):
        self.conexion = mysql.connector.connect( host='localhost',
                                            database ='base_datos', 
                                            user = 'root',
                                            password ='')
    ################### login data ########################
    def elimina_admin(self,users):
        # Indica que se genero un error o no existe dicho ussers
        a=0
        try:
            cur = self.conexion.cursor()
            sql = "DELETE FROM login_datos WHERE users = %s"
            cur.execute(sql,(users,))
            a = cur.rowcount
            self.conexion.commit()    
        except Exception as e:
            a=0
        finally:
            cur.close() 
            return a

    def add_admin(self,users, password):
        mensaje=""
        try:
            cur = self.conexion.cursor()
            sql='''INSERT INTO login_datos (USERS, PASSWORD) 
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
        sql = "SELECT * FROM login_datos WHERE Users = {}".format(users)
        cur.execute(sql)
        usersx = cur.fetchone()
        cur.close()     
        return usersx 

    def busca_password(self, password):
        cur = self.conexion.cursor()
        sql = "SELECT * FROM login_datos WHERE Password = {}".format(password)
        cur.execute(sql)
        passwordx = cur.fetchall()
        cur.close()     
        return passwordx
    
    # Se cambia la contraseña del usuario
    def actualiza_password(self, users, password):
        cur = self.conexion.cursor()
        sql ='''UPDATE login_datos SET Password = '{}'
        WHERE USERS = '{}' '''.format(password,users)
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
    def insertar_project(self,code_project, name, responsible, region, province,district,start_project,end_project,reference):
        start_project=self.convert_date(start_project)
        end_project=self.convert_date(end_project)
        cur = self.conexion.cursor()
        sql= '''INSERT INTO tproject (code_project, name, responsible, region, province,district,start_project,end_project,reference) 
        VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
        # Convert data into tuple format
        insert_blob_tuple = (code_project, name, responsible, region, province,district,start_project,end_project,reference)
        cur.execute(sql,insert_blob_tuple)
        self.conexion.commit()    
        cur.close()

    def show_tproject(self):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM tproject" 
        cursor.execute(sql)
        registro = cursor.fetchall()
        return registro

    # Manejar datos of region
    
    def get_region(self):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM ubigeo_peru_departments" 
        cursor.execute(sql)
        name_region = cursor.fetchall()
        return name_region
    
    def get_provinces(self,department_id):
        cur = self.conexion.cursor()
        sql = "SELECT * FROM ubigeo_peru_provinces WHERE department_id = {}".format(department_id)
        cur.execute(sql)
        name_provinces = cur.fetchall()
        cur.close()     
        return name_provinces
    
    def get_districts(self,province_id):
        cur = self.conexion.cursor()
        sql = "SELECT * FROM ubigeo_peru_districts WHERE province_id = {}".format(province_id)
        cur.execute(sql)
        name_districts = cur.fetchall()
        cur.close()     
        return name_districts