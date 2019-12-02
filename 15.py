import xml.etree.ElementTree as ET

drzewo = ET.parse("pierwszy.xml")
korzen = drzewo.getroot()


for element in korzen.iter('przykladowyT'):

    element.text = 'nasz_tekst'
    print(element.text)

drzewo.write('pierwszy.xml')
