import json
from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom import minidom

def generate_rss(json_file, output_file):
    with open(json_file, 'r') as f:
        blog_entries = json.load(f)

    rss = Element('rss', version='2.0')
    channel = SubElement(rss, 'channel')

    title = SubElement(channel, 'title')
    title.text = 'English (US)'

    link = SubElement(channel, 'link')
    link.text = 'https://ramuklawjju.medium.com/'

    description = SubElement(channel, 'description')
    description.text = 'Information from Twitter\'s engineering team about our tools, technology and services.'

    for entry in blog_entries:
        item = SubElement(channel, 'item')
        item_title = SubElement(item, 'title')
        item_title.text = entry['title']
        item_link = SubElement(item, 'link')
        item_link.text = entry['link']
        item_description = SubElement(item, 'description')
        item_description.text = entry['description']
        item_pubDate = SubElement(item, 'pubDate')
        item_pubDate.text = entry['pubDate']
        item_guid = SubElement(item, 'guid')
        item_guid.text = entry['guid']

    xml_str = minidom.parseString(tostring(rss)).toprettyxml(indent="  ")
    with open(output_file, 'w') as f:
        f.write(xml_str)

if __name__ == "__main__":
    generate_rss('data/blog.json', 'index.html')