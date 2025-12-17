import io
import sys
import platform
import subprocess
import matplotlib.pyplot as plt
from prompt_toolkit import PromptSession
from prompt_toolkit.history import InMemoryHistory
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.filters import Condition
from PIL import Image

# Configuration
DPI = 300
FONT_SIZE = 50

# Style: Computer Modern
plt.rcParams["mathtext.fontset"] = "cm"
plt.rcParams["font.family"] = "serif"

# --- INTELLISENSE LIST ---
latex_commands = [
    # Greek lowercase
    "alpha",
    "beta",
    "gamma",
    "delta",
    "epsilon",
    "varepsilon",
    "zeta",
    "eta",
    "theta",
    "vartheta",
    "iota",
    "kappa",
    "lambda",
    "mu",
    "nu",
    "xi",
    "omicron",
    "pi",
    "varpi",
    "rho",
    "varrho",
    "sigma",
    "varsigma",
    "tau",
    "upsilon",
    "phi",
    "varphi",
    "chi",
    "psi",
    "omega",
    # Greek uppercase
    "Gamma",
    "Delta",
    "Theta",
    "Lambda",
    "Xi",
    "Pi",
    "Sigma",
    "Upsilon",
    "Phi",
    "Psi",
    "Omega",
    # Binary operators
    "pm",
    "mp",
    "times",
    "div",
    "cdot",
    "ast",
    "star",
    "circ",
    "bullet",
    "oplus",
    "ominus",
    "otimes",
    "oslash",
    "odot",
    "bigcirc",
    "diamond",
    "uplus",
    "triangleleft",
    "triangleright",
    "bigtriangleup",
    "bigtriangledown",
    "wedge",
    "vee",
    "cap",
    "cup",
    "sqcap",
    "sqcup",
    "amalg",
    "dagger",
    "ddagger",
    "wr",
    "setminus",
    # Relations
    "leq",
    "le",
    "geq",
    "ge",
    "equiv",
    "models",
    "prec",
    "succ",
    "sim",
    "perp",
    "preceq",
    "succeq",
    "simeq",
    "mid",
    "ll",
    "gg",
    "asymp",
    "parallel",
    "subset",
    "supset",
    "approx",
    "bowtie",
    "subseteq",
    "supseteq",
    "cong",
    "sqsubset",
    "sqsupset",
    "neq",
    "ne",
    "smile",
    "sqsubseteq",
    "sqsupseteq",
    "doteq",
    "frown",
    "in",
    "ni",
    "propto",
    "vdash",
    "dashv",
    "notin",
    "notsubset",
    # Arrows
    "leftarrow",
    "gets",
    "longleftarrow",
    "rightarrow",
    "to",
    "longrightarrow",
    "leftrightarrow",
    "longleftrightarrow",
    "mapsto",
    "longmapsto",
    "hookleftarrow",
    "hookrightarrow",
    "leftharpoonup",
    "rightharpoonup",
    "leftharpoondown",
    "rightharpoondown",
    "rightleftharpoons",
    "Leftarrow",
    "Longleftarrow",
    "Rightarrow",
    "Longrightarrow",
    "Leftrightarrow",
    "Longleftrightarrow",
    "iff",
    "implies",
    "uparrow",
    "downarrow",
    "updownarrow",
    "Uparrow",
    "Downarrow",
    "Updownarrow",
    "nearrow",
    "searrow",
    "swarrow",
    "nwarrow",
    # Delimiters
    "left",
    "right",
    "big",
    "Big",
    "bigg",
    "Bigg",
    "langle",
    "rangle",
    "lfloor",
    "rfloor",
    "lceil",
    "rceil",
    "lbrace",
    "rbrace",
    "lbrack",
    "rbrack",
    # Large operators
    "sum",
    "prod",
    "coprod",
    "int",
    "oint",
    "iint",
    "iiint",
    "bigcap",
    "bigcup",
    "bigsqcup",
    "bigvee",
    "bigwedge",
    "bigodot",
    "bigotimes",
    "bigoplus",
    "biguplus",
    # Functions
    "sin",
    "cos",
    "tan",
    "cot",
    "sec",
    "csc",
    "arcsin",
    "arccos",
    "arctan",
    "arccot",
    "arcsec",
    "arccsc",
    "sinh",
    "cosh",
    "tanh",
    "coth",
    "log",
    "ln",
    "lg",
    "exp",
    "lim",
    "limsup",
    "liminf",
    "sup",
    "inf",
    "max",
    "min",
    "arg",
    "det",
    "dim",
    "deg",
    "gcd",
    "hom",
    "ker",
    "Pr",
    "mod",
    "bmod",
    "pmod",
    # Accents
    "hat",
    "check",
    "breve",
    "acute",
    "grave",
    "tilde",
    "bar",
    "vec",
    "dot",
    "ddot",
    "dddot",
    "ddddot",
    "widehat",
    "widetilde",
    "overline",
    "underline",
    "overbrace",
    "underbrace",
    "overrightarrow",
    "overleftarrow",
    # Fractions & roots
    "frac",
    "dfrac",
    "tfrac",
    "cfrac",
    "sqrt",
    "surd",
    # Spacing
    "quad",
    "qquad",
    ",",
    ":",
    ";",
    "!",
    "thinspace",
    "medspace",
    "thickspace",
    "negthinspace",
    "negmedspace",
    "negthickspace",
    # Text & fonts
    "text",
    "textrm",
    "textit",
    "textbf",
    "textsf",
    "texttt",
    "mathrm",
    "mathit",
    "mathbf",
    "mathsf",
    "mathtt",
    "mathcal",
    "mathbb",
    "mathfrak",
    "mathscr",
    "boldsymbol",
    # Structure
    "binom",
    "choose",
    # Symbols
    "infty",
    "partial",
    "nabla",
    "emptyset",
    "varnothing",
    "forall",
    "exists",
    "nexists",
    "neg",
    "lnot",
    "land",
    "lor",
    "angle",
    "measuredangle",
    "sphericalangle",
    "top",
    "bot",
    "prime",
    "backslash",
    "ell",
    "hbar",
    "hslash",
    "imath",
    "jmath",
    "wp",
    "Re",
    "Im",
    "aleph",
    "beth",
    "gimel",
    "daleth",
    # Dots
    "cdots",
    "ldots",
    "vdots",
    "ddots",
    # Matrices
    "matrix",
    "pmatrix",
    "bmatrix",
    "Bmatrix",
    "vmatrix",
    "Vmatrix",
    "cases",
    "split",
    "aligned",
    # Miscellaneous
    "displaystyle",
    "textstyle",
    "scriptstyle",
    "scriptscriptstyle",
    "limits",
    "nolimits",
]
# Add backslashes
latex_completer = WordCompleter(
    [f"\\{c}" for c in latex_commands],
    ignore_case=True,
    sentence=True,
    match_middle=False,
)


