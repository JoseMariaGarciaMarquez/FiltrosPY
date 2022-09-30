#Diseño de filtros---------------------------------------------------------------------------------

#----Filtro-Pasa-Bajas-----------------------------------------------------------------------------
#----INICIO----------------------------------------------------------------------------------------
def PB_JMGM(t,FC,señal):
#--------Transformar la señal recibida-------------------------------------------------------------
    señal_ff = fftshift(fft(señal))
#--------Crear el dominio temporal-----------------------------------------------------------------
    N = len(t)
    dt = t[1]-t[0]
#--------Crear el dominio de Fourier---------------------------------------------------------------
    FN = 1/(2*dt)
    F0 = 1/(N*dt)

    F = np.arange(-FN,FN,F0)
#--------Crear el filtro---------------------------------------------------------------------------    
    LowPass = [0]*len(F)
    for i in range (len(LowPass)):
        if abs(F[i]) <= FC:
            LowPass[i] = 1
#--------Filtrar en el dominio de Fourier----------------------------------------------------------
    señal_f = []
    for i in range (len(LowPass)):
        señal_f.append(señal_ff[i]*LowPass[i])
#--------Reconstruir la señal con las amplitudes filtradas----------------------------------------    
    señal_r = ifft(ifftshift(señal_f))

#--------Gráficas----------------------------------------------------------------------------------
    fig, ax = plt.subplots(2,2, figsize = (15,10), dpi = 150)
    ax[0,0].plot(t,señal)
    ax[0,0].set_title("Señal original")
    ax[0,0].set_xlabel("Radiación")
    ax[0,0].set_ylabel("Años")
    ax[0,0].grid()
    
    ax[0,1].plot(F,señal_ff, c = 'red')
    ax[0,1].scatter(F,señal_ff, c = 'salmon')
    ax[0,1].set_title("Espectro de amplitud")
    ax[0,1].set_xlabel("Frecuencia [años^-1]")
    ax[0,1].set_ylabel("Amplitud")
    ax[0,1].grid()
    
    ax[1,0].plot(F, LowPass)
    ax[1,0].set_title("Filtro pasa-bajas")
    ax[1,0].grid()
    
    ax[1,1].plot(t,señal_r)
    ax[1,1].set_title("Señal filtrada")
    ax[1,1].set_title("Señal original")
    ax[1,1].set_xlabel("Radiación")
    ax[1,1].set_ylabel("Años")
    ax[1,1].grid()
    
    fig.suptitle("FILTRO PASA-BAJAS", fontsize = "20")
    
    return fig,ax
#----FIN-------------------------------------------------------------------------------------------
