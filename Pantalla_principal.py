import tkinter as tk
from PIL import ImageTk, Image
import requests
import base64
from io import BytesIO

class Pantalla_principal:
    
    def __init__(self, master,informacion_local,ventana0):
        
        self.master = master
        self.master.geometry("900x900")
        self.master.title("Pantalla Principal")
        self.master.config(bg = "light gray")
        self.master.resizable(False, False)
        
        self.ventana0=ventana0
        
        self.informacion_local=informacion_local
        
        
        self.lista_id_imagenes = self.funcion_id_imagenes(self.informacion_local)
        
        self.creador_marcos(self.informacion_local)
        self.buscador_con_boton(self.informacion_local, self.lista_id_imagenes)
        self.creacion_botones(self.lista_id_imagenes)
    

    def creador_marcos(self, informacion_local):
        
        lista_contenedores = []
        
        fila = 0
        columna = 0
        
        for _ in range(9):
                
            self.contenedores = tk.Frame(self.master, bg = "light gray", width = 300, height = 260)
            
            self.contenedores.grid(row = fila, column = columna)
            
            lista_contenedores.append(self.contenedores)
            
            columna += 1
            
            if fila == 0 and columna == 3:
                
                fila = 1
                columna = 0
            
            elif fila == 1 and columna == 3:
                
                fila = 2 
                columna = 0
            
        self.creador_canvas_imagenes(lista_contenedores, informacion_local)
        
    def funcion_id_imagenes(self, informacion_local):
        
        self.id_cine = int(informacion_local["cinema_id"])
        
        self.url_api_1 = f'http://vps-3701198-x.dattaweb.com:4000/cinemas/{self.id_cine}/movies'
        self.token_1 = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.DGI_v9bwNm_kSrC-CQSb3dBFzxOlrtBDHcEGXvCFqgU'
        self.headers_1 = {'Authorization': f'Bearer {self.token_1}'}
        self.id_ubicacion = requests.get(self.url_api_1, headers=self.headers_1)
        
        lista_id_peliculas = self.id_ubicacion.json()[0]["has_movies"]
        
        lista_para_for = [lista_id_peliculas[0], lista_id_peliculas[1], lista_id_peliculas[2], 
                        lista_id_peliculas[3], lista_id_peliculas[4], lista_id_peliculas[5]]
        
        return lista_para_for


    def volver_pantalla_inicial_boton(self):
        
        self.master.withdraw()
        
        self.ventana0.deiconify()

    def creacion_botones(self, lista_id_imagenes):
        
        posicion_y = 200
        
        iterar_imagenes = 0
        
        for n in range(1,7):
            
            posicion_x = 100
            
            if n % 2 == 0: posicion_x = 700
            
            if n == 3: posicion_y = 460
            
            elif n == 5: posicion_y = 720
            
            if n == 1: n = 0
            
            url_info_pelis_botones_ver = "http://vps-3701198-x.dattaweb.com:4000/movies/" + f"{lista_id_imagenes[iterar_imagenes]}"
            
            iterar_imagenes += 1
        
            token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.DGI_v9bwNm_kSrC-CQSb3dBFzxOlrtBDHcEGXvCFqgU"
            headers= {"Authorization": f"Bearer {token}"} 
        
            info_pelis_botones_ver = requests.get(url_info_pelis_botones_ver, headers = headers)
                
            self.botones = tk.Button(self.master, text = "Ver", width = 10, height = 1, bd = "7",
                                    command = lambda dict_boton_ver = info_pelis_botones_ver.json():self.ir_pagina_secundaria(dict_boton_ver))
            
            self.botones.place(x = posicion_x, y = posicion_y)   
        
            
        
        boton_volver=tk.Button(self.master, text="<-- Volver", bg="Black",fg="White",bd=5,cursor="hand2",
                            command=lambda: self.volver_pantalla_inicial_boton())
        boton_volver.place(x=420,y=30)     
        
            
    def ir_pagina_secundaria(self, dict_info_peliculas):
        
        self.master.withdraw()
        
        ventana_2 = tk.Tk()
        
        # pantalla_secundaria = Ventana2(ventana_2,dict_info_peliculas,self.master,self.informacion_local)
        #IR A VENTANA 2
        
        
    def verificar_pelicula(self, ingreso_del_usuario, lista_id_imagenes): 
        
        for i in range(len(lista_id_imagenes)):
            
            url_info_pelis = "http://vps-3701198-x.dattaweb.com:4000/movies/" + f"{lista_id_imagenes[i]}"
            
            token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.DGI_v9bwNm_kSrC-CQSb3dBFzxOlrtBDHcEGXvCFqgU"
            headers= {"Authorization": f"Bearer {token}"}
            
            self.info_pelis = requests.get(url_info_pelis, headers = headers)
            
            self.nombres_pelis = (self.info_pelis.json()["name"])
            
            self.nombres_pelis_minusculas = self.nombres_pelis.lower()
            
            if self.nombres_pelis_minusculas == ingreso_del_usuario:
            
                self.ir_pagina_secundaria(self.info_pelis.json())
            
    def buscador_con_boton(self, informacion_local, lista_id_imagenes):
        
        ubicacion = informacion_local["location"]
        
        ingreso_del_usuario = tk.StringVar(self.master)
        
        self.entrada_de_texto = tk.Entry(self.master, width = 37,  fg = "White", bg = "black", justify = "center", textvariable = ingreso_del_usuario)
        self.entrada_de_texto.place(x = 340, y = 300)
        
        
        self.boton_buscar = tk.Button(self.master, text = "Buscar Película",
                                    width = 15, command = lambda: self.verificar_pelicula(ingreso_del_usuario.get(), lista_id_imagenes))
        self.boton_buscar.place(x = 395, y = 350)
        
        self.etiqueta_ubicacion = tk.Label(self.master, text = f"Usted está en el cine de {ubicacion}", bg = "light gray",
                                        justify = "center").place(x = 355, y = 730)
        

    def creador_canvas_imagenes(self, lista_contenedores, informacion_local):
        
        self.id_cine = int(informacion_local["cinema_id"])
        
        self.url_api_1 = f'http://vps-3701198-x.dattaweb.com:4000/cinemas/{self.id_cine}/movies'
        self.token_1 = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.DGI_v9bwNm_kSrC-CQSb3dBFzxOlrtBDHcEGXvCFqgU'
        self.headers_1 = {'Authorization': f'Bearer {self.token_1}'}
        self.id_ubicacion = requests.get(self.url_api_1, headers=self.headers_1)
        
        lista_id_peliculas = self.id_ubicacion.json()[0]["has_movies"]
        
        lista_para_for = [lista_id_peliculas[0], 0, lista_id_peliculas[1], lista_id_peliculas[2], 0,
                        lista_id_peliculas[3], lista_id_peliculas[4], 0, lista_id_peliculas[5]]
        
        lista_imagenes = []
        
        for i in lista_para_for:
            
            if i == 0: 
                lista_imagenes.append(0)
                continue
            
            self.url_api = 'http://vps-3701198-x.dattaweb.com:4000/posters/' + f"{i}"
            self.token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.DGI_v9bwNm_kSrC-CQSb3dBFzxOlrtBDHcEGXvCFqgU'
            self.headers = {'Authorization': f'Bearer {self.token}'}
            self.response = requests.get(self.url_api, headers=self.headers)
            
            self.codigo_base64 = self.response.content.decode("utf-8")
            self.codigo_base64 = self.codigo_base64.split(",", 1)[1]
            
            self.longitud_requerida = len(self.codigo_base64) + (4 - len(self.codigo_base64) % 4) % 4
            self.codigo_base64_modificado = self.codigo_base64.ljust(self.longitud_requerida, "=")
            
            self.imagen_bytes = base64.b64decode(self.codigo_base64_modificado)
            
            lista_imagenes.append(self.imagen_bytes)
            
        for i in range(len(lista_imagenes)):
            
            if lista_imagenes[i] == 0: 
                continue
            
            canvas_general = tk.Canvas(lista_contenedores[i], bg = "black", height = 260, width = 300, borderwidth = 0, highlightthickness = 0)
            canvas_general.grid(row = 0, column = 0, sticky = "nesw", padx = 0, pady = 0)
            
            imagen_en_canvas = Image.open(BytesIO(lista_imagenes[i]))
            canvas_general.image = ImageTk.PhotoImage(imagen_en_canvas.resize((135, 192), Image.LANCZOS))
            canvas_general.create_image((300 - 135) / 2, (200 - 192) / 2, image = canvas_general.image, anchor = 'nw')

def main():
    ventana_principal = tk.Tk()

    app = Pantalla_principal(ventana_principal)
    ventana_principal.mainloop()

main()