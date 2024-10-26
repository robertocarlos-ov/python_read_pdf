import pymupdf, re

#Se define función
def leer_archivo_pdf(pdf_file_name, csv_file_name):
    #Archivo fuente
    archivo_pdf=pymupdf.open(pdf_file_name)

    #Mostrar total de páginas
    print("Total de páginas: " + str(len(archivo_pdf)))

    #Archivo destino
    archivo_csv=open(csv_file_name, "w")

    #Escribir en archivo
    archivo_csv.write("Folio Fiscal,RFC Emisor,RFC Receptor,Estado del Comprobante,Fecha Certificación" + "\n")

    #Recorrer páginas
    for i_page in range(len(archivo_pdf)):
        #Cargar página
        pagina_pdf=archivo_pdf.load_page(i_page)
        #Obtener texto
        texto_pdf=pagina_pdf.get_text()

        #Buscar patrón de texto
        matches_folio_fiscal=re.findall("Folio Fiscal:.*", texto_pdf)

        #Buscar patrón de texto
        matches_emisor_rfc=re.findall("RFC Emisor:.* ", texto_pdf)
        #for index in matches_rfc_emisor:
        #print(str(matches_emisor_rfc))   

        #Buscar patrón de texto
        matches_nombre=re.findall("Nombre o Razón Social:.* ", texto_pdf)
        #for index in matches_rfc_emisor:
        #print(str(matches_nombre))  

        #Buscar patrón de texto
        matches_receptor_rfc=re.findall("RFC Receptor:.* ", texto_pdf)
        #for index in matches_rfc_emisor:
        #print(str(matches_receptor_rfc))   

        #buscar patrón de texto
        matches_fecha_cert=re.findall("Fecha Certificación:.*", texto_pdf)

        #Buscar patrón de texto
        matches_estado_comprobante=re.findall("Estado del Comprobante:.* ", texto_pdf)
        #for index in matches_rfc_emisor:
        #print(str(matches_estado_comprobante))  

        #Recorrer folios
        for i_folio in range(len(matches_folio_fiscal)):
            #Folio Fiscal
            folio_fiscal = (str(matches_folio_fiscal[i_folio]).split(": "))[1]
            #Emisor RFC
            emisor_rfc = (str(matches_emisor_rfc[i_folio]).split(": "))[1]
            #Receptor RFC 
            receptor_rfc = (str(matches_receptor_rfc[i_folio]).split(": "))[1]
            #Estado del comprobante
            estado_comprobante = (str(matches_estado_comprobante[i_folio]).split(": "))[1]
            #Fecha Certificación
            fecha_cert = ((str(matches_fecha_cert[i_folio]).split(": "))[1]).split("T")[0]

            #Imprimir Folio Fiscal, RFC Emisor, RFC Receptor, Estado del Comprobante
            print(folio_fiscal + "," + 
                emisor_rfc   + "," + 
                receptor_rfc + "," + 
                estado_comprobante + "," +
                fecha_cert )

            #Escribir en archivo
            archivo_csv.write(folio_fiscal + "," + 
                            emisor_rfc   + "," + 
                            receptor_rfc + "," + 
                            estado_comprobante + "," + 
                            fecha_cert + "\n")

    #Mostrar total de páginas
    print("Total de páginas: " + str(len(archivo_pdf)))

    #Cerrar archivos
    archivo_pdf.close()
    archivo_csv.close()

#Llamar función que realiza el proceso
leer_archivo_pdf("Resultados (66).pdf", "Resultados (66).csv")