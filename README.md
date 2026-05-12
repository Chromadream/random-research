# Random Research

LLMs are good at creating HTMLs nowadays; this is just a public repo to serve
those random research over GitHub Pages for my own convenience.

## Scripts

This is a script based on https://til.simonwillison.net/llms/llm-shebang. It
requires
[llm-tools-read-write-file](https://github.com/Chromadream/llm-tools-read-write-file)
to automatically write a file somewhere. It also requires
[Exa](https://github.com/daturkel/llm-tools-exa), for internet stuff. You can
also swap out the model with other models that LLM support, as long as it
supports tool-calling. All scripts will generate the HTML files shown in this
repo.

The scripts are:

- research.sh: used for researching things, comparison and so on

- paper-explainer.sh: used to generate an explainer of a paper.
