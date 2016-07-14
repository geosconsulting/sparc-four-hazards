valori <- read.csv("C:\\sparc\\intermedi\\calcolettiR\\valori_da_regredire.csv")
summary(valori)

plot(valori$Prec.,valori$Inc.)

modReg <- lm(Inc. ~ Prec. + Evapotra. + AVP,data = valori)
summary(modReg)

modReg1 <- lm(Inc. ~ Prec. + Evapotra.,data = valori)
summary(modReg1)

modReg2 <- lm(Inc. ~ Prec.,data = valori)
summary(modReg2)

modReg3 <- lm(Inc. ~ Prec. + AVP,data = valori)
summary(modReg3)

modReg4 <- lm(Inc. ~ Evapotra. + AVP,data = valori)
summary(modReg4)
