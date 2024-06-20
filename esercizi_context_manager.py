class FileManager:
    def __init__(self,file_name:str,opening_mode:str) -> None:
        self.file_name=file_name
        self.opening_mode=opening_mode
        self.file=None


    def __enter__(self):
        self.file=open(self.file_name, self.opening_mode)

        return self.file

    def __exit__(self,exc_type, exc_value, traceback):
        if self.file==True:
            self.file.close()



with FileManager('example.txt', 'w') as f:
    f.write('Hello, world!')
    