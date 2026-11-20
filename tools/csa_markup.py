"""Convierte el markup de enunciados de CSAcademy a HTML y a Markdown estandar.

Sintaxis de CSAcademy usada en los enunciados:
  - cada linea es un parrafo
  - "#2 Titulo"            -> encabezado de nivel 2
  - "- item" / "1. item"   -> listas
  - "```" ... "```"        -> bloque de codigo
  - "*texto*"              -> negrita
  - "$$x$$"                -> formula LaTeX en linea
  - "`code`"               -> codigo en linea
  - <Link value="t" href="u">  -> enlace
  - <TaskExamples />       -> tabla de ejemplos de entrada/salida
"""
import html
import re

INLINE = re.compile(
    r"(?P<code>`[^`]*`)"
    r"|(?P<math>\$\$.+?\$\$)"
    r"|(?P<link><Link\s+value=\"(?P<lv>[^\"]*)\"\s+href=\"(?P<lh>[^\"]*)\"\s*/?>)"
    r"|(?P<bold>\*(?P<bt>[^*\s][^*]*?)\*)"
)
HEADING = re.compile(r"^#(\d)\s+(.*)$")
UL = re.compile(r"^-\s+(.*)$")
OL = re.compile(r"^\d+\.\s+(.*)$")
EXAMPLES = re.compile(r"^\s*<TaskExamples\s*/>\s*$")


# ---------------------------------------------------------------- inline
def inline_html(text):
    out, pos = [], 0
    for m in INLINE.finditer(text):
        out.append(html.escape(text[pos:m.start()], quote=False))
        if m.group("code"):
            out.append(f"<code>{html.escape(m.group('code')[1:-1], quote=False)}</code>")
        elif m.group("math"):
            out.append(f'<span class="math">\\({html.escape(m.group("math")[2:-2], quote=False)}\\)</span>')
        elif m.group("link"):
            out.append(f'<a href="{html.escape(m.group("lh"))}" target="_blank" rel="noopener">'
                       f'{html.escape(m.group("lv"))}</a>')
        else:
            out.append(f"<strong>{inline_html(m.group('bt'))}</strong>")
        pos = m.end()
    out.append(html.escape(text[pos:], quote=False))
    return "".join(out)


def inline_md(text):
    out, pos = [], 0
    for m in INLINE.finditer(text):
        out.append(text[pos:m.start()])
        if m.group("code"):
            out.append(m.group("code"))
        elif m.group("math"):
            out.append(f"${m.group('math')[2:-2].strip()}$")
        elif m.group("link"):
            out.append(f"[{m.group('lv')}]({m.group('lh')})")
        else:
            out.append(f"**{inline_md(m.group('bt'))}**")
        pos = m.end()
    out.append(text[pos:])
    return "".join(out)


# ---------------------------------------------------------------- blocks
def blocks(markup):
    """Genera bloques (tipo, contenido) a partir del markup."""
    lines = markup.replace("\r\n", "\n").split("\n")
    i, n = 0, len(lines)
    while i < n:
        line = lines[i]
        if line.strip().startswith("```"):
            code = []
            i += 1
            while i < n and not lines[i].strip().startswith("```"):
                code.append(lines[i])
                i += 1
            i += 1
            yield ("code", code)
            continue
        if not line.strip():
            i += 1
            continue
        if EXAMPLES.match(line):
            yield ("examples", None)
        elif (h := HEADING.match(line)):
            yield ("heading", (int(h.group(1)), h.group(2).strip()))
        elif UL.match(line) or OL.match(line):
            kind = "ul" if UL.match(line) else "ol"
            pat = UL if kind == "ul" else OL
            items = []
            while i < n and pat.match(lines[i]):
                items.append(pat.match(lines[i]).group(1))
                i += 1
                # una lista continua aunque haya lineas vacias entre sus items
                j = i
                while j < n and not lines[j].strip():
                    j += 1
                if j < n and pat.match(lines[j]):
                    i = j
            yield (kind, items)
            continue
        else:
            yield ("p", line)
        i += 1


def examples_html(examples):
    if not examples:
        return ""
    has_expl = any(e.get("comment") for e in examples)
    head = "<th>Input</th><th>Output</th>" + ("<th>Explanation</th>" if has_expl else "")
    rows = []
    for e in examples:
        row = (f'<td><div class="io-label">Entrada</div><pre class="io">{html.escape(e["input"])}</pre></td>'
               f'<td><div class="io-label">Salida</div><pre class="io">{html.escape(e["output"])}</pre></td>')
        if has_expl:
            row += f'<td class="expl"><div class="io-label">Explicación</div>{to_html(e.get("comment") or "")}</td>'
        rows.append(f"<tr>{row}</tr>")
    cls = "examples has-expl" if has_expl else "examples"
    return f'<table class="{cls}"><thead><tr>{head}</tr></thead><tbody>{"".join(rows)}</tbody></table>'


def to_html(markup, examples=()):
    parts = []
    for kind, c in blocks(markup):
        if kind == "code":
            body = "".join(f"<span>{html.escape(l)}</span>" for l in c)
            parts.append(f'<pre class="code">{body}</pre>')
        elif kind == "examples":
            parts.append(examples_html(examples))
        elif kind == "heading":
            lvl = min(max(c[0], 2), 4)
            parts.append(f"<h{lvl}>{inline_html(c[1])}</h{lvl}>")
        elif kind in ("ul", "ol"):
            parts.append(f"<{kind}>" + "".join(f"<li>{inline_html(x)}</li>" for x in c) + f"</{kind}>")
        else:
            parts.append(f"<p>{inline_html(c)}</p>")
    return "\n".join(parts)


def _md_lines(markup, examples=()):
    out = []
    for kind, c in blocks(markup):
        if kind == "code":
            out += ["```", *c, "```", ""]
        elif kind == "examples":
            for e in examples:
                out += [f"### Ejemplo {e['index']}", "", "Entrada:", "", "```", e["input"].rstrip("\n"), "```",
                        "", "Salida:", "", "```", e["output"].rstrip("\n"), "```", ""]
                if e.get("comment"):
                    out += ["Explicación:", ""] + _md_lines(e["comment"])
        elif kind == "heading":
            out += [f"{'#' * min(max(c[0], 2), 4)} {inline_md(c[1])}", ""]
        elif kind == "ul":
            out += [f"- {inline_md(x)}" for x in c] + [""]
        elif kind == "ol":
            out += [f"{k}. {inline_md(x)}" for k, x in enumerate(c, 1)] + [""]
        else:
            out += [inline_md(c), ""]
    return out


def to_markdown(markup, title, header_lines=(), examples=()):
    out = [f"# {title}", ""] + list(header_lines) + ([""] if header_lines else [])
    out += _md_lines(markup, examples)
    return "\n".join(out).rstrip() + "\n"
