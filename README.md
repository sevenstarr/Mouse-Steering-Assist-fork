# Mouse Steering Assist — Central Deadzone

Mod Lua para dirigir no Assetto Corsa com mouse e teclado, usando o scroll para
dosar acelerador e freio. Este fork acrescenta uma **deadzone central configurável**
e preserva o **FFB opcional** do mod original.

**Configuração recomendada para direção livre:** deadzone de **2%** e **FFB desligado**.
Assim, o script só muda a posição da direção quando o mouse se move; dentro da
região central o comando é exatamente zero. Quem quiser a correção por FFB pode ativá-la.

## Download

**[Baixar ZIP pronto para instalar](https://github.com/sevenstarr/Mouse-Steering-Assist-fork/releases/download/v1.0.5-deadzone.1/Mouse-Steering-Assist-1.0.5-deadzone.1.zip)**
· [Releases](https://github.com/sevenstarr/Mouse-Steering-Assist-fork/releases)

Use o ZIP com nome `Mouse-Steering-Assist-…zip` em **Assets**. Os arquivos automáticos
**Source code** são destinados a quem quer trabalhar com o código.
O arquivo `SHA256SUMS.txt` permite conferir a integridade do pacote.

O código atual de `main` usa `DOFFB=0` para deixar o FFB desligado de forma explícita.
O ZIP da release `1.0.5-deadzone.1` foi publicado antes desse ajuste do padrão:
se você usa esse ZIP e quer direção livre, ajuste também `DOFFB=0` na sua configuração.

## Todas as funções

### Direção pelo mouse

O movimento horizontal do mouse é acumulado num eixo de -1 a +1. Mover para um lado
vira a direção; mover no sentido contrário a traz de volta. Com FFB desligado, o
script mantém a posição acumulada quando o mouse fica parado, inclusive ao acelerar.
Não existe ligação direta do acelerador com a direção.

A sensibilidade básica do mouse vem das configurações de controles do jogo/CSP.
Ela não é controlada por `SMOOTHNESS`, que se aplica aos pedais.

### Deadzone central de 0% a 10%

O padrão é **2%** de cada lado do centro do eixo normalizado. Não significa 2% da
largura da tela nem um número fixo de pixels.

- Dentro da região, incluindo o limite, o comando de direção é **exatamente zero**.
- Fora dela, a resposta é remapeada continuamente e alcança esterçamento completo
  nos dois extremos.
- Movimentos pequenos continuam se acumulando e permitem sair da região central.
- **0% desativa** somente a deadzone.

A deadzone não atrai o volante para o centro, não cria uma trava e não faz correções
automáticas de trajetória. A fórmula aplicada somente à saída é:

```text
abs(input) <= deadzone → output = 0
abs(input) > deadzone  → output = sign(input) × (abs(input) − deadzone) / (1 − deadzone)
```

### FFB opcional: correção da direção

O recurso herdado do mod original lê o FFB calculado pelo CSP e o usa para alterar
a posição acumulada da direção. Pode puxar a direção de volta ou alterar o ângulo
mesmo sem mover o mouse; a reação depende das forças do carro e pode ficar mais
perceptível em movimento/aceleração. Não é uma função para prender o volante na deadzone.

**Para direção livre com zona central: `DOFFB=0`.**
**Para experimentar a reação por FFB: `DOFFB=1`**, ajustando `FFBSENS` aos poucos.
O recurso continua disponível; desligá-lo não desativa a deadzone.

Use **0 ou 1** no arquivo para esse interruptor, em vez das palavras `false`/`true`.
A leitura booleana do INI na API Lua consultada compara o valor com a string `0`;
usar `0` evita que o texto `false` seja interpretado como ligado.
Preferências já salvas no CM/CSP podem prevalecer sobre o arquivo de padrões.

### Acelerador e freio com scroll

Mantenha a tecla/botão do acelerador ou freio pressionado e use o scroll para dosar
o pedal. No primeiro acionamento, o alvo começa em `ONPRESS` (padrão 33%). O scroll
positivo aumenta o alvo e o negativo diminui, em passos definidos por `SCROLL`
(padrão 10 pontos percentuais). O resultado fica limitado a 0–100%.

Ao soltar a tecla/botão, o alvo volta a zero. A saída acompanha esse alvo com a
suavização configurada. Se ambos os pedais estiverem pressionados, o mesmo scroll
ajusta ambos. O scroll não troca marchas neste script.

### Teclas alternativas e botões do mouse

Cada pedal aceita uma tecla principal e uma alternativa. Por exemplo, `W` e o botão
esquerdo podem acionar o acelerador, enquanto `S` e o botão direito acionam o freio.
Use `LeftButton` e `RightButton` para esses botões. Deixe a alternativa vazia se não precisar.

O código também consulta os acionamentos de controle disponibilizados pelo CSP.
Em versões antigas, como o CSP 0.2.11, a função de freio de controle ausente recebe
a proteção herdada do autor; as teclas/botões configurados continuam sendo o caminho
para o freio. Não se promete suporte equivalente de controle em todas as versões.

### Shift e quantidade forçada dos pedais

Segure **Shift junto com a tecla/botão do pedal** para aplicar `FORCEDAMOUNT`
(padrão 100%), antes do ajuste de scroll daquele ciclo. Shift sozinho não aciona um pedal.
Defina `FORCEDAMOUNT=0` para desativar esse recurso.

### Suavização dos pedais

`SMOOTHNESS` controla a aproximação da saída de acelerador/freio ao alvo a cada
atualização. Valores maiores respondem mais rápido; menores fazem uma transição
mais lenta. **1** aproxima imediatamente do alvo; **0 impede a aproximação**, portanto
use um valor maior que zero. O padrão é **0.25**.

### Embreagem e ativação do mouse

Este script não escreve na embreagem e não acrescenta automação de embreagem.
A ativação da direção por mouse e atalhos como **Ctrl+M** ou o botão do meio são
recursos do jogo/CSP, conforme suas configurações, e não opções implementadas pelo MSA.

## Como instalar

1. Feche o Assetto Corsa. Faça backup de `extension/lua/mouse-steering/MSA`
   e anote suas preferências personalizadas.
2. Extraia a pasta `extension` do ZIP na raiz do Assetto Corsa, onde está `acs.exe`.
3. No Content Manager, selecione **Mouse Steering Assist - Central Deadzone** nas
   opções de script da direção por mouse do CSP. No CSP 0.2.x, procure em
   **Settings → Custom Shaders Patch → General Patch settings → Mouse steering tweaks**.
   Nas versões 0.3.x, o autor indica **Keyboard & Mouse**; a interface depende da versão.
4. Ative a direção por mouse nos controles. Reabra o CM se a lista estiver em cache.
5. Reaplique suas opções personalizadas e inicie uma nova sessão.

Esta instalação não modifica arquivos principais do jogo nem controles globais.

## Como configurar

Use as opções do script no Content Manager quando disponíveis. Caso contrário,
edite `extension/lua/mouse-steering/MSA/settings.ini`. Use ponto decimal e reinicie
a sessão depois de mudar valores. Se houver preferências do usuário no CM/CSP,
elas têm prioridade: ajuste a preferência efetiva, não somente o arquivo de padrões.

| Opção | Padrão recomendado | O que controla |
| --- | --- | --- |
| `STEERING_DEADZONE` | `0.02` | Deadzone de 2%; faixa 0–0.1, com 0 desligado. |
| `DOFFB` | `0` | Correção da direção por FFB: 0 desligado, 1 ligado. |
| `FFBSENS` | `0.25` | Intensidade do FFB opcional; faixa declarada 0–1. Só atua com DOFFB ligado. |
| `SMOOTHNESS` | `0.25` | Resposta dos pedais por atualização; use maior que 0 até 1. |
| `SCROLL` | `0.1` | Variação de 10 pontos percentuais por passo processado; faixa 0–1. |
| `THROTTLE` | `W` | Tecla/botão principal do acelerador. |
| `BRAKE` | `S` | Tecla/botão principal do freio. |
| `ALTTHROTTLE` | vazio | Tecla/botão alternativo do acelerador. |
| `ALTBRAKE` | vazio | Tecla/botão alternativo do freio. |
| `FORCEDAMOUNT` | `1` | Quantidade aplicada com Shift; 1 = 100%, 0 desliga o recurso. |
| `ONPRESS` | `0.33` | Quantidade inicial do pedal ao pressionar; 0.33 = 33%. |

Exemplo: direção livre, deadzone de 2%, pedais por teclado ou mouse:

```ini
[SETTINGS]
STEERING_DEADZONE=0.02
DOFFB=0
FFBSENS=0.25
SMOOTHNESS=0.25
SCROLL=0.1
THROTTLE=W
BRAKE=S
ALTTHROTTLE=LeftButton
ALTBRAKE=RightButton
FORCEDAMOUNT=1
ONPRESS=0.33
```

O exemplo configura botões alternativos; eles não são ativados por padrão.
O parâmetro `FFBSENS` usa o cálculo herdado `ffb × FFBSENS / 100` por atualização;
ele não representa diretamente uma porcentagem do ângulo total do volante.

## Se o volante estiver sendo puxado para o centro

Confira **`DOFFB=0`** na preferência efetivamente carregada, reinicie a sessão e
compare com o FFB ligado. Mantenha `STEERING_DEADZONE=0.02`: a direção deve ficar
neutra dentro da região central e livre fora dela. Se o efeito continuar com o
FFB desligado, é necessário investigar outros ajustes do jogo/CSP com uma nova
reprodução; a deadzone por si só não acrescenta centralização.

## Testes, compatibilidade e restauração

Foram aprovadas **28.934 verificações em LuaJIT 2.1**, usando uma API CSP simulada,
para centro, limites, transições, extremos, deadzone desligada e regressão de pedais
com FFB ligado/desligado. Para repetir: `luajit tests/test_deadzone.lua`.

O usuário confirmou funcionamento no jogo em 14/10/2026 no ambiente local com
**CSP 0.2.11 build 3465** e depois relatou centralização indesejada. Por isso o FFB
permanece opcional e a orientação para direção livre é desligá-lo explicitamente.
A aplicação dessa preferência ainda precisa ser confirmada numa nova sessão.
Outras versões/carros e persistência do campo no CM não foram validados separadamente.

Para restaurar a instalação anterior, feche o jogo e copie sua pasta de backup de
volta. Para desligar somente a deadzone, defina `STEERING_DEADZONE=0`.

## Créditos e referências

Mod original **Mouse Steering Assist 1.0.5**: **CrepR / Jasn-tang** —
[repositório original](https://github.com/Jasn-tang/Mouse-Steering-Assist).
Fork e deadzone central: **sevenstarr**. Release comunitária independente.

Referência da leitura de configurações:
[API oficial INIConfig do CSP](https://github.com/ac-custom-shaders-patch/acc-lua-sdk/blob/main/common/ac_extras_ini.lua).

## English quick guide

Mouse steering with a configurable 0–10% central deadzone, scroll-controlled pedals,
alternate keyboard/mouse bindings, Shift pedal amount, pedal smoothing and optional
FFB steering correction. Use **`STEERING_DEADZONE=0.02` and `DOFFB=0`** for free
steering with a neutral central zone. Use **`DOFFB=1`** only if you want the existing
FFB correction, which can move steering without mouse input. Use numeric 0/1 in
the INI file. Restart the session after editing settings; CSP/CM user overrides
take precedence. Back up the MSA folder before extracting the release ZIP into
the Assetto Corsa root. Original author: CrepR/Jasn-tang; community fork: sevenstarr.
