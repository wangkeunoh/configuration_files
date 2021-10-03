"====================================================================================================================="
"                                                  wg_keymap"
"====================================================================================================================="
" initialize plugin

nnoremap <ESC> :nohl<CR>
let mapleader = "\<SPACE>"
" Files
nnoremap <leader>ff :Files<CR>
nnoremap <leader>fg :GFiles<CR>
" Search
nnoremap <leader>sp :Rg<CR>
" Open
nnoremap <leader>ot :terminal<CR>
" Window 
nnoremap <leader>ws :split<CR>
nnoremap <leader>wv :vsplit<CR>
nnoremap <leader>wh <C-w>H
nnoremap <leader>wj <C-w>J
nnoremap <leader>wk <C-w>K
nnoremap <leader>wl <C-w>L

" Remap keys
nnoremap <F1> :TagbarToggle<CR>

" Normal mode
nnoremap <C-Down> :m .+1<CR>==
nnoremap <C-Up> :m .-2<CR>==
" Insert mode
inoremap <C-Down> <ESC>:m .+1<CR>==gi
inoremap <C-Up> <ESC>:m .-2<CR>==gi
" Visual mode
vnoremap <C-Down> :m '>+1<CR>gv=gv
vnoremap <C-Up> :m '<-2<CR>gv=gv

" nnoremap <Down> gj
" nnoremap <Up> gk
" inoremap <Down> <ESC>gja
" inoremap <Up> <ESC>gka


" let mapleader = ","
" noremap <leader>w :w<CR>
" noremap <leader>q :q<CR>
" noremap <leader>gs :CocSearch
" noremap <leader>fs :Files<CR>
" noremap <leader><CR> <CR><c-w>h:q<CR>

" :inoremap ii <Esc>
" :imap ii <Esc>

"====================================================================================================================="
"                                                    end                                                              "
"====================================================================================================================="
