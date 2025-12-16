## README

Kaptive adaptive **d**ata**b**ses for **V**ibrio **pa**rahaemolyticus O/K antigen **sero**typing

本数据库用于副溶血性弧菌分子血清预测(in-silico serotyping)。使用Kaptive工具可以快速对基因组数据进行分子血清型预测称。数据库序列fork自[vibrio_parahaemolyticus_genomoserotyping](https://github.com/aldertzomer/vibrio_parahaemolyticus_genomoserotyping)，但对原数据库的OAgc和CPSgc进行更新。主要更新如下：

1. 新增了地方流行株O10:K4的数据（原数据库会将其鉴定为O4:K4）。
2. 去除了与 GB 4789.7-2013 未包含但是[文章](https://doi.org/10.1016/j.ijfoodmicro.2017.01.010)中提出的O抗原：O14-O16，将其定义成OLU1-3的抗原基因簇。
3. 区分OL3和OL13。默认情况下鉴定为OL3。当K基因簇为KL65时，OL3会被鉴定成OL13:KL65。

### 数据说明：

**血清表型与分子型别定义**

- 已知抗原O1,O2,O3...,O13（根据日本生研血清试剂）,对应的分子序列命名为OL1,OL2,OL3...,OL13。对于OUT抗原命名为OLUT
- K抗原同理

**血清基因簇预测定义**

- 已知抗原对应基因簇OL1,OL2,OL3...,OL12,OL13(只有当KL65时，OL3修改为OL13)
- 对于能用表型鉴定的O抗原基因簇，但是与默认基因簇有基因差异（增加、确实、大片段插入或缺失，重排等）如O10:K4情况的，则命名为OL1V1，表示变异基因簇1。如果有发现其他新的基因簇构成则“V”后标号依次类推
- 对于无法用血清表型验证的基因簇，均表示为OLU（表示为OL Unpredictable)，不同的基因簇用数字标号表示，比如OLU1,OLU2...依次类推。只要基因构成有差异，就用新的数字标号表示
- 一旦有表型实验证据将多个携带某个OLU的菌株鉴定为已知O抗原，则会将其修改为对应的O抗原变异基因簇，但是流水号数字不再占用
- K基因簇同理

个别血清因子尚无法确认对应的基因簇序列，具体信息参见meta.csv。如分离得到这些血清型的菌株并进行基因组测序后，可将OAgc/CPSgc序列发送给[作者](mailto:indexofire@gmail.com)，或者通过github发起issue。

**分子血清型预测案例：**

- OL3:KL6, 为O3K6血清型
- OL10V1:KL4，为O10:K4血清型
- OLUT3:KLUT17，为OUT:KUT血清型

### 使用说明

下载安装kaptive，然后克隆血清数据库即可

```bash
# 建议使用conda虚拟环境
$ conda create -n vpasero
$ conda activate vpasero
# 安装kaptive, 版本3.1.0及以上
$ conda install kaptive

# 下载数据库
(vpasero)$ git clone https://github.com/indexofire/vpa-serodb.git

# 预测一个基因组
(vpasero)$ kaptive assembly VP_OAgc.gbk mygenome.fna -o O_antigen
(vpasero)$ kaptive assembly VP_CPSgc.gbk mygenome.fna -o K_antigen

# 批量预测，获得完整结果
(vpasero)$ ls *.fna | parallel -k --eta kaptive assembly VP_OAgc.gbk {} -t 1 -f O/{/.}_O.fasta -p O_locus_vis > OL.tsv
(vpasero)$ ls *.fna | parallel -k --eta kaptive assembly VP_CPSgc.gbk {} -t 1 -f O/{/.}_K.fasta -p K_locus_vis > KL.tsv

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
