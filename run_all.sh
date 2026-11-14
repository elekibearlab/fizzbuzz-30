set -eu
cd "$(dirname "$0")"
ROOT="$PWD"
export PATH="$ROOT/.runtimes/godot:$ROOT/.runtimes/swift/usr/bin:$ROOT/.runtimes/julia/bin:$ROOT/.runtimes/powershell:$PATH"
mkdir -p "$ROOT/.build/tmp"
export TMPDIR="$ROOT/.build/tmp"
export GOCACHE="$ROOT/.build/go-cache"
export GOPATH="$ROOT/.build/go-path"
export JULIA_DEPOT_PATH="$ROOT/.build/julia-depot"
export XDG_CACHE_HOME="$ROOT/.build/cache"
export XDG_CONFIG_HOME="$ROOT/.build/config"
export XDG_DATA_HOME="$ROOT/.build/data"
export GUILE_AUTO_COMPILE=0
export LC_ALL=C.UTF-8
python3 -B verify.py
exec python3 -B audit.py
