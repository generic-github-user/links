A semi-curated list of interesting and/or useful items from my bookmarks[^2];
adorned with my facetious comments and other information of questionable
usefulness. Mostly restricted to tools and resources I have personally used.

[^2]: entries also drawn from my GitHub stars, various conversations with
friends, memory, etc.

## Programming Languages

### Bash

- https://mywiki.wooledge.org/BashPitfalls

### Rust

- https://www.rust-lang.org/ - a systems language every serious developer should learn
- proselytization
    - https://stackoverflow.blog/2020/01/20/what-is-rust-and-why-is-it-so-popular/
    - https://github.com/rust-fuzz/trophy-case
- learning
    - https://cheats.rs/ - read the Rust book first
    - https://doc.rust-lang.org/rust-by-example/ - a great companion to
    The Book (especially for the impatient, myself included)
    - https://doc.rust-lang.org/book/title-page.html
    - https://tourofrust.com/index.html
    - https://github.com/sger/RustBooks
    - https://rust-lang-nursery.github.io/rust-cookbook/intro.html
    - https://doc.rust-lang.org/nomicon/
- State of the Union
    - https://www.arewelearningyet.com/
    - https://arewegameyet.rs/
    - https://www.arewewebyet.org/
    - http://www.areweguiyet.com/
    - https://isdebianreproducibleyet.com/
    - dirs
        - https://github.com/UgurcanAkkok/AreWeRustYet
        - https://wiki.mozilla.org/Areweyet
        - http://arewemetayet.com/
- https://github.com/rust-unofficial/awesome-rust
- Crates
    - https://github.com/rust-ndarray/ndarray - to take the edge off
    NumPy withdrawal symptoms
    - https://serde.rs/
    - https://github.com/flamegraph-rs/flamegraph
- Miscellanea
    - https://rustacean.net/

### Python

- https://www.python.org/ - my preferred scripting tool, has a nearly
boundless ecosystem and handles metaprogramming, HOFs, etc. quite
gracefully

#### Learning

- https://github.com/TheAlgorithms/Python

#### Contributing

- https://devguide.python.org/

#### Libraries

- Numerical computing
    - http://numba.pydata.org/ - a good stopgap for speeding up
    procedural-style NumPy code or getting it to cooperate with CUDA (prefer
    Julia or Rust when possible)
- Networking
    - https://github.com/psf/requests
- Linguistics
    - https://www.nltk.org/book/ch02.html - NLTK text corpora;
    - convenient for data science experiments
- Machine learning
    - https://github.com/tensorflow/tensorflow
    - Natural language processing
        - https://spacy.io/
    - OCR
        - https://github.com/madmaze/pytesseract - Python bindings
        - for Google's Tesseract
- Parsing
    - https://github.com/lark-parser/lark
- Other text processing
    - https://github.com/seatgeek/fuzzywuzzy
- Plotting/visualization
    - https://seaborn.pydata.org/
    - https://datashader.org/
    - https://matplotlib.org/
    - https://plotnine.readthedocs.io/en/stable/
- Mathematics
    - TODO

#### Other

- https://stackoverflow.com/questions/1132941/least-astonishment-and-the-mutable-default-argument

### Common Lisp

- https://lisp-lang.org/
- https://github.com/CodyReichert/awesome-cl
- Proselytization
    - https://stackoverflow.com/a/4621882
    - https://wiki.c2.com/?LispMacro
- Learn
    - https://cliki.net/
    - http://www.lispworks.com/documentation/HyperSpec/Front/index.htm -
    (regrettably) the most complete documentation for CL; most of the
    content has aged reasonably well over the last 20 years
    - https://quickdocs.org/
    - https://lispcookbook.github.io/cl-cookbook/
    - http://www.paulgraham.com/onlisp.html

### Other

- https://github.com/stedolan/jq - a fun and concise functional language for
wrangling JSON data
- https://www.gnu.org/software/sed/manual/sed.html - "I love writing regexes
so much, I wish they were Turing-complete" (joking aside, deft `sed` use
can adequately replace many white-collar jobs with a 5-line script and it's
almost definitely worth learning if you work with text at all regularly)

### criticism where criticism is due

- PHP
    - https://eev.ee/blog/2012/04/09/php-a-fractal-of-bad-design/
- Go
    - https://github.com/ksimka/go-is-not-good
- JS & Node.js
    - https://medium.com/hackernoon/im-harvesting-credit-card-numbers-and-passwords-from-your-site-here-s-how-9a8cb347c5b5

