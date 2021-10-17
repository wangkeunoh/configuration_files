"====================================================================================================================="
"                                                  wg_rg"
"====================================================================================================================="
" Get text in files with Rg
 command! -bang -nargs=* Rg
  \ call fzf#vim#grep(
  \   'rg --column --line-number --no-heading --color=always --smart-case '.shellescape(<q-args>), 1,
  \   fzf#vim#with_preview(), <bang>0)

" Ripgrep advanced, from README
function! RipgrepFzf(query, fullscreen)
  let command_fmt = 'rg --column --line-number --no-heading --color=always --smart-case -- %s || true'
  let initial_command = printf(command_fmt, shellescape(a:query))
  let reload_command = printf(command_fmt, '{q}')
  let spec = {'options': ['--phony', '--query', a:query, '--bind', 'change:reload:'.reload_command]}
  call fzf#vim#grep(initial_command, 1, fzf#vim#with_preview(spec), 1) "a:fullscreen
endfunction
command! -nargs=* -bang RG call RipgrepFzf(<q-args>, <bang>0)

" Rg sometimes causes Vim to freeze
set nocompatible hidden laststatus=2

nnoremap <A-f> :Rg<CR>

"analysis
let mapleader = "\<SPACE>"
"nnoremap <leader>0 :let @" = expand("%:p")<CR>
"nnoremap <leader>1 :cd /media/wangkeun/hardDisk/perforce/GA_RIL_WangkeunOh_LinuxPc2_Source/RIO/<CR>
"nnoremap <leader>2 :cd /media/wangkeun/hardDisk/perforce/GA_RIL_WangkeunOh_LinuxPc2_Source/SOLO/Common<CR>
"nnoremap <leader>3 :cd /media/wangkeun/hardDisk/perforce/GA_RIL_WangkeunOh_LinuxPc2_Source/VENDOR/<CR>
nnoremap <leader>f :BLines 
