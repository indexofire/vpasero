## Kaptive adaptive databases for Vibrio parahaemolyticus O/K antigen serotyping

这里是副溶血弧菌O/K抗原基因的Kaptive数据库，fork自[vibrio_parahaemolyticus_genomoserotyping](https://github.com/aldertzomer/vibrio_parahaemolyticus_genomoserotyping)。

### 与原数据库差异

1. 新增了地方流行株O10:K4的数据（原数据库会将其鉴定为O4:K4）。
2. 去除了与 GB 4789.7-2013 未包含但是文章中提出的O抗原：O14-O16，将其重新定义成OLU系列的抗原基因簇。
3. 将OL3和OL13区分，只有当K基因簇为KL65时才定义成OL13:KL65


> 说明：
血清表型定义：已知抗原O1,O2,O3...,O13（根据生研血清试剂）,对于O抗原均不凝集称呼为OUT; K抗原同理。
血清基因簇预测定义：已知抗原对应基因簇OL1,OL2,OL3...,OL12,OL13(只有当KL65时，OL3修改为OL13)；对于能用表型鉴定的O抗原基因簇，但是与默认基因簇有基因差异（增加、确实、大片段插入或缺失，重排等）如O10:K4情况的，则命名为OL1V1，表示变异基因簇1。如果有发现其他新的基因簇构成则“V”后标号依次类推。对于无法用血清表型验证的基因簇，均表示为OLU（表示为OL Unpredictable)，不同的基因簇用数字标号表示，比如OLU1,OLU2...依次类推。只要基因构成有差异，就用新的数字标号表示。如果一旦有表型实验能进行已知O抗原关联，则会将其修改为对应的O抗原变异基因簇，但是流水号数字不再占用。K基因簇同理。

### 使用说明

下载安装kaptive，然后克隆血清数据库即可

```bash
# 建议使用conda虚拟环境
$ conda create -n kaptive
$ conda activate kaptive
(kaptive)$ conda install pip
# 目前最新的3.0.6b版本的kaptive对基因数量判别有bugs,需要用仓库的最新代码安装
(kaptive)$ pip install git+https://github.com/klebgenomics/Kaptive.git
(kaptive)$ git clone https://github.com/indexofire/vibrio_parahaemolyticus_genomoserotyping.git
# 预测O抗原
(kaptive)$ kaptive assembly Vpa_adaptive_db_O.gbk *.fasta -o output
```