import os


def to_lowercase(path: str, dry_run: bool = True):
    files = os.listdir(path)

    for file in files:
        old_name = os.path.join(path, file)
        new_name = os.path.join(path, file.lower())
        try:
            if not dry_run:
                os.rename(old_name, new_name)
            print(f'{old_name} -> {new_name}')
        except FileNotFoundError:
            print(f'Not found: {old_name}')


if __name__ == '__main__':
    to_lowercase('/media/ozair/Dados/documentos/frontend_masters', False)
