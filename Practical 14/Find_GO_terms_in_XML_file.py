# open the folder contains the file
import os
os.chdir("/Users/zhuqin/Desktop/academic/IBI/IBI1_2023-24/Practical 14")
# import packages
import xml.dom.minidom 
import datetime
import matplotlib.pyplot as plt
import xml.sax

#DOM
print("Parsing with DOM API...")
start_time_dom = datetime.datetime.now() # Record starting time

DOMTree = xml.dom.minidom.parse("go_obo.xml") # parse the XML file into a DOM document object
collection = DOMTree.documentElement # get the root element of the document
terms = collection.getElementsByTagName("term") # a list of 'term' elements
counts_dom = {'molecular_function': 0, 'biological_process': 0, 'cellular_component': 0} # A dictionary recording the the number of GO terms 
for term in terms:
    namespace = term.getElementsByTagName('namespace')[0].firstChild.nodeValue # get the value
    if namespace in counts_dom: # count 
        counts_dom[namespace] += 1
# print the results
for key in counts_dom:
    print(key + ': ' + str(counts_dom[key]))

end_time_dom = datetime.datetime.now() # Record endding time
dom_duration = (end_time_dom - start_time_dom).total_seconds() # calculate the time taken

# SAX
print("Parsing with SAX API...")
start_time_sax = datetime.datetime.now() # Record starting time

class GOTermsHandler (xml.sax.ContentHandler):
    def __init__(self):
        self.current_element = ''
        self.namespace = ''
    def startElement(self, tag, attrs):
        # extracting tag name
        self.current_element = tag
    def endElement(self, name):
        # when the element ends, if it is namespace, count the GO terms
        if self.namespace in counts_sax:
            counts_sax[self.namespace] += 1
            self.namespace = ''  # reset namespace
        self.current_element = '' # reset urrent element
    def characters(self, content): # extracting content
        if self.current_element == 'namespace':
             self.namespace = content
counts_sax = {'molecular_function': 0, 'biological_process': 0, 'cellular_component': 0}
parser = xml.sax.make_parser() # create an XMLReader
handler = GOTermsHandler() # set ContentHandler 
parser.setContentHandler(handler)
parser.parse("go_obo.xml")
# print the results
for key in counts_sax:
    print(key + ': ' + str(counts_sax[key]))

end_time_sax = datetime.datetime.now() # Record endding time
sax_duration = (end_time_sax - start_time_sax).total_seconds() # calculate the time taken

# reports the time taken
print(f"DOM API took {dom_duration:.2f} seconds")
print(f"SAX API took {sax_duration:.2f} seconds")

# Compare to know which one is faster
if dom_duration < sax_duration:
        print("DOM was faster")
else:
        print("SAX was faster")

# generate graph to display the extracted frequency data
def plot_results(counts):
    labels = counts.keys()
    values = counts.values()
    plt.bar(labels, values)
    plt.xlabel('Ontology')
    plt.ylabel('Number of GO Terms')
    plt.title('Distribution of GO Terms Across Ontologies')
    plt.show()
    plt.clf

plot_results(counts_dom)
plot_results(counts_sax)