## Software

### Text editors

- https://github.com/atom/atom - a decent text editor if you like CSS a little too much, have at least 16GB of RAM, and are scared of vim
    - Packages
        - https://atom.io/packages/latex
        - https://atom.io/packages/atom-clock
        - https://atom.io/packages/atom-beautify
        - https://atom.io/packages/minimap

- https://notepad-plus-plus.org/ - for nostalgia (also a reasonable
choice for those who are staunchly opposed to using a command-line
editor but don't have unlimited RAM to run Atom or VS Code)

- https://code.visualstudio.com/ - a good first approximation if you ever
find yourself in the unenviable position of having to write Java code

#### Vim

- https://github.com/neovim/neovim - my main text editor; extremely efficient
and fairly simple to augment with hundreds of tools developed by obscenely
smart people over the last 30 years
- https://vimcolorschemes.com/ - eye candy to hold you over until the
next PR is finished (work in neovim too)
- https://github.com/junegunn/vim-plug - least painful option for
installing and updating vim/neovim plugins
- Learning
    - "grok[king] vi"
        - https://irian.to/blogs/mastering-vim-grammar/
        - https://stackoverflow.com/a/1220118
    - https://www.openvim.com/
    - https://vim.rtorr.com/
- https://vimawesome.com/
- https://github.com/akrawchyk/awesome-vim

### Diagramming

- https://app.diagrams.net/ (draw.io)

### Document conversion

- https://github.com/jgm/pandoc

### Web browsers

- https://vivaldi.com/ - elegant Chromium-based browser with more
features for power users
- https://www.mozilla.org/en-US/firefox/
- https://www.torproject.org/ - for the truly paranoid
    
### Media and animation

- https://www.blender.org/ - quite literally the best free software I've ever used
- https://github.com/3b1b/manim

### Terminal emulators

- https://konsole.kde.org/ - built into KDE and generally pleasant to
use; plays nicely with [Fira Code](https://github.com/tonsky/FiraCode)
ligatures
- https://sw.kovidgoyal.net/kitty/ - a stable and *very* well-optimized
TE; includes enough shortcuts out of the box to be a decent standalone
tmux replacement[^1]

[^1]: By design

    - https://github.com/kovidgoyal/kitty/issues/391#issuecomment-638320745
    - https://news.ycombinator.com/item?id=13342516

## Web

- JavaScript
    - Plotting/visualization
        - https://github.com/mrdoob/three.js
        - https://github.com/chartjs/Chart.js
    - Physics
        - http://wellcaffeinated.net/PhysicsJS/
    - https://github.com/jquery/jquery
    - https://github.com/ocelot-ide/Stopify
- Design
    - https://material.io/
- Frameworks
    - https://getbootstrap.com/
- https://getmdl.io/

### Demos

- Chrome Experiments
    - https://experiments.withgoogle.com/
    - https://experiments.withgoogle.com/collection/chrome
    - https://jayweeks.com/medusae/
    - AI/ML
        - https://experiments.withgoogle.com/ai/ai-duet/view/
        - https://artsexperiments.withgoogle.com/tsnemap/
        - https://xviniette.github.io/FlappyLearning/
    - Fluid
        - https://haxiomic.github.io/GPU-Fluid-Experiments/html5/
        - https://paveldogreat.github.io/WebGL-Fluid-Simulation/
    - Fractals
        - https://andrew.wang-hoyer.com/experiments/chaos-game/
        - https://crh.dev/TreeGenerator/TreeD.html
    - https://konard.github.io/twittermatrix/messages.html
    - http://cubictime.ru/
    - https://www.samcodes.co.uk/project/game-of-life/
    - https://labs.fluuu.id/geo/dist/

### Productivity

- https://todoist.com/ - one of the better todo managers I've worked with
(was actually my daily driver for almost two years); great for a
multi-device workflow

### Command-line/shell

- Search
    - https://github.com/BurntSushi/ripgrep
    - https://github.com/sharkdp/fd
- zsh
    - https://ohmyz.sh/
- Navigation
    - https://github.com/wting/autojump
    - https://github.com/ajeetdsouza/zoxide

### IoT and automation

- https://www.home-assistant.io/

## Games

### Chess

- https://lichess.org/
- https://www.chessprogramming.org/Main_Page
- https://www.chessgames.com/index.html - an astoundingly outdated
website containing a wealth of quality information
- Notable games
    - https://en.wikipedia.org/wiki/Immortal_Game
    - https://www.chessgames.com/perl/chessgame?gid=1259009
    - https://www.chessgames.com/perl/chessgame?gid=1008361
    - https://www.chessgames.com/perl/chessgame?gid=1233404
    - https://www.chessgames.com/perl/chessgame?gid=1277959
    - https://www.chessgames.com/perl/chessgame?gid=1011478

### Space

- https://www.kerbalspaceprogram.com/
- https://www.nomanssky.com/

### Falling-sand games

- https://en.wikipedia.org/wiki/Falling-sand_game
- https://sandspiel.club/
- https://github.com/The-Powder-Toy/The-Powder-Toy

### Minecraft

- World editors
    - https://www.amuletmc.com/
    - https://www.mcedit.net/
- Common Sense
    - https://www.minecraft.net/en-us/article/minecraft-and-nfts

### Word games

- https://www.nytimes.com/puzzles/spelling-bee
- https://www.powerlanguage.co.uk/wordle/
- https://www.nytimes.com/crosswords/game/daily
- https://www.nytimes.com/crosswords/game/mini

### Other

- https://github.com/vicgeralds/vitetris

## Unix

- https://github.com/torvalds/linux - the Linux kernel source
- https://github.com/ibraheemdev/modern-unix - fast & modern Unix
command-line tools; in particular, I recommend `lsd`, `fd`, `ripgrep`,
`jq`, `tldr`, and `zoxide` (some of these have other entries scattered
about the place)
- learning
    - https://missing.csail.mit.edu/ - recommended very highly for anyone who
    uses any Unix shell on a regular basis; comes in both video and text form
- KDE
    https://kde.org/plasma-desktop/ - my preferred desktop (I recommend
    enabling the "Wobbly Windows" desktop effect)
    - themes
        - sweet mars
            - https://github.com/EliverLara/Sweet/tree/mars/kde
            - https://store.kde.org/p/1393507
        - https://github.com/vinceliuice/Layan-kde
