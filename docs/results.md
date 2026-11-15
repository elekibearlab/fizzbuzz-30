# Execution results

UTC: 2026-11-14T18:41:24.301018+00:00
Platform: Linux-6.18.58.1-microsoft-standard-WSL2-x86_64-with-glibc2.35

OK: 60 / NG: 0 (58 prior Linux results + 2 Windows Batch results)

| slug | version | result | detail |
| --- | --- | --- | --- |
| c | aligned | OK |  |
| c | idiomatic | OK |  |
| cpp | aligned | OK |  |
| cpp | idiomatic | OK |  |
| csharp | aligned | OK |  |
| csharp | idiomatic | OK |  |
| java | aligned | OK |  |
| java | idiomatic | OK |  |
| python | aligned | OK |  |
| python | idiomatic | OK |  |
| javascript | aligned | OK |  |
| javascript | idiomatic | OK |  |
| go | aligned | OK |  |
| go | idiomatic | OK |  |
| rust | aligned | OK |  |
| rust | idiomatic | OK |  |
| php | aligned | OK |  |
| php | idiomatic | OK |  |
| ruby | aligned | OK |  |
| ruby | idiomatic | OK |  |
| kotlin | aligned | OK |  |
| kotlin | idiomatic | OK |  |
| swift | aligned | OK |  |
| swift | idiomatic | OK |  |
| lua | aligned | OK |  |
| lua | idiomatic | OK |  |
| bash | aligned | OK |  |
| bash | idiomatic | OK |  |
| batch | aligned | OK | Windows cmd /d /c; 100 lines; CRLF/LF normalized; exit 0; stderr empty |
| batch | idiomatic | OK | Windows cmd /d /c; 100 lines; CRLF/LF normalized; exit 0; stderr empty |
| powershell | aligned | OK |  |
| powershell | idiomatic | OK |  |
| r | aligned | OK |  |
| r | idiomatic | OK |  |
| julia | aligned | OK |  |
| julia | idiomatic | OK |  |
| fortran | aligned | OK |  |
| fortran | idiomatic | OK |  |
| gdscript | aligned | OK |  |
| gdscript | idiomatic | OK |  |
| cobol | aligned | OK |  |
| cobol | idiomatic | OK |  |
| sql | aligned | OK |  |
| sql | idiomatic | OK |  |
| asm | aligned | OK |  |
| asm | idiomatic | OK |  |
| commonlisp | aligned | OK |  |
| commonlisp | idiomatic | OK |  |
| scheme | aligned | OK |  |
| scheme | idiomatic | OK |  |
| haskell | aligned | OK |  |
| haskell | idiomatic | OK |  |
| elixir | aligned | OK |  |
| elixir | idiomatic | OK |  |
| erlang | aligned | OK |  |
| erlang | idiomatic | OK |  |
| prolog | aligned | OK |  |
| prolog | idiomatic | OK |  |
| brainfuck | aligned | OK |  |
| brainfuck | idiomatic | OK |  |

## Runtime versions

| slug | runtime |
| --- | --- |
| c | gcc (Ubuntu 11.4.0-1ubuntu1~22.04.3) 11.4.0 / Copyright (C) 2021 Free Software Foundation, Inc. |
| cpp | g++ (Ubuntu 11.4.0-1ubuntu1~22.04.3) 11.4.0 / Copyright (C) 2021 Free Software Foundation, Inc. |
| csharp | Mono C# compiler version 6.8.0.105 |
| java | openjdk version "11.0.32.1" 2026-08-18 / OpenJDK Runtime Environment (build 11.0.32.1+1-post-1ubuntu1-22.04-Ubuntu) |
| python | Python 3.10.12 |
| javascript | v12.22.9 |
| go | go version go1.18.1 linux/amd64 |
| rust | rustc 1.75.0 (82e1608df 2023-12-21) (built from a source tarball) |
| php | PHP 8.1.2-1ubuntu2.28 (cli) (built: Oct 19 2026 18:54:45) (NTS) / Copyright (c) The PHP Group |
| ruby | ruby 3.0.2p107 (2021-07-07 revision 0db68f0233) [x86_64-linux-gnu] |
| kotlin | info: kotlinc-jvm 1.3-SNAPSHOT (JRE 11.0.32.1+1-post-1ubuntu1-22.04-Ubuntu) |
| swift | Swift version 5.10.1 (swift-5.10.1-RELEASE) / Target: x86_64-unknown-linux-gnu |
| lua | Lua 5.4.4  Copyright (C) 1994-2022 Lua.org, PUC-Rio |
| bash | GNU bash, version 5.1.16(1)-release (x86_64-pc-linux-gnu) / Copyright (C) 2020 Free Software Foundation, Inc. |
| batch | Microsoft Windows [Version 10.0.26300.9974] |
| powershell | PowerShell 7.4.13 |
| r | R scripting front-end version 4.1.2 (2021-11-01) |
| julia | julia version 1.10.10 |
| fortran | GNU Fortran (Ubuntu 11.4.0-1ubuntu1~22.04.3) 11.4.0 / Copyright (C) 2021 Free Software Foundation, Inc. |
| gdscript | 4.3.stable.official.77dcf97d8 |
| cobol | cobc (GnuCOBOL) 3.1.2.0 / Copyright (C) 2020 Free Software Foundation, Inc. |
| sql | 3.37.2 2022-01-06 13:25:41 872ba256cbf61d9290b571c0e6d82a20c224ca3ad82971edc46b29818d5dalt1 |
| asm | NASM version 2.15.05 |
| commonlisp | SBCL 2.1.11.debian |
| scheme | guile (GNU Guile) 3.0.7 / Packaged by Debian (3.0.7-deb+3.0.7-1) |
| haskell | The Glorious Glasgow Haskell Compilation System, version 8.8.4 |
| elixir | Erlang/OTP 24 [erts-12.2.1] [source] [64-bit] [smp:16:16] [ds:16:16:10] [async-threads:1] [jit] / Elixir 1.12.2 (compiled with Erlang/OTP 24) |
| erlang | OTP 24 / ERTS 12.2.1 |
| prolog | SWI-Prolog version 8.4.2 for x86_64-linux |
| brainfuck | bf - a Brainfuck interpreter       version 20041219 / (C) 2003, 2004, Stephan Beyer, GPL, s-beyer@gmx.net |

## Unavailable runtimes

None.

## Verification

The 58 unchanged programs retain the Linux results dated above.
Batch was verified separately on 2026-11-15T05:08:50.629475+00:00
on Windows-11-10.0.26300-SP0. Both cmd /d /c outputs match expected.txt
after CRLF/LF normalization (100 lines, exit 0, empty stderr).
Linux verify.py skips Batch; it does not claim a Windows pass.

Each non-Batch source is built independently and executed with a 180-second
timeout. Its output is compared byte-for-byte using diff -u.
Build commands, stdout, stderr and diffs remain in .build/.
Only the Godot startup banner is removed before comparison.
SQL runs in a fresh in-memory SQLite database.
Brainfuck runs with unsigned 8-bit wrapping cells.

stats.csv counts nonempty lines and Unicode characters other
than whitespace. Source files contain no comments.
