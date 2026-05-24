# CSV Excel Batch Converter

本プログラムは，inputディレクトリ内のCSVファイルを一括で読み込み，Excelファイルへ変換してoutputディレクトリへ保存するPythonツールです．

複数CSVファイルをまとめて処理できます．

---

## 使用技術
- Python
- pandas
- openpyxl

---

## 実行方法

1. 本リポジトリを clone する．
2. コンソール上で保存したディレクトリへ移動する．
3. 以下コマンドを実行し，必要なライブラリを install する．

    ```bash
    pip install -r requirements.txt
    ```

4. input ディレクトリ内へ CSV ファイルを配置する．

    例：
    ```text
    input/
    ├ sales_tokyo.csv
    ├ sales_osaka.csv
    └ sales_nagoya.csv
    ```

5. `csv_excel_batch_converter.py` を実行する．

    例：
    ```bash
    python csv_excel_batch_converter.py
    ```
    ```bash
    py csv_excel_batch_converter.py
    ```

---

## 出力ファイル

CSVファイルと同名の Excelファイルが，outputディレクトリ内へ保存されます．

例：
```text
output/
├ sales_tokyo.xlsx
├ sales_osaka.xlsx
└ sales_nagoya.xlsx
```

---

## 補足

- UTF-8 / Shift-JIS(cp932) / UTF-16 の読み込みに対応しています．
- 読み込み失敗時はエラーメッセージを表示します．
- 空CSVファイルは自動的にスキップされます．

---

# English

## Overview

This is a Python tool that batch converts CSV files into Excel files.

The program reads all CSV files stored in the `input` directory and exports them as Excel files into the `output` directory.

Multiple CSV files can be processed at once.

---

## Tech stack

- Python
- pandas
- openpyxl

---

## Usage

1. Clone this repository.
2. Move to the saved directory in the console.
3. Run the following command to install the required libraries.

   ```bash
   pip install -r requirements.txt
   ```

4. Place CSV files into the `input` directory.

   Example:

   ```text
   input/
   ├ sales_tokyo.csv
   ├ sales_osaka.csv
   └ sales_nagoya.csv
   ```

5. Run `csv_excel_batch_converter.py`.

   Example:

   ```bash
   python csv_excel_batch_converter.py
   ```

   ```bash
   py csv_excel_batch_converter.py
   ```

---

## Output Files

Excel files with the same names as the original CSV files are saved in the `output` directory.

Example:

```text
output/
├ sales_tokyo.xlsx
├ sales_osaka.xlsx
└ sales_nagoya.xlsx
```

---

## Notes

* Supports UTF-8, Shift-JIS(cp932), and UTF-16 encoded CSV files.
* Error messages are displayed when file loading fails.
* Empty CSV files are automatically skipped.

