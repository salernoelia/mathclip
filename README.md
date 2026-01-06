# Mathclip

<img width="842" height="606" alt="Screenshot 2025-12-28 at 22 28 59" src="https://github.com/user-attachments/assets/7ee65cff-c4fd-4727-880e-33d21177723f" />

<img
  width="1144"
  height="231"
  alt="image"
  style="background-color: #ffffff"
  src="https://github.com/user-attachments/assets/f53adcc5-ef6d-4988-b51f-8f470edd277f"
/>


**Mathclip** converts LaTeX strings into high-resolution transparent PNG images and copies them directly to your clipboard.

## Usage

Run `python -m mathclip.main` to start.  
Use `-w`, `-r`, `-b`, or `-g` to render in white, red, blue, or green for the session.  
Type LaTeX, press Enter to copy image to clipboard. Type `exit` to quit.

## Functionality

* **Render LaTeX to Image:** Uses Matplotlib to generate a high-quality (300 DPI) image from math syntax.
* **Automatic Clipboard Copy:** Detects your OS (Windows, macOS, Linux) and sends the rendered image to the system clipboard for immediate pasting into documents or chat apps.
* **Interactive CLI:** Includes a command-line interface with:
* **Tab-completion:** Suggests LaTeX commands and symbols as you type.
* **Snippets:** Automatically inserts brackets for complex commands (e.g., `\frac{}{}`).
* **Smart Navigation:** Use `Ctrl + Space` to jump between placeholders in snippets.
* **Auto-pairing:** Automatically closes braces, parentheses, and brackets.


## Install (with uv package manager)


Fetch deps:
```sh
uv sync
```

Global Install:
```sh
uv tool install . 
```

### Linux

Requires xclip to run, ubuntu / debian: 

```sh
sudo apt install xclip
```

