import xml.etree.ElementTree as ET

input = '''
<stuff>
    <users>
        <user x='2'>
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x='7'>
            <id>009</id>
            <name>Alex</name>
        </user>
    </users>
</stuff>
'''

stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
print(f'User count: {len(lst)}')

count = 1
for i in lst:
    print(f'{count} user')
    print('Name:\t', i.find('name').text.strip())
    print('ID:\t\t', i.find('id').text.strip())
    print('Attr x:\t', i.get('x').strip())
    count += 1
