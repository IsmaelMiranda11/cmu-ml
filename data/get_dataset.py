import kaggle
import json
from pathlib import Path

def main():
    #https://www.kaggle.com/datasets/ealtman2019/credit-card-transactions/data?select=User0_credit_card_transactions.csv
    dataset = "uciml/german-credit"
    dataset_path = dataset.split('/')[1]
    folder = Path(f'./{dataset_path}')
    folder.mkdir(exist_ok=True)
    kaggle.api.dataset_download_files(dataset, folder)

    # Unzip the file inside the folder
    for file in folder.iterdir():
        if file.suffix == '.zip':
            import zipfile
            with zipfile.ZipFile(file, 'r') as zip_ref:
                zip_ref.extractall(folder)
            break
    # Delete the zip file
    file.unlink()
    

if __name__ == '__main__':
    main()

