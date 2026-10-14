# Changelog

## 1.0.5-deadzone.1 — 2026-10-14

- Add a central steering deadzone: default 2%, adjustable from 0% to 10%.
- Remap the accumulated normalized axis only at final steering output.
- Preserve full lock, pedal code, optional FFB and upstream CSP compatibility guard.
- Add LuaJIT regression tests: 28,934 assertions passed with a simulated CSP API.
- User reported successful in-game testing in the local CSP 0.2.11 build 3465 environment.
- Add a versioned installable ZIP, SHA-256 checksum, reproducible packager and
  Portuguese/English installation and restoration instructions.
- Identify the package as the sevenstarr community fork; retain original author credits.
