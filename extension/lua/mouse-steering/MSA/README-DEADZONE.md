# Mouse Steering Assist — Central Deadzone

## Português

Fork comunitário do Mouse Steering Assist 1.0.5 de CrepR/Jasn-tang.
Adiciona deadzone central de 0% a 10%, com padrão de 2%. A posição acumulada
do mouse é preservada e somente a saída de direção é remapeada. Os extremos
continuam em -1 e +1. Acelerador, freio, embreagem e FFB opcional não foram alterados.

### Instalação

1. Feche o Assetto Corsa. Faça backup da pasta existente
   `extension/lua/mouse-steering/MSA` e anote suas configurações personalizadas.
2. Extraia a pasta `extension` deste ZIP na pasta raiz do Assetto Corsa,
   onde está `acs.exe`. Confirme a substituição dos arquivos do MSA.
3. No Content Manager, selecione Mouse Steering Assist - Central Deadzone:
   CSP 0.2.x: Settings → Custom Shaders Patch → General Patch settings →
   Mouse steering tweaks → Use script. CSP 0.3.x: Keyboard & Mouse, conforme
   a interface da versão instalada. Ative também a direção por mouse nos controles.
4. Reinicie o Content Manager se o nome/opção não atualizar e inicie uma sessão.
   Preserve suas atribuições de pedais; esta versão não muda controles globais.

### Configuração

Procure Steering deadzone nas opções do script, se suportado pelo CM/CSP.
Se a opção não aparecer, edite `settings.ini` nesta pasta e mantenha a seção existente:

```ini
[SETTINGS]
STEERING_DEADZONE=0.02
```

`0.02` = 2%; `0.1` = 10%; `0` = desligado. Use ponto decimal e reinicie a sessão.
Preferências já salvas pelo CSP/CM podem prevalecer sobre o padrão do arquivo.
O ZIP substitui os padrões do MSA; reaplique seus valores personalizados após atualizar.

### Validação e restauração

28.934 verificações passaram em LuaJIT 2.1 com API CSP simulada. O usuário do fork
testou esta lógica dentro do Assetto Corsa e confirmou funcionamento em 14/10/2026,
no ambiente local com CSP 0.2.11 build 3465. O empacotamento altera apenas
identificação e documentação em relação à lógica testada. Outros CSPs e carros
não foram validados por essa sessão. Não houve verificação separada da persistência
do campo no Content Manager. Para desfazer, restaure sua pasta de backup; para
desativar apenas a deadzone, use 0%.

## English

Community fork of Mouse Steering Assist 1.0.5 by CrepR/Jasn-tang. Adds a configurable
0–10% central deadzone, default 2%, without changing pedal code or optional FFB.
Raw accumulated steering is preserved; only the final output is remapped.

Close the game, back up your existing `extension/lua/mouse-steering/MSA` folder
and settings, then extract `extension` into the Assetto Corsa root containing
`acs.exe`. Select Mouse Steering Assist - Central Deadzone in CSP's mouse steering
script settings in Content Manager. Reopen CM if the script label is cached.
Keep your existing pedal bindings and reapply custom script settings after updating.

Use Steering deadzone in the script options where supported, or edit the existing
`[SETTINGS]` section of `settings.ini`: `STEERING_DEADZONE=0.02`. Use `0` to disable
or `0.1` for 10%. CSP/CM user overrides take precedence. Restart the session.

28,934 assertions passed under LuaJIT 2.1 with a simulated CSP API. The fork user
reported successful in-game testing on 2026-10-14 in the local CSP 0.2.11 build
3465 environment. Other CSP versions/cars and CM settings persistence were not
separately validated. Restore your backup to uninstall.

## Credits / Créditos

Original mod: CrepR / Jasn-tang — https://github.com/Jasn-tang/Mouse-Steering-Assist
Central deadzone fork: sevenstarr — https://github.com/sevenstarr/Mouse-Steering-Assist-fork
This is an independent community release, not an official upstream release.
