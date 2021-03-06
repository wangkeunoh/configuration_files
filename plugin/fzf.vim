"========================================================================================="
"                                                  wg_init                                "
"========================================================================================="
map <C-f> :Files<CR>

" This is the default extra key bindings, at popup view
let g:fzf_action = {
  \ 'ctrl-t': 'tab split',
  \ 'ctrl-x': 'split',
  \ 'ctrl-v': 'vsplit' }
let g:fzf_tags_command = 'ctags -R'
" Border color
let g:fzf_layout = {'up':'~90%', 'window': { 'width': 0.8, 'height': 0.8,
    \'yoffset':0.5,'xoffset': 0.5, 'highlight': 'Todo', 'border': 'sharp' } }
let $FZF_DEFAULT_OPTS = '--layout=reverse --info=inline'
let $FZF_DEFAULT_COMMAND="rg --files --hidden"
"Get Files
command! -bang -nargs=? -complete=dir Files
    \ call fzf#vim#files(<q-args>, fzf#vim#with_preview({'options': ['--layout=reverse', 
    \'--info=inline']}), <bang>0)
let g:fzf_tags_command = 'ctags -R'
let $FZF_DEFAULT_OPTS='--bind=alt-a:select-all,alt-d:deselect-all'
