from schemas.dcc.v3_0_0 import dcc
from schemas.SI_Format.v2_0_0 import SI_Format
from schemas.statement import statement
import sys
from lxml import etree
import xml.etree.ElementTree as ET
import pandas as pd
import numpy as np
import datetime
import copy

DEGREECELSIUS = '\\degreeCelsius'

RELATIVEHUMIDITY = '\\kilogram\\tothe{1}\\metre\\tothe{-3}'\
                   '\\kilogram\\tothe{-1}\\metre\\tothe{3}'

OHM = '\\kilogram\\metre\\tothe{2}\\second\\tothe{-3}\\ampere\\tothe{-2}'

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
    coreData = dcc.coreDataType(
        performanceLocation=dcc.performanceLocationType(
            valueOf_=dcc.stringPerformanceLocationType.LABORATORY))
    items = dcc.itemListType()
    calibrationLaboratory = dcc.calibrationLaboratoryType()
    respPersons = dcc.respPersonListType()
    statements = dcc.statementListType()

    calibrationLaboratory_contact_location_further = dcc.textType()

    cell = adm_df.loc
    table = {item:idx for idx,item in enumerate(cell[:,'A']) if item in CONST}
    for name, idx in table.items():
        if name == '0A':
            usedSoftware,version = cell[idx,'D'],cell[idx+1,'D']
            software_name = dcc.textType()
            software_name.add_content(
                dcc.stringWithLangType(
                    lang="en",
                    valueOf_=usedSoftware
                    )
            )
            software = dcc.softwareType(name=software_name,
                                        release=version)
            dccSoftware.add_software(software)
        if name == '0B':
            coreData.set_countryCodeISO3166_1(cell[idx,'D'])
        elif name == '0C':
            # puede haber varios pero inicialmente asumo que hay 1.
            # Proximamente lo modificaremos para leer mas de 1.
            coreData.add_usedLangCodeISO639_1(cell[idx,'D'])
        elif name == '0D':
            # puede haber varios pero inicialmente asumo que hay 1.
            # Proximamente lo modificaremos para leer mas de 1.
            coreData.add_mandatoryLangCodeISO639_1(cell[idx,'D'])
        elif name == '0E':
            type,cc,certificateNumber,part,total = tuple(
                cell[idx+j,'D'] for j in range(5)
                )
            uniqueIdenPrefix = type+' '+('0'*(8-len(cc)))+cc+'-'+\
                               ('0'*(8-len(certificateNumber)))+\
                               certificateNumber+'-'
            if part == '??nico':
                coreData.set_uniqueIdentifier(uniqueIdenPrefix+part)
            else:
                coreData.set_uniqueIdentifier(uniqueIdenPrefix+'Parcial '+
                                              part+' de '+
                                              total)
        elif name == '0F':
            coreData.set_receiptDate(cell[idx,'D'])
        elif name == '0G':
            coreData.set_beginPerformanceDate(cell[idx+1,'D'])
            coreData.set_endPerformanceDate(cell[idx+2,'D'])
        elif name == '0H':
            object,description = cell[idx+1,'D'],cell[idx+2,'D']
            if object:
                items_name = dcc.textType()
                items_name.add_content(
                    dcc.stringWithLangType(
                        valueOf_=object
                        )
                    )
                items.set_name(items_name)
            if description:
                items_description = dcc.richContentType()
                items_description.add_content(
                    dcc.stringWithLangType(
                        valueOf_=description
                    )
                )
                items.set_description(items_description)
        elif name == '0I':
            oname,street,number,other,pc,postOfficeBox,department,\
            province,country,phone1,phone2,email,countryCode,adInfo = \
            tuple(cell[idx+j,'D'] for j in range(1,15))
            owner_name = dcc.textType()
            owner_name.add_content(
                dcc.stringWithLangType(
                    lang="es",
                    valueOf_=oname
                )
            )

            further = dcc.textType()
            further.add_content(
                dcc.stringWithLangType(
                    valueOf_=phone2
                )
            )

            owner_location = dcc.locationType(
                city=[province+', '+department],
                countryCode=[countryCode],
                postCode=[pc],
                postOfficeBox=[postOfficeBox],
                state=[country],
                street=[street],
                streetNo=[number],
                further=[further]
                )
            owner = dcc.contactType(name=owner_name,
                                      eMail=email,phone=phone1,
                                      location=owner_location)
        elif name == '0J':
            for i in range(idx, table['0K']-9,10):
                object,description,adInfo,manufacturer,\
                brand,model,serialNumber,userId = \
                tuple(cell[i+j,'D'] for j in range(1,9))
                if object and description and manufacturer and serialNumber:
                    item_name = dcc.textType()
                    item_name.add_content(
                        dcc.stringWithLangType(
                            lang="es",
                            valueOf_=object
                            )
                        )
                    item_description = dcc.richContentType()
                    item_description.add_content(
                        dcc.stringWithLangType(
                            lang="es",
                            valueOf_=description
                        )
                    )
                    manufacturer_name = dcc.textType()
                    manufacturer_name.add_content(
                        dcc.stringWithLangType(
                            valueOf_=manufacturer
                        )
                    )
                    manufacturer = dcc.contactNotStrictType(
                        name=manufacturer_name)

                    identifications = dcc.identificationListType()
                    identification = dcc.identificationType(
                        issuer="manufacturer",
                        value=serialNumber)
                    identification_name = dcc.textType()
                    identification_name.add_content(
                        dcc.stringWithLangType(
                            lang="es",
                            valueOf_="Numero de serie"
                        )
                    )
                    identification.set_name(identification_name)
                    identifications.add_identification(identification)

                    item = dcc.itemType(name=item_name,
                                        manufacturer=manufacturer,
                                        model=model,
                                        identifications=identifications)
                    item.set_description(item_description)
                    items.add_item(item)
        elif name == '0K':
            description = cell[idx+1,'B'] +' '+cell[idx+1,'D']+'??C '+\
            cell[idx+2,'B'] + ' '+cell[idx+2,'D'] + '??C'
            items_description = dcc.richContentType()
            items_description.add_content(
                dcc.stringWithLangType(
                    lang="es",
                    valueOf_=description
                )
            )
            items.set_description(items_description)
        elif name == '0L':
            ID = {
                'INM':'inm',
                'Gerencia':'management',
                'Subgerencia':'assistantManagement',
                'Departamento':'inmDepartment',
                'Calle':'street',
                'N??mero':'streetNo',
                'Otro':'other',
                'CP':'postCode',
                'Partido':'department',
                'Provincia':'province',
                'Pa??s':'country',
                'Tel??fono 1':'phone1',
                'Tel??fono 2':'phone2',
                'Interno':'extensionNumber',
                'E-mail':'eMail'
            }

            for j in range(1,16):
                calibrationLaboratory_contact_location_further.add_content(
                    dcc.stringWithLangType(
                        id=ID[cell[idx+j,'B']],
                        valueOf_=cell[idx+j,'D']
                    )
                )
        elif name == '0M':
            # Usar para generar el pdf
            # Preguntar d??nde se ponen estos datos
            #adm_data[name] = (cell[idx,3],cell[idx+1,3])
            pass
        elif name == '0N':
            cname,management,assistantManager,department,\
            internalNameDepartment,street,number,other,pc,postOfficeBox,\
            department,province,country,phone1,phone2,email,countryCode,\
            adInfo = tuple(cell[idx+j,'D'] for j in range(1,19))
            phone = phone1 + ' / ' + phone2
            contact_name = dcc.textType()
            contact_name.add_content(
                dcc.stringWithLangType(
                    lang="es",
                    valueOf_=cname
                )
            )

            location = dcc.locationType(
                city=[department+', '+province],
                countryCode=[countryCode],
                postCode=[pc],
                postOfficeBox=[postOfficeBox],
                state=[country],
                street=[street],
                streetNo=[number],
                further=[calibrationLaboratory_contact_location_further]
                )
            contact = dcc.contactType(id=internalNameDepartment,
                                      name=contact_name,
                                      eMail=email,phone=phone,
                                      location=location)
            calibrationLaboratory.set_contact(contact)
        elif name == '0P':
            responsible,responsibleEmail,technician,\
            technicianEmail,signer,signerEmail = \
            tuple(cell[idx+j,'D'] for j in range(1,7))
            respPersons.add_respPerson(
                dcc.respPersonType(
                    id="Responsible",
                    person=dcc.contactNotStrictType(
                        name=dcc.textType(
                            content=[
                                dcc.stringWithLangType(
                                    valueOf_=responsible
                                    )
                                ]
                            ),
                        eMail=responsibleEmail
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
                                    valueOf_=technician
                                    )
                                ]
                            ),
                        eMail=technicianEmail
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
                                    valueOf_=signer
                                    )
                                ]
                            ),
                        eMail=signerEmail
                        )
                    )
                )
        elif name == '0Q':
            cname,street,number,other,pc,postOfficeBox,department,province,\
            country,phone1,phone2,email,countryCode,adInfo = \
            tuple(cell[idx+j,'D'] for j in range(1,15))
            customer_name = dcc.textType()
            customer_name.add_content(
                dcc.stringWithLangType(
                    lang="es",
                    valueOf_=cname
                )
            )

            further = dcc.textType()
            further.add_content(
                dcc.stringWithLangType(
                    valueOf_=phone2
                )
            )
            location = dcc.locationType(
                city=[department+', '+province],
                countryCode=[countryCode],
                postCode=[pc],
                postOfficeBox=[postOfficeBox],
                state=[country],
                street=[street],
                streetNo=[number],
                further=[further]
                )
            customer = dcc.contactType(name=customer_name,
                                      eMail=email,phone=phone1,
                                      location=location)

        elif name == '0S':
            # Hablar con Diego sobre cuales de estos campos van a pedir
            # MOSTRAR esquema y charlarlo.
            for i in range(idx, len(cell[:])-5,6):
                id,convention,norm,reference,declaration = \
                tuple(cell[i+j,'D'] for j in range(1,6))

                statement = dcc.statementMetaDataType()
                if id:
                    statement.set_id = id
                if convention:
                    statement.set_convention = convention
                if norm:
                    statement.set_norm = norm
                if reference:
                    statement.set_reference = reference
                if declaration:
                    statement_declaration = dcc.textType()
                    statement_declaration.add_content(
                        dcc.stringWithLangType(
                            lang="es",
                            valueOf_=declaration
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

def measurementResults(res_df, administrativeData_):

    """
    measurementResults():

    input:
    res_df (dataframe) => data retrieved from the spreadsheet to create the
    ring 2
    administrativeData_ (administrativeDataType) => some information from ring 1
    will be used in ring 2

    output: measurementResults_ (measurementResultListType) => ring 2


    name.add_prueba


    """
    #El d??a que lo presentemos va a ser lo mejor usar una jupyter notebook.
    #
    #https://www.ptb.de/dcc/v2.4.0/en/measurementResult/#tree-structure
    #
    #alrazonar las estructuras, hay que tener en cuenta que los m??todos
    #ya saben a que padre tiene que linkearse y no hace falta referenciarlos.
    #

    measurementResults_ = dcc.measurementResultListType()
    #creo un dcc:measurementResults

    measurementResult = dcc.measurementResultType(
        name=dcc.textType(content=[
            dcc.stringWithLangType(valueOf_="Resultados pt-100")]),
        usedSoftware=administrativeData_.get_dccSoftware())
    #creo un dcc:measurementResult

    usedMethods = dcc.usedMethodListType()
    #creo un dcc:usedMethods

    usedSoftware = dcc.softwareListType()
    #creo un dcc:usedSoftware

    influenceConditions = dcc.influenceConditionListType()
    #genero el influence conditions

    #influenceCondition = dcc.conditionType()
    #genero el influence condition

    results = dcc.resultListType()
    #genero el results

    #genero el result
    result = dcc.resultType(data=dcc.dataType())

    #
    #arriba genero todos los elementos ppales
    #

    # Gets the used languages from the ring 1. This a first approach.
    # Retrieves the first language that will be used.
    # In the future, this will get the whole list.
    lang = administrativeData_.get_coreData().get_usedLangCodeISO639_1()[0]

    cell = res_df.loc
    #modifico el df para leer las columnas con n??meros y no letras desde cell[]

    table = {item:idx for idx,item in enumerate(cell[:,'A']) if item in CONST}
    #asigno una tabla de ??ndices(row-1) respecto a cada asignaci??n {??ndice = [n??mero|letra]}

    for name, idx in table.items():
        #itero todos los items de la tabla uqe gener?? antes: 0A, 0B, 0C ...
        if name == '0A':
            usedMethod_name = dcc.textType()
            usedMethod_name.add_content(
            #al name que cree le agrego el dcc:content
                dcc.stringWithLangType(
                    lang=lang,
                    #para cuando haya mas de un idioma.
                    #el idioma deber??a ser un vector.
                    valueOf_=cell[idx,'B']
                    #agrega el valor de "Met..." dentro del contenido
                )
            )

            usedMethod_description = dcc.richContentType()
            #agrego dcc:description al method a usedMethod

            usedMethod_description.add_content(
                dcc.stringWithLangType(
                    lang=lang,
                    valueOf_=cell[idx,'D']
                )
            )

            usedMethod = dcc.usedMethodType(
                name=usedMethod_name,
                description=usedMethod_description
                )
            usedMethods.add_usedMethod(usedMethod)
        elif name == '0B':
            influenceCondition_name = dcc.textType()
            influenceCondition_name.add_content(
                dcc.stringWithLangType(
                    valueOf_=cell[idx,'B']
                )
            )
            data_text = dcc.richContentType()
            data_text.add_content(
                dcc.stringWithLangType(
                    lang=lang,
                    valueOf_=cell[idx,'D']
                )
            )
            data = dcc.dataType(text=[data_text])
            influenceCondition = dcc.conditionType(
                name=influenceCondition_name,
                data=data
                )
            influenceConditions.add_influenceCondition(influenceCondition)

        elif name == '0C':
            influenceCondition_name = dcc.textType()
            influenceCondition_name.add_content(
                dcc.stringWithLangType(
                    valueOf_=cell[idx,'B']
                )
            )
            data = dcc.dataType()
            from_, to = cell[idx+1,'C'], cell[idx+1, 'D']
            for i in range(2):
                j = idx+i+2
                name,lower_value,upper_value,uncertainty,unit = cell[j,'B':'F']

                list_ = dcc.listType1(
                    name=dcc.textType(
                        content=[
                            dcc.stringWithLangType(lang=lang,valueOf_=name)
                            ]
                        )
                    )

                for bound,value in [(from_,lower_value), (to,upper_value)]:
                    if value:
                        quantity_name = dcc.textType()
                        quantity_name.add_content(
                            dcc.stringWithLangType(
                                lang=lang,
                                valueOf_=bound
                            )
                        )
                        expandedUnc = SI_Format.expandedUncType(uncertainty=uncertainty,
                                                            coverageFactor=2,
                                                            coverageProbability=0.95)
                        real = SI_Format.realQuantityType(value=value,
                                              unit=unit,
                                              expandedUnc=expandedUnc)
                        quantity = dcc.quantityType(name=quantity_name,real=real)
                        list_.add_quantity(quantity)
                data.add_list(list_)

            influenceCondition = dcc.conditionType(name=influenceCondition_name,
                                                   data=data)
            influenceCondition.set_data(data)
            influenceConditions.add_influenceCondition(influenceCondition)
        elif name == '0D':
            data = result.get_data()
            description_name = dcc.richContentType()
            description_name.add_content(
                dcc.stringWithLangType(
                    lang=lang,
                    valueOf_=cell[idx+1,'B']
                )
            )
            description = dcc.richContentType(name=description_name)
            description.add_formula(dcc.formulaType(latex=cell[idx+2,'E']))
            for j in range(4,10):
                var,_,value,unit,des = cell[idx+j,'B':'F']

                quantity = dcc.quantityType(
                    description=dcc.richContentType(
                        formula=[dcc.formulaType(latex=var)]),
                    real=SI_Format.realQuantityType(
                        value=value,
                        unit=unit
                        )
                    )
                data.add_quantity(quantity)
            result.set_description(description)

        elif name == '0E':
            quantity,u = cell[idx+2,'B'],cell[idx+1,'E']
            lower_value,upper_value,uncertainty,unit=cell[idx+2,'C':'F']
            usedMethod = dcc.usedMethodType(
                name=dcc.textType(
                    content=[
                        dcc.stringWithLangType(
                            lang=lang,
                            valueOf_=cell[idx,'B']
                        )
                    ]
                ),
                description=dcc.richContentType(
                    formula=[
                        dcc.formulaType(
                            latex="\SI{{{}}}{{{}}} \( \leq \) {} \( \leq \)" \
                            "\SI{{{}}}{{{}}} \\\ {} = \SI{{+-{}}}{{{}}}"
                            .format(lower_value,unit,quantity,upper_value,unit,
                                    u,uncertainty,unit)
                            )
                        ]
                    )
                )
            usedMethods.add_usedMethod(usedMethod)

        elif name == '0F':
            k, prob = cell[idx,'I'],cell[idx+1,'I']
            data = result.get_data()
            list_ = dcc.listType1()
            for j in range(idx+2, len(res_df)):
                temperature,resistance,uncertainty = \
                cell[j,'D'],cell[j,'E'],cell[j,'F']

                quantity1 = dcc.quantityType(
                    real=SI_Format.realQuantityType(
                        value=temperature,
                        unit=DEGREECELSIUS
                        )
                    )

                quantity2 = dcc.quantityType(
                    real=SI_Format.realQuantityType(
                        value=resistance,
                        unit=OHM,
                        expandedUnc=SI_Format.expandedUncType(
                            uncertainty=uncertainty,
                            coverageFactor=k,
                            coverageProbability=prob
                            )
                        )
                    )

                innerList = dcc.listType1(quantity=[quantity1,quantity2])
                list_.add_list(innerList)
            data.add_list(list_)

            result_name = dcc.textType()
            result_name.add_content(
                dcc.stringWithLangType(
                    lang=lang,
                    valueOf_=cell[idx,'B']
                )
            )
            result.set_name(result_name)
            results.add_result(result)

    measurementResult.set_usedMethods(usedMethods)
    measurementResult.set_influenceConditions(influenceConditions)
    measurementResult.set_results(results)

    measurementResults_.add_measurementResult(measurementResult)
    return measurementResults_


def comment(com_df):
    cell = com_df.loc
    title = cell[0,'A']
    comment_ = dcc.commentType()
    statements = statement.statements(title=title)
    allow_substatement = False
    for j in range(1,cell[:,'A'].size):
        lvl1,lvl2 = cell[j,'B':'C']
        if lvl1:
            #add new statement
            statements.add_statement(statement.statementType(content=lvl1))
            allow_substatement = True
        elif allow_substatement:
            if lvl2:
                #add new substatement
                statements.get_statement()[-1].add_statement(
                    statement.statementType(content=lvl2))
            else:
                allow_substatement = False

    comment_.add_anytypeobjs_(statements)
    return comment_

def change_dtype(value):
    if not isinstance(value, datetime.datetime):
        return str(value)
    else:
        return value

def read(file_path):
    # Lee la primera hoja del excel. Devuelve la informacion
    # en un dataframe de pandas.
    adm_df = pd.read_excel(file_path,
                           sheet_name='Administrativo',
                           header=None,
                           usecols="A:G",
                           names=['A','B','C','D','E','F','G'])

    adm_df = adm_df.replace(np.nan, '', regex=True)
    adm_df.loc[:, 'D'] = adm_df['D'].apply(change_dtype)

    # Lee la segunda hoja del excel.
    res_df = pd.read_excel(file_path,
                           sheet_name="Resultados",
                           header=None,
                           usecols="A:J",
                           names=['A','B','C','D','E','F','G','H','I','J'])
    res_df = res_df.replace(np.nan, '', regex=True)

    com_df = pd.read_excel(file_path,
                           sheet_name="Comentarios",
                           header=None,
                           usecols="A:C",
                           names=['A','B','C'])
    com_df = com_df.replace(np.nan, '', regex=True)

    return adm_df,res_df,com_df

def main():
    # Toma el nombre de archivo como argumento
    if len(sys.argv) == 2:
        file_name = sys.argv[1]
    else:
        file_name = 'Certificado.ods'

    # Lee spreadsheet
    adm_df,res_df,com_df = read(file_name)

    # Genera el administrativeData
    administrativeData_ = administrativeData(adm_df)

    # Genera el measurementResults
    measurementResults_ = measurementResults(res_df, administrativeData_)

    # Genera el comment
    comment_ = comment(com_df)

    # Integra toda la informacion del administrativeData y measurementResults
    # para generar el digitalCalibrationCertificate
    digitalCalibrationCertificate = dcc.digitalCalibrationCertificateType(
        schemaVersion="3.0.0",
        administrativeData=administrativeData_,
        measurementResults=measurementResults_,
        comment=comment_
    )
    nsmap_ = {
        'dcc' : 'https://ptb.de/dcc',
        'xsi' : 'http://www.w3.org/2001/XMLSchema-instance',
        'si' : 'https://ptb.de/si',
        'ext' : 'extension'
    }
    name_ = 'digitalCalibrationCertificate'
    NS = "http://www.w3.org/2001/XMLSchema-instance"

    # Pasa la estructura de objetos anidados a un objeto Element (Element API)
    elem = digitalCalibrationCertificate.to_etree(name_=name_,nsmap_=nsmap_)

    # Agrega el schemaLocation al xml
    elem.attrib['{{{pre}}}schemaLocation'.format(pre=NS)] = \
    'https://ptb.de/dcc https://ptb.de/dcc/v3.0.0/dcc.xsd'

    # Genera el xml
    tree = etree.ElementTree(elem)
    tree.write('dcc.xml', encoding='UTF-8',
                              xml_declaration=True,
                              pretty_print=True)

if __name__ == '__main__':
    main()
