from pathlib import Path
_code=''.join(p.read_text(encoding='utf-8') for p in sorted((Path(__file__).resolve().parent/'parts').glob('*.txt')))
exec(compile(_code,__file__,'exec'),globals(),globals())
