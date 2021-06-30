import dcc
import SI_Format
import sys
from lxml import etree
import xml.etree.ElementTree as ET
import pandas as pd

CONST = {
    '0A','0B','0C','0D','0E','0F','0G','0H',
    '0I','0J','0K','0L','0M','0N','0O','0P','0Q','0R','0S'
}

def administrativeData(adm_df):

    """
    administrativeData():
    
    recibe: data frame administrativo

    retorna el xml administrativo
    
    
    """
    
    administrativeData_ = dcc.administrativeDataType()

    dccSoftware = dcc.softwareListType()
    coreData = dcc.coreDataType()
    items = dcc.itemListType()
    calibrationLaboratory = dcc.calibrationLaboratoryType()
    respPersons = dcc.respPersonListType()
    customer = dcc.contactType()
    statements = dcc.statementListType()

    cell = adm_df.iloc
    table = {item:idx for idx,item in enumerate(cell[:,0]) if item in CONST}
    for name, idx in table.items():
        if name == '0A':
            SoftwareUtilizado,Version = cell[idx,3],cell[idx+1,6]
            software_name = dcc.textType()
            software_name.add_content(
                dcc.stringWithLangType(
                    lang="en",
                    valueOf_=SoftwareUtilizado
                    )
            )
            software = dcc.softwareType(name=software_name,
                                        release=str(Version)[1:])
            dccSoftware.add_software(software)
        if name == '0B':
            coreData.set_countryCodeISO3166_1(cell[idx,3])
        elif name == '0C':
            # puede haber varios pero inicialmente asumo que hay 1.
            # Proximamente lo modificaremos para leer mas de 1.
            coreData.add_usedLangCodeISO639_1(cell[idx,3])
        elif name == '0D':
            # puede haber varios pero inicialmente asumo que hay 1.
            # Proximamente lo modificaremos para leer mas de 1.
            coreData.add_mandatoryLangCodeISO639_1(cell[idx,3])
        elif name == '0E':
            Tipo,CC,NroDeCertificado,Parcial,TotalDeParciales = tuple(
                cell[idx+j,3 if j not in (1,2) else 6] for j in range(5)
                )
            uniqueIdenPrefix = Tipo+' '+('0'*(8-len(CC)))+CC+'-'+\
                               ('0'*(8-len(NroDeCertificado)))+\
                               NroDeCertificado+' '
            if Parcial == 'Único':
                coreData.set_uniqueIdentifier(uniqueIdenPrefix+Parcial)
            else:
                coreData.set_uniqueIdentifier(uniqueIdenPrefix+'Parcial '+
                                              str(Parcial)+' de '+
                                              str(TotalDeParciales))
        elif name == '0F':
            coreData.set_receiptDate(cell[idx+1,3])
        elif name == '0G':
            _,FechaCalibracionDesde,\
            _,FechaCalibracionHasta = tuple(cell[idx+j,3] for j in range(1,5))
            coreData.set_beginPerformanceDate(FechaCalibracionDesde)
            coreData.set_endPerformanceDate(FechaCalibracionHasta)
        elif name == '0H':
            # Preguntar por el campo Dueño. Es un contactType
            Objeto,Descripcion,Dueno = cell[idx+1,3],cell[idx+2,3],cell[idx+3,3]
            Objeto,Descripcion,Dueno = "some_name","some_description","some_dueño"
            name = dcc.textType()
            name.add_content(
                dcc.stringWithLangType(
                    valueOf_=Objeto
                    )
                )
            description = dcc.textType()
            description.add_content(
                dcc.stringWithLangType(
                    valueOf_=Descripcion
                )
            )
            items.set_name(name)
            items.set_description(description)

        elif name == '0J':
            for i in range(idx, table['0K']-9,10):
                t = tuple(
                    cell[i+j,3 if j not in (6,7) else 6] for j in range(1,9)
                    )
                Objeto,Descripcion,AdInfo,Fabricante,\
                Marca,Modelo,NumeroSerie,Idusuario = \
                tuple(
                    cell[i+j,3 if j not in (6,7) else 6] for j in range(1,9)
                    )

                if not pd.isna(Objeto):
                    name = dcc.textType()
                    name.add_content(
                        dcc.stringWithLangType(
                            lang="es",
                            valueOf_=Objeto
                            )
                        )

                if not pd.isna(Descripcion):
                    description = dcc.textType()
                    description.add_content(
                        dcc.stringWithLangType(
                            lang="es",
                            valueOf_=Descripcion
                        )
                    )

                # Que hacer con el CAMPO ADICIONAR INFORMACION
                if not pd.isna(Fabricante):
                    manufacturer_name = dcc.textType()
                    manufacturer_name.add_content(
                        dcc.stringWithLangType(
                            valueOf_=Fabricante
                        )
                    )
                    manufacturer = dcc.contactNotStrictType(name=manufacturer_name)

                if not pd.isna(NumeroSerie):
                    identifications = dcc.identificationListType()
                    identification = dcc.identificationType(issuer="manufacturer",
                                                            value=NumeroSerie)
                    identification_description = dcc.textType()
                    identification_description.add_content(
                        dcc.stringWithLangType(
                            lang="es",
                            valueOf_="Numero de serie"
                        )
                    )
                    identification.set_description(identification_description)
                    identifications.add_identification(identification)

                item = dcc.itemType(name=name,manufacturer=manufacturer,
                                    model=Modelo,
                                    identifications=identifications)
                item.add_description(description)
                items.add_item(item)
        elif name == '0K':
            # Usar para generar el pdf
            # Preguntar dónde se ponen estos datos
            #adm_data[name] = (cell[idx+1,6],cell[idx+2,6])
            pass
        elif name == '0L':
            # Usa para generar el pdf
            # Preguntar dónde se ponen estos datos
            #adm_data[name] = tuple(
            #    cell[idx+j,3 if j not in (6,8) else 6] for j in range(1,16)
            #    )
            pass
        elif name == '0M':
            # Usar para generar el pdf
            # Preguntar dónde se ponen estos datos
            #adm_data[name] = (cell[idx,3],cell[idx+1,3])
            pass
        elif name == '0N':
            Nombre,Gerencia,Subgerencia,Departamento,NombreInternoDepto,\
            Calle,Numero,Otro,CP,ApartadoPostal,Partido,\
            Provincia,Pais,Telefono1,Telefono2,Email,CodigoPais,AdInfo = \
            tuple(
                cell[idx+j,3 if j not in (7,9,10) else 6] for j in range(1,19)
                )
            name = dcc.textType()
            name.add_content(
                dcc.stringWithLangType(
                    lang="es",
                    valueOf_=Nombre
                )
            )

            further = dcc.textType()
            for data in [Departamento,Telefono2,Otro,Gerencia,Subgerencia]:
                further.add_content(
                    dcc.stringWithLangType(
                        valueOf_=data
                    )
                )

            location = dcc.locationType(
                city=[Provincia+', '+Partido],
                countryCode=[CodigoPais],
                postCode=[CP],
                postOfficeBox=[ApartadoPostal],
                state=[Pais],
                street=[Calle],
                streetNo=[Numero],
                further=[further]
                )
            contact = dcc.contactType(id=NombreInternoDepto,name=name,
                                      eMail=Email,phone=Telefono1,
                                      location=location)
            calibrationLaboratory.add_contact(contact)
        elif name == '0P':
            ResponsableP,ResponsableE,TecnicoP,\
            TecnicoE,FirmanteP,FirmanteE = \
            tuple(cell[idx+j,3] for j in range(1,7))
            respPersons.add_respPerson(
                dcc.respPersonType(
                    id="Responsible",
                    person=dcc.contactNotStrictType(
                        name=dcc.textType(
                            content=[
                                dcc.stringWithLangType(
                                    valueOf_=ResponsableP
                                    )
                                ]
                            ),
                        eMail=ResponsableE
                        )
                    )
                )
            respPersons.add_respPerson(
                dcc.respPersonType(
                    id="Technician",
                    person=dcc.contactNotStrictType(
                        name=dcc.textType(
                            content=[
                                dcc.stringWithLangType(
                                    valueOf_=TecnicoP
                                    )
                                ]
                            ),
                        eMail=TecnicoE
                        )
                    )
                )
            respPersons.add_respPerson(
                dcc.respPersonType(
                    id="Signature",
                    person=dcc.contactNotStrictType(
                        name=dcc.textType(
                            content=[
                                dcc.stringWithLangType(
                                    valueOf_=FirmanteP
                                    )
                                ]
                            ),
                        eMail=FirmanteE
                        )
                    )
                )
        elif name == '0Q':
            Nombre,Calle,Numero,Otro,CP,ApartadoPostal,Partido,Provincia,Pais,\
            Telefono1,Telefono2,Email,CodigoPais,AdInfo = \
            tuple(
                cell[idx+j,3
                     if j not in (2,3,4,5,6,10,11) else 6] for j in range(1,15)
                )
            name = dcc.textType()
            name.add_content(
                dcc.stringWithLangType(
                    lang="es",
                    valueOf_=Nombre
                )
            )

            further = dcc.textType()
            further.add_content(
                dcc.stringWithLangType(
                    valueOf_=Telefono2
                )
            )

            location = dcc.locationType(
                city=[Provincia+', '+Partido],
                countryCode=[CodigoPais],
                postCode=[CP],
                postOfficeBox=[ApartadoPostal],
                state=[Pais],
                street=[Calle],
                streetNo=[Numero],
                further=[further]
                )
            customer = dcc.contactType(name=name,
                                      eMail=Email,phone=Telefono1,
                                      location=location)

        elif name == '0S':
            # Hablar con Diego sobre cuales de estos campos van a pedir
            # MOSTRAR esquema y charlarlo.
            for i in range(idx, len(cell[:])-5,6):
                Id,Convencion,Norma,Referencia,Declaracion=\
                tuple(cell[i+j,3] for j in range(1,6))

                statement = dcc.statementMetaDataType()
                if not pd.isna(Id):
                    statement.set_id = Id
                if not pd.isna(Convencion):
                    statement.set_convention = Convencion
                if not pd.isna(Norma):
                    statement.set_norm = Norma
                if not pd.isna(Referencia):
                    statement.set_reference = Referencia
                if not pd.isna(Declaracion):
                    statement_declaration = dcc.textType()
                    statement_declaration.add_content(
                        dcc.stringWithLangType(
                            lang="es",
                            valueOf_=Declaracion
                        )
                    )
                    statement.set_declaration(statement_declaration)
                statements.add_statement(statement)


    administrativeData_.set_dccSoftware(dccSoftware)
    administrativeData_.set_coreData(coreData)
    administrativeData_.set_items(items)
    administrativeData_.set_calibrationLaboratory(calibrationLaboratory)
    administrativeData_.set_respPersons(respPersons)
    administrativeData_.set_customer(customer)
    administrativeData_.set_statements(statements)
    return administrativeData_

