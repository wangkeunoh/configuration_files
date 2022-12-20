"====================================================================================================================="
"                                                  wg_rg"
"====================================================================================================================="
" Get text in files with Rg
 command! -bang -nargs=* Rg
  \ call fzf#vim#grep(
  \   'rg --column --line-number --no-heading --color=always --smart-case '.shellescape(<q-args>), 1,
  \   fzf#vim#with_preview(), <bang>0)

" New for dir
command! -bang -nargs=* PRg
  \ call fzf#vim#grep("rg --column --line-number --no-heading --color=always --smart-case ".shellescape(<q-args>), 1, fzf#vim#with_preview({'dir': system('git rev-parse --show-toplevel 2> /dev/null')[:-2]}), <bang>0)

"Since this seems to be the top search result for this topic, I'll add a slight variation for those who might be interested. This will perform an Rg search from the project root of the current buffer (as opposed to the current working directory used by the variation above).
command! -bang -nargs=* BRg
  \ call fzf#vim#grep("rg --column --line-number --no-heading --color=always --smart-case ".shellescape(<q-args>), 1, {'dir': system('git -C '.expand('%:p:h').' rev-parse --show-toplevel 2> /dev/null')[:-2]}, <bang>0)

":Rg2 apple ./folder_test
command! -bang -nargs=* Rg2
  \ call fzf#vim#grep(
  \    "rg --column --line-number --no-heading --color=always --smart-case ".<q-args>, 1, 
  \    {'dir': system('git -C '.expand('%:p:h').' rev-parse --show-toplevel 2> /dev/null')[:-2]}, 
  \    <bang>0
  \ )



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

nnoremap <A-f> :call SearchBranchRg()<CR>

"analysis
let mapleader = "\<SPACE>"
nnoremap <leader>0 :let @" = expand("%:p")<CR>
"nnoremap <leader>1 :cd /media/wangkeun/hardDisk/perforce/GA_RIL_WangkeunOh_LinuxPc2_Source/RIO/<CR>
"nnoremap <leader>2 :cd /media/wangkeun/hardDisk/perforce/GA_RIL_WangkeunOh_LinuxPc2_Source/SOLO/Common<CR>
"nnoremap <leader>3 :cd /media/wangkeun/hardDisk/perforce/GA_RIL_WangkeunOh_LinuxPc2_Source/VENDOR/<CR>
nnoremap <leader>f :BLines 
"
function SearchBranchRg()
  let curline = getline('.')
  call inputsave()
  let branch = input('which branch you want for rg ? ')
  call inputrestore()

  if strlen(branch) < 1
    :Rg
  elseif branch ==? 'wiki'
    let word = input('keyword ? ')
    call inputrestore()
    call fzf#vim#grep("rg --column --line-number --no-heading --color=always --smart-case " .. shellescape(word), 1, {'dir':  '/home-mc/wangkeun.oh/git_workspace/KinGoodWiki/'})
  elseif branch ==? 'tiger'
    let word = input('keyword ? ')
    call inputrestore()
    call fzf#vim#grep("rg --column --line-number --no-heading --color=always --smart-case " .. shellescape(word), 1, {'dir':  '/home-mc/wangkeun.oh/Perforce/GA_RIL_WangkeunOh_VdiLinuxPc_Source/TIGER/Cinnamon/'})
  elseif branch ==? 'solo'
    let word = input('keyword ? ')
    call inputrestore()
    call fzf#vim#grep("rg --column --line-number --no-heading --color=always --smart-case " .. shellescape(word), 1, {'dir':  '/home-mc/wangkeun.oh/Perforce/GA_RIL_WangkeunOh_VdiLinuxPc_Source/SOLO/Cinnamon/'})
  elseif branch ==? 'etc'
    let word = input('keyword ? ')
    call inputrestore()
    call fzf#vim#grep("rg --column --line-number --no-heading --color=always --smart-case " .. shellescape(word), 1, {'dir':  '/home-mc/wangkeun.oh/Perforce/GA_RIL_WangkeunOh_VdiLinuxPc_Source/ETC/RIL/VENDOR/'})
  elseif branch ==? 'import'
    let word = input('keyword ? ')
    call inputrestore()
    call fzf#vim#grep("rg --column --line-number --no-heading --color=always --smart-case " .. shellescape(word), 1, {'dir':  '/home-mc/wangkeun.oh/Perforce/GA_RIL_WangkeunOh_VdiLinuxPc_Source/IMPORT/Google/})
  else
    echo 'not match any branch'

  endif

endfunction

function! RgDir()
    let branch = 'work'
    call fzf#vim#grep("rg --column --line-number --no-heading --color=always --smart-case " .. shellescape(branch), 1, {'dir':  '/home-mc/wangkeun.oh/Perforce/GA_RIL_WangkeunOh_VdiLinuxPc_Source/TIGER/'})
endfunction

"https://github.com/junegunn/fzf.vim/issues/837
