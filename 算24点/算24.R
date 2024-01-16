#' @description 4位整数通过四则运算算24点
#' @example cal24(c(1,2,3,4))
#' @author lw
cal24 <- function(numbers) {
    operators <- c("+", "-", "*", "/")
    operators_com <- expand.grid(operators, operators, operators)
    numbers_com <- perm(numbers)
    # 每组数字最多计算：24（数字组合）*64（四则运算组合）*4（括号改变计算顺序） = 6144 次，计算量很小，无需优化
    for (i in seq_len(nrow(numbers_com))) {
        for (j in seq_len(nrow(operators_com))) {
            # 所有可能的运算方式
            base_formulas <- paste0(numbers_com[i, 1], operators_com[j, 1], numbers_com[i, 2], operators_com[j, 2], numbers_com[i, 3], operators_com[j, 3], numbers_com[i, 4])
            # 考虑运算顺序（TODO：有没有更简洁的方式呢？如果能够解决括号问题，这个算法可以扩展到任意数目的数字）
            formulas_ordered <- c(
                paste0("(", numbers_com[i, 1], operators_com[j, 1], numbers_com[i, 2], ")", operators_com[j, 2], numbers_com[i, 3], operators_com[j, 3], numbers_com[i, 4]), # (a+b)*c+d
                paste0("(", numbers_com[i, 1], operators_com[j, 1], numbers_com[i, 2], ")", operators_com[j, 2], "(", numbers_com[i, 3], operators_com[j, 3], numbers_com[i, 4], ")"), # (a+b)*(c+d)
                paste0("(", numbers_com[i, 1], operators_com[j, 1], numbers_com[i, 2], operators_com[j, 2], numbers_com[i, 3], ")", operators_com[j, 3], numbers_com[i, 4]), # (a+b+c)*d
                paste0(numbers_com[i, 1], operators_com[j, 1], "(", numbers_com[i, 2], operators_com[j, 2], "(", numbers_com[i, 3], operators_com[j, 3], numbers_com[i, 4], "))") # a*(b+c+d)
            )
            all_formulas <- c(base_formulas, formulas_ordered)
            for (f in all_formulas) {
                result <- eval(parse(text = f))
                if (!is.na(result) && abs(result - 24) < 1e-3) {
                    print(f)
                    return(TRUE) # 有结果即可，无需算出所有解
                }
            }
        }
    }
    message(paste(numbers, collapse = ","), "无解.")
}

# https://www.r-bloggers.com/2019/06/learning-r-permutations-and-combinations-with-base-r/
perm <- function(v) {
    n <- length(v)
    if (n == 1) {
        v
    } else {
        X <- NULL
        for (i in 1:n) X <- rbind(X, cbind(v[i], perm(v[-i])))
        X
    }
}
########
# 2024-01-16
########
#' -----------测试案例-----------
# # 数据来源：http://www.cnblogs.com/grenet/archive/2013/02/28/2936965.html
# source("D:/OneDrive - hrbmu.edu.cn/workspace/MyScripts/算24点/题库.R")
# for (card in cards) {
#     cal24(card)
# }
#' -----------结束测试-----------
#####################
