import dxpy, os
#import hail as hl
import pandas as pd
testing = True

field_id = "23159"

obj_gen = dxpy.find_data_objects(properties={"field_id":field_id}, name="*.bgen", name_mode="glob")

id_list = [a["id"] for a in obj_gen]

# Grab describe objects for every file id
out_describe = [dxpy.bindings.dxdataobject_functions.describe(id) for id in id_list]

#make a list of file paths with /mnt/project prepended and using only basename of file
dxfuse_list = [f"file://mnt/project/" +  desc["folder"] + "/" + os.path.splitext(desc["name"])[0] for desc in out_describe]

#grab file name
index_list = [desc["name"] for desc in out_describe]
#make list of hdfs locations for index
hdfs_list = [f"hdfs:///" + desc["name"] + ".idx2" for desc in out_describe]
#make list of bgen locations in project storage
bgen_list = [dx + ".bgen" for dx in dxfuse_list]
#make list of sample locations in project storage
sample_list = [dx + ".sample" for dx in dxfuse_list]

#glue everything into a Pandas DataFrame, which we'll use to process files
manifest = pd.DataFrame({"bgen": bgen_list, "sample": sample_list,"index":index_list, "hdfs": hdfs_list})  

if(testing):
    manifest = manifest.head(5)

#file_out = "bgen_manifest.csv"
manifest.to_csv(file_out)

#save file manifest to project sstorage
dxpy.upload_local_file(filename=file_out)

#index bgen files
for i, row in manifest.iterrows():
    hl.index_bgen(path=row["bgen"],
                  index_file_map={row["bgen"]:row["hdfs"]},
                  reference_genome="GRCh38",
                  contig_recoding=None,
                  skip_invalid_loci=False)

#build index file dictionary    
map_dict = {(row["bgen"]):(row["hdfs"]) for i, row in manifest.iterows()}

#finally, import all bgen files
mt = hl.import_bgen([manifest["bgen"].tolist()],
                    entry_fields=['GT', 'GP'],
                    sample_file = [manifest["sample"].tolist()],
                    n_partitions=None,
                    block_size=None,
                    variants=None,
                    index_file_map = [map_dict])

# Set database name and matrix table name

db_name = "mt_bgen"
mt_name = "geno.mt"

# Create database in DNAX

stmt = f"CREATE DATABASE IF NOT EXISTS {db_name} LOCATION 'dnax://'"
print(stmt)
spark.sql(stmt).show()

# Store Table in DNAXc

import dxpy

# find database ID of newly created database using a dxpy method
db_uri = dxpy.find_one_data_object(name=f"{db_name}", classname="database")['id']
url = f"dnax://{db_uri}/{tb_name}"

mt.write(url) # Note: output should describe size of Table (i.e. number of rows, partitions)