- https://www.reddit.com/r/unixporn/

## Cheatsheets

- Bash
    - *some unsolicited advice: if you find yourself nesting more than 3
    layers of escaped quotes in bash, it's time to use Python*
    https://devhints.io/bash
    https://github.com/dylanaraps/pure-bash-bible
- https://github.com/tldr-pages/tldr
- https://learnxinyminutes.com/ - "Good Enough" introductions to various programming languages
- https://tmuxcheatsheet.com/

## Git

- https://git-scm.com/
- https://ndpsoftware.com/git-cheatsheet.html
- https://git-scm.com/book/en/v2

## ML

### Learning

- https://mml-book.github.io/

### Datasets

- https://www.kaggle.com/
- https://huggingface.co/datasets

### OCR

- https://github.com/tesseract-ocr/tesseract

### Architectures

- Autoencoders
    - https://cs.stanford.edu/people/karpathy/convnetjs/demo/autoencoder.html
        - tags: demo
    - https://www.jeremyjordan.me/variational-autoencoders/
    - https://kvfrans.com/variational-autoencoders-explained/

### Neuroevolution

- https://en.wikipedia.org/wiki/Neuroevolution - an alright introduction
to evolutionary methods in ML
- https://xviniette.github.io/FlappyLearning/
- https://www.youtube.com/watch?v=qv6UVOQ0F44 - the video that got me
into machine learning originally

### Organizations

- https://www.uber.com/us/en/uberai/
- https://openai.com/
- https://www.deepmind.com/
- https://opencog.org/

### Tools

- https://github.com/josephmisiti/awesome-machine-learning
- https://colab.research.google.com/ - Jupyter-like notebook environment for
ML and data science experimentation; has fairly decent hardware available
for "free" (go to `Runtime > Change runtime type` and set to GPU or TPU;
works best with larger datasets and batch sizes)

### Miscellanea

- https://en.wikipedia.org/wiki/Automated_machine_learning

## Mathematics

### Recreational math

### Cellular automata

- https://en.wikipedia.org/wiki/Cellular_automaton
- https://en.wikipedia.org/wiki/Langton%27s_ant
- Conway's Game of Life
    - https://conwaylife.com/
- Software
    - http://golly.sourceforge.net/ - unreasonably efficient desktop
    GUI program for simulating cellular automata
- https://en.wikipedia.org/wiki/Von_Neumann_universal_constructor

### Fractals

#### Mandelbrot

