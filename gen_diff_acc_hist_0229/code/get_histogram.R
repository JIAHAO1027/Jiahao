library(ggplot2)

# setwd("//Users/Jiahao/Dropbox/urap_programming/Jiahao/gen_diff_acc_hist_0229")
setwd("C:/Users/xin_chen/Dropbox/urap_programming/Jiahao/gen_diff_acc_hist_0229")
dic <- read.csv("output/forgraph.csv")
pdf(file = "histogram")
pdf(file = "C:/Users/xin_chen/Dropbox/urap_programming/Jiahao/gen_diff_acc_hist_0229/output/graph/Histogram of Delta_n Accessories Rel B1.pdf")
ggplot(dic) + geom_bar(aes(x=index))
dev.off()

# setwd("/Users/Jiahao/Dropbox/urap_programming/Jiahao/gen_diff_acc_hist_0229")
setwd("C:/Users/xin_chen/Dropbox/urap_programming/Jiahao/gen_diff_acc_hist_0229")
#fixme keep item_id as an input column
df <- read.csv("output/for_individual_graph.csv")
df.count <- df %>%
  group_by(bundle_index,dic_index)%>%
  summarize(c=n())%>%
  filter(c>15)
pdf(file = "C:/Users/xin_chen/Dropbox/urap_programming/Jiahao/gen_diff_acc_hist_0229/output/graph/Histogram of Delta_n Accessories by Category Rel B1.pdf")
ggplot(df.count) + geom_bar(aes(dic_index,c), stat="identity") + facet_wrap(~bundle_index, nrow = 3) + labs(title = "Histogram of Delta_n Accessories by Category Rel B1")
dev.off()

