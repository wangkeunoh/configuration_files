"====================================================================================================================="
"                                                  wg_init                                                            "
"====================================================================================================================="
map <C-f> :call SearchBranchFzf()<CR>
" This is the default extra key bindings, at popup view
let g:fzf_action = {
  \ 'ctrl-t': 'tab split',
  \ 'ctrl-x': 'split',
  \ 'ctrl-v': 'vsplit' }

" Border color
let g:fzf_layout = {'up':'~90%', 'window': { 'width': 0.8, 'height': 0.8,'yoffset':0.5,'xoffset': 0.5, 'highlight': 'Todo', 'border': 'sharp' } }

let $FZF_DEFAULT_OPTS = '--layout=reverse --info=inline'

" below is very intersting and important when FZF_DEFAULT_COMMAND not exists
" then excute  below
" find . -path '*/\.*' -prune -o -type f -print -o -type l -print 2> /dev/null | sed s/^..//
"
"let $FZF_DEFAULT_COMMAND="rg --files --follow --hidden"
let $FZF_DEFAULT_COMMAND="find -L * -path '*/\.*' -prune -o -type f -print -o -type l -print 2> /dev/null"

"Get Files
"command! -bang -nargs=? -complete=dir Files
"    \ call fzf#vim#files(<q-args>, fzf#vim#with_preview({'options': ['--layout=reverse', '--info=inline']}), <bang>0) //disable preview
command! -bang -nargs=? -complete=dir Files
    \ call fzf#vim#files(<q-args>, <bang>0)

let g:fzf_tags_command = 'ctags -R'

"nmap <F2> :Files /home-mc/wangkeun.oh/Perforce/GA_RIL_WangkeunOh_VdiLinuxPc_Source/RIO/<CR>
"nmap <F2> :Files /home-mc/wangkeun.oh/Perforce/GA_RIL_WangkeunOh_VdiLinuxPc_Source/TIGER/<CR>
"nmap <F3> :Files /home-mc/wangkeun.oh/Perforce/GA_RIL_WangkeunOh_VdiLinuxPc_Source/SOLO/<CR>
"nmap <F4> :Files /home-mc/wangkeun.oh/Perforce/GA_RIL_WangkeunOh_VdiLinuxPc_Source/VENDOR/<CR>
"nmap <F5> :Files /home-mc/wangkeun.oh/Perforce/GA_RIL_WangkeunOh_VdiLinuxPc_Source/VENDOR_OS_UP/<CR>
"

let $FZF_DEFAULT_OPTS='--bind=alt-a:select-all,alt-d:deselect-all'

function SearchBranchFzf()
  let curline = getline('.')
  call inputsave()
  let branch = input('which branch you want for fzf ? ')
  call inputrestore()

  if strlen(branch) < 1
    :Files
  elseif branch ==? 'tiger'
    :Files /home-mc/wangkeun.oh/Perforce/GA_RIL_WangkeunOh_VdiLinuxPc_Source/TIGER/
  elseif branch ==? 'solo'
    :Files /home-mc/wangkeun.oh/Perforce/GA_RIL_WangkeunOh_VdiLinuxPc_Source/SOLO/
  elseif branch ==? 'etc'
    :Files /home-mc/wangkeun.oh/Perforce/GA_RIL_WangkeunOh_VdiLinuxPc_Source/ETC/RIL/VENDOR/
  elseif branch ==? 'import'
    :Files /home-mc/wangkeun.oh/Perforce/GA_RIL_WangkeunOh_VdiLinuxPc_Source/IMPORT/
  elseif branch ==? 'utah'
    :Files /home-mc/wangkeun.oh/Perforce/GA_RIL_WangkeunOh_VdiLinuxPc_Source/UTAH/
  else
    echo 'not match any branch'

  endif

endfunction

