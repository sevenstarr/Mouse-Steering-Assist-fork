"""Build and verify the installable MSA ZIP using only Python's standard library."""
from pathlib import Path
import argparse
import hashlib
import re
import zipfile

ROOT = Path(__file__).resolve().parent.parent
APP = 'extension/lua/mouse-steering/MSA'
FILES = tuple(f'{APP}/{name}' for name in (
    'assist.lua', 'settings.ini', 'manifest.ini', 'README-DEADZONE.md'))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-dir', type=Path, default=ROOT / 'dist')
    args = parser.parse_args()
    manifest = (ROOT / APP / 'manifest.ini').read_text(encoding='utf-8')
    version = re.search(r'^VERSION\s*=\s*([A-Za-z0-9.\-]+)\s*$', manifest, re.M).group(1)
    settings = (ROOT / APP / 'settings.ini').read_text(encoding='utf-8')
    assert re.search(r'^STEERING_DEADZONE=0\.02\s*;', settings, re.M), 'Expected default: 2%'
    assert 'Central Deadzone' in manifest and 'CrepR' in manifest, 'Missing identity/credits'
    args.output_dir.mkdir(parents=True, exist_ok=True)
    archive = args.output_dir / f'Mouse-Steering-Assist-{version}.zip'
    with zipfile.ZipFile(archive, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for name in FILES:
            data = (ROOT / name).read_bytes()
            info = zipfile.ZipInfo(name, date_time=(2026, 10, 14, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            z.writestr(info, data, compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
    with zipfile.ZipFile(archive) as z:
        assert tuple(z.namelist()) == FILES, 'Unexpected package entries'
        assert z.testzip() is None, 'ZIP integrity failure'
        for name in FILES:
            assert z.read(name) == (ROOT / name).read_bytes(), f'Content mismatch: {name}'
    digest = hashlib.sha256(archive.read_bytes()).hexdigest()
    (args.output_dir / 'SHA256SUMS.txt').write_text(f'{digest}  {archive.name}\n', encoding='ascii')
    print(f'PASS: {len(FILES)} verified entries, default 2%, original author credited.')
    print(f'{digest}  {archive.name}')


if __name__ == '__main__':
    main()
