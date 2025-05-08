
import xml.etree.ElementTree as ET
from datetime import datetime

def generate_sitemap(urls, domain, filename="sitemap.xml"):
    urlset = ET.Element("urlset", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")
    for url in urls:
        url_element = ET.SubElement(urlset, "url")
        ET.SubElement(url_element, "loc").text = url
        ET.SubElement(url_element, "lastmod").text = datetime.today().strftime("%Y-%m-%d")
    tree = ET.ElementTree(urlset)
    tree.write(filename, encoding="utf-8", xml_declaration=True)
