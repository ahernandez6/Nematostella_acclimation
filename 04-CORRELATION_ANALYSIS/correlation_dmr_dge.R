library("ggpubr")
data<-read.csv("dmr_dge_F15_v_F20_alpha_0.05.csv")
#test for normality
shapiro.test(data$Mean.difference.in.methylation)
shapiro.test(data$logFC)
#since the data is not normally distributed, we will use the spearman correlation
ggscatter(data, x = "Mean.difference.in.methylation", y = "logFC", 
          add = "reg.line", conf.int = TRUE, 
          cor.coef = TRUE, cor.method = "spearman",
          xlab = "difference in methylation", ylab = "log2 fold change")

data2<-read.csv("dmr_dge_F20_v_F25_alpha_0.05.csv")
#test for normality
shapiro.test(data2$Mean.difference.in.methylation)
shapiro.test(data2$logFC)
#since the data is not normally distributed, we will use the spearman correlation
ggscatter(data2, x = "Mean.difference.in.methylation", y = "logFC", 
          add = "reg.line", conf.int = TRUE, 
          cor.coef = TRUE, cor.method = "spearman",
          xlab = "difference in methylation", ylab = "log2 fold change")

data3<-read.csv("dmr_dge_F15_v_F25_alpha_0.05.csv")
#test for normality
shapiro.test(data3$Mean.difference.in.methylation)
shapiro.test(data3$logFC)
#since the data is not normally distributed for differentially expressed genes, we will use the spearman correlation
ggscatter(data2, x = "Mean.difference.in.methylation", y = "logFC", 
          add = "reg.line", conf.int = TRUE, 
          cor.coef = TRUE, cor.method = "spearman",
          xlab = "difference in methylation", ylab = "log2 fold change")
