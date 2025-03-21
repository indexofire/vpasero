## README

vpa-serodb: Kaptive adaptive **d**ata**b**ses for **V**ibrio **pa**rahaemolyticus O/K antigen **sero**typing

这是用于分子血清预测(in-silico serotyping)副溶血弧菌O/K抗原的Kaptive数据库，fork自[vibrio_parahaemolyticus_genomoserotyping](https://github.com/aldertzomer/vibrio_parahaemolyticus_genomoserotyping)。

### 与原数据库差异

1. 新增了地方流行株O10:K4的数据（原数据库会将其鉴定为O4:K4）。
2. 去除了与 GB 4789.7-2013 未包含但是[文章](https://doi.org/10.1016/j.ijfoodmicro.2017.01.010)中提出的O抗原：O14-O16，将其重新定义成OLU系列的抗原基因簇。
3. 将OL3和OL13区分，默认情况下均鉴定为OL3。当K基因簇为KL65时会被鉴定成OL13:KL65。

### 定义说明：

**血清表型定义**

- 已知抗原O1,O2,O3...,O13（根据生研血清试剂）,对于O抗原均不凝集称呼为OUT
- K抗原同理

**血清基因簇预测定义**

- 已知抗原对应基因簇OL1,OL2,OL3...,OL12,OL13(只有当KL65时，OL3修改为OL13)
- 对于能用表型鉴定的O抗原基因簇，但是与默认基因簇有基因差异（增加、确实、大片段插入或缺失，重排等）如O10:K4情况的，则命名为OL1V1，表示变异基因簇1。如果有发现其他新的基因簇构成则“V”后标号依次类推
- 对于无法用血清表型验证的基因簇，均表示为OLU（表示为OL Unpredictable)，不同的基因簇用数字标号表示，比如OLU1,OLU2...依次类推。只要基因构成有差异，就用新的数字标号表示
- 一旦有表型实验证据将多个携带某个OLU的菌株鉴定为已知O抗原，则会将其修改为对应的O抗原变异基因簇，但是流水号数字不再占用
- K基因簇同理

### 使用说明

下载安装kaptive，然后克隆血清数据库即可

```bash
# 建议使用conda虚拟环境
$ conda create -n kaptive
$ conda activate kaptive

# 目前最新的3.0.6b版本的kaptive对基因数量判别有bugs,需要用仓库的最新代码安装
(kaptive)$ conda install pip pandas
(kaptive)$ pip install git+https://github.com/klebgenomics/Kaptive.git

# 下载数据库
(kaptive)$ git clone https://github.com/indexofire/vpa-serodb.git

# 预测OK抗原
# 预测一个基因组
(kaptive)$ kaptive assembly vpa_adaptive_db_O.gbk mygenome.fasta -o output
# 批量预测，获得完整结果
(kaptive)$ ls *.fna | parallel -k --eta kaptive assembly vpa_adaptive_db_O.gbk {} -t 1 -f O/{/.}_O.fasta -p O_locus_vis > OL.tsv
(kaptive)$ ls *.fna | parallel -k --eta kaptive assembly vpa_adaptive_db_O.gbk {} -t 1 -f O/{/.}_K.fasta -p K_locus_vis > KL.tsv
# 合并数据
(kaptive)$ cat OL.tsv KL.tsv | sort -u > OK_antigen.tsv
(kaptive)$ python scripts/merge.py -i OK_antigen.tsv -o output
# 数据结果
OK_antigen_info.tsv     包含汇总信息
OK_antigen_detail.tsv   包含分析结果的详细信息，包括基因序列情况
O_locus_vis/*.png       包含O抗原基因分布可视化图
K_locus_vis/*.png       包含K抗原基因分布可视化图
O/*_O.fasta             提取的匹配O抗原序列
K/*_K.fasta             提取的匹配K抗原序列
```