import pandas as pd

# 读取TSV文件
df = pd.read_csv('OK_antigen.tsv', sep='\t', dtype=str)

# 分离KL和OL行（根据Best match locus列的内容）
kl_rows = df[df['Best match locus'].str.startswith('KL')]
ol_rows = df[df['Best match locus'].str.startswith('OL')]

# 添加前缀到列名
ol_columns = {col: f'O_{col}' for col in df.columns if col != 'Assembly'}
kl_columns = {col: f'K_{col}' for col in df.columns if col != 'Assembly'}

# 重命名列
ol_rows = ol_rows.rename(columns=ol_columns)
kl_rows = kl_rows.rename(columns=kl_columns)

# 按Assembly进行合并
merged_df = pd.merge(ol_rows, kl_rows, on='Assembly', how='outer')

# 保存完整的合并结果
merged_df.to_csv('OK_antigen_detail.tsv', sep='\t', index=False)

# 仅保留指定的列
selected_columns = [
    'Assembly', 
    'O_Best match locus', 
    'K_Best match locus', 
    'O_Match confidence', 
    'K_Match confidence', 
    'O_Coverage', 
    'O_Identity', 
    'K_Coverage', 
    'K_Identity', 
    'O_Expected genes in locus', 
    'K_Expected genes in locus'
]

# 创建一个新的DataFrame，只包含所需列
selected_df = merged_df[selected_columns]

# 保存精简的结果到新文件
selected_df.to_csv('OK_antigen_info.tsv', sep='\t', index=False)

print("合并完成，完整结果已保存为 OK_antigen_detail.tsv")
print("选定字段已保存为 OK_antigen_info.tsv")
