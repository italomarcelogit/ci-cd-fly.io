# CI CD fly.io
### Tutorial CI CD de uma aplicação web Flask utilizando Fly.io e Github

Segue os passos que você deverá fazer na sua máquina local

**1. PC Local - Clonando o repositório**

| Ação | Explicação |
| --- | --- |
| `Clonar git` | Clone este repositório para a sua máquina local, git clone https://github.com/italomarcelogit/ci-cd-fly.io.git|
| `Veja os scripts` | Acesse o diretório, utilizando o VSCode ou sua IDE preferedida e conheça toda a aplicação clonada para o pc local |
| `delete 2 arquivos` | Exclua os arquivos Procfile e fly.toml |
| `atualize o seu github` | Crie / atualize seu github com esse repositório com os comandos abaixo |
| `git add .` | seleciona os scripts novos e alterados |
| `git commit -m "atualizando repo` | comitando o push, com os arquivos selecionados |
| `git push -u origin main` | uploading o repositório clonado para o seu repositório |

**2. GitHub**
| Ação | Explicação |
| --- | --- |
| `Verificar` | Veja se os arquivos que você clonou agora está em seu github |


**3. PC Fly.io**
| Ação | Explicação |
| --- | --- |
| `brew install flyctl` | instalar o flyctl no macOS |
| `fly auth login` | autenticar seu termnal com o fly.io (somente a primeira vez) |
| `fly tokens create deploy -x 999999h` | Esse comando irá gerar uma token. Após a execução copie ou salve essa saída, pois utilizaremos no github setting do repositório |

**4. GitHub**
| Ação | Explicação |
| --- | --- |
| `Setting` | Acesse o seu repositório no github e clique em settings (configurações) |
| `Secrets e Variables` | Acesse no menu local, Secrets e Variables e clique em Actions |
| `Secret Repository` | Crie um novo segredo de REPOSITÓRIO chamado FLY_API_TOKEN e em valor, cole a chave gerada anteriormente no passo 3 |

**5. PC local**
| Ação | Explicação |
| --- | --- |
| `fly.yml` | Este arquivo eu já deixei criado, mas ele serve para a sua aplicação fazer o deploy das atualizações. Neste exemplo, minha branch era *main* mas se a sua for *master* é só alterar esse arquivo |
| `push` | Agora faça o push dos arquivos locais para o remote (os últimos 3 comandos da etapa 1) |


Boa sorte e qualquer coisa, manda o comentário no meu linkedin (https://www.linkedin.com/in/italomarcelo/).
Abraços