


class FileRepo:
    
    @classmethod
    def save_to_file(cls, data: str) -> str:
        try:
            with open('data/user.txt', 'a') as file_writer:
                file_writer.write(f'{data}\n')
                return f'SUCCESS - Podaci su uspjesno pohranjeni u datoteku'
        except Exception as ex:
             return f'ERROR - Dogodila se greska {ex}'
        

    @classmethod
    def read_from_file(cls) -> str:
        try:
            with open('data/user.txt', 'r') as file_reader:
                return file_reader.readlines()
        except Exception as ex:
             return f'ERROR - Dogodila se greska {ex}'
