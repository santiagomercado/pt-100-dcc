<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
                xmlns:dcc="https://ptb.de/dcc"
                xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                xmlns:si="https://ptb.de/si"
                xmlns:ext="extension"
                version="1.0">
    <xsl:strip-space elements="*"/>
    <xsl:output method="text" encoding="UTF-8" indent="no" omit-xml-declaration="yes"/>

    <xsl:template match="/">
      <xsl:text>
        \documentclass[a4paper]{article}
        \usepackage[includeheadfoot,
                    left=1.5cm,
                    right=1.5cm,
                    top=1.5cm,
                    bottom=1.5cm,
                    headheight=90pt,
                    ]{geometry}
        \usepackage{longtable}
        \usepackage{tabularx}
        \usepackage{lastpage}
        \usepackage{siunitx}
        \usepackage{fancyhdr}
        \usepackage{graphicx}
        \usepackage{enumitem}
        \usepackage{datetime2}
        \usepackage[utf8x]{inputenc}

        \usepackage[defaultfam,tabular]{montserrat}
        \usepackage[T1]{fontenc}

        \usepackage{enumitem}
        \setlist[enumerate]{label*=\arabic*.}
        \usepackage{array}
        \graphicspath{{./assets/}}
        \DTMsetup{datesep=/}
        \sisetup{locale = FR}
        \renewcommand{\headrulewidth}{0px}
        \renewcommand{\footrulewidth}{0px}
        \fancyhf{}

        \fancypagestyle{style1}{%
            \fancyhead[L]{\includegraphics[width=\textwidth]{header.png}
                          \Large{\textbf{Certificado de Calibraci\'on}}}
            \fancyhead[R]{\text{</xsl:text><xsl:value-of select="/dcc:digitalCalibrationCertificate/dcc:administrativeData/dcc:coreData/dcc:uniqueIdentifier" /><xsl:text>}\\P\'agina \thepage\ de \pageref{LastPage}}
            \fancyfoot[L]{\includegraphics[width=\textwidth]{footer.png}}
            \setlength{\footskip}{48pt}
        }

        \fancypagestyle{style2}{%
            \fancyhead[L]{}
            \fancyhead[L]{\includegraphics[width=\textwidth]{header.png}}
        }

        \begin{document}
        \pagestyle{style1}
        </xsl:text>
        <xsl:apply-templates select="/dcc:digitalCalibrationCertificate/dcc:administrativeData"/>
        <xsl:text>
        \noindent
        Buenos Aires, 12 de Junio de 2020.(hardcodeado)
        \newpage
        \begin{center}
        \includegraphics[width=\textwidth]{clause.png}
        \end{center}
        \newpage
        \pagestyle{style2}
        </xsl:text>
        <xsl:apply-templates select="/dcc:digitalCalibrationCertificate/dcc:measurementResults/dcc:measurementResult/dcc:usedMethods"/>
        <xsl:apply-templates select="/dcc:digitalCalibrationCertificate/dcc:measurementResults/dcc:measurementResult/dcc:influenceConditions"/>
        <xsl:apply-templates select="/dcc:digitalCalibrationCertificate/dcc:measurementResults/dcc:measurementResult/dcc:results"/>
        <xsl:text>
        \section*{</xsl:text><xsl:value-of select="/dcc:digitalCalibrationCertificate/dcc:measurementResults/dcc:measurementResult/dcc:results/dcc:result/dcc:name/dcc:content"/><xsl:text>}
        \begin{center}
        \begin{longtable}{|S[table-format=4.4]|S[table-format=4.4]|S[table-format=4.4]|}
        \hline \multicolumn{1}{|c|}{\textbf{Temperatura [\si{\degreeCelsius}]}} &amp; \multicolumn{1}{c|}{\textbf{Resistencia [\si{\ohm}]}} &amp; \multicolumn{1}{c|}{\textbf{Incertidumbre [\si{\ohm}]}} \\ \hline
        \endfirsthead
        \endhead
        \endfoot
        \endlastfoot
      </xsl:text>
      <xsl:for-each select="/dcc:digitalCalibrationCertificate/dcc:measurementResults/dcc:measurementResult/dcc:results/dcc:result/dcc:data/dcc:list/dcc:list">
        <xsl:variable name = "first-val" select="dcc:quantity[1]/si:real/si:value"/>
        <xsl:variable name = "second-val" select="dcc:quantity[2]/si:real/si:value"/>
        <xsl:variable name = "third-val" select="dcc:quantity/si:real/si:expandedUnc/si:uncertainty"/>
          <xsl:value-of select="$first-val"/><xsl:text>&amp;</xsl:text><xsl:value-of select="$second-val"/><xsl:text>&amp;</xsl:text><xsl:value-of select="$third-val"/><xsl:text>\\ \hline</xsl:text>
      </xsl:for-each>
      <xsl:text>
      \end{longtable}
      \end{center}
      </xsl:text>
      <xsl:apply-templates select="/dcc:digitalCalibrationCertificate/dcc:measurementResults/dcc:measurementResult/dcc:results"/>
      <xsl:apply-templates select="/dcc:digitalCalibrationCertificate/dcc:comment/ext:statements"/>
      <xsl:text>
        \newpage
        \input{./assets/lastpage.tex}
      \end{document}
      </xsl:text>
    </xsl:template>


<xsl:template match = "dcc:customer">
  <xsl:text>
  \textbf{Solicitante} &amp; \csname @minipagetrue\endcsname
  \begin{itemize}[label={},noitemsep,leftmargin=*,topsep=0pt,partopsep=0pt]
      \item \textbf{\uppercase{</xsl:text><xsl:value-of select="dcc:name/dcc:content"/><xsl:text>}}
      \item </xsl:text><xsl:value-of select="concat('Calle',' ',dcc:location/dcc:street, ' ', 'N°', dcc:location/dcc:streetNo)" /><xsl:text>
      \item </xsl:text><xsl:value-of select="dcc:location/dcc:city" /><xsl:text>
  \end{itemize}\\
  </xsl:text>
</xsl:template>

<xsl:template match="dcc:administrativeData">
  <xsl:text>
  \noindent
  \begin{tabularx}{\columnwidth}{l X}</xsl:text>
    <xsl:apply-templates select="dcc:items/dcc:item"/>
    <xsl:apply-templates select="dcc:items"/>
    <xsl:apply-templates select="dcc:coreData"/>
    <xsl:apply-templates select="dcc:customer"/>
    <xsl:apply-templates select="dcc:calibrationLaboratory"/><xsl:text>
  \end{tabularx}
  </xsl:text>
</xsl:template>

<xsl:template match="dcc:items">
  <xsl:text>
  \textbf{Determinaciones requeridas} &amp; \csname @minipagetrue\endcsname
  \begin{itemize}[label={},noitemsep,leftmargin=*,topsep=0pt,partopsep=0pt]
      \item </xsl:text><xsl:value-of select="dcc:description"/><xsl:text>
  \end{itemize}\\</xsl:text>
</xsl:template>

<xsl:template match="dcc:item">
  <xsl:text>
    \textbf{Elemento} &amp; \csname @minipagetrue\endcsname
      \begin{itemize}[label={},noitemsep,leftmargin=*,topsep=0pt,partopsep=0pt]
        \item \textbf{Objeto:} \text{</xsl:text><xsl:value-of select="dcc:name/dcc:content"/><xsl:text>}
        \item \textbf{Fabricante/Marca:} \text{</xsl:text><xsl:value-of select="dcc:manufacturer/dcc:name/dcc:content"/><xsl:text>}
        \item \textbf{Modelo/Número de serie:} \text{</xsl:text><xsl:value-of select="dcc:model"/><xsl:text>/</xsl:text><xsl:value-of select="dcc:identifications/dcc:identification/dcc:value"/><xsl:text>}
        \item \textbf{Id. del usuario:} \text{item 96 (hardcodeado)}
      \end{itemize}\\
  </xsl:text>
</xsl:template>

<xsl:template match="dcc:coreData">
  <xsl:text>
    \textbf{Fecha de recepción} &amp; \csname @minipagetrue\endcsname
      \begin{itemize}[label={},noitemsep,leftmargin=*,topsep=0pt,partopsep=0pt]
        \item {\DTMsetdatestyle{ddmmyyyy}\DTMdate{</xsl:text><xsl:value-of select="dcc:receiptDate"/><xsl:text>}}
      \end{itemize}\\

      \textbf{Fecha de calibración} &amp; \csname @minipagetrue\endcsname
      \begin{itemize}[label={},noitemsep,leftmargin=*,topsep=0pt,partopsep=0pt]
          \item Desde {\DTMsetdatestyle{ddmmyyyy}\DTMdate{</xsl:text><xsl:value-of select="dcc:beginPerformanceDate"/><xsl:text>}} hasta
          {\DTMsetdatestyle{ddmmyyyy}\DTMdate{</xsl:text><xsl:value-of select="dcc:endPerformanceDate"/><xsl:text>}}
      \end{itemize}\\
  </xsl:text>
</xsl:template>

<xsl:template match="dcc:contact">
  <xsl:variable name="performanceLocation" select="dcc:location/dcc:further/dcc:content"/>
  <xsl:text>
    \textbf{Lugar de realización} &amp; \csname @minipagetrue\endcsname
      \begin{itemize}[label={},noitemsep,leftmargin=*,topsep=0pt,partopsep=0pt]
        \item </xsl:text><xsl:value-of select="concat(
        $performanceLocation[@id='inm'],'-',
        $performanceLocation[@id='management'],'-',
        $performanceLocation[@id='assistantManagement'],'-',
        $performanceLocation[@id='inmDepartment'])" /><xsl:text>

        \item </xsl:text><xsl:value-of select="concat(
        $performanceLocation[@id='street'],' ',
        $performanceLocation[@id='streetNo'],', ',
        $performanceLocation[@id='other'],' [CP ',
        $performanceLocation[@id='postCode'], '] ')" /><xsl:text>

        \item </xsl:text><xsl:value-of select="concat(
        $performanceLocation[@id='department'],', ',
        $performanceLocation[@id='province'],', ',
        $performanceLocation[@id='country'])" /><xsl:text>

        \item </xsl:text><xsl:value-of select="concat(
        'Teléfono: ',
        $performanceLocation[@id='phone1'],' / ',
        $performanceLocation[@id='phone2'],' (interno ',
        $performanceLocation[@id='extensionNumber'],')')"/><xsl:text>

        \item </xsl:text><xsl:value-of select="concat('E-mail: ',
        $performanceLocation[@id='eMail'])"/><xsl:text>

      \end{itemize}\\
  </xsl:text>
