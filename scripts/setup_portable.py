from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import subprocess
import sys
import urllib.request
import zipfile

root = Path(__file__).resolve().parent.parent
downloads = root / '.downloads'
runtimes = root / '.runtimes'
downloads.mkdir(exist_ok=True)
runtimes.mkdir(exist_ok=True)

packages = [
    ('godot',
     'https://github.com/godotengine/godot/releases/download/'
     '4.3-stable/Godot_v4.3-stable_linux.x86_64.zip'),
    ('swift',
     'https://download.swift.org/swift-5.10.1-release/'
     'ubuntu2204/swift-5.10.1-RELEASE/'
     'swift-5.10.1-RELEASE-ubuntu22.04.tar.gz'),
    ('julia',
     'https://julialang-s3.julialang.org/bin/linux/x64/'
     '1.10/julia-1.10.10-linux-x86_64.tar.gz'),
    ('powershell',
     'https://github.com/PowerShell/PowerShell/releases/'
     'download/v7.4.13/powershell-7.4.13-linux-x64.tar.gz'),
]

def install(package):
    name, url = package
    extension = 'zip' if name == 'godot' else 'tar.gz'
    archive = downloads / f'{name}.{extension}'
    target = runtimes / name
    target.mkdir(exist_ok=True)
    if (target / '.installed').exists():
        return
    if not archive.exists():
        print(f'Downloading {name}', flush=True)
        urllib.request.urlretrieve(url, archive)
    if name == 'godot':
        with zipfile.ZipFile(archive) as package:
            package.extractall(target)
        executable = target / 'Godot_v4.3-stable_linux.x86_64'
        executable.rename(target / 'godot')
        (target / 'godot').chmod(0o755)
    else:
        args = ['tar', '-xzf', str(archive), '-C', str(target)]
        if name != 'powershell':
            args.append('--strip-components=1')
        subprocess.run(args, check=True)
    if name == 'powershell':
        (target / 'pwsh').chmod(0o755)
    (target / '.installed').touch()
    print(f'Installed {name}', flush=True)

with ThreadPoolExecutor(max_workers=3) as pool:
    list(pool.map(install, [
        p for p in packages if len(sys.argv) == 1
        or p[0] in sys.argv[1:]
    ]))
