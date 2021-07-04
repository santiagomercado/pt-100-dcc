from schemas.dcc.v3_0_0_rc_4 import dcc
from schemas.SI_Format.v2_0_0 import SI_Format
import sys
from lxml import etree
import xml.etree.ElementTree as ET
import pandas as pd

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
    customer = dcc.contactType()
    statements = dcc.statementListType()

    cell = adm_df.iloc
    table = {item:idx for idx,item in enumerate(cell[:,0]) if item in CONST}
    for name, idx in table.items():
        if name == '0A':
            usedSoftware,version = cell[idx,3],cell[idx+1,6]
            software_name = dcc.textType()
            software_name.add_content(
                dcc.stringWithLangType(
                    lang="en",
                    valueOf_=usedSoftware
                    )
            )
            software = dcc.softwareType(name=software_name,
                                        release=str(version)[1:])
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
            type,cc,certificateNumber,part,total = tuple(
                cell[idx+j,3 if j not in (1,2) else 6] for j in range(5)
                )
            uniqueIdenPrefix = type+' '+('0'*(8-len(cc)))+cc+'-'+\
                               ('0'*(8-len(certificateNumber)))+\
                               certificateNumber+' '
            if part == 'Único':
                coreData.set_uniqueIdentifier(uniqueIdenPrefix+part)
            else:
                coreData.set_uniqueIdentifier(uniqueIdenPrefix+'Parcial '+
                                              str(part)+' de '+
                                              str(total))
        elif name == '0F':
            coreData.set_receiptDate(cell[idx,3])
        elif name == '0G':
            coreData.set_beginPerformanceDate(cell[idx+1,3])
            coreData.set_endPerformanceDate(cell[idx+2,3])
        elif name == '0H':
            object,description = cell[idx+1,3],cell[idx+2,3]
            if not pd.isna(object):
                items_name = dcc.textType()
                items_name.add_content(
                    dcc.stringWithLangType(
                        valueOf_=object
                        )
                    )
                items.set_name(items_name)
            if not pd.isna(description):
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
            tuple(
                cell[idx+j,3
                     if j not in (2,3,4,5,6,10,11) else 6] for j in range(1,15)
                )
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
                t = tuple(
                    cell[i+j,3 if j not in (6,7) else 6] for j in range(1,9)
                    )
                object,description,adInfo,manufacturer,\
                brand,model,serialNumber,userId = \
                tuple(
                    cell[i+j,3 if j not in (6,7) else 6] for j in range(1,9)
                    )
                if not(pd.isna(object) or pd.isna(description) or
                       pd.isna(manufacturer) or pd.isna(serialNumber)):
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

                    item = dcc.itemType(name=item_name,manufacturer=manufacturer,
                                        model=model,
                                        identifications=identifications)
                    item.set_description(item_description)
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
            cname,management,assistantManager,department,\
            internalNameDepartment,street,number,other,pc,postOfficeBox,\
            department,province,country,phone1,phone2,email,countryCode,\
            adInfo = \
            tuple(
                cell[idx+j,3 if j not in (7,9,10) else 6] for j in range(1,19)
                )
            contact_name = dcc.textType()
            contact_name.add_content(
                dcc.stringWithLangType(
                    lang="es",
                    valueOf_=cname
                )
            )

            further = dcc.textType()
            for data in [department,phone2,other,management,assistantManager]:
                further.add_content(
                    dcc.stringWithLangType(
                        valueOf_=data
                    )
                )

            location = dcc.locationType(
                city=[province+', '+department],
                countryCode=[countryCode],
                postCode=[pc],
                postOfficeBox=[postOfficeBox],
                state=[country],
                street=[street],
                streetNo=[number],
                further=[further]
                )
            contact = dcc.contactType(id=internalNameDepartment,
                                      name=contact_name,
                                      eMail=email,phone=phone1,
                                      location=location)
            calibrationLaboratory.set_contact(contact)
        elif name == '0P':
            responsible,responsibleEmail,technician,\
            technicianEmail,signer,signerEmail = \
            tuple(cell[idx+j,3] for j in range(1,7))
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
            tuple(
                cell[idx+j,3
                     if j not in (2,3,4,5,6,10,11) else 6] for j in range(1,15)
                )
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
                city=[province+\
                      ', '+department],countryCode=[countryCode],
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
                tuple(cell[i+j,3] for j in range(1,6))

                statement = dcc.statementMetaDataType()
                if not pd.isna(id):
                    statement.set_id = id
                if not pd.isna(convention):
                    statement.set_convention = convention
                if not pd.isna(norm):
                    statement.set_norm = norm
                if not pd.isna(reference):
                    statement.set_reference = reference
                if not pd.isna(declaration):
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