</xsl:template>

<xsl:template match="dcc:usedMethods">
  <xsl:text>\section*{Metodología Empleada}</xsl:text>
  <xsl:apply-templates match="dcc:usedMethod"/>
</xsl:template>

<xsl:template match="dcc:usedMethod">
  <xsl:text>
    \section*{</xsl:text><xsl:value-of select="dcc:name/dcc:content"/><xsl:text>}
  </xsl:text>
  <xsl:value-of select="dcc:description/dcc:content"/>
  <xsl:value-of select="dcc:description/dcc:formula/dcc:latex"/>
</xsl:template>

<xsl:template match="dcc:influenceConditions">
  <xsl:text>\section*{Condiciones de Influencia}</xsl:text>
  <xsl:apply-templates match="dcc:influenceCondition"/>
</xsl:template>

<xsl:template match="dcc:influenceCondition">
  <xsl:text>
    \section*{</xsl:text><xsl:value-of select="dcc:name/dcc:content"/><xsl:text>}</xsl:text>
    <xsl:value-of select="dcc:data/dcc:text/dcc:content"/>
    <xsl:for-each select="dcc:data/dcc:list">
      <xsl:variable name = "quantity" select="dcc:name/dcc:content"/>
      <xsl:variable name = "from" select = "dcc:quantity/dcc:name/dcc:content[text() = 'Desde']/../../si:real/si:value"/>
      <xsl:variable name = "to" select = "dcc:quantity/dcc:name/dcc:content[text() = 'Hasta']/../../si:real/si:value"/>
      <xsl:variable name = "unit" select = "dcc:quantity/si:real/si:unit"/>
      <xsl:if test="$from">
        <xsl:value-of select="concat('\SI{',$from,'}{',$unit,'} ')"/>
        <xsl:text disable-output-escaping="yes">\(<![CDATA[<]]>\)</xsl:text>
      </xsl:if>
      <xsl:value-of select="concat(' ',$quantity,' ')"/>
      <xsl:if test="$to">
        <xsl:text disable-output-escaping="yes">\(<![CDATA[<]]>\)</xsl:text>
        <xsl:value-of select="concat(' \SI{',$to,'}{',$unit,'}\\')"/>
      </xsl:if>
    </xsl:for-each>
