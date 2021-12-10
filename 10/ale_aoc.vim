function! ale_linters#aoc#aoc#Handle(buffer, lines) abort
    " Error format: <filename>:<lnum>:<col>: <text>
    " Error format: <filename>:<lnum>:<col>: error: <text>
    " Warning format: <filename>:<lnum>:<col>: warning: <text>
    let l:re = '\v(.+):([0-9]+):([0-9]+):\s+(warning:)?\s*(.+)\s*'
    let l:output = []

    for l:match in ale#util#GetMatches(a:lines, l:re)
        let l:cur_file = ale#path#Simplify(expand('#' . a:buffer . ':p'))
        let l:item = {
        \   'bufnr': a:buffer,
        \   'filename': l:match[1],
        \   'lnum': str2nr(l:match[2]),
        \   'col': str2nr(l:match[3]),
        \   'type': l:match[4] is# 'warning:' ? 'W' : 'E',
        \   'text': l:match[5],
        \}
        let l:error_file = ale#path#Simplify(l:item.filename)

        call add(l:output, l:item)
    endfor

    return l:output
endfunction



call ale#linter#Define('aoc', {
\   'name': 'aoc',
\   'executable': '/home/marco/workspace/Mindustry/aoc_2021/10/linter.py',
\   'command': '/home/marco/workspace/Mindustry/aoc_2021/10/linter.py %s --lint',
\   'callback': 'ale_linters#aoc#aoc#Handle',
\   'output_stream': 'stdout',
\})
