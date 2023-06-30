___doc___ = """Implement adapter pattern from_txt_to_html
for example, we have a such structure in txt:

name,surname,age,salary
Bohdan,Dovbysh,28,100
I want to see:

<name>Bohdan</name>
<surname>Dovbysh</surname>
.............
It should work with any file with such a structure"""


class FromTxtToHtmlAdapter:
    def __init__(self, file_path):
        self.__file_path = file_path

    def from_txt_to_html(self):
        with open(self.__file_path, 'r') as file:
            lines = file.readlines()
        headers = lines[0].replace('\n', '').split(',')

        data = [item.replace('\n', '').split(',') for item in lines[1:]]
        result = ""
        for user_data in data:
            for field, value in zip(headers, user_data):
                result += f"<{field}>{value}</{field}>\n"
        return result


if __name__ == '__main__':
    html_adapter = FromTxtToHtmlAdapter('users.txt')
    html_output = html_adapter.from_txt_to_html()
    print(html_output)
