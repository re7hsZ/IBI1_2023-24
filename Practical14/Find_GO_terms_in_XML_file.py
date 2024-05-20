# Import necessary libraries for XML parsing, datetime manipulation, and plotting.
import os
import xml.dom.minidom 
import datetime
import matplotlib.pyplot as plt
import xml.sax
from xml.sax import make_parser, ContentHandler

# Change the current working directory to where the XML file is stored.
os.chdir("C:\Users\lenovo\Desktop\IBI\IBI1_2023-24\IBI1_2023-24\Practical14")

# Define a function to plot the results in a bar graph.
def plot_results(counts, title):
    """
    Plot the results of GO term counts in a bar graph.

    Parameters:
    counts (dict): A dictionary containing the counts of GO terms per ontology.
    title (str): The title of the plot.
    """
    # Extract labels and values from the counts dictionary.
    labels = list(counts.keys())
    values = list(counts.values())
    
    # Plot the bar graph.
    plt.bar(labels, values)
    plt.xlabel('Ontology')
    plt.ylabel('Number of GO Terms')
    plt.title(title)
    plt.show()

# DOM API parsing.
print("Parsing with DOM API...")
start_time_dom = datetime.datetime.now()  # Record the starting time.

# Parse the XML file into a DOM document object.
DOMTree = xml.dom.minidom.parse("go_obo.xml")
# Get the root element of the document.
collection = DOMTree.documentElement
# Get a list of 'term' elements.
terms = collection.getElementsByTagName("term")

# Initialize a dictionary to record the number of GO terms for each ontology.
counts_dom = {'molecular_function': 0, 'biological_process': 0, 'cellular_component': 0}

# Iterate over each term and count the occurrences based on the namespace.
for term in terms:
    namespace = term.getElementsByTagName('namespace')[0].firstChild.nodeValue
    if namespace in counts_dom:  # Count the term if the namespace is one of interest.
        counts_dom[namespace] += 1

# Print the results.
for key in counts_dom:
    print(f"{key}: {counts_dom[key]}")

# Record the ending time and calculate the duration.
end_time_dom = datetime.datetime.now()
dom_duration = (end_time_dom - start_time_dom).total_seconds()
print(f"DOM API took {dom_duration:.2f} seconds") # DOM API took 12.25 seconds.

# SAX API parsing.
print("Parsing with SAX API...")
start_time_sax = datetime.datetime.now()  # Record the starting time.

# Define the ContentHandler class for SAX parsing.
class GOTermsHandler(ContentHandler):
    def __init__(self):
        self.current_element = ''
        self.namespace = ''
        self.counts_sax = {'molecular_function': 0, 'biological_process': 0, 'cellular_component': 0}
    
    def startElement(self, tag, attrs):
        self.current_element = tag
    
    def endElement(self, name):
        if self.namespace and self.current_element == 'namespace':
            self.counts_sax[self.namespace] += 1
        self.current_element = ''
    
    def characters(self, content):
        if self.current_element == 'namespace':
            self.namespace = content

# Create an XMLReader and set the ContentHandler.
parser = make_parser()
handler = GOTermsHandler()
parser.setContentHandler(handler)
parser.parse("go_obo.xml")

# Print the results.
for key in handler.counts_sax:
    print(f"{key}: {handler.counts_sax[key]}")

# Record the ending time and calculate the duration.
end_time_sax = datetime.datetime.now()
sax_duration = (end_time_sax - start_time_sax).total_seconds()
print(f"SAX API took {sax_duration:.2f} seconds") # SAX API took 1.32 seconds.

# Compare to determine which API was faster and print a statement.
if dom_duration < sax_duration:
    print("DOM was faster")
else:
    print("SAX was faster")
#SAX was faster

# Generate graphs to display the extracted frequency data.
plot_results(counts_dom, "DOM Result")
plot_results(counts_sax, "SAX Result")
# Summay:DOM API took 12.25 seconds, SAX API took 1.32 seconds, SAX was faster