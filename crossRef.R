 githlibrary(tidyverse)
library("dplyr")

#Submission time to active ingredients to SMILES
products <- read.csv('Products.csv')
submissions <- read.csv('Submissions.csv')
smiles <- read.csv('ALL_FDA_SMILES.csv')

merged <- merge(products, submissions, by = "ApplNo")
newMerged <- merged[,c('ApplNo', 'DrugName', 'ActiveIngredient', 'SubmissionStatusDate')]

fullMerge <- merge(merged, smiles, by = 'ActiveIngredient')
mergeWithSMILES <- merge(newMerged, smiles, by = 'ActiveIngredient')

#SMILES to weighted scores 
AdmetLab <- read.csv('Weighted_Admetlab2.0.csv')
XunDrug <- read.csv('Weighted_XUNdrug.csv')

#Simplify to necessary values (Molecular Score - Final )
admetReduced <- AdmetLab[,c('SMILES', 'Molecule.Score...Final')]
xundrugReduced <- XunDrug[,c('SMILES', 'Molecule.Score...Final')]

admetReduced <- admetReduced %>% 
  rename("AdmetLabWeighted" = "Molecule.Score...Final")
xundrugReduced <- xundrugReduced %>%
  rename("XunDrugWeighted" = "Molecule.Score...Final")

#Final merge using SMILES (1 reduced version, one complete/raw version with all datasets)
finalMerge <- mergeWithSMILES %>%
  left_join(admetReduced, by = 'SMILES', relationship = "many-to-many") %>%
  left_join(xundrugReduced, by = 'SMILES', relationship = "many-to-many")

completeDatasets <- fullMerge %>% 
  left_join(AdmetLab, by = 'SMILES', relationship = "many-to-many") %>%
  left_join(XunDrug, by = 'SMILES', relationship = "many-to-many")

write.csv(finalMerge, 'admetlab-xundrug-timeline.csv', row.names = FALSE)
write.csv(completeDatasets, 'full-datasets.csv', row.names = FALSE)