def measurementResults(res_df):

    """
    measurementResults():
    
    recibe: data frame resultados

    retorna return measurementResults_
    
    
    name.add_prueba
    
    
    """    
    #El día que lo presentemos va a ser lo mejor usar una jupyter notebook.
    #
    #https://www.ptb.de/dcc/v2.4.0/en/measurementResult/#tree-structure
    #
    #alrazonar las estructuras, hay que tener en cuenta que los métodos
    #ya saben a que padre tiene que linkearse y no hace falta referenciarlos.
    #
    
    
    measurementResults_ = dcc.measurementResultListType()
    #creo un dcc:measurementResults

    measurementResult = dcc.measurementResultType()
    #creo un dcc:measurementResult
    
    usedMethods = dcc.usedMethodListType()
    #creo un dcc:usedMethods
    
    usedSoftware = dcc.softwareListType()
    #creo un dcc:usedSoftware
    
    influenceConditions = dcc.influenceConditionListType()
    #genero el influence conditions    
    
    influenceCondition = dcc.conditionType()
    #genero el influence condition
    
    results = dcc.resultListType()
    #genero el results
    
    #
    #arriba genero todos los elementos ppales
    #
    
    res_data = {}
    #genero un dic de resultados ¿para qué?
    
    cell = res_df.iloc
    #modifico el df para leer las columnas con números y no letras desde cell[]
    
    table = {item:idx for idx,item in enumerate(cell[:,0]) if item in CONST}
    #asigno una tabla de índices(row-1) respecto a cada asignación {índice = [número|letra]}
    
    for name, idx in table.items():
        #itero todos los items de la tabla uqe generé antes: 0A, 0B, 0C ...
        if name == '0A':
            
            for key,value in {"Metodología_Empleada":cell[idx, 3],
                           "Procedimiento":cell[idx+1,3]}.items():
            # este harcoddeo no me gusta, y la frase tiene que estar
            #entera, unir las dos rows fijarse del excel   
            #crear un solo usedMethod
            #con cell leo [row,column]
            
                usedMethod_name = dcc.textType(id=key)
                #?
                #agrego dcc:name a usedMethod y le asigno el id=Metod...
                #el id es palabra reservada y puedo agregarlo así
                
                usedMethod_name.add_content(
                #al name que cree le agrego el dcc:content
                    dcc.stringWithLangType(
                        lang="es",
                        #no tiene que estar harcodeado, tiene que estar leido
                        #idioma que le asigné en el administrativo
                        #para cuando haya mas de un idioma. 
                        #el idioma debería ser un vector.
                        valueOf_=key
                        #agrega el valor de "Met..." dentro del contenido
                    )
                )

                usedMethod_description = dcc.textType()
                #agrego dcc:description al method a usedMethod
                                
                usedMethod_description.add_content(
                    dcc.stringWithLangType(
                        lang="es",
                        valueOf_=value
                    )
                )

                usedMethod = dcc.usedMethodType(
                    name=usedMethod_name,
                    description=[usedMethod_description]
                    )
                usedMethods.add_usedMethod(usedMethod)
        #elif name == '0B':
        #    res_data[name] = (cell[idx, 3],cell[idx+1,7])
        #    software_name = dcc.textType()
        #    software_name.add_content(
        #        dcc.stringWithLangType(
        #            valueOf_=cell[idx, 3]
        #        )
        #    )
        #    software = dcc.softwareType(
        #        name=software_name,
        #        release=cell[idx+1,7]
        #    )
        #    usedSoftware.add_software(software)
        elif name == '0B':
            #res_data[name] = cell[idx, 3]
            influenceCondition_name = dcc.textType()
            influenceCondition_name.add_content(
                dcc.stringWithLangType(
                    valueOf_=cell[idx,3]
                )
            )
            influenceCondition.set_name(influenceCondition_name)
        elif name == '0C':
            res_data[name] = (cell[idx+1,3],cell[idx+2,3],cell[idx+3,3])
            data = dcc.dataType()
            CondicionesAmbientales = (
                ("Temperatura mayor a",cell[idx+1,3],"\\degreeCelsius"),
                ("Temperatura menor a",cell[idx+2,3],"\\degreeCelsius"),
                ("Humedad Relativa",cell[idx+3,3],"\\kilogram\\tothe{1}\\metre"\
                 "\\tothe{-3}\\kilogram\\tothe{-1}\\metre\\tothe{3}"))

            for name,value,unit in CondicionesAmbientales:
                quantity_name = dcc.textType()
                quantity_name.add_content(
                    dcc.stringWithLangType(
                        lang="es",
                        valueOf_=name
                    )
                )
                expandedUnc = SI_Format.expandedUnc(uncertainty=0.2,
                                                    coverageFactor=2,
                                                    coverageProbability=0.95)
                real = SI_Format.real(value=float(value),
                                      unit=unit,
                                      expandedUnc=expandedUnc)
                quantity = dcc.quantityType(name=quantity_name,real=real)
                data.add_quantity(quantity)

            influenceCondition.set_data(data)
            influenceConditions.add_influenceCondition(influenceCondition)
        elif name == '0D':
            res_data[name] = (cell[idx+3, 3],cell[idx+6,3],
                              cell[idx+7,3],cell[idx+8,3],
                              cell[idx+9,3],cell[idx+10,3])
        elif name == '0E':
            res_data[name] = (cell[idx+1, 3],cell[idx+2,3],cell[idx+3,3])
        elif name == '0F':
            for j in range(idx,table['0G']-4):
                if not pd.isna(cell[j,3]):
                    obs = cell[j,3]
                    if name in res_data:
                        res_data[name].append(obs)
                    else:
                        res_data[name] = [obs]
        elif name == '0G':
            Resultados = (
                ("Temperatura",[],0.2,"\\degreeCelsius"),
                ("Resistencia",[],[],"\\kilogram\\metre\\tothe{2}"\
                 "\\second\\tothe{-3}\\ampere\\tothe{-2}")
            )
            data = dcc.dataType()
            for j in range(idx+2, len(res_df)):
                Temperatura,Resistencia,Incertidumbre = \
                float(cell[j,3]),float(cell[j,4]),float(cell[j,5])

                quantity_nominal_name = dcc.textType()
                quantity_nominal_name.add_content(
                    dcc.stringWithLangType(
                        lang="es",
                        valueOf_="Valor nominal"
                    )
                )
                noQuantity = dcc.textType()
                noQuantity.add_content(
                    dcc.stringWithLangType(
                        valueOf_=str(Temperatura)
                    )
                )
                quantity_nominal = dcc.quantityType(name=quantity_nominal_name,
                                                    noQuantity=noQuantity)

                expandedUnc = SI_Format.expandedUnc(uncertainty=Incertidumbre,
                                                    coverageFactor=2,
                                                    coverageProbability=0.95)
                real = SI_Format.real(value=Resistencia,
                                      unit="\\kilogram\\metre\\tothe{2}"\
                                       "\\second\\tothe{-3}\\ampere\\tothe{-2}",
                                      expandedUnc=expandedUnc)
                quantity = dcc.quantityType(real=real)

                list_ = dcc.listType()
                list_.add_quantity(quantity_nominal)
                list_.add_quantity(quantity)
                data.add_list(list_)

            result_name = dcc.textType()
            result_name.add_content(
                dcc.stringWithLangType(
                    lang="es",
                    valueOf_="Resultados"
                )
            )
            result = dcc.resultType(name=result_name,data=data)
            results.add_result(result)

    measurementResult.set_usedMethods(usedMethods)
    measurementResult.set_influenceConditions(influenceConditions)
    measurementResult.set_results(results)

    measurementResults_.add_measurementResult(measurementResult)
    return measurementResults_


