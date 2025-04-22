import os
from datetime import datetime
from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom.minidom import parseString

rss = Element('rss', version='2.0')
channel = SubElement(rss, 'channel')
SubElement(channel, 'title').text = "My Blog"
SubElement(channel, 'link').text = "https://yourusername.github.io/"
SubElement(channel, 'description').text = "Latest blog posts"

# 遍历 Markdown 文件生成 RSS 条目
for md_file in os.listdir('posts'):
    if md_file.endswith('.md'):
        item = SubElement(channel, 'item')
        SubElement(item, 'title').text = md_file.replace('.md', '')
        SubElement(item, 'link').text = f"https://yourusername.github.io/posts/{md_file}"
        SubElement(item, 'pubDate').text = datetime.now().strftime('%a, %d %b %Y %H:%M:%S GMT')

xml_str = parseString(tostring(rss)).toprettyxml(indent="  ")
with open('feed.xml', 'w') as f:
    f.write(xml_str)
