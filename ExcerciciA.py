import xml.etree.ElementTree as ET

def arxiuXML():
    stu = ET.Element('students')

    s0 = ET.SubElement(stu, 'student')
    s0.set("Nationality", "Spanish")
    a0 = ET.SubElement(s0, 'Name')
    a0.text = "Carlos"
    a1 = ET.SubElement(s0, 'Surname')
    a1.text = "Sanchez"
    a2 = ET.SubElement(s0, 'Email')
    a2.text = "carlossa@gmail.com"
    a3 = ET.SubElement(s0, 'DNI')
    a3.text = "73895319L"

    s1 = ET.SubElement(stu, 'student')
    s1.set("Nationality", "Italian")
    b0 = ET.SubElement(s1, 'Name')
    b0.text = "Mario"
    b1 = ET.SubElement(s1, 'Surname')
    b1.text = "da Vinci"
    b2 = ET.SubElement(s1, 'Email')
    b2.text = "leodavi@gmail.com"
    b3 = ET.SubElement(s1, 'DNI')
    b3.text = "37984987M"

    s2 = ET.SubElement(stu, 'student')
    s2.set("Nationality", "Russian")
    c0 = ET.SubElement(s2, 'Name')
    c0.text = "Igor"
    c1 = ET.SubElement(s2, 'Surname')
    c1.text = "Popov"
    c2 = ET.SubElement(s2, 'Email')
    c2.text = "igorpov@gmail.com"
    c3 = ET.SubElement(s2, 'DNI')
    c3.text = "63242389P"

    s3 = ET.SubElement(stu, 'student')
    s3.set("Nationality", "Japanese")
    d0 = ET.SubElement(s3, 'Name')
    d0.text = "Akira"
    d1 = ET.SubElement(s3, 'Surname')
    d1.text = "Toriyama"
    d2 = ET.SubElement(s3, 'Email')
    d2.text = "Akitori@gmail.com"
    d3 = ET.SubElement(s1, 'DNI')
    d3.text = "7899823Y"

    s4 = ET.SubElement(stu, 'student')
    s4.set("Nationality", "Brasilian")
    e0 = ET.SubElement(s4, 'Name')
    e0.text = "João"
    e1 = ET.SubElement(s4, 'Surname')
    e1.text = "Da Silva"
    e2 = ET.SubElement(s4, 'Email')
    e2.text = "jodasil@gmail.com"
    e3 = ET.SubElement(s4, 'DNI')
    e3.text = "90366112R"

    tree = ET.ElementTree(stu)
    tree.write('students.xml')
    ET.indent(stu)
    ET.dump(stu)
