import glob
import os
import pandas as pd 

def join_csv(title):
    path = "hmr/output/csv/" + title
    all_files = glob.glob(os.path.join(path, "*.csv"))
    all_files.sort(key=lambda x: (x.split('/')[-1].split('.')[0]))
    df_from_each_file = (pd.read_csv(f) for f in all_files)
    concatenated_df   = pd.concat(df_from_each_file, ignore_index=True)

    concatenated_df['frame'] = concatenated_df.index+1
    concatenated_df.to_csv("hmr/output/csv_joined/" + title + ".csv", index=False)