- https://mandel.gart.nz/
- http://www.mandelbrotgenetics.com/
- https://mathworld.wolfram.com/MandelbrotSet.html
- https://web.archive.org/web/20010419182449/http://www.df.lth.se/~lft/vim/mandelbrot - Mandelbrot set vim macro

#### Mandelbulb

- https://en.wikipedia.org/wiki/Mandelbulb
- http://www.bugman123.com/Hypercomplex/#MandelbulbZ
- https://www.skytopia.com/project/fractal/mandelbulb.html
- https://www.mandelbulb.com/
- https://mandelbulber.com/

### Number theory

- https://en.wikipedia.org/wiki/Taxicab_number
- https://en.wikipedia.org/wiki/P-adic_valuation
- https://www.mersenne.org/, https://en.wikipedia.org/wiki/Great_Internet_Mersenne_Prime_Search

### Geometry

- https://ocw.mit.edu/courses/6-849-geometric-folding-algorithms-linkages-origami-polyhedra-fall-2012/
  Geometric Folding Algorithms: Linkages, Origami, Polyhedra (Prof.
  Erik Demaine); computational origami. One of my all-time favorite
  courses, online or otherwise.
- https://en.wikipedia.org/wiki/Moving_sofa_problem

### Calculus

- Cheat sheets
    - https://tutorial.math.lamar.edu/pdf/calculus_cheat_sheet_all.pdf
    - https://www.math.utah.edu/~macarthu/summer15/math2210/calc3_cheat_sheet_onesheet.pdf

### Other

- https://oeis.org/
- https://learnxinyminutes.com/docs/set-theory/ - very basic set theory introduction

## YouTube

### Channels

- Educational
    - https://www.youtube.com/user/Computerphile
    - https://www.youtube.com/c/inanutshell
    - https://www.youtube.com/c/3blue1brown - possibly the single best
    educational YouTube channel; some particularly outstanding samples are
    listed below
        - TODO
- miscellaneous
    - https://www.youtube.com/c/TomScottGo
- https://www.youtube.com/channel/UCbfYPyITQ-7l4upoX8nvctg - one of my
all-time favorites (mainly covers machine learning and computer graphics)

### TED talks

- https://youtu.be/wAIP6fI0NAI
- https://www.youtube.com/watch?v=arj7oStGLkU
- https://www.youtube.com/watch?v=XFnGhrC_3Gs
- https://www.youtube.com/watch?v=UyyjU8fzEYU

### Other

- https://youtu.be/Fm5Ust7vEhk

## Reading

- https://chomsky.info/ - various works of the illustrious Noam Chomsky
(mostly re: politics, though his work in linguistics is also seminal)
- Books
    - *note: for hopefully obvious reasons, I'm only posting links to books that
    have been publicly posted by their authors (or with their express
    permission)*
    - https://www.historyisaweapon.com/zinnapeopleshistory.html - *A People's
    History Of The United States* (Howard Zinn)
- Misc. literature
    - http://shakespeare.mit.edu/hamlet/full.html
    - https://www.gutenberg.org/files/768/768-h/768-h.htm
    - https://www.poetryfoundation.org/poems/50465/thanatopsis
    - "The Yellow Wallpaper" (Charlotte Perkins Gilman)
- History
    - https://en.wikipedia.org/wiki/Coal_Wars
- Blogs
    - https://waitbutwhy.com/

## etc

Things I haven't read or used yet but consistently hear good reviews of (or
have other reason to think highly of). I do intend to get to most of these
eventually and will update this list accordingly.

### Low-level programming

- https://www.nand2tetris.org/
- https://craftinginterpreters.com/
- https://github.com/cfenollosa/os-tutorial

### Programming languages

- Lisp
    - https://buildyourownlisp.com/
    - https://github.com/norvig/paip-lisp
- Python
    - https://github.com/google/python-fire
    - https://github.com/seperman/deepdiff
- Rust
    - https://github.com/rust-ml/linfa

### Research

- https://github.com/papers-we-love/papers-we-love

### Front-end

- https://github.com/thedaviddias/Front-End-Checklist
- https://github.com/pallets/flask

### Web scraping

- https://github.com/scrapy/scrapy
- https://secretagent.dev/

### Markdown

- https://github.com/mermaid-js/mermaid
- https://github.com/adam-p/markdown-here

### Other

- https://www.nushell.sh/
- https://en.algorithmica.org/hpc/
- https://git-secret.io/
- https://github.com/trimstray/the-book-of-secret-knowledge
- https://www.wikiwand.com/
- http://structuresynth.sourceforge.net/
