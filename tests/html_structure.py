from models import HtmlStructure


html_tag_structure = HtmlStructure()
html_tag_structure.add_tag_val(tag='class', value='logo')
html_tag_structure.add_tag_val(tag='img')
print(html_tag_structure.structure)
