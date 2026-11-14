set -eu
cd "$(dirname "$0")"
apt-get update
DEBIAN_FRONTEND=noninteractive apt-get install -y \
    build-essential mono-mcs default-jdk python3 nodejs \
    golang-go rustc php-cli ruby kotlin scala lua5.4 \
    r-base-core gfortran godot3-server gnucobol sqlite3 \
    nasm sbcl guile-3.0 ghc elixir swi-prolog bf \
    curl xz-utils unzip libicu70 libxml2 libncurses6 \
    libpython3.10 libcurl4 libedit2 libsqlite3-0
