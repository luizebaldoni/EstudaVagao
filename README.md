# EstudaVagao

Este é o repositorio de trabalho do projeto de desenvolvimento do site Estuda Vagao.

## O PROJETO

Este repositorio esta dividido e organizado em pastas, sendo elas:

- [Static](/static) que possui todos os arquivos estaticos do projeto como arquivos javascript, css e imagens (separados em pastas nomeadas atravez tipo de arquivo), dentro da static possuem outras pastas para melhor organização do site e tambem algumas que sao dependencias de bibliotecas que utilizamos;

- [cmsm_PROJECT](/cmsm_PROJECT/) onde esta os arquivos principais do Django e suas dependecias;

- [App](/app/) que tambem contem arquivos basicos do Django e possui os arquivos [models](/app/models.py) que servira para o banco de dados e o arquivo [views](/app/views.py) que servira para defirnirmos as paginas e juntamente com o arquivo [url](/cmsm_PROJECT/urls.py) definir as rotas.

- [Register](/register/) onde estao os arquivos utilizados para fazermos o login, cadastro e atualização de perfil dos usuarios do site.

- [media](/media/) onde é armazenado a foto de perfil dos usuarios.

- [Templates](/templates/) que possui todos os templates html do projeto;

- Alem de arquivos que nao estao em pastas porem sao cruciais para o funcionanmento do site, como o  [manage.py](/manage.py), arquivo que faz o site rodar, a [dbatabase](/db.sqlite3/) da aplicação, onde esta nosso scrip sql, e tambem os [requirements.txt](/requirements.Txt) onde estao definidas as depencias da aplicação.
