# Jupyter notebooks

The notebook is a web application that allows you to combine explanatory text, math equations, code, and visualizations all in one easily sharable document.
Notebooks have quickly become an essential tool when working with data. You'll find them being used for data cleaning and exploration, visualization, machine learning, and big data analysis. 

Example notebook - https://github.com/mcleonard/blog_posts/blob/master/body_fat_percentage.ipynb

The central point is the notebook server. You connect to the server through your browser and the notebook is rendered as a web app. Code you write in the web app is sent through the server to the kernel. The kernel runs the code and sends it back to the server, then any output is rendered back in the browser. When you save the notebook, it is written to the server as a JSON file with a .ipynb file extension.

The new name Jupyter comes from the combination of Julia, Python, and R.

## Installation

Use Anaconda to install Jupiter.
```
conda install jupyter notebook
```

Also available through pip with 
```
pip install jupyter notebook.
```

## Launching

To start the a notebook server:
```
jupyter notebook
```
This will start the server in the directory you ran the command in. That means any notebook files will be saved in that directory. Typically you'd want to start the server in the directory where your notebooks live.

Default Port: 8888


## Tabs

The tabs at the top show Files, Running, and Cluster. Files shows all the files and folders in the current directory. Clicking on the Running tab will list all the currently running notebooks. From there you can manage them.

Clusters previously was where you'd create multiple kernels for use in parallel computing. Now that's been taken over by ipyparallel so there isn't much to do there.

If you're running the notebook server from a conda environment, you'll also have access to a "Conda" tab shown below. Here you can manage your environments from within Jupyter. You can create new environments, install packages, update packages, export environments and more.

## Command palette

The little keyboard is the command palette. This will bring up a panel with a search bar where you can search for various commands. This is really helpful for speeding up your workflow as you don't need to search around in the menus with your mouse.

## Code cells

Most of your work in notebooks will be done in code cells. This is where you write your code and it gets executed. In code cells you can write any code, assigning variables, defining functions and classes, importing packages, and more. Any code executed in one cell is available in all other cells.

## Markdown cells

As mentioned before, cells can also be used for text written in Markdown. Markdown is a formatting syntax that allows you to include links, style text as bold or italicized, and format code. As with code cells, you press Shift + Enter or Control + Enter to run the Markdown cell, where it will render the Markdown to formatted text.
[Doc](https://daringfireball.net/projects/markdown/basics)

## Math expressions

You can create math expressions in Markdown cells using LaTeX symbols. Notebooks use MathJax to render the LaTeX symbols as math symbols. To start math mode, wrap the LaTeX in dollar signs $y = mx + b$ for inline math.

Use $$ for math blocks.

[Complete cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)

## Magic keywords
Magic keywords are special commands you can run in cells that let you control the notebook itself or perform system calls such as changing directories. For example, you can set up matplotlib to work interactively in the notebook with %matplotlib.

Magic commands are preceded with one or two percent signs (% or %%) for line magics and cell magics, respectively. Line magics apply only to the line the magic command is written on, while cell magics apply to the whole cell.

## Timing code
At some point, you'll probably spend some effort optimizing code to run faster. Timing how quickly your code runs is essential for this optimization. You can use the timeit magic command to time how long it takes for a function to run, like so:
If you want to time how long it takes for a whole cell to run, you’d use %%timeit like so.

## Embedding visualizations in notebooks
As mentioned before, notebooks let you embed images along with text and code. This is most useful when you’re using matplotlib or other plotting packages to create visualizations. You can use %matplotlib to set up matplotlib for interactive use in the notebook.

To render figures directly in the notebook, you should use the inline backend with the command %matplotlib inline.

On higher resolution screens such as Retina displays, the default images in notebooks can look blurry. Use %config InlineBackend.figure_format = 'retina' after %matplotlib inline to render higher resolution images.

## Debugging in the Notebook
With the Python kernel, you can turn on the interactive debugger using the magic command %pdb. When you cause an error, you'll be able to inspect the variables in the current namespace.

[Doc](https://docs.python.org/3/library/pdb.html)


## All Magic commands

Built-in Magic commands are listed [here](http://ipython.readthedocs.io/en/stable/interactive/magics.html)


## Converting notebooks

Notebooks are just big JSON files with the extension .ipynb.

Since notebooks are JSON, it is simple to convert them to other formats. Jupyter comes with a utility called `nbconvert` for converting to HTML, Markdown, slideshows, etc.

Converting to HTML:
```
jupyter nbconvert --to html notebook.ipynb
```

[Doc](https://nbconvert.readthedocs.io/en/latest/usage.html)