</xsl:template>

<xsl:template match="dcc:results">
  <xsl:text>\section*{Resultados}</xsl:text>
  <xsl:apply-templates match="dcc:result"/>
</xsl:template>

<xsl:template match="dcc:result">
  <xsl:value-of select="dcc:description/dcc:name/dcc:content"/>
  <xsl:text>\\[5pt] \[</xsl:text>
  <xsl:value-of select="dcc:description/dcc:formula/dcc:latex"/>
  <xsl:text>\] \\</xsl:text>
  <xsl:for-each select="dcc:data/dcc:quantity">
    <xsl:variable name = "var" select="dcc:description/dcc:formula/dcc:latex"/>
    <xsl:variable name = "val" select="si:real/si:value"/>
    <xsl:variable name = "unit" select="si:real/si:unit"/>
      <xsl:text>\(</xsl:text>
      <xsl:value-of select="$var"/><xsl:text> = \SI{</xsl:text><xsl:value-of select="$val"/><xsl:text>}{</xsl:text><xsl:value-of select="$unit"/><xsl:text>} \) \\</xsl:text>
  </xsl:for-each>
</xsl:template>


<xsl:template match="dcc:comment">
  <xsl:apply-templates select="ext:statements"/>
</xsl:template>


<xsl:template match="ext:statements">
  <xsl:text>\section*{</xsl:text><xsl:value-of select="ext:title"/><xsl:text>}</xsl:text>
  <xsl:apply-templates select="ext:statement"/>
</xsl:template>

<xsl:template match="ext:statement">
  <xsl:text>
    \begin{enumerate}
    \item[]</xsl:text><xsl:value-of select="ext:content"/>
    <xsl:apply-templates select="ext:statement"/>
    <xsl:text>
      \end{enumerate}
    </xsl:text>
</xsl:template>

</xsl:stylesheet>
