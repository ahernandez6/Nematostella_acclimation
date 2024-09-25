library(DSS)
library(bsseq)
file_list=list.files(path=".", pattern = "\\dF\\d+.*bismark.cov.gz", full.names = TRUE)
bsseq_temp=bsseq::read.bismark(files = file_list, colData=DataFrame(row.names=c("1F15","1F20","1F25", "2F15", "2F20", "2F25", "3F15", "3F20", "3F25")))

#Comparing 15 degrees to 20 degrees
dmlTest15_20 = DMLtest(bsseq_temp, group1=c("1F15","2F15","3F15"), group2=c("1F20", "2F20", "3F20"))
dmls15_20 = callDML(dmlTest15_20, p.threshold=0.05)
dmrs15_20 = callDMR(dmlTest15_20, p.threshold=0.05)
write.csv(dmrs15_20, "dmr_F15_v_F20.csv", row.names = FALSE)

#Comparing 20 degrees to 25 degrees
dmlTest20_25 = DMLtest(bsseq_temp,group1=c("1F20", "2F20", "3F20"), group2=c("1F25","2F25","3F25"),)
dmls20_25 = callDML(dmlTest20_25, p.threshold=0.05)
dmrs20_25 = callDMR(dmlTest20_25, p.threshold=0.05)
write.csv(dmrs20_25, "dmr_F20_v_F25.csv", row.names = FALSE)

#Comparing 15 degrees to 25 degrees
dmlTest15_25 = DMLtest(bsseq_temp, group1=c("1F15","2F15","3F15"), group2=c("1F25", "2F25", "3F25"))
dmls15_25 = callDML(dmlTest15_25, p.threshold=0.05)
dmrs15_25 = callDMR(dmlTest15_25, p.threshold=0.05)
write.csv(dmrs15_25, "dmr_F15_v_F25.csv", row.names = FALSE)
