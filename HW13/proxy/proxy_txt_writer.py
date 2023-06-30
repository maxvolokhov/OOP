from HW13.proxy.txt_writer import TxtWriter


class TxtProxyWriter:
    def __init__(self, file_path):
        self.__result = None
        self.__is_actual = False
        self.__txt_writer = TxtWriter(file_path)

    def write_file(self):
        if not self.__is_actual:
            self.__result = self.__txt_writer.write('Hello')
            self.__is_actual = True
        return self.__result


if __name__ == '__main__':
    proxy_writer = TxtProxyWriter('data.txt')
    print(proxy_writer.write_file())
    print('\n')
    print(proxy_writer.write_file())
