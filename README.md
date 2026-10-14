# Mouse Steering Assist — Central Deadzone

Community fork with a configurable central mouse steering deadzone: **2% by default**,
adjustable from **0% to 10%**. Set 0% to restore the original steering response.

## Download / Baixar

**[Download Mouse-Steering-Assist-1.0.5-deadzone.1.zip](https://github.com/sevenstarr/Mouse-Steering-Assist-fork/releases/download/v1.0.5-deadzone.1/Mouse-Steering-Assist-1.0.5-deadzone.1.zip)** · [Release notes](https://github.com/sevenstarr/Mouse-Steering-Assist-fork/releases/tag/v1.0.5-deadzone.1)

Download the ready-to-install ZIP from Assets. The automatically generated Source
code archives are for source browsing; the named ZIP contains the installation layout.

## Install / Instalar

Close the game, back up your existing `extension/lua/mouse-steering/MSA` folder and
settings, then extract the ZIP's `extension` folder into the Assetto Corsa root.
Select **Mouse Steering Assist - Central Deadzone** in Content Manager's CSP mouse
steering settings. See the [Portuguese/English installation guide](extension/lua/mouse-steering/MSA/README-DEADZONE.md).

Feche o jogo, faça backup da pasta MSA e de suas configurações, extraia `extension`
na raiz do Assetto Corsa e selecione **Mouse Steering Assist - Central Deadzone**
no Content Manager. O padrão é 2%; 0% desliga a deadzone.

## Behavior and verification

The deadzone applies to the accumulated normalized steering axis, not individual
mouse deltas. The continuous linear remap preserves full lock and the accumulated
position. Pedal code, clutch behavior and optional FFB remain unchanged.

**28,934 LuaJIT assertions passed** with a simulated CSP API. The fork user reported
successful in-game testing on 2026-10-14 in the local CSP 0.2.11 build 3465 environment.
Other versions/cars and CM settings persistence were not separately validated.

Run `luajit tests/test_deadzone.lua` from the repository root.
Build the same installable ZIP with `python tools/make_release.py --output-dir dist`.
The packager also writes a SHA-256 checksum and verifies every archive entry.

## Credits

Original Mouse Steering Assist 1.0.5 by **CrepR / Jasn-tang**:
[upstream repository](https://github.com/Jasn-tang/Mouse-Steering-Assist).
Central deadzone fork maintained by **sevenstarr**. This is an independent
community release, not an official release from the original author.

[Technical details](docs/steering-deadzone.md) · [Changelog](CHANGELOG.md)