def get_image_bytes(image_buffer, fmt="PNG"):
    img = Image.open(image_buffer)
    with io.BytesIO() as out:
        if fmt == "BMP":
            bg = Image.new("RGB", img.size, (255, 255, 255))
            bg.paste(img, mask=img.split()[3])
            bg.save(out, format=fmt)
            return out.getvalue()[14:]
        img.save(out, format=fmt)
        return out.getvalue()


def send_to_clipboard(png_buffer):
    system = platform.system()
    png_buffer.seek(0)

    if system == "Darwin":
        with open("/tmp/latex_temp.png", "wb") as f:
            f.write(png_buffer.getvalue())
        cmd = 'set the clipboard to (read (POSIX file "/tmp/latex_temp.png") as «class PNGf»)'
        subprocess.run(["osascript", "-e", cmd], check=True)

    elif system == "Windows":
        import win32clipboard

        png_data = get_image_bytes(png_buffer, "PNG")
        png_buffer.seek(0)
        dib_data = get_image_bytes(png_buffer, "BMP")

        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        try:
            CF_PNG = win32clipboard.RegisterClipboardFormat("PNG")
            win32clipboard.SetClipboardData(CF_PNG, png_data)
        except:
            pass
        try:
            win32clipboard.SetClipboardData(win32clipboard.CF_DIB, dib_data)
        except:
            pass
        win32clipboard.CloseClipboard()

    elif system == "Linux":
        process = subprocess.Popen(
            ["xclip", "-selection", "clipboard", "-t", "image/png", "-i"],
            stdin=subprocess.PIPE,
        )
        process.communicate(input=png_buffer.getvalue())


def render_latex(formula):
    buf = io.BytesIO()
    fig = plt.figure(figsize=(0.1, 0.1))
    text = fig.text(
        0.5,
        0.5,
        f"${formula}$",
        fontsize=FONT_SIZE,
        ha="center",
        va="center",
        color="black",
    )

    fig.canvas.draw()
    bbox = text.get_window_extent()
    fig.set_size_inches((bbox.width / fig.dpi) + 0.1, (bbox.height / fig.dpi) + 0.1)

    plt.axis("off")
    plt.savefig(
        buf,
        format="png",
        dpi=DPI,
        transparent=True,
        bbox_inches="tight",
        pad_inches=0.05,
    )
    plt.close(fig)
    buf.seek(0)
    return buf


def main():
    # Create key bindings for auto bracket matching
    kb = KeyBindings()

    @kb.add("{")
    def _(event):
        event.current_buffer.insert_text("{}")
        event.current_buffer.cursor_left()

    @kb.add("(")
    def _(event):
        event.current_buffer.insert_text("()")
        event.current_buffer.cursor_left()

    @kb.add("[")
    def _(event):
        event.current_buffer.insert_text("[]")
        event.current_buffer.cursor_left()

    # Pass completer and key bindings to session
    session = PromptSession(
        history=InMemoryHistory(),
        completer=latex_completer,
        key_bindings=kb,
        enable_open_in_editor=False,
    )
    print("LaTeX CLI (TAB for Intellisense). Type 'exit' to quit.")

    while True:
        try:
            # complete_while_typing=True makes the menu pop up automatically
            text = session.prompt("LaTeX > ", complete_while_typing=True)

            if text.strip().lower() in ["exit", "quit"]:
                break
            if not text.strip():
                continue

            try:
                png_buffer = render_latex(text)
                send_to_clipboard(png_buffer)
                print("✓ Copied")
            except Exception as e:
                print(f"Error: {e}")

        except KeyboardInterrupt:
            continue
        except EOFError:
            break


if __name__ == "__main__":
    main()
