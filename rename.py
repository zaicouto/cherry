import hyphen_for_underscore
import space_for_underscore
import to_lowercase


if __name__ == '__main__':
    path = '/media/ozair/Dados/imagens/screenshots'

    hyphen_for_underscore.hyphen_for_underscore(path, False)
    space_for_underscore.space_for_underscore(path, False)
    to_lowercase.to_lowercase(path, False)