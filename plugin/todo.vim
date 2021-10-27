let maplocalleader = "\\"
" Disable default key bindings
" :help simple-todo-maps
let g:simple_todo_map_keys = 0

" Map your keys
map <LocalLeader>i <Plug>(simple-todo-new)
map <LocalLeader>y <Plug>(simple-todo-mark-as-done)

