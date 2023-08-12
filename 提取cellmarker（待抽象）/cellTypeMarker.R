library(dplyr)
celltype_markers <- read.table("clipboard", sep = "\t", quote = NULL, header = T, na.strings = "") # 空白转为NA
colnames(celltype_markers) <- c("cell_type", "gene")

celltype_marker_combined <- celltype_markers %>%
  tidyr::fill(cell_type) %>% # 细胞类型为空白直接使用第一个出现值
  group_by(cell_type) %>%
  top_n(n = 4000) %>% # 每个细胞类型最多保留4000基因
  summarise(concated_genes = paste(gene, collapse = ","))

clipr::write_clip(celltype_marker_combined, allow_non_interactive = TRUE) # 输出data.frame到剪贴板
message("已输出到剪贴板")
