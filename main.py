import tkinter as tk
from PIL import Image, ImageTk
from binding import render_image

# Configurações da imagem
width, height = 800, 600

# Renderizar a imagem usando Ray Tracing em C
image = render_image(width, height)

# Converter o array numpy para um objeto PIL Image
img = Image.fromarray(image)

# Configuração da interface gráfica usando Tkinter
root = tk.Tk()
root.title("Ray Tracing")

# Converter a imagem PIL para o formato Tkinter e exibi-la
img_tk = ImageTk.PhotoImage(image=img)
label = tk.Label(root, image=img_tk)
label.pack()

# Executar o loop principal do Tkinter
root.mainloop()
