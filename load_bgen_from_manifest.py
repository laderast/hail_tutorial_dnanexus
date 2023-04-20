hdfs dfs -put "/mnt/project/indexes/*.idx2"

import pandas as pd
import hail as hl
manifest = pd.read_csv("/mnt/project/bgen_manifest.csv")

map_dict = {(row["bgen"]):(row["hdfs"]) for count, row in manifest.iterows()}

mt = hl.import_bgen([manifest["bgen"]],
                    entry_fields=['GT', 'GP'],
                    sample_file = [manifest["sample"]],
                    n_partitions=None,
                    block_size=None,
                    variants=None,
                    index_file_map = [map_dict])

