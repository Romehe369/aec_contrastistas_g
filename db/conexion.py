import mysql.connector
import datetime

class Registro_datos():

    def __init__(self):
        self.conexion = mysql.connector.connect( host='localhost',
                                            database ='base_datos', 
                                            user = 'root',
                                            password ='')
    def busca_users(self, users):
        cur = self.conexion.cursor()
        sql = "SELECT * FROM login_datos WHERE Users = {}".format(users)
        cur.execute(sql)
        usersx = cur.fetchall()
        cur.close()     
        return usersx 

    def busca_password(self, password):
        cur = self.conexion.cursor()
        sql = "SELECT * FROM login_datos WHERE Password = {}".format(password)
        cur.execute(sql)
        passwordx = cur.fetchall()
        cur.close()     
        return passwordx

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

    # Modifcar los datos de trabajador

    def insertar_trabajador(self,dni, nombres, apellidos, sexo, fecha_inicio,correo,nro_celular,categoria,foto):
        fechain=fecha_inicio.split("/")       
        fecha_inicio=datetime.date(int(fechain[2]), int(fechain[1]), int(fechain[0]))
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