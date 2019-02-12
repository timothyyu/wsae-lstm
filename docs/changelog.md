# Changelog

- creation of `data/pickled` folder for pickled data (i.e. pickled dataframes)
- additional files added to `references` 
- `README.md` update to reflect changes 
- new functions in`utils.py`: `interval_split(), dict_interval_split(), pickle_save, pickle_load()` (refactored from `1d_train_test_split_exploration.ipynb`)
- required imports update (`requirements.txt/environment.yml`):
  - monthdelta 
  - pickle
  - `from statsmodels.robust import mad`
  - `from scipy import signal`
- wavelet transform exploration start in `1c_wavelet_draft_test_exploration.ipynb`
- start of train-validate-test split implementation in`1f_tvt_split_exploration.ipynb`
- double datetime index & datetime column fixed from `interval_split()` in `utils.py`

## v0.1.0
- clean_dataset.py in `wsae_lstm` folder to clean raw dataset, output stored in `data/interim` folder (refactored from `notebooks\0_initial_data_exploration.ipynb` notebook)
- Refactors from `1b_data_clean_load_datetime.ipynb` notebook:
  - `utils.py` for `frames_to_excel(),dictmap_load(), dictmap_datetime()` functions in `wsae_lstm` source/root folder
    - Functions to load and save a dictionary of dataframes to and from disk
    - `clean_data.py` updated with function imports from `utils.py`
    - `frames_to_excel()` can now accept optional `key_order` kwarg
- Data in `data/processed` has date column in datetime object format
- Minor syntax/variable name reference consistency changes
- `readme.md` update with repository structure section & other minor clarification changes 

