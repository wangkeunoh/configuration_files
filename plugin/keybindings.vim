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
" 
map <F12> :%s/^.*\| //g<CR>
nnoremap <C-A> ggVG

"====================================================================================================================="
"                                                    end                                                              "
"====================================================================================================================="
