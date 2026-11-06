import re

content = open('shiplog_dump.html', encoding='utf-8').read() if False else None
# Let's inspect the exact HTML structure of section 2 and section 3 in shiplog
with open('shiplog_extracted.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Let's see rules for .section, .section-top, .friction, .blue-band, .signal-layout, .signal-intro, .signal-list, .signal-row
for name in ['.section', '.section-top', '.section-kicker', '.friction', '.blue-band', '.signal-layout', '.signal-intro', '.signal-list', '.signal-row', '.signal-index']:
    m = re.findall(rf'({re.escape(name)}[^{{}}]*\{{[^}}]+}})', css)
    for rule in m:
        print(rule)
