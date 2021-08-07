import cv2

# Define o tamanho desejado para a janela
w = 1000
h = 720

# Define a janela de exibição das imagens, com tamanho automático
winName = 'Janela de Teste para o SOPT'
cv2.namedWindow(winName, cv2.WINDOW_AUTOSIZE)

# Posiciona a janela na metade direita do (meu) monitor
cv2.moveWindow(winName, 960, 0)

# Abre a webcam para captura de vídeo
cam = cv2.VideoCapture(0)

# Laço de execução infinito (até que o usuário feche com a tecla 'q' ou ESC)
while True:

    # Captura um novo quadro da webcam
    ok, frame = cam.read()
    if not ok:
        break

    # Altera o tamanho da imagem para o desejado
    frame = cv2.resize(frame, (w, h))

    # Exibe a imagem na janela existente
    cv2.imshow(winName, frame)

    # Aguarda o pressionamento de uma tecla ou 30 milisegundos
    k = cv2.waitKey(10)
    if k == ord('q') or k == ord('Q') or k == 27:
        break

# Libera a memória do programa
cam.release()
cv2.destroyAllWindows()