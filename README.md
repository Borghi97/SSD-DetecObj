# SSD-DetecObj LEIA-ME

Treinando modelo para reconhecer especificamente mouse na webcam in real time.

Por que o modelo SSD foi escolhido?

O modelo SingleShotDetector atinge um bom equilíbrio entre velocidade e precisão. 
O SSD executa uma rede convolucional na imagem de entrada apenas uma vez e calcula um mapa de recursos. 
Executando um pequeno kernel convolucional de tamanho 3 × 3 neste mapa de recursos para prever as caixas delimitadoras e a probabilidade de classificação. 
O SSD também usa caixas de âncora em várias proporções semelhantes ao Faster-RCNN e aprende o deslocamento em vez de aprender a caixa. 
Para lidar com a escala, o SSD prevê caixas delimitadoras após várias camadas convolucionais. 
Como cada camada convolucional opera em uma escala diferente, ela é capaz de detectar objetos de várias escalas.

Os Single Shot Detectors têm um FPS bastante impressionante, usando imagens de resolução mais baixa em detrimento da precisão.
Esses papéis tentam provar que podem superar a precisão dos detectores baseados na região. 
No entanto, isso é menos conclusivo, pois imagens de resolução mais alta costumam ser usadas para tais alegações.
Portanto, seus cenários estão mudando. Além disso, diferentes técnicas de otimização são aplicadas e dificultam o isolamento do mérito de cada modelo.
Na verdade, os detectores de tiro único e baseados em região estão ficando muito semelhantes em design e implementações agora.
Mas com alguma reserva, podemos dizer:
Detectores baseados em região, como o Faster R-CNN, demonstram uma pequena vantagem de precisão se a velocidade em tempo real não for necessária.
Detectores de disparo único estão aqui para processamento em tempo real. Mas os aplicativos precisam verificar se atendem aos requisitos de precisão.

Precisão = mAP

![gpu](https://user-images.githubusercontent.com/122883539/220191387-993e803d-fe4b-4b31-93e6-b9779699923f.PNG)


