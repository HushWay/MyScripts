# TODO: 建立scoop current链接
#
# Author: liuwei
# Date:2023-04-13
###############################################################################
# XX/scoop/apps地址，根据情况设定
scoop_app_path <- "C:/Users/way/OneDrive - hrbmu.edu.cn/scoop/apps"
# library(tidyverse)
all_app_dir <- list.files(file.path(scoop_app_path), full.names = TRUE)
for (i in all_app_dir) {
    cat("正在映射", i, "\n")
    link <- file.path(i, "current")
    if (!dir.exists(link)) {
        target <- list.dirs(i, recursive = FALSE, full.names = TRUE)[1]
        cmd <- paste0("mklink /d ", '"', link, '" "', target, '"')
        shell(cmd)
    }
}
