"""Construye el sitio estatico en _site/ a partir de problemas/.

Uso: python tools/build_site.py
"""
import json
import shutil
import zipfile
from pathlib import Path

from csa_markup import to_html

REPO = Path(__file__).resolve().parent.parent
PROB = REPO / "problemas"
OUT = REPO / "_site"


def zip_dir(zf, folder, arc_root):
    for p in sorted(folder.rglob("*")):
        if p.is_file():
            zf.write(p, f"{arc_root}/{p.relative_to(folder).as_posix()}")


def main():
    OUT.mkdir(exist_ok=True)
    for child in OUT.iterdir():  # vaciar sin borrar la carpeta (puede estar en uso)
        shutil.rmtree(child) if child.is_dir() else child.unlink()
    (OUT / "descargas").mkdir()
    shutil.copytree(PROB, OUT / "problemas")

    tasks = []
    folders = sorted(p for p in PROB.iterdir() if p.is_dir())
    for f in folders:
        meta = json.loads((f / "meta.json").read_text(encoding="utf-8"))
        markup = (f / "enunciado.csa.txt").read_text(encoding="utf-8")
        meta["html"] = to_html(markup, meta["examples"])
        tasks.append(meta)
        with zipfile.ZipFile(OUT / "descargas" / f"{f.name}.zip", "w", zipfile.ZIP_DEFLATED) as zf:
            zip_dir(zf, f, f.name)

    with zipfile.ZipFile(OUT / "descargas" / "ieeextreme20-tareas.zip", "w", zipfile.ZIP_DEFLATED) as zf:
        zf.write(REPO / "README.md", "ieeextreme20-tareas/README.md")
        for f in folders:
            zip_dir(zf, f, f"ieeextreme20-tareas/{f.name}")

    tasks.sort(key=lambda t: t["order"])
    data = json.dumps(tasks, ensure_ascii=False).replace("</", "<\\/")
    page = (REPO / "site" / "template.html").read_text(encoding="utf-8").replace("/*DATA*/", data)
    (OUT / "index.html").write_text(page, encoding="utf-8")
    (OUT / ".nojekyll").write_text("", encoding="utf-8")
    print(f"Sitio generado en {OUT} con {len(tasks)} tareas")


if __name__ == "__main__":
    main()
