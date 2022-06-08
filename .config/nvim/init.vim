" --- General

" enable syntax highlighting
syntax on

" number of spaces in a <Tab>
set tabstop=4
set shiftwidth=4  " Indents will have a width of 4.
set softtabstop=4
set expandtab

" enable autoindents
set smartindent

" text width
set colorcolumn=80

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

" jump to the last position when reopening a file
if has("autocmd")
    au BufReadPost * if line("'\"") <= line("$")
                \| exe "normal! g'\"" | endif
endif

" --- Plugins

call plug#begin('~/.config/nvim/plugged')

" define your plugins
Plug 'sainnhe/everforest'
Plug 'neovim/nvim-lspconfig'
Plug 'windwp/nvim-autopairs'
Plug 'hrsh7th/cmp-nvim-lsp'
Plug 'hrsh7th/cmp-buffer'
Plug 'hrsh7th/cmp-path'
Plug 'hrsh7th/cmp-cmdLine'
Plug 'hrsh7th/nvim-cmp'
Plug 'hrsh7th/cmp-vsnip'
Plug 'hrsh7th/vim-vsnip'

call plug#end()

" require plugin configs
lua require('config')

" --- Colors

if has('termguicolors')
        set termguicolors
endif
set background=dark
let g:everforest_background = 'hard'
colorscheme everforest

" Set transparent background
hi Normal ctermbg=NONE guibg=NONE
hi EndOfBuffer ctermbg=NONE guibg=NONE
