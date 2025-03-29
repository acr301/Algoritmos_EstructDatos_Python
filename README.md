# Mi entorno de desarrollo para Python

[2025-03-29 00-36-28.webm](https://github.com/user-attachments/assets/7602b97b-63d9-4855-9028-b611cb72abbb)


## Versión del lenguaje

Uso el administrador de paquetes para Mac [brew](https://brew.sh/). Para Windows recomiendo [scoop](https://scoop.sh/). Para Linux su respectivo package manager de la distribución. De ahora en adelante las instrucciones solo tendrán sentido para Linux/Mac.

Lo instalamos con el script ``/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"``

Luego un simple ``brew install python`` nos descargará una de [las versiones](https://devguide.python.org/versions/) de Python 3. 

Para ver información sobre entornos de desarrollo virtuales en python, pip, setuptools, módulos, ubicaciones de binarios, configuraciones, variables de entorno y la documentación de quienes mantienen el paquete, está el artículo [Homebrew and Python](https://docs.brew.sh/Homebrew-and-Python).

El concepto de administradores de paquetes puede parecer extraño. Pero consolidar el versionado, plataformas, dependencias, conflictos, enlaces de sistemas, y lo más importante, la certeza del software que estás usando lo podés modificar a tu gusto tanto como si vos mismo lo hubieras compilado y empaquetado, no tiene precio. npm, cargo, pip, son algunos ejemplos. En tipos de desarrollo bleeding-edge (actualizaciones frecuentes como [ArchLinux](https://archlinux.org/)), versiones "no-estables" puede lograrse paradojicamente, una muy buena estabilidad si se aprovecha el potencial de un administrador de paquetes.
 

## Editor de texto

Uso el emulador de terminal [Kitty](https://sw.kovidgoyal.net/kitty/) [Neovim](https://neovim.io/) con [Lazyvim](https://www.lazyvim.org/) con sus plugins base, más [Mason](https://github.com/williamboman/mason.nvim) para instalar [pyright](https://microsoft.github.io/pyright/#/features) que hará de type checker, formateador, sugerencias de código, para Python. En nuestro caso, en Neovim, con toda la universalidad de la edición modal como en vi, agregamos el poder agregar plugins modularmente escritos en Lua. Lazylua es un cargador y mantenedor de plugins. No es necesario saber programar en Lua para entender qué está pasando. Y no se necesita pensar mucho para [escribir comandos y scripts propios](https://neovim.io/doc/user/lua-guide.html). 

1. Instalamos neovim ``brew install neovim``
2. Creamos un respaldo de la configuración de neovim ``mv ~/.config/nvim{,.bak}``
3. Clonamos una configuración inicial de Lazyvim ``git clone https://github.com/LazyVim/starter ~/.config/nvim``
4. Borramos el archivo .git ``rm -rf ~/.config/nvim/.git`` para poder hacer version-tracking de nuestra configuración más luego.
5. Ya podemos correr ``nvim`` 

Si es tu primera vez usando un editor de texto modal, te recomiendo tomarte el momento para aprender cómo salir de neovim, cambiar entre modo. Para esto puede ser util presionar la barra espaciadora en el modo Normal, y explorar las diferentes opciones. Esto es gracias a un plugin de calidad de vida que trae Lazyvim.

* El arranque es ``~/.config/nvim/init.lua``
* Dentro de ``nvim/lua`` hay ``lua/config`` y ``lua/plugins`` para configuración de los plugins agregados e agregar plugins, respectivamente.

1. Creamos ``lua/plugins/lsp.lua``
2. Dentro, pegamos : 
```return {
  -- agrear mason y su config, si notás, va al código fuente del plugin!
  {
    "williamboman/mason.nvim",
    config = true,
  },
  {
    "williamboman/mason-lspconfig.nvim",
    config = function()
      require("mason-lspconfig").setup({
        -- aqui van los servidores de lenguaje
        ensure_installed = {
          "pyright", -- Python
        },
      })
    end,
  },
}
```
3. Luego en ``lua/config/lsp.lua`` pegamos lo siguiente, para poder tener una configuración desglosada por servidor de lenguaje por lenguaje. 
```
local lspconfig = require("lspconfig")

-- pyright for Python
lspconfig.pyright.setup({})

```

Con esto, ya es posible hacer `nvim programa.py` y al escribir el código tendremos algo como un Vscode, personalizado, liviano, rápido.
Al guardar y salir, lo corremos con ``python3 programa.py``.

En la medida que comience a usar Python más, tal vez trataría de replicar un [Jupyter Notebook](https://jupyter.org/try-jupyter/notebooks/?path=notebooks/Intro.ipynb).

Gracias.
