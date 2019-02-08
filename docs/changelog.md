# Changelog

## v0.1.0
- clean_dataset.py in `wsae_lstm` folder to clean raw dataset, output stored in `data/interim` folder (refactored from `notebooks\0_data_clean_load.ipynb` notebook)
- Refactors from `1_data_clean_load_datetime.ipynb` notebook:
  - `utils.py` for `frames_to_excel(),dictmap_load(), dictmap_datetime()` functions in `wsae_lstm` source/root folder
    - Functions to load and save a dictionary of dataframes to and from disk
    - `clean_data.py` updated with function imports from `utils.py`
    - `frames_to_excel()` can now accept optional `key_order` kwarg
- Data in `data/processed` has date column in datetime object format
- Minor syntax/variable name reference consistency changes
- `readme.md` update with repository structure section & other minor clarification changes 

