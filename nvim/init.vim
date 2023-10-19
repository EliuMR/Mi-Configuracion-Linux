syntax on

set mouse=a
set sw=2
set expandtab
set smartindent
set number
set nowrap
set noswapfile
set incsearch
set ignorecase
set clipboard=unnamedplus
set encoding=utf-8
set cursorline
set termguicolors

call plug#begin('/home/eliu/.config/nvim/plugged')
"temas
Plug 'https://github.com/morhetz/gruvbox.git'
Plug 'sonph/onehalf'
Plug 'https://github.com/folke/tokyonight.nvim.git'
Plug 'tiagovla/tokyodark.nvim'
"Para las lineas de ident
Plug 'Yggdroot/indentLine' 
"Para el arbol de archivos
Plug 'preservim/nerdtree'
"iconos en nerdtree
Plug 'ryanoasis/vim-devicons'
call plug#end()
colorscheme tokyodark

