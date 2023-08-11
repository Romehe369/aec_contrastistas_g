import mysql.connector
from datetime import date, datetime, timedelta
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
    def add_admin(self,dni,users, password):
        agregado=True
        try:
            cur = self.conexion.cursor()
            sql="""INSERT INTO tlogin_data (dni,users, password) VALUES (%s, %s,%s)"""
            val=(dni,users,password)
            cur.execute(sql,val)
            self.conexion.commit() 
        except Exception as e:
            agregado=False
        finally:
            cur.close()
        return agregado
    def elimina_admin(self,users):
        # Indica que se genero un error o no existe dicho ussers
        eliminado=True
        try:
            cur = self.conexion.cursor()
            sql = """DELETE FROM tlogin_data WHERE users = %s"""
            val= (users,)
            cur.execute(sql,val)
            cur.rowcount
            self.conexion.commit()    
        except Exception as e:
            eliminado=False
        finally:
            cur.close() 
        return eliminado

    def busca_users(self, users):
        try:
            cur = self.conexion.cursor()
            sql = """SELECT * FROM tlogin_data WHERE users = %s"""
            val=(users,)
            cur.execute(sql,val)
            encontrado = cur.fetchone()
        except Exception as e:
            encontrado=None
        finally:
            cur.close()
        return encontrado

    def showfull_admin(self):
        try:
            cur = self.conexion.cursor()
            sql = """SELECT dni,users,password FROM tlogin_data"""
            cur.execute(sql)
            table_admin = cur.fetchall()
        except Exception as e:
            table_admin=[]
        finally:
            cur.close()
        return table_admin

    # Se cambia la contraseña del usuario
    def actualiza_password(self,id,password):
        update=True
        try:
            cur = self.conexion.cursor()
            sql="""UPDATE tlogin_data SET password=%s  WHERE id = %s"""
            val = (password,id)
            cur.execute(sql,val)
            a = cur.rowcount
            # Se guarde y persista simpre
            self.conexion.commit()    
            cur.close()
        except Exception as e:
            update=False
        finally:
            return update
    ################### login data #######################
    ################################### date ######################
    def convert_date(self,date_str):
        # Falta modificar para no presentar errores, con la funcion datetime
        date_str= date_str.split("/")       
        date_str=date(int(date_str[2]), int(date_str[1]), int(date_str[0]))
        return date_str
    # Modifcar los datos de trabajador
    def insertar_trabajador(self,dni, nombres, apellidos, sexo, fecha_inicio,correo,nro_celular,categoria,sueldo_diario,foto):
        fecha_inicio=self.convert_date(fecha_inicio)
        cur = self.conexion.cursor()
        sql= """INSERT INTO ttrabajador (DNI, NOMBRES, APELLIDOS, SEXO, FECHA_INICIO,CORREO,NRO_CELULAR,CATEGORIA,SUELDO_DIARIO,FOTO) 
        VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
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

    def show_all_dni(self):
        try:
            cur = self.conexion.cursor()
            sql = "SELECT dni,nombres,apellidos,categoria,sueldo_diario FROM ttrabajador"
            cur.execute(sql)
            table_trabajador = cur.fetchall()
        # Se ejecuta cuando se comete un error     
        except Exception as e:
            table_trabajador=[]
        finally:
            cur.close()
        return table_trabajador

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
    ###################################### DISTRIBUCION  ASISTENCIA##########################
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
    ###################################### ASISTENCIA ################################
    def add_presence(self,date_month,id_distribucion,code_project, dni, asistencia, observacion, justificacion):
        agregado=True
        date_month=self.convert_date(date_month)
        try:
            cur = self.conexion.cursor()
            sql= """INSERT INTO tasistencia(date_month, id_distribucion,code_project, dni, asistencia, observacion, justificacion) 
            VALUES(%s,%s,%s,%s,%s,%s,%s)"""
            # Convert data into tuple format
            val = (date_month, id_distribucion,code_project, dni, asistencia, observacion, justificacion)
            cur.execute(sql,val)
            self.conexion.commit() 
        except Exception as e:
            agregado=False
        finally:
            cur.close()
        return agregado

    def show_all_data(self,date_month):
        date_month=self.convert_date(date_month)
        try:
            cur = self.conexion.cursor()
            sql = "SELECT code_project,dni,asistencia FROM tasistencia WHERE date_month = '{}'".format(date_month)
            cur.execute(sql)
            asistencia = cur.fetchall()
        # Se ejecuta cuando se comete un error     
        except Exception as e:
            asistencia=[]
        finally:
            cur.close()
        return asistencia

    def delete_asistence(self,id):
        cont_row=0
        try:
            cur = self.conexion.cursor()
            sql = "DELETE FROM tasistencia WHERE id = %s"
            val=(id,)
            cur.execute(sql,val)
            cont_row=cur.rowcount
            self.conexion.commit()    
        except Exception as e:
            # Si no se logro elimianar
            cont_row=0
        finally:
            cur.close() 
        return cont_row
    ##################################### ADD FACTURA ################################
    def add_factura(self,cod_factura, date_filed, date_issue, payment_date, document_type, document_number, payment_method, check_number, rotated_to, type_expenditure, cost_center, amount, expense_made, igv, observation):
        agregado=True
        date_filed=self.convert_date(date_filed)
        date_issue=self.convert_date(date_issue)
        try:
            cur = self.conexion.cursor()
            sql= """INSERT INTO tfactura(cod_factura, date_filed, date_issue, payment_date, document_type, document_number, payment_method, check_number, rotated_to, type_expenditure, cost_center, amount, expense_made, igv, observation) 
            VALUES(%s,%s,%s,%s,%s,%s,%s)"""
            val = (cod_factura, date_filed, date_issue, payment_date, document_type, document_number, payment_method, check_number, rotated_to, type_expenditure, cost_center, amount, expense_made, igv, observation)
            cur.execute(sql,val)
            self.conexion.commit() 
        except Exception as e:
            agregado=False
        finally:
            cur.close()
        return agregado
    ##################################### END FACTURA ################################
    ##################################### ADD MATERIAL ################################
    def add_material(self,code_material, cod_factura, material, guia_de_remision, cantidad, precio_unitario, precio_total):
        agregado=True
        try:
            cur = self.conexion.cursor()
            sql= """INSERT INTO tmaterial(code_material, cod_factura, material, guia_de_remision, cantidad, precio_unitario, precio_total) 
            VALUES(%s,%s,%s,%s,%s,%s,%s)"""
            val = (code_material, cod_factura, material, guia_de_remision, cantidad, precio_unitario, precio_total)
            cur.execute(sql,val)
            self.conexion.commit() 
        except Exception as e:
            agregado=False
        finally:
            cur.close()
        return agregado
    ##################################### END MATERIAL ################################

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
    #######################################END UBICACION########################
    def update_password(self):
        id=8
        dni="76213933"
        users="ronald3"
        password="admin199"
        update=True
        try:
            cur = self.conexion.cursor()
            sql="""UPDATE tlogin_data SET dni=%s, users=%s, password=%s  WHERE id = %s"""
            val = (dni,users,password,id)
            cur.execute(sql,val)
            a = cur.rowcount
            # Se guarde y persista simpre
            self.conexion.commit()    
        except Exception as e:
            update=False
        finally:
            cur.close()
        return update

    def delete_dispresence(self,id_distribucion):
        eliminado=True
        try:
            cur = self.conexion.cursor()
            sql = "DELETE FROM ttrabajador_distribucion WHERE id_distribucion = %s"
            val=(id_distribucion,)
            cur.execute(sql,val)
            cur.rowcount
            self.conexion.commit()    
        except Exception as e:
            # Si no se logro elimianar
            eliminado=False
        finally:
            cur.close() 
        return eliminado

    def update_dispresence(self,id_distribucion,estado):
        eliminado=True
        try:
            cur = self.conexion.cursor()
            sql="""UPDATE ttrabajador_distribucion SET estado=%s  WHERE id_distribucion = %s"""
            val = (estado,id_distribucion,)
            cur.execute(sql,val)
            eliminado=cur.rowcount
            self.conexion.commit()    
        except Exception as e:
            # Si no se logro elimianar
            eliminado=False
        finally:
            cur.close() 
        return eliminado

    def group_by(self,this):
        eliminado=True
        try:
            cur = self.conexion.cursor()
            sql="""UPDATE ttrabajador_distribucion SET estado=%s  WHERE id_distribucion = %s"""
            val = (estado,id_distribucion,)
            cur.execute(sql,val)
            eliminado=cur.rowcount
            self.conexion.commit()    
        except Exception as e:
            # Si no se logro elimianar
            eliminado=False
        finally:
            cur.close() 
        return eliminado
    def consultar(self):
        find = "SELECT  department,sum(strength) from college_data GROUP BY(department) HAVING sum(strength)<=400 ";

    def group_by_dni(self):
        try:
            cur = self.conexion.cursor()
            # Consulta para obtener la cantidad de países únicos
            query="""
            SELECT dni 
            FROM ttrabajador_distribucion 
            GROUP BY dni
            ORDER BY dni DESC;
            """
            cur.execute(query)
            # Obtener el resultado
            result = cur.fetchall()
            total_paises = result
        except Exception as e:
            # Si no se logro elimianar
            eliminado=False
        finally:
            cur.close() 
        return eliminado

    # Condicion AND  fetchone = None y fetchall = []
    def datemonth_and_dni(self,date_month,dni):
        date_month=self.convert_date(date_month)
        result=[]
        try:
            cur = self.conexion.cursor()
            # Consulta para obetener dos datos
            query="""
            SELECT * FROM tasistencia
            WHERE date_month = %s AND dni = %s ;
            """
            val=(date_month,dni,)
            cur.execute(query,val)
            # Obtener el resultado
            result = cur.fetchall()
        except Exception as e:
            # Si no se logro elimianar
            result=[]
        finally:
            cur.close() 
        return result

    def count_and_dni(self,date_month,dni):
        result=[]
        try:
            cur = self.conexion.cursor()
            # Consulta para obetener dos datos
            query="""
            SELECT COUNT(dni)
            FROM tasistencia
            WHERE date_month = %s AND dni = %s ;
            """
            val=(date_month,dni,)
            cur.execute(query,val)
            # Obtener el resultado
            result = cur.fetchone()
        except Exception as e:
            # Si no se logro elimianar
            result=[]
        finally:
            cur.close() 
        return result
        
    def between_month(self,date_start,date_end,dni):
        #date_start=self.convert_date(date_start)
        #date_end=self.convert_date(date_end)
        result=[]
        try:
            cur = self.conexion.cursor()
            # Consulta para obetener dos datos
            query="""
            SELECT COUNT(dni)
            FROM tasistencia
            WHERE (date_month BETWEEN %s AND %s) AND dni = %s;
            """
            val=(date_start,date_end,dni,)
            cur.execute(query,val)
            # Obtener el resultado
            result = cur.fetchall()
        except Exception as e:
            # Si no se logro elimianar
            result=[]
        finally:
            cur.close() 
        return result
    ################################ INSERT OPTIONS #############################
    def set_option(self,document_type, rotated_to, payment_method, cost_center, expense_made, type_expenditure):
        agregado=True
        try:
            cur = self.conexion.cursor()
            sql= """INSERT INTO topcion (document_type, rotated_to, payment_method, cost_center, expense_made, type_expenditure) 
            VALUES(%s,%s,%s,%s,%s,%s)"""
            val = (document_type, rotated_to, payment_method, cost_center, expense_made, type_expenditure,)
            cur.execute(sql,val)
            self.conexion.commit() 
        except Exception as e:
            agregado=False
        finally:
            cur.close()
        return agregado

    def get_option(self):
        try:
            cur = self.conexion.cursor()
            sql = """SELECT * FROM topcion"""
            cur.execute(sql)
            asistencia = cur.fetchall()
        # Se ejecuta cuando se comete un error     
        except Exception as e:
            asistencia=[]
        finally:
            cur.close()
        return asistencia

    def update_option(self,id,document_type, rotated_to, payment_method, cost_center, expense_made, type_expenditure):
        update=True
        try:
            cur = self.conexion.cursor()
            sql="""
            UPDATE topcion 
            SET document_type = %s, rotated_to = %s, payment_method = %s, cost_center = %s, expense_made = %s, type_expenditure = %s  
            WHERE id = %s"""
            val = (document_type, rotated_to, payment_method, cost_center, expense_made, type_expenditure,id,)
            cur.execute(sql,val)
            a = cur.rowcount
            # Se guarde y persista simpre
            self.conexion.commit()  
        except Exception as e:
            update=False
        finally:
            cur.close()
        return update

    def delete_options(self,id):
        cont_row=0
        try:
            cur = self.conexion.cursor()
            sql = "DELETE FROM topcion WHERE id = %s"
            val=(id,)
            cur.execute(sql,val)
            cont_row=cur.rowcount
            self.conexion.commit()    
        except Exception as e:
            # Si no se logro elimianar
            cont_row=0
        finally:
            cur.close() 
        return cont_row
    ################################ INSERT OPTIONS #############################





#variable=Registro_datos()
#var=variable.show_all_data(variable.convert_date("05/08/2023"))
#var=variable.delete_asistence("72773129017")
#r=variable.contar()
#print(var)
#r=variable.datemonth_and_dni(variable.convert_date("5/8/2023"),"78254969")
#r=variable.between_month("01/08/2023","20/08/2022","76213932")
#print(r[0][0])
#print(len(variable.get_option()))
#print(variable.delete_options(10))

# ALTER TABLE `tasistencia` AUTO_INCREMENT = 1;