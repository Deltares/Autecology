import sys
from matplotlib import pyplot as plt


sys.path.append("../")
from autecology_xml import AutecologyXML


#xmltest = AutecologyXML(filename = "../../../_knowledgerules/parameters/water_quality/Light_extinction.xml")
xmltest = AutecologyXML(filename = "../../../_knowledgerules/parameters/hydrodynamics/Fetch.xml")
#xmltest = AutecologyXML(filename = "../../../_knowledgerules/parameters/hydrodynamics/Watersurface.xml")
xmltest._readxml()
print(type(xmltest.xmlroot))
xmltest._scan()
print(xmltest.topic_name)
print(xmltest.commonnames)

xmltest._scan_modeltype("HSI")
print(xmltest.modeltypename)
print(xmltest.systems)

xmltest._scan_knowledgerules(modeltypename = "HSI", systemname = "ijsselmeergebied")
print(xmltest.XMLconvention["allowed_knowledgeRulesCategories"])
print(xmltest.knowledgeRulesNames)
print(all(elem in xmltest.XMLconvention["allowed_knowledgeRulesCategories"] for elem \
									in xmltest.knowledgeRulesCategories))