def read(file_path):
    # Lee la primera hoja del excel. Devuelve la informacion
    # en un dataframe de pandas.
    adm_df = pd.read_excel(file_path,
                           sheet_name='Administrativo',
                           header=None,
                           usecols="A:G")

    # Lee la segunda hoja del excel.
    res_df = pd.read_excel(file_path,
                           sheet_name="Resultados",
                           header=None,
                           usecols="A:J")

    return adm_df,res_df

def main():
    # Toma el nombre de archivo como argumento
    if len(sys.argv) == 2:
        file_name = sys.argv[1]
    else:
        file_name = 'Certificado.ods'

    # Lee spreadsheet
    adm_df,res_df = read(file_name)

    # Genera el administrativeData
    administrativeData_ = administrativeData(adm_df)

    # Genera el measurementResults
    measurementResults_ = measurementResults(res_df)
    measurementResult = measurementResults_.get_measurementResult()
    measurementResult[0].set_usedSoftware(administrativeData_.get_dccSoftware())

    # Integra toda la informacion del administrativeData y measurementResults
    # para generar el digitalCalibrationCertificate
    digitalCalibrationCertificate = dcc.digitalCalibrationCertificateType(
        schemaVersion="2.4.0",
        administrativeData=administrativeData_,
        measurementResults=measurementResults_
    )
    nsmap_ = {
        'dcc' : 'https://ptb.de/dcc',
        'xsi' : 'http://www.w3.org/2001/XMLSchema-instance',
        'si' : 'https://ptb.de/si'
    }
    name_ = 'digitalCalibrationCertificate'
    NS = "http://www.w3.org/2001/XMLSchema-instance"

    # Pasa la estructura de objetos anidados a un objeto Element (Element API)
    elem = digitalCalibrationCertificate.to_etree(name_=name_,nsmap_=nsmap_)

    # Agrega el schemaLocation al xml
    elem.attrib['{{{pre}}}schemaLocation'.format(pre=NS)] = \
    'https://ptb.de/dcc https://ptb.de/dcc/v2.4.0/dcc.xsd'

    # Genera el xml
    tree = etree.ElementTree(elem)
    tree.write('dcc.xml', encoding='UTF-8',
                              xml_declaration=True,
                              pretty_print=True)

if __name__ == '__main__':
    main()
