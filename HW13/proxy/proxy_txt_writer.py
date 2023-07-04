from HW13.proxy.txt_writer import TxtWriter


class TxtProxyWriter:
    def __init__(self, file_path):
        self.__result = None
        self.__txt_writer = TxtWriter(file_path)

    def write_file(self, new_data):
        self.__result = self.__txt_writer.write(new_data)
        return self.__result


if __name__ == '__main__':
    proxy_writer = TxtProxyWriter('data.txt')
    print(proxy_writer.write_file('Hello'))
    print('\n')
    print(proxy_writer.write_file('World'))
