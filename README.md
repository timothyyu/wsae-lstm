# wsae-lstm

Repository that aims to implement the WSAE-LSTM model and replicate the results of said model as defined in *"A deep learning framework for financial time series using stacked autoencoders and long-short term memory"* by Wei Bao, Jun Yue, Yulei Rao (2017).

https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0180944

## Source journal (APA)

Bao W, Yue J, Rao Y (2017). "A deep learning framework for financial time series using stacked autoencoders and long-short term memory". PLOS ONE 12(7): e0180944. https://doi.org/10.1371/journal.pone.0180944

<u>Diagram Illustrating the WSAE-LSTM model on an abstract level:</u>

![wsae lstm model funnel diagram](https://github.com/timothyyu/wsae-lstm/blob/master/docs/wsae%20lstm%20model%20funnel%20diagram.png)

### Source journal data (saved into `data/raw` folder):
DOI:10.6084/m9.figshare.5028110
https://figshare.com/articles/Raw_Data/5028110

## Repository structure

This repository uses a directory structured based upon [Cookiecutter Datascience]( http://drivendata.github.io/cookiecutter-data-science/#directory-structure).

Repository package requirements/dependencies are defined in `requirements.txt` for pip and/or `environment.yml` for Anaconda/Conda. 

### `mlpanda/DeepLearning_Financial`:

[Repository of an existing attempt to replicate above paper in PyTorch](mlpanda/DeepLearning_Financial: https://github.com/mlpanda/DeepLearning_Financial), checked out as a `git-subrepo` for reference in `submodules` folder. 



