dati_fao <- read.csv("data_rain_evapo.csv")


dati_fao['prec_norm'] <- (dati_fao$precipitation- min(dati_fao$precipitation))/(max(dati_fao$precipitation)-min(dati_fao$precipitation))
dati_fao['inc_norm'] <- (dati_fao$incidents - min(dati_fao$incidents))/(max(dati_fao$incidents)-min(dati_fao$incidents))
dati_fao['evap_norm'] <- (dati_fao$evapotranspiration - min(dati_fao$evapotranspiration))/(max(dati_fao$evapotranspiration)-min(dati_fao$evapotranspiration))
dati_fao['avp_norm'] <- (dati_fao$AVP - min(dati_fao$AVP))/(max(dati_fao$AVP)-min(dati_fao$AVP))

barplot(dati_fao$precipitation)
plot(dati_fao$prec_norm,type = 'b',col='red')
lines(dati_fao$inc_norm,type = 'b',col='blue')
lines(dati_fao$evap_norm,type = 'b',col='green')
lines(dati_fao$avp_norm,type = 'b')

regAll <- lm(incidents ~ precipitation + evapotranspiration + AVP, data = dati_fao)
print(summary(regAll))

regPrec <- lm(incidents ~ precipitation, data = dati_fao)
print(summary(regPrec))

regPrecEv <- lm(incidents ~ precipitation + evapotranspiration, data = dati_fao)
print(summary(regPrecEv))

regLog <- glm(incidents ~ precipitation + evapotranspiration, data = dati_fao)
print(summary(regLog))


      





