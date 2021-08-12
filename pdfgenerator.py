import lxml.etree as ET
import subprocess


dom1 = ET.parse("dcc.xml")
xslt1 = ET.parse("XSLT/character_escaping.xsl")
transform1 = ET.XSLT(xslt1)
newdom1 = transform1(dom1)
newdom1.write_output("xml_temp.xml")

dom2 = ET.parse("xml_temp.xml")
xslt2 = ET.parse("XSLT/XML2LaTeX.xsl")
transform2 = ET.XSLT(xslt2)
newdom2 = transform2(dom2)
newdom2.write_output("certificate.tex")
subprocess.run(["latexmk", "-pdf", "certificate.tex"])

#try:
#    subprocess.check_call(["latexmk", "-pdf","latex_header_footer.tex"])
#except subprocess.CalledProcessError:
    #print ("Failed making")
#else:
#     subprocess.call(["latexmk", "-c", "latex_header_footer.tex"])
