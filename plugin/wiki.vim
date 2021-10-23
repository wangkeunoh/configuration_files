" local leader key setting
let maplocalleader = "\<SPACE>"
let g:vimwiki_list = [
    \{
    \   'path': '~/git_workspace/wangkeunoh.github.io/_wiki/',
    \   'ext' : '.md',
    \   'diary_rel_path': '.',
    \},
    \{
    \   'path': '~/Dropbox/p_wiki/',
    \   'ext' : '.md',
    \   'diary_rel_path': '.',
    \},
\]
let g:vimwiki_conceallevel = 1
let g:vimwiki_global_ext = 0

" frequently used key 
command! WikiIndex :VimwikiIndex
nmap <LocalLeader>ww <Plug>VimwikiIndex
nmap <LocalLeader>wi <Plug>VimwikiDiaryIndex
nmap <LocalLeader>w<LocalLeader>w <Plug>VimwikiMakeDiaryNote
nmap <LocalLeader>wt :VimwikiTable<CR>
nmap <LocalLeader>l :VimwikiToggleListItem<CR>

" leader a  키를 누르면 커서가 놓인 단어를 위키에서 검색한다.
nmap <LocalLeader>a :execute "VWS /" . expand("<cword>") . "/" <Bar> :lopen<CR>
" leader b  키를 누르면 현재 문서를 링크한 모든 문서를 검색한다
nmap <LocalLeader>b :execute "VWB" <Bar> :lopen<CR>

function! LastModified()
    if &modified
        let save_cursor = getpos(".")
        let n = min([10, line("$")])
        keepjumps exe '1,' . n . 's#^\(.\{,10}updated\s*: \).*#\1' .
              \ strftime('%Y-%m-%d %H:%M:%S +0900') . '#e'
        call histdel('search', -1)
        call setpos('.', save_cursor)
    endif
endfun
autocmd BufWritePre *.md call LastModified()


function! NewTemplate()
    if line("$") > 1
        return
    endif

    let l:template = []
    call add(l:template, '---')
    call add(l:template, 'title   : ')
    call add(l:template, 'summary : ')
    call add(l:template, 'date    : ' . strftime('%Y-%m-%d %H:%M:%S +0900'))
    call add(l:template, 'updated : ' . strftime('%Y-%m-%d %H:%M:%S +0900'))
    call add(l:template, 'tags    : ')
    call add(l:template, 'parent  : ')
    call add(l:template, '---')
    call setline(1, l:template)
    execute 'normal! G'
    execute 'normal! $'

    echom 'new wiki page has created'
endfunction
autocmd BufRead,BufNewFile *.md call NewTemplate()

augroup vimwikiauto
    autocmd BufWritePre *wiki/*.md call LastModified()
    autocmd BufRead,BufNewFile *wiki/*.md call NewTemplate()
augroup END
