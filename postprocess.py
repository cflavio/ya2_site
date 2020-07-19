title_line = '    <meta name="twitter:description" content="%s" />\n'
img_line = '    <meta name="twitter:image" content="%s" />\n'

new_tags = [
    '    <meta name="twitter:card" content="summary" />\n',
    '    <meta name="twitter:site" content="@ya2tech" />\n',
    '    <meta name="twitter:title" content="Ya2 blog" />\n']

from os import listdir
from os.path import isfile, join
rst_files = [f for f in listdir('posts') if isfile('posts/' + f)]
for rst_file in rst_files:
    with open('posts/'+rst_file) as f:
        lines = f.readlines()
        for line in lines:
            if line.startswith('.. cover '):
                img_path = line.strip()[9:]
                tag_lines = new_tags
                tag_lines += [title_line % lines[0].strip()]
                tag_lines += [img_line % img_path]
                new_lines = []
                with open('_build/html/posts/' + rst_file[:-3] + 'html') as fhtml:
                    hlines = fhtml.readlines()
                    for hline in hlines:
                        new_lines += [hline]
                        if '<link rel="alternate" type="application/rss+xml" title="Ya2\'s RSS" href="https://www.ya2.it/index.rss" />' in hline:
                            new_lines += new_tags
                with open('_build/html/posts/' + rst_file[:-3] + 'html', 'w') as fhtml:
                    fhtml.write(''.join(new_lines))
