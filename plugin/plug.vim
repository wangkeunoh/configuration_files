" ================================================================================
"                                    PLUGINS INSTALL                             "
" ================================================================================
"
" Git
Plug 'tpope/vim-fugitive'
" Utils
Plug 'airblade/vim-rooter'
Plug 'thaerkh/vim-workspace' " Save the session status
Plug 'junegunn/fzf', { 'do': { -> fzf#install() } } " { 'dir': '~/.fzf', 'do': './install --all' }
Plug 'junegunn/fzf.vim',
Plug 'scrooloose/nerdtree'
Plug 'tpope/vim-surround'
Plug 'jiangmiao/auto-pairs' " Autocomplete simbols
" Plug 'jremmen/vim-ripgrep'
Plug 'majutsushi/tagbar'
Plug 'neoclide/coc.nvim', {'branch': 'release'}
Plug 'tpope/vim-fireplace'
Plug 'luochen1990/rainbow'
Plug 'guns/vim-sexp'
Plug 'tpope/vim-sexp-mappings-for-regular-people'
Plug 'peitalin/vim-jsx-typescript'
Plug 'sheerun/vim-polyglot'
Plug 'alampros/vim-styled-jsx'
Plug 'amiralies/vim-rescript'
Plug 'editorconfig/editorconfig-vim'
" Powerline Color
Plug 'itchyny/lightline.vim'
Plug 'taohexxx/lightline-buffer'
" Theme Color
Plug 'joshdick/onedark.vim'
Plug 'rakr/vim-one'
Plug 'morhetz/gruvbox'
" nerd multi open
Plug 'philrunninger/nerdtree-visual-selection'
" wiki
Plug 'vimwiki/vimwiki'
Plug 'mhinz/vim-startify'
Plug 'vitalk/vim-simple-todo'
let g:simple_todo_tick_symbol = '*'
Plug 'itchyny/calendar.vim'