# res_df y administrativeData_ no se usan pq el measurementResult que genero
# es apartir de todos datos hardcodeados.
def measurementResults(res_df, administrativeData_):

    DCC_PREFIX = "{https://ptb.de/dcc}"
    SI_PREFIX = "{https://ptb.de/si}"
    CONTENT = "content"
    SOME_TEXT = "some text"
    NUMBER = "4"

    #measurementResults = etree.SubElement(dcc, DCC_PREFIX+"measurementResults")
    measurementResults_ = etree.Element(DCC_PREFIX+"measurementResults")
    measurementResult = etree.SubElement(measurementResults_, DCC_PREFIX+"measurementResult")
    name = etree.SubElement(measurementResult, DCC_PREFIX+"name")
    etree.SubElement(name, DCC_PREFIX+CONTENT).text = SOME_TEXT
    usedMethods = etree.SubElement(measurementResult, DCC_PREFIX+"usedMethods")
    usedMethod = etree.SubElement(usedMethods, DCC_PREFIX+"usedMethod")
    name = etree.SubElement(usedMethod, DCC_PREFIX+"name")
    etree.SubElement(name, DCC_PREFIX+CONTENT, lang="es").text = SOME_TEXT
    description = etree.SubElement(usedMethod, DCC_PREFIX+"description")
    etree.SubElement(description, DCC_PREFIX+CONTENT, lang="es").text = SOME_TEXT
    usedSoftware = etree.SubElement(measurementResult, DCC_PREFIX+"usedSoftware")
    software = etree.SubElement(usedSoftware, DCC_PREFIX+"software")
    name = etree.SubElement(software, DCC_PREFIX+"name")
    etree.SubElement(name, DCC_PREFIX+CONTENT).text = SOME_TEXT
    release = etree.SubElement(software, DCC_PREFIX+"release").text = SOME_TEXT

    influenceConditions = etree.SubElement(measurementResult, DCC_PREFIX+"influenceConditions")
    influenceCondition = etree.SubElement(influenceConditions, DCC_PREFIX+"influenceCondition")
    name = etree.SubElement(influenceCondition, DCC_PREFIX+"name")
    etree.SubElement(name, DCC_PREFIX+CONTENT, lang="es").text = SOME_TEXT
    data = etree.SubElement(influenceCondition, DCC_PREFIX+"data")
    list = etree.SubElement(data, DCC_PREFIX+"list")
    name = etree.SubElement(list, DCC_PREFIX+"name")
    etree.SubElement(name, DCC_PREFIX+CONTENT, lang="es").text = SOME_TEXT
    list = etree.SubElement(list, DCC_PREFIX+"list", id="temperature")
    name = etree.SubElement(list, DCC_PREFIX+"name")
    etree.SubElement(name, DCC_PREFIX+CONTENT, lang="es").text = "temperature"

    quantity = etree.SubElement(list, DCC_PREFIX+"quantity")
    name = etree.SubElement(quantity, DCC_PREFIX+"name")
    etree.SubElement(name, DCC_PREFIX+CONTENT, lang="es").text = "Temperatura >"
    real = etree.SubElement(quantity, SI_PREFIX+"real")
    value = etree.SubElement(real, SI_PREFIX+"value").text = NUMBER
    unit = etree.SubElement(real, SI_PREFIX+"unit").text = "\degreeCelsius"
    expandedUnc = etree.SubElement(real, SI_PREFIX+"expandedUnc")
    etree.SubElement(expandedUnc, SI_PREFIX+"uncertainty").text = "0.5"
    etree.SubElement(expandedUnc, SI_PREFIX+"coverageFactor").text = "2"
    etree.SubElement(expandedUnc, SI_PREFIX+"coverageProbability").text = "0.95"

    quantity = etree.SubElement(list, DCC_PREFIX+"quantity")
    name = etree.SubElement(quantity, DCC_PREFIX+"name")
    etree.SubElement(name, DCC_PREFIX+CONTENT, lang="es").text = "Temperatura <"
    real = etree.SubElement(quantity, SI_PREFIX+"real")
    value = etree.SubElement(real, SI_PREFIX+"value").text = NUMBER
    unit = etree.SubElement(real, SI_PREFIX+"unit").text = "\degreeCelsius"
    expandedUnc = etree.SubElement(real, SI_PREFIX+"expandedUnc")
    etree.SubElement(expandedUnc, SI_PREFIX+"uncertainty").text = "0.5"
    etree.SubElement(expandedUnc, SI_PREFIX+"coverageFactor").text = "2"
    etree.SubElement(expandedUnc, SI_PREFIX+"coverageProbability").text = "0.95"

    results = etree.SubElement(measurementResult, DCC_PREFIX+"results")
    result = etree.SubElement(results, DCC_PREFIX+"result")
    name = etree.SubElement(result, DCC_PREFIX+"name")
    etree.SubElement(name, DCC_PREFIX+CONTENT, lang="es").text = \
    "Conventional mass and maximum permissible error corresponding to OIML R 111"

    data = etree.SubElement(result, DCC_PREFIX+"data", id="OIML_R_111")
    list = etree.SubElement(data, DCC_PREFIX+"list")
    quantity = etree.SubElement(list, DCC_PREFIX+"quantity")
    name = etree.SubElement(quantity, DCC_PREFIX+"name")
    etree.SubElement(name, DCC_PREFIX+CONTENT, lang="es").text = "Nominal value"
    noQuantity = etree.SubElement(quantity, DCC_PREFIX+"noQuantity")
    etree.SubElement(noQuantity, DCC_PREFIX+CONTENT).text = "10 g"

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
    measurementResults_ = measurementResults(res_df, administrativeData_)

    # Comienzo a crear el dcc
    digitalCalibrationCertificate = dcc.digitalCalibrationCertificateType(
        schemaVersion="3.0.0-rc.4",
        administrativeData=administrativeData_
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

    # Integro el measurementResult_ (tipo lxml Element) al Element del dcc
    elem.append(measurementResults_)
    tree = etree.ElementTree(elem)
    tree.write('dcc.xml', encoding='UTF-8',
                              xml_declaration=True,
                              pretty_print=True)

if __name__ == '__main__':
    main()
