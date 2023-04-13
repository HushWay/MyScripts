# install.packages("easyPubMed")
library(easyPubMed)

titles <- c(
    "Phenotypic plasticity and genetic control in colorectal cancer evolution",
    "Clonal Evolution and Heterogeneity of Osimertinib Acquired Resistance Mechanisms in EGFR Mutant Lung Cancer"
)

pmids <- get_pubmed_ids(titles)
