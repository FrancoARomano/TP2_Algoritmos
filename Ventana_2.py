class Ventana2:
    
    def __init__(self, ventana, dict_info_peliculas: dict, ventana1, informacion_local:dict) -> None:
        
        """
        crea la ventana2, que muestra la información de la pelicula
        """
        
        self.ventana_2 = ventana
        self.ventana_2.geometry("800x500+200+100")
        self.ventana_2.config(bg= "black")
        self.ventana_2.title("Demostración")
        self.ventana_2.resizable(False,False)
        
        self.informacion_local=informacion_local
        
        self.informacion=dict_info_peliculas
        
        self.id=self.informacion["id"]
        
        self.crear_frames(ventana1)
        print(self.informacion_local)
    
    def crear_frames(self,ventana1) -> None:
        
        """
        crea los frames dentro de la ventana2
        """
        self.pantalla_ventana_2_num1 = tk.Frame(self.ventana_2, bg= "gray", width=400, height=400, relief= "groove", bd= 4)
        self.pantalla_ventana_2_num1.place(x= 0, y= 100)

        self.pantalla_ventana_2_num2 = tk.Frame(self.ventana_2, bg= "gray", width=400, height=430, relief= "groove", bd= 4)
        self.pantalla_ventana_2_num2.place(x=400, y= 0)
    
        self.crear_etiquetas(ventana1)    
    
    def crear_texto_informativo(self, posicion: int) -> str:
        
        """
        crea la información de la película para luego mostrarla
        """
        self.url= "http://vps-3701198-x.dattaweb.com:4000/movies/" + self.id

        self.token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.DGI_v9bwNm_kSrC-CQSb3dBFzxOlrtBDHcEGXvCFqgU"

        self.headers = {"Authorization":f"Bearer {self.token}"}

        self.response= requests.get(self.url, headers=self.headers)

        self.dict_poster = self.response.json()
    
        self.claves_texto = ["name", "synopsis", "gender", "duration", "actors", "directors", "rating"]
        self.reemplazo_claves_texto = ["Titulo: ", "Sinopsis: ", "Género: ", "Duración: ","Actores: ", "Directores: ", "Rating: " ]
        self.texto_completo = f"{self.reemplazo_claves_texto[posicion]}{self.dict_poster[self.claves_texto[posicion]]}" 

        return self.texto_completo
    
    def crear_imagen(self) -> any:
        
        """
        obtiene las imagenes y las muestra despues de decodificarlas
        """
        self.url_api = 'http://vps-3701198-x.dattaweb.com:4000/posters/'+ f"{self.id}"
        self.token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.DGI_v9bwNm_kSrC-CQSb3dBFzxOlrtBDHcEGXvCFqgU'
        self.headers = {'Authorization': f'Bearer {self.token}'}
        self.response = requests.get(self.url_api, headers=self.headers)
        
        self.codigo_base64 = self.response.content.decode("utf-8")
        self.codigo_base64 = self.codigo_base64.split(",", 1)[1]
        
        self.longitud_requerida = len(self.codigo_base64) + (4 - len(self.codigo_base64) % 4) % 4
        self.codigo_base64_padded = self.codigo_base64.ljust(self.longitud_requerida, "=")
        
        self.imagen_bytes = base64.b64decode(self.codigo_base64_padded)
        self.imagen_pillow = Image.open(BytesIO(self.imagen_bytes))
        self.imagen_pillow = self.imagen_pillow.resize((387,387))
        self.tk_imagen = ImageTk.PhotoImage(self.imagen_pillow)
        
        return self.tk_imagen
        
    def crear_etiquetas(self, ventana1) -> None:
        
        """
        crea el canvas en el que iría la imagen
        """
        self.etiqueta_imagen = tk.Label(self.pantalla_ventana_2_num1, image= self.crear_imagen())
        
        self.etiqueta_imagen.pack()
        
        for i in range(7):
            self.descripcion= tk.Label(self.pantalla_ventana_2_num2,text= self.crear_texto_informativo(i),width=45,height=1, font= ["Arial", 10], anchor= "w")
            if i == 1:
                self.descripcion = tk.Text(self.pantalla_ventana_2_num2, wrap=tk.WORD, width=52, height=16, font=["Arial", 10])
                self.descripcion.insert(tk.END, self.crear_texto_informativo(i))
                self.descripcion.config(state=tk.DISABLED)
                self.descripcion.place(x=12,y=30)
            elif i == 0:
                self.descripcion.place(x=12,y=5)
            else:
                self.descripcion.place(x=12,y=245 + 25*i)
        
        self.crear_botones(ventana1)
    
    def ir_ventana3(self) -> None:
        
        """
        cierra la ventana2 y abre la ventana3
        """
        self.ventana_2.withdraw() 
        
        #CONSTRUCTOR A VENTANA 3
        ventana3=tk.Tk()
        
        url="http://vps-3701198-x.dattaweb.com:4000"+"/snacks" 
        token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.DGI_v9bwNm_kSrC-CQSb3dBFzxOlrtBDHcEGXvCFqgU"
        headers = {"Authorization": f"Bearer {token}"}    
        conseguir_url = requests.get(url, headers=headers)
        
        pantalla_reserva=Ventana_3(ventana3,conseguir_url,self.informacion,self.informacion_local)
        
        pantalla_reserva.ventana3.mainloop()
        
    
    def volver_ventana1(self,ventana1) -> None:
        
        """
        vuelve a la ventana1, cerrando la ventana2
        """
        self.ventana_2.withdraw() 
        ventana1.deiconify()
    
    def crear_botones(self,ventana1) -> None:
        
        """
        crea los botones que llevan a la ventana3 y a la ventana1 respectivamente
        """
        self.boton0_ir_a_pantalla_3= tk.Button(self.ventana_2, bg= "gray", text= "boton compra (dirige a pantalla 3)", 
                                            fg= "black", font= ("Arial", 15), relief= "groove", bd = 15, cursor="hand2",
                                            command=lambda: self.ir_ventana3())
        self.boton0_ir_a_pantalla_3.place(x=433, y=432)
        
        self.boton1_ir_a_pantalla_1 = tk.Button(self.ventana_2, bg= "gray", text= "<= Volver", fg= "black", font= ("Arial", 15), 
                                                relief= "groove", bd= 15, cursor= "hand2",
                                                command=lambda: self.volver_ventana1(ventana1))
        self.boton1_ir_a_pantalla_1.place(x= 30, y= 15)
