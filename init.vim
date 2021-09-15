"====================================================================================================================="
"                                                  wg_init                                                            "
"====================================================================================================================="
" initialize plugin
call plug#begin('~/.local/share/nvim/plugged')
source ~/.config/nvim/plug.vim
call plug#end()

" import conf files
 source ~/.config/nvim/plugin/rg.vim 
 source ~/.config/nvim/plugin/fzf.vim 

" general settings
set title                           " show the file name on terminal window.
set number                          " show line numbers.  
set relativenumber 
set mouse=a                         " enable mouse interaction.
set history=1000                    " increase history size.
set nowrap                          " do not divide the line if it is long.
set cursorline                      " show the current line.
set synmaxcol=160
set tabstop=2                       " tabs with 4 spaces.
set shiftwidth=2
set softtabstop=2
set shiftround
set expandtab                       " inserts spaces indest <Tab>s.
set autoread                        " autoReload if a file is modified
au FocusGained * :checktime

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

"====================================================================================================================="
"                                                    end                                                              "
"====================================================================================================================="
