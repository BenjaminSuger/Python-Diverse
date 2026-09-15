from load_image import ft_load

'''
pense a mettre plein de test de chose qui marche pas;
pas de permission (bon juste a la correction)
fichier non existant
pas de JPEG or JPG mais qui est une image
pas un fichier image du tout genre un le fichier.py
un JPEG ou JPG "vide" => je sais pas encore le comportement
'''

def main() -> None:
    """main tester"""
    try:
        print(ft_load("./images/landscape.jpg"))
    except Exception as e:
        print(f"{(type(e).__name__} : {e}")

if __name__ == "__main__":
    main()
