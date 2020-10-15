# Machine Learning na AWS para desenvolvedores - Demo


Com o Amazon Rekognition Custom Labels, você pode identificar os objetos e as cenas nas imagens que são específicos às necessidades dos seus negócios. Por exemplo, você pode encontrar seu logotipo em postagens de mídias sociais, identificar seus produtos nas prateleiras das lojas, diferenciar plantas saudáveis ou infectadas, classificar as peças de máquina em uma linha de montagem ou detectar personagens animados em vídeos.

Saiba mais acessando a [documentação](https://aws.amazon.com/pt/rekognition/custom-labels-features/)

## :memo: Parte 1: Prepare suas imagens


- Aprenda mais sobre a [preparação das imagens](https://docs.aws.amazon.com/pt_br/rekognition/latest/customlabels-dg/pi-prepare-images.html).
- Use o [dataset Standford Dogs](https://www.kaggle.com/jessicali9530/stanford-dogs-dataset).

## :rocket: Parte 2: faça o upload do seu dataset para o S3, incluindo as pastas que definem as raças dos cães.

- Aprenda mais obre como fazer upload para o [Amazon S3](https://docs.aws.amazon.com/pt_br/AmazonS3/latest/user-guide/upload-objects.html).
- A estrutura de pastas do seu bucket deve se parecer com essa:

![](https://i.imgur.com/pwPFi5f.png)

## :rocket: Parte 3: Amazon Rekognition Custom Labels: crie o dataset.

- Crie seu dataset à partir do bucket do Amazon S3 que você criou anteriormente. As pastas serão usadas como labels das suas imagens definindo qual a raça representada pelas imagens.
- Você pode usar essa [documentação](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/cd-s3.html)  para te orientar.

## :rocket: Parte 4: Amazon Rekognition Custom Labels: crie o seu projeto.

- Você pode seguir os passos da [documentação](https://https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/cp-create-project.html).

- Ou você pode usar este script [:link:][GitHub-Sync]. Importante: não é um código preparado para produção, é um exemplo para demonstração.


## :rocket: Parte 5: Amazon Rekognition Custom Labels: treine seu modelo.

- Você pode seguir os passos da [documentação](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/tm-console.html).

- Ou você pode usar este script [:link:][GitHub-Sync]. Importante: não é um código preparado para produção, é um exemplo para demonstração.

## :rocket: Parte 6: Amazon Rekognition Custom Labels: inicialize o modelo e comece a testar!


- Importante: lembre-se de dar stop no seu projeto se não estiver em uso. [Revise a precificação do treinamento e das inferências na documentação](https://aws.amazon.com/pt/rekognition/pricing/).

- Você pode usar este projeto [Github-demo] para criar uma interface para START/STOP do projeto e também para testar as inferências.Importante: não é um código preparado para produção, é um exemplo para demonstração.

![](https://i.imgur.com/27dW7vS.png)


- Ou ainda, você pode usar este script para o START do projeto [:link:][GitHub-Start] e este para o STOP [:link:][GitHub-Stop]. Importante: não é um código preparado para produção, é um exemplo para demonstração.

[GitHub-Sync]: https://github.com/claudiacharro/rekognitioncl-demo/blob/main/sample-scripts/start-project.py

[GitHub-Start]: https://github.com/claudiacharro/rekognitioncl-demo/blob/main/sample-scripts/start-project.py

[GitHub-Stop]: https://github.com/claudiacharro/rekognitioncl-demo/blob/main/sample-scripts/start-project.py

[Github-demo]: https://github.com/aws-samples/amazon-rekognition-custom-labels-demo

