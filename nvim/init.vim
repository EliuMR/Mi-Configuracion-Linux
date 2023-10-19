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
"Copilot
Plug 'github/copilot.vim'
"Para la barra de estado
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'
call plug#end()
"key leader
let mapleader = " "
"tema
colorscheme tokyodark
"establecer que airline salga la linea superior
let g:airline#extensions#tabline#enabled = 1
let g:airline#extensions#tabline#left_sep = '|'
"tema deus line de airline
let g:airline_theme='deus'
"TERMINAL
vnoremap <c-t> :split<CR> :term<CR>
nnoremap <c-t> :split<CR> :term<CR>
"normal mode terminal
tnoremap <Esc> <C-\><C-n>
"PARA NERDTREE
"para que se vea el arbol de archivos con la letra lider + m
nnoremap <leader>m :NERDTreeToggle<CR>

"PARA LOS BUFFERS
"crear nuevo buffer con la letra lider + n
nnoremap <leader>n :tabe<CR>
"moverse al buffer siguiente con la letra lider + k
nnoremap <leader>k :tabnext<CR>
"moverse al buffer anterior con la letra lider + j
nnoremap <leader>j :tabprevious<CR>
"cerrar buffer con la letra lider + q
nnoremap <leader>w :bdelete<CR>
"hacer un split vertical con la letra lider + v
nnoremap <leader>v :vsplit<CR>
"hacer un split horizontal con la letra lider + h
nnoremap <leader>h :split<CR>
"Para reducir el tamaño de la ventana con la letra lider  con control + l
nnoremap <C-h> :vertical resize -2<CR>
"Para aumentar el tamaño de la ventana con la letra lider  con control + h
nnoremap <C-l> :vertical resize +2<CR>
"Para reducir el tamaño de la ventana con la letra lider  con control + j
nnoremap <C-j> :resize -2<CR>
"Para aumentar el tamaño de la ventana con la letra lider  con control + k
nnoremap <C-k> :resize +2<CR>
