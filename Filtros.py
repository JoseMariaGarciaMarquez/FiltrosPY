def Filtros(t, señal):
    print("---------------------------------------------------------------------------------\n"
          "Este programa contiene varios filtros con ciclo for para filtrar señales en \n"
          "El dominio de Fourier, mostrar la señal original, la señal filtrada y el espectro\n"
          "---------------------------------------------------------------------------------")
 #--------Transformar la señal recibida-------------------------------------------------------------
    señal_ff = fftshift(fft(señal))
 #--------Crear el dominio temporal-----------------------------------------------------------------
    N = len(t)
    dt = t[1]-t[0]
 #--------Crear el dominio de Fourier---------------------------------------------------------------
    FN = 1/(2*dt)
    F0 = 1/(N*dt)

    F = np.arange(-FN,FN,F0)

 #----Mostramos el espectro de Fourier para el usuario----------------------------------------------
    fig  = plt.figure(figsize = (10,6), dpi = 175)
    plt.plot(F, señal_ff, c = "red")
    plt.scatter(F, señal_ff, c = "salmon")
    plt.title("Espectro de amplitud")
    plt.grid()
    plt.show()
    
    si = int(input("¿Quieres hacerle zoom a los datos?\n1. SI\n2. NO\n"))
    if si == 1:
        zoom = int(input("1. X1\n2. X2\n3. X3\n"))
        fig = plt.figure(figsize = (10,6), dpi = 175)
        plt.plot(F, señal_ff**(1/zoom), c = "red")
        plt.scatter(F, señal_ff**(1/zoom), c = "salmon")
        plt.title("Espectro de amplitud")
        plt.grid()
        plt.show()
    else:
        zoom = 1;

 #---------Preguntamos al usuario el tipo de filtro que desea usar---------------------------------
    filtro = int(input("Seleccione el filtro que desea usar\n1. Pasa Bajas\n2. Pasa Altas\n3. Pasa Bandas\n"))
    P = [0]*len(F)
    if filtro ==1:
        FC = float(input("Freuencia de corte para el Pasa Bajas: "))
        #------------Diseñamps el filtro-----------------------------------------------------------
       
        for i in range(len(F)):
            if abs(F[i]) < FC:
                P[i] = 1
        fig = plt.figure(figsize = (10,6), dpi = 175)
        plt.plot(F, señal_ff**(1/zoom), c = "red")
        plt.scatter(F, señal_ff**(1/zoom), c = "salmon")
        plt.axvspan(abs(FC),0, facecolor = "pink", alpha = 0.9, label = "Filtro")
        plt.axvspan(-1*(FC),0, facecolor = "pink", alpha = 0.9)
        plt.title("Espectro de amplitud")
        plt.legend()
        plt.grid()
        plt.show()
        
    elif filtro == 2:
        FC = float(input("Frecuencia para el filtro Pasa Altas: "))

        for i in range(len(F)):
            if abs(F[i]) > FC:
                P[i] = 1
        fig = plt.figure(figsize = (10,6), dpi = 175)
        plt.plot(F, señal_ff**(1/zoom), c = "red")
        plt.scatter(F, señal_ff**(1/zoom), c = "salmon")
        plt.axvspan(abs(FC),max(F), facecolor = "pink", alpha = 0.9, label = "Filtro")
        plt.axvspan(-1*(FC),-1*max(F), facecolor = "pink", alpha = 0.9)
        plt.title("Espectro de amplitud")
        plt.legend()
        plt.grid()
        plt.show()

    else:
        FC1 = float(input("Frecuencia menor para el filtro Pasa Bandas: "))
        FC2 = float(input("Frecuencia mayor para el filtro Pasa Bandas: "))
        
        for i in range(len(F)):
            if FC1 <= abs(F[i]) <= FC2:
                P[i] = 1;
        fig = plt.figure(figsize = (10,6), dpi = 175)
        plt.plot(F, señal_ff**(1/zoom), c = "red")
        plt.scatter(F, señal_ff**(1/zoom), c = "salmon")
        plt.axvspan(abs(FC1),abs(FC2), facecolor = "pink", alpha = 0.9, label = "Filtro")
        plt.axvspan(-1*(FC1),-1*(FC2), facecolor = "pink", alpha = 0.9)
        plt.title("Espectro de amplitud")
        plt.legend()
        plt.grid()
        plt.show()

        
    señal_filtro = señal_ff * P;
    señal_filtrada = abs(ifft(fftshift(señal_filtro)));

    fig, ax= plt.subplots(2,1, figsize = (10,6), dpi = 170)
    ax[0].plot(t, señal, c = "salmon", label = "Seál original")
    ax[0].scatter(t, señal, c = "pink")
    ax[0].set_title("Señal original")
    ax[0].grid()
    
    ax[1].plot(t, señal_filtrada, c = "magenta", linewidth = 2, label = "Señal filtrada")
    ax[1].scatter(t, señal_filtrada, c = "pink")
    ax[1].set_title("Señal filtrada")
    ax[1].grid()


    
    plt.suptitle("⚙️Resultados⚙️", fontsize = 20)
    
    
    resp = int(input("¿Deseas guardar los resultados?\n1. SI\n2. NO\n"))

    
    if resp == 1:
        nombre_archivo = input("Nombre del archivo: ")
        expension = input("Extension: ")
        plt.savefig("{}.{}".format(nombre_archivo,expension))
        print("-----------------------------------------------------------------------\n"
          "CODE BY: GARCÍA MÁRQUEZ JOSÉ MARÍA\n"
          "UNAM GEOPHYSICAL ENGINEERING STUDENT\n"
          "SAY THANKS AT: https://paypal.me/Chemitas96?country.x=MX&locale.x=es_XC\n"
         "------------------------------------------------------------------------")
    else:
        print("-----------------------------------------------------------------------\n"
          "CODE BY: GARCÍA MÁRQUEZ JOSÉ MARÍA💻\n"
          "UNAM GEOPHYSICAL ENGINEERING STUDENT✏️\n"
          "SAY THANKS🤑 AT: https://paypal.me/Chemitas96?country.x=MX&locale.x=es_XC\n"
          "Suggestions✉️ at: josemariagarciamarquez2.72@gmail.com Subject: SUGGEST\n"
         "---------------------------------------------------------------------------")
        return
        


    return