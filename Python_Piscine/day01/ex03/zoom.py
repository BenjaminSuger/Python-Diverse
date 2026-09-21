from load_image import ft_load
import matplotlib.pyplot as plt #temporaire parce que pas legit
#je vais peut etre importe scipy pour le zoom mais apres je comprend pas l'output

def ft_zoom(path: str, zoom: int ) -> list:
    # a mon avis des securite sur le zoom
    # mais je sasi pas comment faire le zoom
    arr = ft_load(path)
    print(arr)

    arr = arr[300:600, 300:600, 0] #la j'ai fais le slicing pour le moment a la main et ensuite faudra calculer (voir plus bas)

    
    plt.imshow(arr, cmap='gray')
    plt.show()

    print(f"New shape after slicing: ")
    print(arr)




if __name__ == "__main__":
    try:
        ft_zoom("./images/animal.jpeg", 2)
    except Exception as e:
        print(f"{type(e).__name__} : {e}")


'''
hauteur, largeur = arr.shape[0], arr.shape[1]

nouvelle_h = hauteur // zoom
nouvelle_l = largeur // zoom

centre_y = hauteur // 2
centre_x = largeur // 2

debut_y = centre_y - nouvelle_h // 2
debut_x = centre_x - nouvelle_l // 2

zoom_arr = arr[debut_y:debut_y + nouvelle_h, debut_x:debut_x + nouvelle_l, 0]
'''
