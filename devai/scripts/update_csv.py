import pandas as pd
from fire import Fire


def update_csv(old_path_or_df, new_path_or_df, output_path=None, save_csv=True, encoding="latin"):
    old = pd.read_csv(old_path_or_df, encoding=encoding) if type(
        old_path_or_df) == str else old
    new = pd.read_csv(new_path_or_df, encoding=encoding) if type(
        new_path_or_df) == str else new
    df = pd.concat([old, new])
    df.drop_duplicates(inplace=True, keep="last")
    df.reset_index(inplace=True)
    if save_csv:
        if not output_path:
            output_path = old_path_or_df if type(
                old_path_or_df) == str else "updated.csv"
        df[old.columns].to_csv(output_path)
    else:
        return df


if __name__ == "__main__":
    Fire(update_csv)
