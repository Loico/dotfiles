" --- General

" enable syntax highlighting
syntax on

" number of spaces in a <Tab>
set tabstop=4
set softtabstop=4
set expandtab

" enable autoindents
set smartindent

" adds line numbers
set number
set relativenumber

" columns used for the line number
set numberwidth=4

" start scrolling when 8 lines from top or bottom
set scrolloff=8

" highlights the matched text pattern when searching
set incsearch
set hlsearch

" open splits intuitively
set splitbelow
set splitright


" --- Plugins

call plug#begin('~/.config/nvim/plugged')

" define your plugins
Plug 'sainnhe/everforest'

call plug#end()

" --- Colors

if has('termguicolors')
        set termguicolors
endif
set background=dark
let g:everforest_background = 'hard'
colorscheme everforest

