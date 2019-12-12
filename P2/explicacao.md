Os nós no Blender são equivalentes à etapas do pipeline de um shader. As funções desses nós é explicada a baixo:

* NoiseTexture:
	- As NoiseTexture 3D são procedimentos que geram uma cor aleatória pra um dado ponto no espaço tridimensional
	- A textura em duas dimensões, por exemplo, lembram algo similar a manchas coloridas aleatórias na malha. Em três dimensões não é diferente
	- O parâmetros de entrada deste nó, dizem apenas como a cor aleatória do ponto vai parecer

* ColorRamp:
	- Esses nós possuem um vetor de intervalos reais sucessivos pertinentes a [0,1], cada qual com uma cor base.
	- O parametro de entrada é um ponto flutuante pertinente a [0,1] também chamado de tom de cinza pelo Blender
	- O procedimento é encontrar a qual intervalo o ponto flutuante pertence, com isso a cor de saída é o resultado da interpolação
	(degradê) da cor base deste intervalo com a cor base do próximo intervalo, de acordo com a proximidade da entrada com as bounds

* MixRGB:
	- Esses nós específicos de cores, recebem duas cores, aplicam o algoritmo de mistura de cor escolhido sobre elas e gera uma única cor de saída
	- A propriedade "clamp" apenas faz os pontos flutuantes da saída passarem pela função: ( x < 0 ? 0 : x > 1 ? 1 : x )
	- Tipo Color Dodge: C = B/(1-A) , onde A é cor de cima, B é a cor de baixo e C é a saída. Mix: mais B quanto mais A
	- Tipo screen: C = 1-(1-A)(1-B) , onde A é cor de cima, B é a cor de baixo e C é a saída. Mix: mais brilhante

* Volume Scatter (Dispersão volumétrica):
	- Garante que a luz que irradiada diretamente sobre o volume seja "dispersa" em outras direções que não a de emissão
	- Diferente do que ocorre fisicamente, quando disperça, esta luz não perde intensidade em nenhum espectro
	- As duas entradas são: cor da dispersão que dá um efeito colorido naquele ponto, a densidade (alfa) e a anisotropia
	- A anisotropia varia entre [-1,1] e quanto mais próximo de -1 mais luz é "refletida" de volta ao emissor, quão mais
	próximo de 1 mais luz transmitida apenas na direção original de transmissão. Por isso o valor escolhido é '0' (ominidirecional).

* Volume Absortion (Absorção volumétrica):
	- Serve apenas para reduzir a intensidade da luz que atravessa aquele ponto de acordo com a densidade (alfa) do mesmo
	- É um shader auxiliar para dar realismo aos outros. Tornando a resposta à luz mais parecida com a que ocorre na realidade
	- As duas entradas são: cor e densidade, a densidade é equivalente à de cima: descreve um valor similar ao alfa daquele ponto
	- A cor diz respeito a algum espectro que não é absorvido pelo volume, no nosso caso, 'preto' quer dizer: todas são absorvidas

* Add Shader:
	- Apenas uma maneira de dizer ao Blender que ambos os pipelines devem ser executados para se concluir propriedades
	sobre um dado ponto no espaço em algum momento

Renderização de volume: a renderização (desenho) do volução ocorre atráves de uma "materialização" de vários planos dentro
do domínio deste volume (samples no Blender), onde as texturas destes (cor de cada ponto) são dadas pelo processamento dos
shaders volumétricos apresentados anteriormente. Por isso a rederização de volumes detalhados é tão cara. Pois quanto mais
detalhes mais samples (planos) são necessários renderizar, e quanto mais planos, mais a quantidade de ponto tende à real
área cúbica do domínio do volume.

Nota: o domínio do volume é uma figura geométrica que limita a formação dos planos (samples) para renderização volumétrica.

Os exemplos na pasta 'RenderCycles' mostram a renderização de imagens 360º feitas com uma câmera panorâmica em modo
equiretangular em diferentes coordenadas dentro do volume, apenas para fins demonstrativos. Cada imagem levou
aproximadamente 20 minutos para ser renderizada com uma GPU Nvidia GTX 965m e 6 processadores em paralelo com resolução
de 4096x2048 pixels (baixa para imagens 360º) e 32 samples (planos). Mostrando o quão custosa é esse tipo de
renderização ainda hoje.

Nota 2: as imagens de exemplo que terminam em 'render.bmp' são as geradas diretamente pelo renderizador Cycles do Blender.
Já as terminadas em 'dnoise.bmp' são pós processadas por uma (IA da Nvidia)[https://developer.nvidia.com/optix-denoiser]
apenas para remoção do ruído (noise).