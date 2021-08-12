<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
                xmlns:dcc="https://ptb.de/dcc"
                xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                xmlns:si="https://ptb.de/si"
                version="1.0">
    <xsl:strip-space elements="*" />
    <xsl:output method="xml" encoding="UTF-8" indent="yes"/>


    <xsl:template match="node()|@*">
      <xsl:copy>
        <xsl:apply-templates select="node()|@*"/>
      </xsl:copy>
    </xsl:template>

    <xsl:template match="si:unit|dcc:latex">
      <xsl:copy-of select="."/>
    </xsl:template>

    <xsl:template match="text()">
      <xsl:call-template name="string-replace-all">
          <xsl:with-param name="text" select="." />
      </xsl:call-template>
    </xsl:template>

    <xsl:template name="string-replace-all">
        <xsl:param name="text" />
        <xsl:variable name="head" select="substring($text, 1, 1)"/>
      <xsl:if test=" $head != '' ">
        <xsl:choose>
            <xsl:when test="$head = '#' ">
                <xsl:value-of select=" '\#' " />
            </xsl:when>

            <xsl:when test="$head = '$' ">
                <xsl:value-of select=" '\textdollar' " />
            </xsl:when>

            <xsl:when test="$head = '%' ">
                <xsl:value-of select=" '\percent' " />
            </xsl:when>

            <xsl:when test="$head = '&amp;' ">
                <xsl:value-of select=" '\&amp;' " />
            </xsl:when>

            <xsl:when test="$head = '\' ">
                <xsl:value-of select=" '\textbackslash ' " />
            </xsl:when>

            <xsl:when test="$head = '^' ">
                <xsl:value-of select=" '\textcircumflex ' " />
            </xsl:when>

            <xsl:when test="$head = '_'">
                <xsl:value-of select=" '\textunderscore ' " />
            </xsl:when>

            <xsl:when test="$head = '{'">
                <xsl:value-of select=" '\textbraceleft ' " />
            </xsl:when>

            <xsl:when test="$head = '|'">
                <xsl:value-of select=" '\textbar ' " />
            </xsl:when>

            <xsl:when test="$head = '}'">
                <xsl:value-of select="'\textbraceright '" />
            </xsl:when>

            <xsl:when test="$head = '~'">
                <xsl:value-of select="'\textasciitilde '" />
            </xsl:when>

            <xsl:otherwise>
                <xsl:value-of select="$head" />
            </xsl:otherwise>
        </xsl:choose>
        <xsl:call-template name="string-replace-all">
            <xsl:with-param name="text" select="substring-after($text,$head)" />
        </xsl:call-template>
    </xsl:if>
    </xsl:template>

</xsl:stylesheet>
