# 🐧 Linux Command Finder

Monawada karanna one kiyala simple widihata (English/Singlish) liyuwahama,
gälapena Linux command eka pennana simple desktop app ekak.

## Awashya dewal

- **Python 3** witharai one (Ubuntu/Debian/Mint wage distros walata dan systema
  ekama tiyenawa).
- `tkinter` module eka. Adaala nathnam terminal eke mehema danna:

```bash
sudo apt update
sudo apt install python3-tk
```

## Run karana krama

1. Zip file eka extract karanna.
2. Terminal eka open karala eka folder ekata yanna:

```bash
cd linux-cmd-finder
```

3. App eka run karanna:

```bash
python3 main.py
```

Ithin app window eka open weyi. Uda thiyena search box eke oyaage
kaarayak liyala **Search** button eka click karanna (nathnam Enter
danna). Gälapena commands tika card widihata pennei — ethanin
**Copy** button eken command eka copy karaganna puluwan.

## Files tika mokakda

- `main.py` — App eke GUI eka saha search logic eka.
- `commands_db.py` — Commands (~70k) tika, description saha keywords
  ekka thiyena database eka. Mehema aluth command ekak add karanna
  one nam, `COMMANDS` list ekata aluth dictionary ekak add karanna.

## Aluth command ekak add karanna krama

`commands_db.py` file eka open karala mehema entry ekak add karanna:

```python
{
    "command": "df -h",
    "description": "Disk eke space kochchara athida kiyala balanawa",
    "keywords": ["disk space", "storage balanna", "df"],
},
```

`keywords` list eke oyaata one wenam widihen (English/Singlish) liyanna
puluwan — search eka e okkoma walin match wenawa.

Enjoy! 🎉
