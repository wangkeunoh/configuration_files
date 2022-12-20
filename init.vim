"========================================================================================="
"                                                  wg_init                                "
"========================================================================================="
" initialize plugin
call plug#begin('~/.local/share/nvim/plugged')
source ~/.config/nvim/plug.vim
call plug#end()

" import conf files
 source ~/.config/nvim/plugin/rg.vim 
 source ~/.config/nvim/plugin/fzf.vim 
 source ~/.config/nvim/plugin/nerd.vim 
 source ~/.config/nvim/plugin/wiki.vim 
 source ~/.config/nvim/plugin/startify.vim 
 source ~/.config/nvim/plugin/todo.vim

" general settings
set noswapfile
set wrap
set title                           " show the file name on terminal window.
set number                          " show line numbers.  
set relativenumber 
set mouse=a                         " enable mouse interaction.
set history=1000                    " increase history size.
set cursorline                      " show the current line.
set synmaxcol=160
set tabstop=4                       " tabs with 4 spaces.
set shiftwidth=4
set softtabstop=4
set shiftround
set expandtab                       " inserts spaces indest <Tab>s.
set autoread                        " autoReload if a file is modified
au FocusGained * :checktime
set splitright
set splitbelow

" search options
set ignorecase                      " ignore uppercase in searches.
set smartcase                       " do not ignore uppercase if the word contains uppercase.
set nostartofline                   " hold the cursor position when changing buffer.
set hidden                          " allow buffer switching without saving
filetype plugin indent on

set spelllang=en,es                 " spell check (english and spanish)
set encoding=UTF-8                  " encodig utf-8
set backspace=indent,eol,start      " backspaceever work on insert mode

" theme color settings
set background=dark                 " theme background light or dark
colorscheme onedark                 " onedark theme name
if (has("termguicolors"))
    set termguicolors               " enable true colors
endif

" Clipboard, you need install xsel
set clipboard+=unnamedplus

"buffer navigation 
nnoremap<C-h> :bprevious<CR>
nnoremap<C-l> :bnext<CR>

"buffer close
map t :bp <BAR> bd #<CR>

"window close
nnoremap <leader>qq :q!<CR>
nnoremap <leader>ss :w<CR>

"pane close when vi command mode
nnoremap q :q<CR>

"tagbar width
let g:tagbar_width=40

"pane size
nnoremap <left> :vertical resize -5<CR>
nnoremap <down> :resize resize -5<CR>
nnoremap <up> :resize +5<CR>
nnoremap <right> :vertical resize +5<CR>

" get current directory path in nerd
autocmd vimenter * silent! lcd %:p:h

"============================================================================================"
"                                                              end                           "
"============================================================================================"
