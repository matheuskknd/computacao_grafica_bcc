Nós 

* NoiseTexture:
	- As NoiseTexture 3D são procedimentos que geram uma cor aleatória pra um dado ponto no espaço tridimensional
	- A textura em duas dimensões, por exemplo, lembram algo similar a manchas coloridas aleatórias na malha. Em três dimensões não é diferente
	- O parâmetros de entrada deste nó, dizem apenas como a textura gerada vai parecer

* ColorLamp:
	- Esses nós possuem um vetor de intervalos reais sucessivos pertinentes a [0,1], cada qual com uma cor base.
	- O parametro de entrada é um ponto flutuante pertinente a [0,1] também chamado de tom de cinza pelo Blender
	- O procedimento é encontrar a qual intervalo o ponto flutuante pertence, com isso a cor de saída é o resultado da interpolação
	(degradê) da cor base deste intervalo com a cor base do próximo intervalo, de acordo com a proximidade da entrada com as bounds
