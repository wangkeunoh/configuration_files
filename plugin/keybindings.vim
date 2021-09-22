"====================================================================================================================="
"                                                  wg_keymap"
"====================================================================================================================="
" initialize plugin

let mapleader = "\<SPACE>"
nnoremap <leader><SPACE> :NERDTreeToggle<CR>
" Files
nnoremap <leader>ff :Files<CR>
nnoremap <leader>fg :GFiles<CR>
" Search
nnoremap <leader>sp :Rg<CR>
" Open
nnoremap <leader>on :NERDTreeToggle<CR>
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
" nnoremap <C-Left> :bprevious<CR>
" nnoremap <C-Right> :bnext<CR>
" nnoremap <F2> :FZF<CR>
" inoremap <F2> <Esc>:FZF<CR>
" nnoremap <F3> :Buffers<CR>
" inoremap <F3> <Esc>:Buffers<CR>
" nnoremap <F4> :NERDTreeToggle<CR>
" inoremap <F4> <Esc>:NERDTreeToggle<CR>
" nnoremap <F5> :Rg<CR>
" inoremap <F5> <Esc>:Rg<CR>
" inoremap <F6> <Esc>:TagbarToggle<CR>


" Move line
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
