from load_image import ft_load
import matplotlib.pyplot as plt #temporaire parce que pas legit
#je vais peut etre importe scipy pour le zoom mais apres je comprend pas l'output

def ft_zoom(path: str) -> list:
    """zoom on the image with a calculation from the
    original dimension (zoom == 2)"""
    arr = ft_load(path)
    print(arr)

    height, length = arr.shape[0], arr.shape[1]
    nouvelle_h = height // 2
    nouvelle_l = length // 2
    centre_y = height // 2
    centre_x = length // 2
    debut_y = centre_y - nouvelle_h // 2
    debut_x = centre_x - nouvelle_l // 2

#reverifier si le 0 necessaire
    zoom_arr = arr[debut_y:debut_y + nouvelle_h, debut_x:debut_x + nouvelle_l, 0]
    plt.imshow(zoom_arr, cmap='gray')
    plt.show()
    #ici probleme car je dois avoir un qui affiche les channels (troisieme truc)
    print(f"New shape after slicing: {zoom_arr.shape} or {zoom_arr.shape}")



if __name__ == "__main__":
    try:
        ft_zoom("./images/animal.jpeg")
    except Exception as e:
        print(f"{type(e).__name__} : {e}")
